# 📈 ΦBTC — A Coherence-Based Bitcoin Valuation Model

## Overview
**ΦBTC** is a predictive model for Bitcoin’s exchange rate based on a weighted, log-domain sum of key systemic, network, and sentiment metrics. It blends crypto-native indicators (like hash rate, halving cycles, and liquidity) with macroeconomic stress and real-time sentiment, using a symbolic coherence function \( \Phi(t) \).

This repository includes:
- The mathematical model and assumptions
- Real-time data fetching tools (via public APIs)
- Live simulation + comparison to actual BTC/USD pricing
- A dashboard-ready prediction curve

---

## 🔣 Core Formula

\[
P_{\text{BTC}}(t) = P_0 \cdot \exp\left[\lambda \cdot \Phi(t)\right]
\]

Where:

\[
\Phi(t) = \omega_H \log H(t) + \omega_N \log N(t) + \omega_M M(t) + \omega_S S(t) + \omega_L \log L(t) + \omega_C C(t) + \omega_{\text{halv}} H_{\text{event}}(t)
\]

| Term                  | Meaning                                       |
|-----------------------|-----------------------------------------------|
| \( H(t) \)            | Network hash rate                             |
| \( N(t) \)            | Network usage (tx count / block size)         |
| \( M(t) \)            | Macro stress index (VIX, inflation, etc.)     |
| \( S(t) \)            | Sentiment polarity (Fear & Greed, news)       |
| \( L(t) \)            | Liquidity or volume                           |
| \( C(t) \)            | Regulatory signal (coherence/confidence)      |
| \( H_{\text{event}}(t) \) | Halving proximity index                |

---

## 🧰 Project Structure

```bash
📁 phiBTC-model
├── README.md                  # Project description & formula
├── model_phiBTC.py           # Core formula + weights
├── fetch_data.py             # API calls (CoinGecko, Blockchain.com)
├── simulate_phiBTC.py        # Run the model on real-time data
├── requirements.txt          # Dependencies
└── notebooks/
    └── PhiBTC_Dashboard.ipynb  # Live Jupyter notebook view
