
# %%
import pandas as pd
import re

CLEAN_CODES = "code_list.csv"
DATAPATH = "raw_codes.txt"
CODES_SHEET = "raw_list.xlsx"

# %%
codes = pd.read_excel(CODES_SHEET)
codes.head()
# %%
raw_codes = (codes["comment"].to_list())
print(raw_codes)

# %%
processed_comments = []
for i in raw_codes:
    print(i)
    author,comment = i.split("]:")
    processed_comments.append(comment)

print(processed_comments)
    
# %%
processed_comments = pd.DataFrame(processed_comments)
processed_comments.to_csv(CLEAN_CODES, index=False)
# %%
