import pandas as pd
import researchpy as rp
import scipy.stats as stats

# To load a sample dataset for this demonstration
import statsmodels.api as sm

df = sm.datasets.webuse("citytemp2")

print("here")
# print(rp.summary_cat(df[["agecat", "region"]]))
