"""Run the real Jacobian lens on our demo prompt and dump JSON for the lesson.

Uses the pre-fitted neuronpedia lens (qwen-n1000) on Qwen3.5-4B — the same setup
as the repo walkthrough. Prints top-k J-lens tokens (with softmax %) at four
layers for the boot/currency prompt, and writes results.json.
"""
import json
import torch
import transformers
import jlens

MODEL_NAME = "Qwen/Qwen3.5-4B"
LENS_REPO = "neuronpedia/jacobian-lens"
LENS_REVISION = "qwen-n1000"
LENS_FILE = "qwen3.5-4b/jlens/Salesforce-wikitext/Qwen3.5-4B_jacobian_lens_n1000.pt"
PROMPT = "Fact: The currency used in the country shaped like a boot is"
TOPK = 6

jlens.configure_logging()

hf_model = transformers.AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, dtype=torch.bfloat16
).cuda()
tokenizer = transformers.AutoTokenizer.from_pretrained(MODEL_NAME)
model = jlens.from_hf(hf_model, tokenizer)

lens = jlens.JacobianLens.from_pretrained(
    LENS_REPO, filename=LENS_FILE, revision=LENS_REVISION
)

n = model.n_layers
layers = [n // 4, n // 2, n // 4 * 3, n - 2]

jlens_logits, model_logits, _ = lens.apply(model, PROMPT, layers=layers, positions=[-2])


def topk(logits, k=TOPK):
    probs = torch.softmax(logits.float(), dim=-1)
    vals, idx = probs.topk(k)
    out = []
    for v, t in zip(vals.tolist(), idx.tolist()):
        tokstr = tokenizer.decode([t]).strip()
        out.append({"token": tokstr, "pct": round(v * 100, 1)})
    return out


result = {
    "model": MODEL_NAME,
    "lens": f"{LENS_REPO}@{LENS_REVISION}",
    "prompt": PROMPT,
    "n_layers": n,
    "layers": {},
}
for layer in layers:
    result["layers"][str(layer)] = topk(jlens_logits[layer][0])

result["model_final"] = topk(model_logits[0])

print(json.dumps(result, indent=2, ensure_ascii=False))
with open("results.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print("\nwrote results.json")
