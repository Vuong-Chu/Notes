# Notes on Quant Finance

### 1. Algorithmic trading

Advances in telecommunications and computer technologies during the past decade have cre ated increasingly global, dynamic, and complex financial markets, which in turn have stimulated trading by computer programs and the rise of systems for algorithmic trading. Related and confused terms include electronic trading, order-management systems, automated trading, systematic trading, and algorithmic trading. Central to these systems’ operation are financial protocols, such as the __Financial Information Exchange (FIX) protocol__, a series of messaging specifications for the electronic communication of trade-related messages.

<p align="center">
  <img src="Algorithmic Trading.jpg" width="533" height="467">
</p>

* Pre-trade analysis: is the most common use of algorithms within a trading environment. It analyzes financial data or news with the aim of forecasting future price movement or volatility in order to emcompass any system that uses financial data or news to analyze certain properties of an asset.
  * Alpha model: predicts the future behavior of the financial instruments to trade.
  * Risk model: evaluates the levels of exposure/risk associated with the financial instruments.
  * Transaction cost model: calculates the (potential) costs associated with trading the financial instruments.
* Trading signal generation:
  * Portfolio construction model: consists of the portfolio construction model. This model takes as its inputs the results of the alpha, risk, and transaction cost models and decides what portfolio of financial instruments should be owned going forward and in what quantities.
*  Trade execution: determines how best to execute the trade to minimize market impact and timing risk.
  * Execution model: executes the trades, making several decisions with constraints on (actual) transaction costs and trading duration. The most general decision is the trading strategy followed by the venue and order type.
*  Post-trade analysis:

Example: 
Objective: replicate the FTSE 100 index by trading a subset of stocks (that is, not the entire index) that provides a similar performance to the index while minimizing the transaction costs naturally incurred when rebalancing any replicating portfolio.


