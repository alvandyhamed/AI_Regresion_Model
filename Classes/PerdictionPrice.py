import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from Classes.strategy.ShowChart import ShowChartStoke, ShowChartPerdict


class PredictionPrice:
    def __init__(self, stock_symbol, start_date, end_date):
        self.stock_symbol = stock_symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        self.predicted_prices = None
        self.show_char = ShowChartStoke()
        self.show_perdict_chart = ShowChartPerdict()

    def get_stock_data(self):
        self.data = yf.download(self.stock_symbol, start=self.start_date, end=self.end_date)

    def labeled(self):
        self.data['Prediction'] = self.data['Close'].shift(-1)
        self.data.dropna(inplace=True)
        return self.data

    def learning(self):
        X = np.array(self.data[['Close']])
        y = np.array(self.data['Prediction'])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("تعداد داده‌های آموزشی:", len(self.X_train))
        print("تعداد داده‌های تست:", len(self.X_test))

    def regression(self):
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        score = self.model.score(self.X_test, self.y_test)
        print(f"دقت مدل: {score * 100:.2f}%")

    def prediction(self):
        self.predicted_prices = self.model.predict(self.X_test)

    def run(self):
        self.get_stock_data()
        self.labeled()
        self.learning()
        self.regression()
        self.prediction()
        self.show_perdict_chart.show_chart(self.y_test, self.predicted_prices)
