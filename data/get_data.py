
import pandas as pd

url_latest = "https://www.fdic.gov/bank/individual/failed/banklist.csv"
url_previous = "https://pfabankapi.app.cloud.gov/api/failures?fields=NAME%2CCERT%2CFIN%2CCITYST%2CFAILDATE%2CSAVR%2CRESTYPE%2CCOST%2CRESTYPE1%2CCHCLASS1%2CQBFDEP%2CQBFASSET&filters=FAILYR%3A%5B1934%20TO%202017%5D&limit=10000&react=true&sort_by=FAILDATE&sort_order=desc&subtotal_by=RESTYPE&total_fields=QBFDEP%2CQBFASSET%2CCOST&format=csv&download=true&filename=bank-data"

latest_data = pd.read_csv(url_latest)
previous_data = pd.read_csv(url_previous)

latest_data["Closing Date"] = pd.to_datetime(latest_data["Closing Date"])
latest_data["Updated Date"] = pd.to_datetime(latest_data["Updated Date"])

