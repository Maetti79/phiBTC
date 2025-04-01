# simulate_phiBTC.py

from model_phiBTC import PhiBTCModel
from fetch_data import DataFetcher

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
