# simulate_phiBTC.py

from model_phiBTC import PhiBTCModel
from fetch_data import DataFetcher
import matplotlib.pyplot as plt
import datetime

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

    # Print results
    print("Φ(t):", round(phi, 4))
    print("Predicted BTC Price:", round(predicted_price, 2), "USD")

    # Plot predicted price
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    plt.figure(figsize=(6, 4))
    plt.bar(['Predicted BTC Price'], [predicted_price], color='orange')
    plt.title(f"ΦBTC Prediction\n{now}")
    plt.ylabel("USD")
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()
