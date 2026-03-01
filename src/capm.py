import yfinance as yf
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import het_white
import scipy.stats as stats


def download_returns(ticker, start, end, interval="1mo"):
    data = yf.download(
    ticker,
    start=start,
    end=end,
    interval=interval,
    progress=False,
    auto_adjust=False
)
    returns = np.log(data["Close"] / data["Close"].shift(1)).dropna()
    return returns


def run_capm(stock, market="^BSESN", start="2020-04-06", end="2025-04-06"):
    stock_ret = download_returns(stock, start, end)
    market_ret = download_returns(market, start, end)

    df = pd.concat([market_ret, stock_ret], axis=1).dropna()
    df.columns = ["Market", "Stock"]

    X = sm.add_constant(df["Market"])
    y = df["Stock"]

    model = sm.OLS(y, X).fit()

    beta = model.params["Market"]
    alpha = model.params["const"]

    # Diagnostics
    white_test = het_white(model.resid, model.model.exog)
    normal_test = stats.normaltest(model.resid)

    return {
        "stock": stock,
        "alpha": alpha,
        "beta": beta,
        "r_squared": model.rsquared,
        "white_test_pvalue": white_test[1],
        "normality_pvalue": normal_test.pvalue,
        "model": model,
        "data": df
    }


def plot_security_line(result):
    df = result["data"]
    model = result["model"]
    stock = result["stock"]

    X = sm.add_constant(df["Market"])

    plt.figure(figsize=(6,4))
    plt.scatter(df["Market"], df["Stock"], alpha=0.7)
    plt.plot(df["Market"], model.predict(X), color="red")
    plt.xlabel("Market Returns")
    plt.ylabel("Stock Returns")
    plt.title(f"Security Characteristic Line: {stock}")
    plt.show()


def run_sector_analysis(stocks):
    results = []

    for s in stocks:
        res = run_capm(s)
        results.append(res)

    summary = pd.DataFrame([
        {
            "Stock": r["stock"],
            "Alpha": r["alpha"],
            "Beta": r["beta"],
            "R_squared": r["r_squared"],
            "White_p": r["white_test_pvalue"],
            "Normality_p": r["normality_pvalue"]
        }
        for r in results
    ])

    return summary, results


def plot_beta_comparison(summary):
    plt.figure(figsize=(8,5))
    plt.bar(summary["Stock"], summary["Beta"])
    plt.ylabel("Beta")
    plt.title("CAPM Beta Comparison Across Paint Sector")
    plt.xticks(rotation=45)
    plt.show()