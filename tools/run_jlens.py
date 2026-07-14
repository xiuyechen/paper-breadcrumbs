"""Run the real Jacobian lens on our demo prompt and dump JSON for the lesson.

Uses the pre-fitted neuronpedia lens (qwen-n1000) on Qwen3.5-4B — the same setup
as the repo walkthrough. Sweeps a few end positions across four layers so we can
pick the position where the currency concept actually surfaces, and writes
results.json (all positions) plus results_best.json (chosen position).

The currency answer forms AFTER "is", so position -1 (the final token) is where
the concept-resolution should appear; -2 lands on "boot" (structural). We dump
several to choose honestly rather than assume.
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
POSITIONS = [-1, -2, -3]
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

# which actual tokens sit at those positions, for labeling
ids = tokenizer(PROMPT, return_tensors="pt").input_ids[0].tolist()
pos_tokens = {p: tokenizer.decode([ids[p]]).strip() for p in POSITIONS}


def topk(logits, k=TOPK):
    probs = torch.softmax(logits.float(), dim=-1)
    vals, idx = probs.topk(k)
    out = []
    for v, t in zip(vals.tolist(), idx.tolist()):
        tokstr = tokenizer.decode([t]).strip()
        out.append({"token": tokstr, "pct": round(v * 100, 1)})
    return out


jlens_logits, model_logits, _ = lens.apply(model, PROMPT, layers=layers, positions=POSITIONS)

result = {
    "model": MODEL_NAME,
    "lens": f"{LENS_REPO}@{LENS_REVISION}",
    "prompt": PROMPT,
    "n_layers": n,
    "pos_tokens": pos_tokens,
    "by_position": {},
}
for pi, p in enumerate(POSITIONS):
    result["by_position"][str(p)] = {
        "token_here": pos_tokens[p],
        "layers": {str(L): topk(jlens_logits[L][pi]) for L in layers},
    }

result["model_final_at_-1"] = topk(model_logits[0])

print(json.dumps(result, indent=2, ensure_ascii=False))
with open("results.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print("\nwrote results.json")
