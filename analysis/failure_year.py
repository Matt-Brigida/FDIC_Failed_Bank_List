
import pandas as pd

latest_data = pd.read_csv("./data/latest_data.csv")

# read data from pkl which keeps column type
latest_data = pd.read_pickle("./data/latest_data.pkl")
previous_data = pd.read_pickle("./data/previous_data.pkl")


previous_data.fail_year.value_counts()
latest_data.fail_year.value_counts()


# see column names
latest_data.columns.values

# create only

failure_count = latest_data["Closing Date"].value_counts()

failure_count_df = pd.DataFrame(failure_count)

# failure_count.set_index('Closing Date', inplace=True)

failure_count_df.resample('QS').sum()


            


