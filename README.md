# Finance FAQ AI Assistant — Domain-Specific Fine-Tuning with Unsloth

## Project Overview

A domain-specific AI assistant for finance and banking, built by fine-tuning an open-source LLM through three progressive stages: non-instruction fine-tuning, supervised instruction fine-tuning (SFT), and DPO preference alignment.

---

## Domain

**Finance & Banking FAQ Assistant**

The assistant answers questions related to:
- Personal finance and budgeting
- Banking products (savings accounts, FDs, loans, credit cards)
- Investment basics (mutual funds, SIPs, stocks, bonds)
- Tax planning and filing (India-focused)
- Financial terminology and concepts

---

## Business Problem

General-purpose LLMs give vague, generic answers to finance questions. A domain-specifically fine-tuned model:
- Uses accurate financial terminology
- Gives India-context-aware answers (RBI, SEBI, tax slabs, UPI, etc.)
- Maintains a professional, clear tone
- Reduces hallucination on financial facts

---

## Model Used

- **Base model**: `unsloth/Llama-3.2-1B` (4-bit quantized via QLoRA)
- **Fine-tuning framework**: Unsloth + TRL
- **Hardware**: Kaggle T4 GPU (15GB VRAM)

---

## Dataset Details

| Dataset | Source | Size | Purpose |
|---|---|---|---|
| Non-instruction raw text | `gbharti/finance-alpaca` + Investopedia scrape | 50+ paragraphs | Stage 1: domain language |
| Instruction dataset | `gbharti/finance-alpaca` (filtered + cleaned) | 100 Q&A pairs | Stage 2: SFT |
| Preference dataset | Manually created from SFT outputs | 50 pairs | Stage 3: DPO alignment |

---

## Fine-Tuning Pipeline

```
Base Model (Llama-3.2-1B)
        ↓
Stage 1: Non-Instruction Fine-Tuning
  - Raw finance text (50+ paragraphs)
  - Trains domain language & terminology
        ↓
Stage 2: Instruction Fine-Tuning (SFT)
  - 100 finance Q&A pairs
  - Trains question-answering behavior
        ↓
Stage 3: DPO Preference Alignment
  - 50 chosen/rejected pairs
  - Trains response quality & professionalism
        ↓
Final Finance FAQ Assistant
```

---

## LoRA / QLoRA Configuration

| Parameter | Value |
|---|---|
| Rank (r) | 16 |
| Alpha | 16 |
| Dropout | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj, up_proj, down_proj, gate_proj |
| Quantization | 4-bit (QLoRA) |
| Learning rate | 2e-4 |
| Batch size | 2 |
| Gradient accumulation | 4 |
| Max sequence length | 512 |
| Epochs | 3 |

---

## Training Screenshots / Logs

<!-- Add screenshots of training loss curves here -->

**Non-Instruction FT Training Loss:**
> *(Add screenshot)*

**SFT Training Loss:**
> *(Add screenshot)*

**DPO Training Loss:**
> *(Add screenshot)*

---

## Before vs After — Output Comparison

> See `reports/final_evaluation.md` for the full 3-way comparison table.

**Example:**

**Question:** What is a mutual fund SIP?

| Stage | Answer |
|---|---|
| Base model | A SIP is a way to invest money regularly. |
| After SFT | A Systematic Investment Plan (SIP) allows you to invest a fixed amount in a mutual fund at regular intervals — weekly, monthly, or quarterly. It enables rupee cost averaging and is suitable for long-term wealth creation. |
| After DPO | A Systematic Investment Plan (SIP) is a disciplined investment method where you invest a fixed amount in a mutual fund scheme at regular intervals. SIPs leverage rupee cost averaging, meaning you buy more units when markets are low and fewer when high, reducing the average cost over time. Starting with as low as ₹500/month, SIPs are ideal for salaried individuals building long-term wealth. |

---

## Final Observations

<!-- Fill in after completing training -->

---

## Challenges Faced

<!-- Fill in after completing training -->

---

## Future Improvements

- Compare fine-tuned model vs RAG-based finance assistant (using existing LangGraph pipeline) on factual accuracy, hallucination rate, and response relevance
- Evaluate with RAGAS metrics
- Deploy as FastAPI + Streamlit app

---

## Repository Structure

```
finance-ai-assistant/
├── data/
│   ├── non_instruction_data.txt
│   ├── instruction_dataset.jsonl
│   └── preference_dataset.jsonl
├── notebooks/
│   ├── non_instruction_finetuning.ipynb
│   ├── instruction_finetuning.ipynb
│   └── dpo_alignment.ipynb
├── reports/
│   ├── base_model_evaluation.md
│   ├── sft_model_comparison.md
│   ├── final_evaluation.md
│   └── fine_tuning_explanation.md
├── src/
│   └── inference.py
├── README.md
└── requirements.txt
```

---

## How to Run Inference

```python
from src.inference import generate_answer

question = "What is the difference between a savings account and a fixed deposit?"
answer = generate_answer(question)
print(answer)
```
