import sys
args = sys.argv
print("arguments",args)
day = int(args[1])

import pandas as pd
df = pd.DataFrame({"A":[1,2],"B":[3,4]})
df.head()

print(f"data loaded for day:{day}")
