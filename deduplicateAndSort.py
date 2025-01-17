# Python code​​​​​​‌‌​​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌‌​‌‌ below
# Use print("messages...") to debug your solution.

def prepare_list(animals): # animals is a list of strings 
    # Your code goes here
    # need to deduplicate this list, i have read that a set perserves unique records only
    unique = set(animals)
    sorted_set = sorted(unique)
    return sorted_set
