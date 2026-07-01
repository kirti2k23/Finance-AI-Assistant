# SFT Model Comparison: Base vs Instruction Fine-Tuned

**Base model:** `unsloth/Llama-3.2-1B`
**SFT model:** Stage 2 adapter — trained on 100 finance Q&A pairs
**Evaluation criteria:** Correctness · Domain accuracy · Clarity · Helpfulness · Less generic

## Comparison Table

| # | Question | Base Model Answer | SFT Model Answer | Better | Reason |
|---|---|---|---|---|---|
| 1 | What is a mutual fund SIP? | | | | |
| 2 | What is the difference between a savings account and a fixed deposit? | | | | |
| 3 | How does compound interest work? | | | | |
| 4 | What is a credit score and why does it matter? | | | | |
| 5 | How can I save tax under Section 80C? | | | | |
| 6 | What is the repo rate and how does it affect loans? | | | | |
| 7 | What is the difference between term insurance and whole life insurance? | | | | |
| 8 | How does the stock market work? | | | | |
| 9 | What is a demat account and how do I open one? | | | | |
| 10 | What is the difference between a mutual fund and an ETF? | | | | |

## Summary

- SFT model wins on [X/10] questions
- Improvements observed: [terminology / specificity / India context / tone]
- Remaining weaknesses: [hallucination / too verbose / missing context]
