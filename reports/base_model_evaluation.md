# Base Model Evaluation

**Model:** `unsloth/Llama-3.2-1B` (base, no fine-tuning)
**Date:** July 12, 2026
**Domain:** Finance & Banking FAQ

## Evaluation Table

| # | Question | Base Model Answer | Problem |
|---|---|---|---|
| 1 | Does wash sale apply if I buy stock on 2 different dates and sell it later | Yes, wash sale applies. The wash sale rule states that if you sell a stock before you buy it back, you will have to pay tax on the profit you made. | Factually incorrect — wash sale applies to losses, not gains |
| 2 | Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes? | Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes (repeated 7 times) | Question echoing — repeats question instead of answering |
| 3 | Are there any disadvantages to DHA Investment Properties? | Yes. The main disadvantage is that DHA Investment Properties are located in the heart of the city in a high-rise building which can make it difficult for investors to access. | Hallucination — fabricated claims about high-rise buildings |
| 4 | Stock Trade Transaction Fee - at what point is it worth it | The stock trade transaction fee is at what point is it worth it? (repeated 10 times) | Repetition loop — echoes question continuously |
| 5 | Why would a car company lend me money at a very low interest rate? | A car company would lend you money at a very low interest rate because they want to make a profit. They would also want to make a profit on the car you buy. (repeated) | Repetition loop — same sentence repeated 10+ times |
| 6 | Swap hedging a currency hedge | Swap hedging a currency hedge | Question echoing — no answer provided at all |
| 7 | Under what circumstance will the IRS charge you a late-payment penalty for taxes? | The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. (repeated 7 times) | Repetition loop — no specific circumstances mentioned |
| 8 | Buy car vs lease vs long term rent for 10 years period | The car is the best option because it will save the company money in the long run. The car will also be more reliable and easier to maintain. (repeated 10 times) | Repetition loop — no comparison of lease vs rent vs buy |
| 9 | How do dividend reinvestment purchases work? | Dividend reinvestment purchases work by allowing you to purchase more shares of a stock at a lower price. This is done by purchasing at a lower price and selling at a higher price. (repeated) | Repetition loop + factually wrong — DRIP is not about buying low and selling high |
| 10 | Are traders 100% responsible for a stock's price changes? | No. Traders are not 100% responsible. Traders are responsible for the risk of their investments. Traders are not responsible for the price of the stock. (repeated) | Repetition loop — provides no explanation of actual factors |

## Summary

**Key observations:**
- 7 out of 10 responses show repetition loops — model repeats the same sentence 8-10 times
- 2 out of 10 responses echo the question itself instead of answering (Q2, Q6)
- 0 out of 10 responses use proper finance domain terminology
- 1 out of 10 responses contain hallucinated facts (Q3 — DHA high-rise claim)

**Key failure modes identified:**

| Failure Mode | Questions Affected |
|---|---|
| Repetition loop | Q4, Q5, Q7, Q8, Q9, Q10 |
| Question echoing | Q2, Q6 |
| Hallucination | Q3 |
| Factually incorrect | Q1 |

**Missing domain-specific terminology:**
- No use of: wash sale rule, DRIP, capital gains tax rates, IRS penalty thresholds, currency swap mechanics, lease NPV analysis, dividend reinvestment

**Conclusion:**
Base model is not suitable for finance domain Q&A without fine-tuning. It lacks domain knowledge, instruction-following ability, and produces repetitive low-quality responses on all 10 finance-specific questions.
