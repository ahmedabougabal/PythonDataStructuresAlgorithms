def build_menu(cakes):
    # Your code goes here
    new_key = max(cakes.keys()) + 1 
    cakes[new_key] = ['Coffee', 1.49]
    my_list = list(cakes.values())
    flattened_list = [i for sublist in my_list for i in sublist]
    formatted_pairs_list=[]
    for i in range(0, len(flattened_list), 2):
        item_name = flattened_list[i]
        price = flattened_list[i+1]

        formatted_price = f"${price}"

        formatted_pair = f"{item_name} Cake - {formatted_price}"

        formatted_pairs_list.append(formatted_pair)

        formatted_pairs_list.sort(reverse=True)

    return formatted_pairs_list




# the following 2 lines of code are for flattening a list of lists , cakes is a dict
    # my_list = list(cakes.values())
    # flattened_list = [i for sublist in my_list for i in sublist]


# This is how your code will be called.
# Your answer should be a list of strings conforming to 
# the instructions.
# You can edit this code to try different testing cases.
cakes = {
		100: ["Carrot", 1.99], 
		101: ["Chocolate", 1.99], 
		102: ["Strawberry", 2.19], 
		103: ["Spice", 2.29], 
		104: ["Vanilla", 1.79]
		}


