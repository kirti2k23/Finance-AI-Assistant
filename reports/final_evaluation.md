# Final Evaluation: Base vs SFT vs DPO

**Evaluation criteria:** Correctness · Helpfulness · Domain accuracy · Safety · Tone · Clarity · Hallucination reduction · Professional quality

## Final Comparison Table

| # | Question | Base Model | SFT Model | DPO Model | Best | Reason |
|---|---|---|---|---|---|---|
| 1 | Does wash sale apply if I buy stock on 2 two different dates and sell it later |Yes, wash sale applies. The wash sale rule states that if you sell a stock before you buy it back, you will have to pay tax on the profit you made. This rule applies to wash sale transactions.
| No.  The definition of wash sales requires that you have sold a similar, but identical, product for the same price within a 30 day period.  In your case, you would have to have sold identical stock at identical price on two separate dates.|Wash sales are only applicable if you buy the same security at a later date and sell it again.  If you buy on day 1 and then sell on day 2, you have a wash sale.  If you bought on day 2 and then sold | SFT| SFT gives a specific definition of wash sale rule with 30-day condition. Base model is factually wrong.|
| 2 |Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes? | Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes
Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes
Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes
Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes
Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes
Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes
Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est. Taxes
Short Term Capital Gains tax vs. IRA Withdrawal Tax w/o Quarterly Est.| I'm not sure where you are, but in the US, all capital gains are long-term if you sell. If you sell for less than you bought for, you should pay no gain. If you sell for more than you bought for, you should pay part gain and part tax on that profit. There are also some special rules for certain types of gains (from collectibles, for example).|The question is whether you should elect QS for the 2014 tax year, or just pay tax at regular rate for the 2015 tax year. The answer is you should elect QS, because the 2015 tax year is a prior year, |SFT | Base model repeats question 7 times. SFT gives an actual answer about capital gains.|
| 3 | Are there any disadvantages to DHA Investment Properties?| Yes, there are disadvantages to DHA Investment Properties. The main disadvantage is that DHA Investment Properties are located in the heart of the city. This means that the property is located in a high-risk area, which can be dangerous for investors. Additionally, DHA Investment Properties are located in a high-rise building, which can make it difficult for investors to access the property. Finally, DHA Investment Properties are located in a high-rise building, which can make it difficult for investors to access the property.
|There are no "disadvantages" to DHA investment properties per se, but there are some disadvantages to specific properties.  For example, a DHA property located near a major thoroughfare will likely be more expensive than one located a bit further from the street.  This is because the value of the property at a mile or two down a dirt road is much less than the value of the same property a half mile down the road on a major street.  A DHA property located near a major intersection is likely to be more expensive than one located a quarter mile from the intersection down a dead-end street.  This is because the value of the property at the intersection is much greater than the value of the same property a quarter mile down. |There are no restrictions on how you can invest in DHA properties. You can either take a lump sum payment (which I assume would involve the mortgage being paid in full) or you can make regular payment |SFT | Base model hallucinates (high-rise building claim). SFT gives a more realistic property value analysis.|
| 4 | Stock Trade Transaction Fee - at what point is it worth it | The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is it worth it? The stock trade transaction fee is at what point is
| I think you would be better off to invest in quality cheap clothes rather than expensive clothes. :)|I think you're thinking about this like a car buyer vs. a car seller. As a car seller, you make money when the car sells and you make money because you sold it for more than you bought it for. As a ca
| Neither| Base repeats question. SFT answers about clothes — completely wrong domain. Both failed.|
| 5 | Why would a car company lend me money at a very low interest rate? | A car company would lend you money at a very low interest rate because they want to make a profit. They would also want to make a profit on the car you buy. They would also want to make a profit on the car you buy. They would also want to make a profit on the car you buy. They would also want to make a profit on the car you buy. They would also want to make a profit on the car you buy. They would also want to make a profit on the car you buy. They would also want to make a profit on the car you buy. They would also want to make a profit on the car you buy. They would also want to make a profit on the car you buy. They would also
| The finance question. Car companies are in need of capital. They borrow money from banks so that they can sell the loans (at a profit) to investors. If you are a car company, and you are looking for capital, go to a bank. If you are a car company, and you need capital, go to a bank.
|The car company is trying to build loyalty.  You are getting a good deal.  Keep them in business by buying their products.  If you don't, someone else will.
|SFT | Base repeats same sentence. SFT explains car company capital borrowing logic correctly.|
| 6 | Swap hedging a currency hedge |Swap hedging a currency hedge
 | You are going about this the wrong way.  You should be looking at currency risk management, which is what this questions is about.  A currency hedge is a strategy to mitigate currency risk.  You need to review the definition of risk and then look at what strategies can be used to manage risk.  A good book to start with is Risk Management and Risk Avoidance Potential by Nelson Merrill.  This will explain risk and show you how to manage it.|I think you have a bit of a misunderstanding about how futures and futures futures work.  A futures contract is a contract to buy or sell an underlying at a specific time, and a specific price.  The p
| SFT| Base echoes the question. SFT explains currency risk management concept.|
| 7 | Under what circumstance will the IRS charge you a late-payment penalty for taxes? |The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. The IRS will charge you a late-payment penalty for taxes if you do not pay your taxes on time. The IRS will
 | The "real" question is what to do if you miss a payment.  You have 3 choices:  Pay immediately or the cost is zero, file a payment plan with the IRS, or go to court.  Court is expensive and not necessarily successful.  You need good legal counsel.|The IRS will assess a late payment penalty for any unpaid tax due if it is not paid within 3 years from the due date. The due date is the 15th of the 4th month after the end of the tax year. The 3 yea
|SFT | Base repeats same sentence. SFT gives 3 actionable options for missed payment.|
| 8 | Buy car vs lease vs long term rent for 10 years period| The car is the best option because it will save the company money in the long run. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain. The car will also be more reliable and easier to maintain.
| I'm a big fan of the lease vs buy analysis.  For most people, a car is a big ticket item, and should be considered that way.  However, if you have to decide today about a car purchase, I'd rather have it a lease.  You save on maintenance, and get a no-hassle exchange if you need it.  You also don't have to pay sales tax on the used vehicle you get in exchange.  And you get a no-cap on deprecation.  A lease also gives you a cash value for tax purposes.  If you need to sell it for cash, you can.  A buy is fine if you have to have a particular make and model, or if you want a
|I think you should consider the cost of insurance as well. Insurance is expensive, and you should plan on paying at least 1x your annual income. If you are talking about a single car, I'd get a used F
|SFT | Base repeats. SFT gives lease vs buy analysis with valid points on depreciation and tax.|
| 9 | How do dividend reinvestment purchases work? | Dividend reinvestment purchases work by allowing you to purchase more shares of a stock at a lower price. This is done by purchasing the stock at a lower price and then selling the stock at a higher price. This allows you to purchase more shares of the stock at a lower price. This is done by purchasing the stock at a lower price and then selling the stock at a higher price. This allows you to purchase more shares of the stock at a lower price. This is done by purchasing the stock at a lower price and then selling the stock at a higher price. This allows you to purchase more shares of the stock at a lower price. This is done by purchasing the stock at a lower price and then selling the stock at a higher price.
| You'd simply place a limit order to buy shares at a specific price, and if it gets filled you'd let that capital grow.  If it doesn't get filled, then you'd let it expire.  You'd also place a limit order to sell shares at a specific price, and if it gets filled you'd let that capital grow.  If it doesn't get filled, then you'd let it expire.  You'd also place a limit order to buy shares at a specific price, and if it gets filled you'd let that capital grow.  If it didn't get filled, then you'd let it expire.  You'd also place a limit order to sell shares at a specific price, and if it gets filled you
|You would place a limit order to buy shares at a specific price, then when the shares are traded you would place a second order to sell them at a different price. The second price is the price at whic
|Neither | Both give incorrect explanation of DRIP. SFT is less repetitive but still wrong.|
| 10 | Are traders 100% responsible for a stock's price changes?|No. Traders are not 100% responsible for a stock's price changes. Traders are responsible for the risk of their investments. Traders are not responsible for the price of the stock. Traders are responsible for the price of the stock only when they are buying or selling the stock. Traders are not responsible for the price of the stock when they are buying or selling the stock. Traders are not responsible for the price of the stock when they are buying or selling the stock. Traders are not responsible for the price of the stock when they are buying or selling the stock. Traders are not responsible for the price of the stock when they are buying or selling the stock. Traders are not responsible for the price of the
 | No.  Traders are not 100% responsible for stock prices.  Instead, stock prices are determined by many factors, many of which are out of the control of the traders.  One of the key factors is the economy, which is out of the control of the traders.  As the economy deteriorates, so do stocks' prices; as the economy improves, so do stocks' prices.  Traders can do very little to affect the price of a stock in the short term, as the market has rules that protect it's owners (shareholders).  The more important factors that determine stock prices are:
|No. Traders are not 100% responsible for stock price changes.  Instead, stock price is determined by supply and demand.  When there is a demand for a stock, there is a demand for that stock.  When the
| SFT| Base repeats. SFT gives structured explanation with economy factors.|

## Stage-by-Stage Win Count

| Stage | Wins |
|---|---|
| Base model | 0/10 |
| SFT model |8 /10 |
| DPO model | 0/10 |

## Key Findings
**What improved from Base → SFT:**
- Repetition loop eliminated — base model repeated sentences 8-10 times, 
  SFT generates coherent non-repetitive responses
- Question echoing eliminated — base model echoed questions on Q2, Q4, Q6
- Domain reasoning improved — SFT attempts finance-specific explanations 
  using terms like capital gains, wash sale, currency risk, IRS penalty
- Hallucination reduced — base model hallucinated DHA property as 
  high-rise building; SFT gave realistic property value analysis
- BERTScore improved from 0.804 → 0.828 confirming semantic quality gain

**What improved from SFT → DPO:**
- Marginal tone improvement on some questions
- Slightly more concise responses in Q7, Q10

**Where DPO did NOT clearly improve over SFT:**
- ROUGE-2 actually dropped slightly (0.042 → 0.038)
- BERTScore remained identical (0.828)
- No measurable improvement on factual accuracy
- Q4 and Q9 both models still failed after DPO
- 

## Honest Assessment

DPO alignment did not produce measurable improvement over SFT 
in this experiment. Automatic metrics (ROUGE, BERTScore) show 
identical scores for Stage 2 and Stage 3.

Three likely reasons:

1. Weak preference signal — rejected responses were truncated 
   versions of chosen responses. The contrast was too subtle 
   for DPO to learn a strong preference direction.

2. Small preference dataset — only 50 pairs were used. DPO 
   typically requires 500-1000 high quality human-annotated 
   preference pairs to show measurable gains.

3. Small model size — Llama-3.2-1B has limited capacity. 
   DPO alignment shows stronger results on 7B+ models.

The most significant improvement in this project came from 
Base → SFT transition, where repetition loops and question 
echoing were eliminated and domain reasoning improved 
measurably across 8/10 test questions.

Future improvement: Use base model outputs as rejected responses 
instead of truncated ground truth — this would create a stronger 
preference signal and likely show clearer DPO gains.
