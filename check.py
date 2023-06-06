import json
import pandas as pd

with open("teamConfig.json", "r") as teamConfigFile:
    data = json.load(teamConfigFile)
    # print(data)
    df = pd.DataFrame(data)
    # print(df)
    ids = df["shortName"]
    duplicates = df[ids.isin(ids[ids.duplicated()])].sort_values("shortName")
    print(duplicates)
