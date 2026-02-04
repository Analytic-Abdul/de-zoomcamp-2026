import sys
print('arguments', sys.argv)
day = sys.argv[1]

import pandas as pd
df= pd.DataFrame({"A":[1,2], "B":[3,4]})
print(f"created a {len(df)} row table")

df.to_parquet(f"parquet_for_day_{day}.parquet")
print("Job finished successfully")
