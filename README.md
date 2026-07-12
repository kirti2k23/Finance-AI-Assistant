# Finance FAQ AI Assistant — Domain-Specific LLM Fine-Tuning

A domain-specific AI assistant for finance and banking, built by fine-tuning **Llama-3.2-1B** through three progressive stages using **Unsloth** and **QLoRA** — non-instruction fine-tuning, supervised instruction fine-tuning (SFT), and DPO preference alignment.

---

## Domain

**Finance & Banking FAQ Assistant**

The assistant answers questions related to:
- Personal finance and investment (mutual funds, SIPs, stocks, ETFs)
- Banking products (savings accounts, fixed deposits, loans, credit cards)
- Tax planning (capital gains, IRS rules, Section 80C)
- Financial instruments (bonds, derivatives, currency hedging)
- Car financing and lease vs buy analysis
- Dividend reinvestment and portfolio management

---

## Business Problem

General-purpose LLMs fail on finance domain Q&A in three specific ways:

| Problem | Example |
|---|---|
| Repetition loop | Repeats the same sentence 8-10 times |
| Question echoing | Repeats the question instead of answering |
| Hallucination | Fabricates financial facts with false confidence |

A domain-specifically fine-tuned model solves these by learning finance terminology, answer structure, and domain-specific reasoning through progressive fine-tuning stages.

---

## Model

| Component | Detail |
|---|---|
| Base model | `unsloth/Llama-3.2-1B` |
| Fine-tuning framework | Unsloth + TRL |
| Quantization | 4-bit QLoRA (NF4) |
| Training hardware | Kaggle T4 GPU (15GB VRAM) |
| Parameters trained | 11,272,192 / 1,247,086,592 (0.90%) |

---

## Dataset

| Stage | Source | Size | Purpose |
|---|---|---|---|
| Stage 1 — Non-instruction | `gbharti/finance-alpaca` (output field only) | 500 paragraphs → 265 chunks | Domain language adaptation |
| Stage 2 — SFT | `gbharti/finance-alpaca` (instruction + output) | 100 examples → 85 after length filtering | Instruction following |
| Stage 3 — DPO | `gbharti/finance-alpaca` (constructed preference pairs) | 50 chosen/rejected pairs | Response quality alignment |
| Evaluation | `gbharti/finance-alpaca` (unseen split, index 500-510) | 10 questions | Testing on unseen data |

**Dataset note:** `gbharti/finance-alpaca` is a Reddit-sourced finance Q&A dataset. It contains personal finance advice in informal style. No separate preference dataset exists for this domain — preference pairs were constructed by using ground truth as chosen and truncated responses as rejected.

---

## Fine-Tuning Pipeline

```
Base Model: unsloth/Llama-3.2-1B
            ↓
Stage 1: Non-Instruction Fine-Tuning
  → Raw finance text (265 chunks from 500 paragraphs)
  → Teaches domain language and terminology
  → Training loss: 2.48
            ↓
Stage 2: Instruction Fine-Tuning (SFT)
  → 85 finance Q&A pairs in Alpaca format
  → Teaches question-answering behavior
  → Training loss: 0.92
            ↓
Stage 3: DPO Preference Alignment
  → 50 chosen/rejected preference pairs
  → Teaches response quality preference
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
| Quantization | 4-bit NF4 (QLoRA) |
| Max sequence length | 512 tokens |

**Training hyperparameters:**

| Parameter | Stage 1 | Stage 2 | Stage 3 |
|---|---|---|---|
| Learning rate | 2e-4 | 2e-4 | 5e-5 |
| Batch size | 2 | 2 | 2 |
| Gradient accumulation | 4 | 4 | 4 |
| Effective batch size | 8 | 8 | 8 |
| Epochs | 3 | 3 | 1 |
| Warmup steps | 10 | 10 | 10 |
| LR scheduler | cosine | cosine | cosine |
| Beta (DPO) | — | — | 0.1 |

---

## Training Loss

| Stage | Final Loss | Interpretation |
|---|---|---|
| Stage 1 Non-instruction | 2.48 | Model learning finance domain language |
| Stage 2 SFT | 0.92 | Model learned Q&A format effectively |

---

## Before vs After — Output Comparison

**Question: Why would a car company lend me money at a very low interest rate?**

| Stage | Answer |
|---|---|
| Base model | A car company would lend you money at a very low interest rate because they want to make a profit. They would also want to make a profit on the car you buy. They would also want to make a profit... (repeated 10 times) |
| After SFT | Car companies borrow money from banks so that they can sell the loans at a profit to investors. If you are a car company and you are looking for capital, go to a bank. |
| After DPO | The car company is trying to build loyalty. You are getting a good deal. Keep them in business by buying their products. |

**Question: Under what circumstance will the IRS charge you a late-payment penalty?**

| Stage | Answer |
|---|---|
| Base model | The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. (repeated 7 times) |
| After SFT | You have 3 choices: pay immediately (zero cost), file a payment plan with the IRS, or go to court. Court is expensive. Get good legal counsel. |
| After DPO | The IRS will assess a late payment penalty for any unpaid tax not paid within 3 years from the due date. The due date is the 15th of the 4th month after the end of the tax year. |

---

## Evaluation Results

### Automatic Metrics (on 10 unseen test questions)

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore F1 |
|---|---|---|---|---|
| Base model | 0.180 | 0.030 | 0.136 | 0.804 |
| Stage 1 Non-instruction | 0.226 | 0.033 | 0.139 | 0.819 |
| Stage 2 SFT | 0.224 | 0.042 | 0.133 | 0.828 |
| Stage 3 DPO | 0.224 | 0.038 | 0.133 | 0.828 |

### Manual Evaluation (10 questions)

| Model | Wins |
|---|---|
| Base model | 0/10 |
| SFT model | 8/10 |
| DPO model | 1/10 |
| Neither | 2/10 |

---

## Final Observations

**What worked:**
- Non-instruction fine-tuning improved domain vocabulary — ROUGE-1 jumped from 0.180 to 0.226 and BERTScore from 0.804 to 0.819 using only raw text with no labels
- SFT eliminated repetition loops and question echoing completely — the most critical improvement
- SFT improved BERTScore to 0.828 — confirming semantic quality gain
- The pipeline is fully reproducible and modular — each stage builds on the previous adapter

**What did not work as expected:**
- DPO did not improve over SFT on automatic metrics — ROUGE and BERTScore stayed identical
- Q4 (stock transaction fees) and Q9 (DRIP) both failed across all three stages — dataset noise from Reddit-style answers introduced wrong answers that fine-tuning amplified
- ROUGE-L slightly dropped after SFT because the Alpaca response format differs structurally from ground truth Reddit-style answers — a known limitation of ROUGE for open-ended generation

---

## Challenges Faced

| Challenge | Solution |
|---|---|
| Unsloth incompatible with Apple Silicon M4 | Moved training to Kaggle T4 GPU |
| Chunks exceeding 512 token limit | Reduced chunking ceiling to 506 tokens with paragraph truncation |
| PicklingError during SFT checkpoint saving | Set `save_strategy="no"` and saved adapter manually |
| Colab session resets wiping model | Saved all adapters to Google Drive after each training stage |
| `gbharti/finance-alpaca` has no preference dataset | Constructed preference pairs by using ground truth as chosen and truncated responses as rejected |
| Banking77 dataset recommended by assignment has no Q&A responses | Used `gbharti/finance-alpaca` instead — intent classification datasets cannot be used for generative fine-tuning |

---

## Future Improvements

- **Compare fine-tuned model vs RAG pipeline** on same 10 questions — expected RAG will win on factual accuracy while fine-tuned model wins on response style and domain fluency
- **Stronger DPO training** — use base model outputs as rejected responses instead of truncated ground truth for stronger preference signal
- **Scale up** — use 500+ instruction pairs and 7B model to see clearer SFT and DPO gains
- **Deploy** — wrap `src/inference.py` in FastAPI + Streamlit for live demo
- **RAGAS evaluation** — add faithfulness, context precision, and answer relevance metrics

---

## Repository Structure

```
finance-ai-assistant/
├── data/
│   ├── non_instruction_data.txt      # Raw finance text (placeholder)
│   ├── instruction_dataset.jsonl     # 100 Q&A pairs format reference
│   └── preference_dataset.jsonl      # 50 preference pairs format reference
├── notebooks/
│   ├── non_instruction_finetuning.ipynb  # Stage 1 training
│   ├── instruction_finetuning.ipynb      # Stage 2 SFT training
│   └── dpo_alignment.ipynb               # Stage 3 DPO training
├── reports/
│   ├── base_model_evaluation.md      # Base model performance on 10 questions
│   ├── sft_model_comparison.md       # Base vs SFT comparison
│   ├── final_evaluation.md           # 3-way comparison with metrics
│   └── fine_tuning_explanation.md    # Concepts explained in own words
├── src/
│   └── inference.py                  # Load DPO model and generate answers
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

---

## Project Story for Interviews

> "I built a finance FAQ assistant by fine-tuning Llama-3.2-1B using Unsloth and QLoRA through three stages. Stage 1 adapted the base model to finance domain language using raw text — eliminating the need for labeled data at this stage. Stage 2 used 85 instruction-response pairs to teach question-answering behavior, eliminating repetition loops and question echoing that the base model exhibited on all 10 test questions. Stage 3 applied DPO alignment using preference pairs. The most significant finding was that DPO did not improve over SFT on automatic metrics with 50 pairs, which led me to understand that preference alignment requires larger, higher-quality datasets and bigger models to show measurable gains. I evaluated using ROUGE and BERTScore on unseen test data and documented honest findings including failure cases."

---

## Tech Stack

`Unsloth` · `TRL` · `PEFT` · `HuggingFace Transformers` · `Datasets` · `PyTorch` · `ROUGE Score` · `BERTScore` · `Google Colab` · `Kaggle` · `Python 3.10`
