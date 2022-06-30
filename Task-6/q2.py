import pandas as pd
data = pd.read_csv("dataset.csv")

data["LotFrontage"].fillna(80, inplace = True)
data["Alley"].fillna("Grv;", inplace = True)
data["BsmtQual"].fillna("TA", inplace = True)
data["BsmtCond"].fillna("TA", inplace = True)
data["BsmtExposure"].fillna("No", inplace = True)
data["BsmtFinType1"].fillna("Unf", inplace = True)
data["BsmtFinType2"].fillna("Unf", inplace = True)

 
data.head(30)