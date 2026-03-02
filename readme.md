# CAPM Analysis of the Indian Paint Sector

## Overview

This project implements the **Capital Asset Pricing Model (CAPM)** to analyze the relationship between stock returns and systematic market risk within the Indian paint industry.

The study estimates beta coefficients, evaluates statistical assumptions, and compares risk exposure across multiple companies in the sector. The objective is to demonstrate practical applications of financial econometrics using Python and real market data.

## Objectives

- Compute stock and market returns from historical price data
- Estimate CAPM parameters (alpha and beta) using OLS regression
- Perform regression diagnostics (heteroskedasticity and normality tests)
- Compare systematic risk across firms within the same industry
- Generate reproducible results and visualizations

## Methodology

The CAPM framework is given by:

```
Ri = αi + βi Rm + εi
```

Where:

- Ri = Asset return  
- Rm = Market return  
- βi = Systematic risk (market sensitivity)  
- αi = Abnormal return component  

Steps implemented:

1. Download price data using `yfinance`
2. Compute log returns
3. Estimate CAPM parameters using `statsmodels` OLS
4. Perform diagnostic tests:
   - White test (heteroskedasticity)
   - Normality test
5. Compare betas across companies
6. Export results for reproducibility

## Sector Studied

The analysis focuses on major companies in the Indian paint industry:

- Asian Paints
- Berger Paints
- Shalimar Paints
- Akzo Nobel India
- Kansai Nerolac

## Results

The analysis reveals meaningful variation in systematic risk across firms:

- Large firms exhibit higher market sensitivity
- Smaller firms show lower beta and weaker explanatory power
- Diagnostic tests indicate acceptable regression assumptions for most cases

A summary of results is exported in:

```
results/capm_sector_results.csv
```

## Project Structure

```
capm-financial-analysis/
│── notebooks/
│     capm_analysis.ipynb
│
│── src/
│     capm.py
│
│── results/
│     capm_sector_results.csv
│
│── requirements.txt
│── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the notebook:

```bash
jupyter notebook notebooks/
```

The notebook performs:

- Sector analysis
- Beta comparison
- Regression diagnostics
- Visualization

## Applications

This framework can be extended to:

- Portfolio construction
- Cost of equity estimation
- Risk management
- Sector comparison studies
- Quantitative equity research

## Author

Vishal K  
BITS Pilani Hyderabad  
Finance | Machine Learning | Quant Finance Enthusiast  

## Disclaimer

This project is for educational and research purposes only and does not constitute financial advice.
