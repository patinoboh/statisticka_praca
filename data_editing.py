import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


data_path = "dataset/supermarket/archive/customer_shopping_data.csv"
updated_data_path = "dataset/supermarket/archive/customer_shopping_data_parsed.csv"


# Load the data

data = pd.read_csv(data_path)


# Add new column with total price
data["total"] = data["quantity"] * data["price"]


# Drop unncecessary columns
data.drop(["invoice_no", "customer_id", "invoice_date", "quantity", "price", "shopping_mall"], axis="columns", inplace=True)


# Where is 60% females and 40% males in the dataset,
# we want this to be equal so I have to drop some males

males = data[data["gender"] == "Male"];females = data[data["gender"] == "Female"];
difference = females.shape[0] - males.shape[0]
dropped_samples = females.sample(n=difference, random_state=1)
data = data.drop(dropped_samples.index)


# Credit card and debit card are the same thing for our purposes

data["payment_method"] = data["payment_method"].map({"Debit Card": "Card", 
                                                     "Credit Card": "Card",
                                                     "Cash": "Cash"})



# Save data in new file

data.to_csv(updated_data_path, index=False)