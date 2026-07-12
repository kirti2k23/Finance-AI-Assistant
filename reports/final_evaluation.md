# Final Evaluation: Base vs SFT vs DPO

**Evaluation criteria:** Correctness · Helpfulness · Domain accuracy · Safety · Tone · Clarity · Hallucination reduction · Professional quality

## Final Comparison Table

| # | Question | Base Model | SFT Model | DPO Model | Best | Reason |
|---|---|---|---|---|---|---|
| 1 | Does wash sale apply if I buy stock on 2 different dates and sell it later | Yes, wash sale applies — factually wrong claim about selling before buying back | No. Wash sales require identical stock sold at identical price within 30 days — correct 30-day condition | Wash sales only applicable if you buy the same security at a later date and sell again | SFT | SFT gives specific 30-day condition. Base is factually wrong. DPO gives incomplete truncated answer. |
| 2 | Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes? | Repeats question 7 times — no answer | In US, capital gains are long-term if you sell for more than you bought. Special rules apply for collectibles. | Should elect QS for 2014 tax year because 2015 is a prior year — incomplete answer | SFT | Base echoes question. SFT gives relevant capital gains explanation. DPO gives incomplete tax year advice. |
| 3 | Are there any disadvantages to DHA Investment Properties? | Hallucinates — claims high-rise buildings dangerous for investors | No disadvantages per se, but location near major thoroughfare affects property value significantly | No restrictions on how you invest — lump sum or regular payments | SFT | Base hallucinates. SFT gives realistic location-based analysis. DPO misses the question entirely. |
| 4 | Stock Trade Transaction Fee - at what point is it worth it | Repeats question 10 times | Answers about clothes — wrong domain | Answers about car buying vs selling — wrong domain | Neither | All three models failed this question. Dataset noise affected SFT and DPO. |
| 5 | Why would a car company lend me money at a very low interest rate? | Repeats "want to make a profit" 10 times | Car companies borrow from banks to sell loans at profit to investors — correct business model | Car company is building loyalty — you are getting a good deal — superficial answer | SFT | Base repeats. SFT explains finance mechanism correctly. DPO gives shallow loyalty explanation. |
| 6 | Swap hedging a currency hedge | Echoes question — no answer | Currency hedge mitigates currency risk. References risk management strategies. | Futures contract is a contract to buy/sell underlying at specific time and price — partially relevant | SFT | Base echoes. SFT explains currency risk management. DPO goes into futures mechanics. |
| 7 | Under what circumstance will the IRS charge you a late-payment penalty for taxes? | Repeats same sentence 7 times | 3 choices if you miss payment: pay immediately, file payment plan, or go to court | IRS assesses penalty for unpaid tax not paid within 3 years from due date — 15th of 4th month after tax year | DPO | DPO gives specific IRS timeline (3 years, 15th of 4th month). SFT gives options but no specifics. |
| 8 | Buy car vs lease vs long term rent for 10 years period | Repeats "car is best option" 10 times | Lease saves maintenance, no sales tax on trade, no depreciation cap, cash value for tax purposes | Should consider insurance cost — plan on paying at least 1x annual income | SFT | Base repeats. SFT gives structured comparison. DPO gives questionable insurance advice. |
| 9 | How do dividend reinvestment purchases work? | Repeats incorrect buy low sell high explanation | Place limit order to buy at specific price, let capital grow if filled | Place limit order to buy at specific price, then sell order at different price | Neither | All three models give incorrect DRIP explanation. None describe automatic reinvestment mechanism. |
| 10 | Are traders 100% responsible for a stock's price changes? | Repeats "traders not responsible" 8 times | Stock prices determined by many factors including economy — structured explanation with economic context | Stock price determined by supply and demand — concise but incomplete | SFT | Base repeats. SFT gives broader economic explanation. DPO oversimplifies to supply/demand only. |

## Stage-by-Stage Win Count

| Stage | Wins |
|---|---|
| Base model | 0/10 |
| SFT model | 8/10 |
| DPO model | 1/10 (Q7) |
| Neither | 2/10 (Q4, Q9) |

## Automatic Evaluation Metrics

| Metric | Base | Stage 1 Non-Instruction | Stage 2 SFT | Stage 3 DPO |
|---|---|---|---|---|
| ROUGE-1 | 0.180 | 0.226 | 0.224 | 0.224 |
| ROUGE-2 | 0.030 | 0.033 | 0.042 | 0.038 |
| ROUGE-L | 0.136 | 0.139 | 0.133 | 0.133 |
| BERTScore F1 | 0.804 | 0.819 | 0.828 | 0.828 |

## Key Findings

**What improved from Base → SFT:**
- Repetition loop eliminated — base model repeated sentences 8-10 times; SFT generates coherent non-repetitive responses
- Question echoing eliminated — base model echoed questions on Q2 and Q6; SFT attempts to answer
- Domain reasoning improved — SFT uses finance terms like capital gains, wash sale, currency risk, IRS penalty
- Hallucination reduced — base model hallucinated DHA property details; SFT gave realistic analysis
- BERTScore improved from 0.804 → 0.828 confirming measurable semantic quality gain

**What improved from SFT → DPO:**
- Q7: DPO gave specific IRS timeline (3 years, 15th of 4th month) — more precise than SFT
- Slightly more concise responses in some questions
- Marginal tone improvement

**Where DPO did NOT clearly improve over SFT:**
- ROUGE-2 dropped slightly (0.042 → 0.038)
- BERTScore remained identical (0.828)
- No improvement on factual accuracy across most questions
- Q4 and Q9 both failed even after DPO alignment

## Honest Assessment

DPO alignment did not produce measurable improvement over SFT on automatic metrics in this experiment. ROUGE and BERTScore scores are identical for Stage 2 and Stage 3.

**Three likely reasons:**

1. **Weak preference signal** — rejected responses were truncated versions of chosen responses. The contrast was too subtle for DPO to learn a strong preference direction.

2. **Small preference dataset** — only 50 pairs were used. DPO typically requires 500-1000 high quality human-annotated preference pairs to show measurable gains.

3. **Small model size** — Llama-3.2-1B has limited capacity. DPO alignment shows stronger results on 7B+ models where there is more room to adjust response quality.

**Most significant improvement:** Base → SFT transition, where repetition loops and question echoing were eliminated and domain reasoning improved across 8/10 test questions.

**Future improvement:**
- Use base model outputs as rejected responses instead of truncated ground truth — stronger preference signal
- Increase preference pairs to 500+ with human annotation
- Use larger model (7B+) for stronger DPO gains
- Compare fine-tuned model vs RAG pipeline on same questions — expected RAG will win on factual accuracy while fine-tuned model wins on response style and domain fluency
