# simulate_phiBTC.py

from model_phiBTC import PhiBTCModel
from fetch_data import DataFetcher
import matplotlib.pyplot as plt
import datetime
import requests


def fetch_actual_btc_price():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': 'bitcoin', 'vs_currencies': 'usd'}
    response = requests.get(url, params=params)
    data = response.json()
    return data['bitcoin']['usd']


if __name__ == '__main__':
    # Initialize model and fetcher
    model = PhiBTCModel()
    fetcher = DataFetcher()

    # Get real-time data
    data = fetcher.get_latest_inputs()

    # Compute Φ(t)
    phi = model.compute_phi(data)

    # Predict BTC price
    predicted_price = model.predict_price(phi)

    # Fetch actual BTC price
    actual_price = fetch_actual_btc_price()

    # Print results
    print(f"Φ(t): {phi:.4f}")
    print(f"Predicted BTC Price: ${predicted_price:.2f} USD")
    print(f"Actual BTC Price: ${actual_price:.2f} USD")

    # Plot predicted vs actual price
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    labels = ['Predicted BTC Price', 'Actual BTC Price']
    prices = [predicted_price, actual_price]
    plt.figure(figsize=(8, 5))
    plt.bar(labels, prices, color=['orange', 'blue'])
    plt.title(f"ΦBTC Prediction vs Actual Price\n{now}")
    plt.ylabel("Price (USD)")
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()
