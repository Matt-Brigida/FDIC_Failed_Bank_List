import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

# latest_data = pd.read_csv("./data/latest_data.csv")

# read data from pkl which keeps column type
latest_data = pd.read_pickle("./data/latest_data.pkl")
previous_data = pd.read_pickle("./data/previous_data.pkl")


previous_data.fail_year.value_counts()
latest_data.fail_year.value_counts()


# see column names
latest_data.columns.values

# create only

failure_count = latest_data["Closing Date"].value_counts()

# convert t oquarterly data-------
failure_count_df = pd.DataFrame(failure_count)

bank_failures_quarterly = failure_count_df.resample('QS').sum()

# quarterly failures from Q3 2000 to Q3 2019
bank_failures_quarterly.columns.values[0] = "num_failures"

# plot
bank_failures_quarterly.plot()
plt.show()

# Get FRED data on GDP growth and run a poisson regression
# Downloaded the data manually

gdp = pd.read_csv("./data/gdp_growth.csv")





# convert to percent change
# we actally don't want to use this
bank_failures_quarterly.pct_change()
