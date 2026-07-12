# Fine-Tuning Concepts Explained

*Written in my own words after completing this assignment.*

## Why full fine-tuning is expensive

Full fine-tuning updates every weights in the model. Llama-3.2-1B has 1 billion parameters. 
Training all of them requires:
- Storing gradients for every parameter (doubles memory)
- Full optimizer states (Adam uses 2x more memory than gradients)
- A100 80GB GPU at minimum for models >7B

For a 1B model in float32: ~4GB just for weights, ~8GB for gradients, ~16GB for optimizer state = 28GB+ minimum. Not feasible on free Colab T4 (15GB VRAM).

## What LoRA does
LoRA is low rank adapter, which do following things:
     - Freezes original weights
     - Adds small trainable matrices A and B (rank r decomposition)
     - Only trains A and B — much smaller parameter count
     - At inference, merges LoRA weights back into original model


## What QLoRA does
QLoRA is quantized LoRA, which is build on top LoRA to use less memory.
     - Quantizes the base model to 4-bit (NF4 format)
     - Keeps LoRA adapters in float16
     - Double quantization to reduce memory further
     - Result: fine-tune a 7B model on a 24GB GPU


## Why QLoRA is useful on limited GPU
     - Without QLoRA: couldn't fit Llama-3.2-1B training in 15GB
     - With QLoRA: model weights use ~0.7GB (4-bit), adapter training ~2GB
     - Total: easily within T4 limits


## What is non-instruction fine-tuning?
     - Also called continued pre-training or domain-adaptive pre-training
     - Feed raw domain text to the model (no Q&A format)
     - Model learns to predict next token in finance domain language
     - Does NOT teach it to answer questions — just teaches domain vocabulary


## What is instruction fine-tuning (SFT)?
     - Supervised Fine-Tuning on instruction-response pairs
     - Teaches the model the format: given a question, produce a helpful answer
     - Uses labeled data: (instruction, response) pairs


## What is DPO?
     - Direct Preference Optimization
     - Uses (prompt, chosen, rejected) triples
     - Teaches model to prefer chosen over rejected responses
     - Does NOT require a reward model (unlike RLHF)
     - Loss function directly optimizes the policy using preference data


## Difference between SFT and DPO

| | SFT | DPO |
|---|---|---|
| Data format | (instruction, response) | (prompt, chosen, rejected) |
| Goal | Teach task format | Improve response quality |
| Needs reward model | No | No |
| Training signal | Cross-entropy on response | Contrastive preference loss |
| When to use | Teaching what to say | Teaching how to say it better |

## Hyperparameter values used

| Parameter | Stage 1 (Non-Instruction) | Stage 2 (SFT) | Stage 3 (DPO) |
|---|---|---|---|
| Rank (r) | 16 | 16 | 16 |
| Alpha | 16 | 16 | 16 |
| Dropout | 0.05 | 0.05 | 0.05 |
| Learning rate | 2e-4 | 2e-4 | 5e-5 |
| Batch size | 2 | 2 | 2 |
| Gradient accumulation | 4 | 4 | 4 |
| Epochs | 3 | 3 | 1 |
| Beta (DPO) | — | — | 0.1 |

## Why these values?

<!-- Briefly justify your choices:
     - r=16: balance between expressiveness and parameter count
     - alpha=16: alpha=r keeps scaling factor at 1.0 (stable starting point)
     - LR 5e-5 for DPO: lower than SFT to avoid overwriting SFT alignment
     - 1 epoch for DPO: preference data is smaller, more epochs risks forgetting SFT
-->
