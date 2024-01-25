import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv("shampoo.csv")
data.columns = ["Month", "Sales"]
data.set_index("Month", inplace=True)

size = int(len(data) * 0.66)
train, test = data[0:size], data[size : len(data)]

model = ARIMA(train, order=(5, 1, 0))
fitted_model = model.fit()

print(fitted_model.summary())

forecast = fitted_model.forecast(len(test), 0.05)  # 95% confidence
forecast = pd.Series(forecast, index=test.index)

plt.figure(figsize=(14, 7))
plt.plot(train, label="Training")
plt.plot(test, label="Actual")
plt.plot(forecast, label="Forecast")
plt.title("Forecast vs Actuals")
plt.legend()
plt.show()
