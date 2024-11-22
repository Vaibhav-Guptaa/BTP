import pandas as pd
from pmdarima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX
import csv

def read_csv_to_nested_list(file_path):
    nested_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        # Strip any extra spaces from the headers
        headers = [header.strip() for header in headers]
        
        # Find index of 'date' and 'y' columns
        date_idx = headers.index('date')
        y_idx = headers.index('y')
        
        # Read the remaining rows
        for row in reader:
            date = row[date_idx].strip()
            y_value = float(row[y_idx].strip())
            nested_list.append([date, y_value])
    
    return nested_list

# Example usage
file_path = 'Line Plot.csv'  # Replace with the path to your CSV file
data = read_csv_to_nested_list(file_path)
print(data , len(data))

# Step 1: Convert nested list to DataFrame
df = pd.DataFrame(data, columns=["date", "y"])
df["date"] = pd.to_datetime(df["date"])  # Convert date strings to datetime
df.set_index("date", inplace=True)       # Set 'Date' as the DataFrame index

df = df.groupby("date").mean()

# Now set the date as the index
df = df.asfreq('15D').interpolate(method='linear')

print(df)


##########################################################################################
# Step 2: Use auto_arima to determine the best order and seasonal_order
# Since the data is weekly and we want quarterly seasonality, set `m=13`
auto_model = auto_arima(df["y"], 
                        seasonal=True,  
                        trace=True,
                        m = 13,
                        error_action='ignore', 
                        suppress_warnings=True, 
                        stepwise=True)  # Set D = 0

# Retrieve the best p, d, q and seasonal P, D, Q values
order = auto_model.order
seasonal_order = auto_model.seasonal_order

print("Optimal order:", order)
print("Optimal seasonal order:", seasonal_order)

# Step 3: Fit SARIMAX model with the identified parameters
model = SARIMAX(df["y"], order=order, seasonal_order=seasonal_order)
sarimax_model = model.fit(disp=False)

# Step 4: Forecast (e.g., forecast the next 10 weeks)
forecast = sarimax_model.get_forecast(steps=10)
predicted_values = forecast.predicted_mean

print(predicted_values)
