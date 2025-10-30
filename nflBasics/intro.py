import nfl_data_py
import pandas as pd
import os

path = os.path.abspath("nfl_records_2024.csv")
records = pd.read_csv(path)
print(records.head())
print(records.columns)

teams = nfl.import_team_desc()

