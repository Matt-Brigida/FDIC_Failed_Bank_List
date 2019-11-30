import pandas as pd

latest_data = pd.read_csv("./data/latest_data.csv")

# read data from pkl which keeps column type
latest_data = pd.read_pickle("./data/latest_data.pkl")
previous_data = pd.read_pickle("./data/previous_data.pkl")

