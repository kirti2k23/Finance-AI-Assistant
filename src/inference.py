"""
Finance FAQ AI Assistant — Inference Script
Stage 3 DPO-aligned model

Usage:
    python src/inference.py

Or import and call:
    from src.inference import generate_answer
    answer = generate_answer("What is a mutual fund SIP?")
    print(answer)
"""

import torch
from unsloth import FastLanguageModel

# ── Config ──
ADAPTER_PATH  = "./outputs/stage3_dpo_adapter"
MAX_SEQ_LEN   = 512
LOAD_IN_4BIT  = True
MAX_NEW_TOKENS = 200
TEMPERATURE    = 0.3

PROMPT_TEMPLATE = """Below is a finance question. Write a clear, accurate, and helpful response.

### Question:
{}

### Answer:
"""

# ── Load model (done once at module level) ──
print("Loading Finance FAQ Assistant...")
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name     = ADAPTER_PATH,
    max_seq_length = MAX_SEQ_LEN,
    dtype          = None,
    load_in_4bit   = LOAD_IN_4BIT,
)
FastLanguageModel.for_inference(model)
print("Model ready.")


def generate_answer(question: str) -> str:
    """
    Generate a finance answer for a given question.

    Args:
        question: User's finance question as a string.

    Returns:
        Model's answer as a string.
    """
    prompt = PROMPT_TEMPLATE.format(question.strip())
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens = MAX_NEW_TOKENS,
            temperature    = TEMPERATURE,
            do_sample      = True,
            pad_token_id   = tokenizer.eos_token_id,
        )

    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Extract only the answer portion
    answer = full_output.split("### Answer:")[-1].strip()
    return answer


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Finance FAQ AI Assistant")
    print("Type your question or 'quit' to exit")
    print("="*60 + "\n")

    while True:
        question = input("Your question: ").strip()
        if question.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not question:
            continue
        print("\nAnswer:", generate_answer(question))
        print()
