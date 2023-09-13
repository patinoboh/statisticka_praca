import numpy as np

def categorize_age(interval, dato):
    for i, age in enumerate(interval):
        if interval[i] <= dato["age"] <= interval[i+1]:
            dato["age"] = age
            return dato

def categorize_ages(interval, data):
    # for each data categorize the age        
    interval = np.append(interval, np.inf)
    for dato in data:
        dato = categorize_age(interval, dato)
    return data