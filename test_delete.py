import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = "dataset/supermarket/archive/customer_shopping_data.csv"
data = pd.read_csv(data_path)

clothing_data = data[data["category"] == "Clothing"]
a = clothing_data["price"].unique()
b = clothing_data["quantity"].unique()
print(a)
print(b)

print(data["price"].unique().shape[0])