# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Droping missing values

# %% load packages
from numpy import nan as NA

# %% generate sample data
df = pd.DataFrame([\
    [1.3, 2.3, 5.2], \
    [2.1, NA, NA], \
    [NA,NA,NA], \
    [NA, 9.2, 2.3]])

# %% print the raw data
df

# console output:
#      0    1    2
# 0  1.3  2.3  5.2
# 1  2.1  NaN  NaN
# 2  NaN  NaN  NaN
# 3  NaN  9.2  2.3

# %% print only rows of non-missing values
df.dropna()

# console output:
#      0    1    2
# 0  1.3  2.3  5.2

# %% drop only completely missing rows
df.dropna(how='all')

# console output:
#      0    1    2
# 0  1.3  2.3  5.2
# 1  2.1  NaN  NaN
# 3  NaN  9.2  2.3

# %% drop rows with two or more missing values
df.dropna(thresh=2)

# console output:
#      0    1    2
# 0  1.3  2.3  5.2
# 3  NaN  9.2  2.3

# %% drop rows for which the first columns
# contains missing values
df.dropna(subset=[0])

# console output:
#      0    1    2
# 0  1.3  2.3  5.2
# 1  2.1  NaN  NaN

