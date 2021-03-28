# Notes on Quant Finance

### 1. Algorithmic trading

Advances in telecommunications and computer technologies during the past decade have cre ated increasingly global, dynamic, and complex financial markets, which in turn have stimulated trading by computer programs and the rise of systems for algorithmic trading. Related and confused terms include electronic trading, order-management systems, automated trading, systematic trading, and algorithmic trading. Central to these systems’ operation are financial protocols, such as the __Financial Information Exchange (FIX) protocol__, a series of messaging specifications for the electronic communication of trade-related messages.

<p align="center">
  <img src="Algorithmic Trading Model.jpg" width="900" height="467">
</p>

* __Pre-trade analysis__: is the most common use of algorithms within a trading environment. It analyzes financial data or news with the aim of forecasting future price movement or volatility in order to emcompass any system that uses financial data or news to analyze certain properties of an asset.
  * Alpha model: predicts the future behavior of the financial instruments to trade.
  * Risk model: evaluates the levels of exposure/risk associated with the financial instruments.
  * Transaction cost model: calculates the (potential) costs associated with trading the financial instruments.
* __Trading signal generation__: takes as its inputs the results of the alpha, risk, and transaction cost models and decides what portfolio of financial instruments should be owned going forward and in what quantities and what specific prices. It might even include risk management recommendations, such as specific stop-loss values. In this stage, the trading strategy can be replayed against historical market data to simulates its performance.
  * Index fund rebalancing strategies: consists of the portfolio construction model. Index funds have defined periods of rebalancing to bring their holdings to par with their respective benchmark indices.
  * Mean reversion (Trading range): is based on the concept that the high and low prices of an asset are a temporary phenomenon that revert to their mean value (average value) periodically.
  * Momentum (Trend-following) strategies: follow trends in moving averages, channel breakouts, price level movements, and related technical indicators. These are the easiest and simplest strategies to implement through algorithmic trading because these strategies do not involve making any predictions or price forecasts.
  * Arbitrage Opportunities: Buying a dual-listed stock at a lower price in one market and simultaneously selling it at a higher price in another market offers the price differential as risk-free profit or arbitrage.
  * Mathematical Model-based Strategies: allow trading on a combination of options and the underlying security. For example, delta neutral is a portfolio strategy consisting of multiple positions with offsetting positive and negative deltas—a ratio comparing the change in the price of an asset, usually a marketable security, to the corresponding change in the price of its derivative—so that the overall delta of the assets in question totals zero.
  * Volume-weighted Average Price: is a measurement that shows the average price of a security, adjusted for its volume. It is used by traders who wish to see a smoothed-out indication of a security’s price over time or used by larger traders who need to ensure that their trades do not move the price of the security they are trying to buy or sell.
  * Time-weighted average price strategy breaks up a large order and releases dynamically determined smaller chunks of the order to the market using evenly divided time slots between a start and end time. The aim is to execute the order close to the average price between the start and end times thereby minimizing market impact.
  * Percentage of Volume: This algorithm continues sending partial orders according to the defined participation ratio and according to the volume traded in the markets.
  * Implementation shortfall strategy: Implementation shortfall is the sum of execution costs and the opportunity cost incurred in case of adverse market movement between the time of the trading decision and order execution, and is a form of slippage (slippage refers to the difference between the expected price of a trade and the price at which the trade is executed). Hence, implementation shortfall strategy aims at minimizing the execution cost of an order by trading off the real-time market, thereby saving on the cost of the order and benefiting from the opportunity cost of delayed execution.
  * Sniffing strategy: Uses the buy side of a large order. Such detection through algorithms will help the market maker identify large order opportunities and enable them to benefit by filling the orders at a higher price.
* __Trade execution__: determines how best to execute the trade to minimize market impact and timing risk. To execute a trade, an order must be submitted to a trading venue, with the choice depending on several factors including order size, trading mechanism, and degree of trader’s anonymity. The system must also determine orders to submit to trading venues. Also, a system might break a large order into several smaller orders to minimize the trade’s impact on the market, because a small order is more likely to flow under the market’s radar than a large order.
  * Execution model: executes the trades, making several decisions with constraints on (actual) transaction costs and trading duration. The most general decision is the trading strategy followed by the venue and order type.
*  __Post-trade analysis__: evaluates the performance of the trade.

Example 1: 
Objective: replicate the FTSE 100 index by trading a subset of stocks (that is, not the entire index) that provides a similar performance to the index while minimizing the transaction costs naturally incurred when rebalancing any replicating portfolio. 
In pretrade analysis, the system compares and contrasts the historical performances of several index-tracking strategies to help the user select the strategy that best suits
current market conditions. The other components work toward implementing the chosen replicating strategy. Specifically, the trading signal component selects the stocks for
constructing the benchmark portfolio and determines the weight of each stock in the portfolio.
After all of the portfolio composition decisions have been made, the trade-execution component determines how best to execute the trade to minimize market impact and timing risk. Strategies in trading signal generation and trade execution are formulated as an optimization problem with multiobjective constraints.

__Pre-trade analysis__  is built on the basis of fundamental analysis, technical analysis and quantitative analysis.
#### 1. Fundamental analysis
Fundamental analysis involves a detailed study of related information that might affect asset prices with the aim of determining the asset’s fair value (or its potential future
price movements). The idea that the current market price for an asset is not equivalent to its fair value contradicts the somewhat controversial efficient-market hypothesis, which suggests that the current price is a reflection of all the available information. They used advanced mathematical and statistical models from machine learning and computational statistics to determine the relationship between the stock price’s future value and its fundamental quantities with the aim of identifying stocks with a potential to appreciate (or depreciate) significantly.
#### 2. Technical analysis
Technical analysis aims to predict future price movements based on asset price history and, sometimes, related trading information such as trade volume. By assuming
that the market’s price reflects all relevant information, technical analysis seeks to identify and exploit price movement patterns rather than examine the underlying factors affecting asset prices.
#### 3. Quantitative analysis
Quantitative analysis treats asset prices as random and uses mathematical and statistical analysis to find a suitable model for describing this randomness. Quantitative analysis is generally related to the pricing of derivative products, whose fair value relies on the underlying asset’s stochastic property as well as the analysis of the temporal convergence and divergence of price movements of pairs and baskets of assets.

