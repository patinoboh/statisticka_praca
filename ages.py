def categorize_ages(categories, data):
    """
    Categorize ages into categories
    """
    data["age"] = data["age"].apply(lambda x: categories[x])
    return data