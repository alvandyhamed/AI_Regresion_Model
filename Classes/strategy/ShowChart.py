from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


class ShowChart(ABC):
    @abstractmethod
    def show_chart(self, *args, **kwargs):
        pass


class ShowChartStoke(ShowChart):
    def show_chart(self, data):
        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label='Close Price')
        plt.title('Apple Stock Price')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()


class ShowChartPerdict(ShowChart):
    def show_chart(self, y_test, predicted_prices):
        plt.figure(figsize=(10, 5))
        plt.plot(y_test, label='Real Prices', color='blue', alpha=0.6)
        plt.plot(predicted_prices, label='Predicted Prices', color='red', alpha=0.6)
        plt.title('Real vs Predicted Stock Prices')
        plt.xlabel('Samples')
        plt.ylabel('Price')
        plt.legend()
        mse = mean_squared_error(y_test, predicted_prices)
        plt.text(0, min(y_test), f'MSE: {mse:.2f}', fontsize=12, color='black', bbox=dict(facecolor='white', alpha=0.5))

        plt.show()
