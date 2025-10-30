import pandas as pd
import nfl_data_py as nfl

schedules = nfl.import_schedules([2024])

records = get_team_records(2024)

print(records)

