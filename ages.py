import numpy as np

def categorize_age(interval, dato):
    for i, age in enumerate(interval):
        if interval[i] <= dato["age"] <= interval[i+1]:
            return np.ceil(age)

def categorize_ages(interval, data):
    interval = np.append(interval, np.inf)
    for index, dato in data.iterrows():
        data.loc[index, "age"] = categorize_age(interval, dato)
    return data