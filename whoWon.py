def find_winner(player_scores):
    # Your code goes here
    my_list = []
    for score in player_scores.values():
        my_list.append(sum(score)/3)

    result =[]
    result.append(list(player_scores.keys())[my_list.index(max(my_list))])
    result.append(max(my_list))

    return result


# This is how your code will be called.
# Your answer should be a list.
# You can edit this code to try different testing cases.
player_scores = {
    'Arthur': [85, 90, 92],
    'Bela': [75, 80, 85],
    'Carol': [90, 92, 95],
    'Deepak': [87, 89, 91]
}

# result = Answer.find_winner(player_scores)



        