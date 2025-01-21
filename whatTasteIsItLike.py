# def describe_items(food_items, color):
#     # Write your code here.
#     apple_taste = food_items['fruits']['temperate']['apple']['taste']
#     beet_taste = food_items['vegetables']['root']['beet']['taste']
#     return [f"The apple is {apple_taste}.", f"The beet is {beet_taste}."] 

from collections import deque
# iterative approach (most-effiecient O(N)- Breadth first Search)
def describe_items(food_items, color):
  result = []
  queue = deque(food_items.items())

  while queue:
    item_name , val = queue.popleft()
    # print("\nCurrent Queue Contents:") for debugging 
    # for item in queue:
    #     print(item)
    if isinstance(val, dict): # check if the current value is a dict 
      # then we have 2 possibilites 
      if val.get('color') == color:
        result.append(f"The {item_name} is {val['taste']}.")
      else: # Add child items to the queue for further processing
        queue.extend(val.items()) # we add unprocessed items to the right using extend and we pop from the left "BFS Under the hood to completely process the dict as a tree of nodes"

  return result



"""
levels traversed in BFS :  TIME COMPLEXITY IS O(N)

Level 1: 2 nodes (fruits, vegetables)
Level 2: 4 nodes (tropical, temperate, leafy, root)
Level 3: 8 nodes (mango, pineapple, apple, pear, spinach, kale, carrot, beet)
"""


# This is how your code will be called.
# Your answer should be a list. 
# You can edit this code to try different testing cases.
food_items = {
    'fruits': {
        'tropical': {
            'mango': {
                'color': 'orange',
                'taste': 'sweet',
                'nutrients': ['vitamin C', 'vitamin A', 'fiber']
            },
            'pineapple': {
                'color': 'yellow',
                'taste': 'tangy',
                'nutrients': ['vitamin C', 'manganese', 'fiber']
            }
        },
        'temperate': {
            'apple': {
                'color': 'red',
                'taste': 'sweet',
                'nutrients': ['vitamin C', 'fiber', 'potassium']
            },
            'pear': {
                'color': 'green',
                'taste': 'juicy',
                'nutrients': ['vitamin C', 'fiber', 'copper']
            }
        }
    },
    'vegetables': {
        'leafy': {
            'spinach': {
                'color': 'green',
                'taste': 'earthy',
                'nutrients': ['vitamin K', 'vitamin A', 'iron']
            },
            'kale': {
                'color': 'green',
                'taste': 'bitter',
                'nutrients': ['vitamin K', 'vitamin A', 'calcium']
            }
        },
        'root': {
            'carrot': {
                'color': 'orange',
                'taste': 'sweet',
                'nutrients': ['vitamin A', 'vitamin K', 'fiber']
            },
            'beet': {
                'color': 'red',
                'taste': 'earthy',
                'nutrients': ['vitamin C', 'folate', 'iron']
            }
        }
    }
}
#* ['The apple is sweet.', 'The beet is earthy.'] is the expected output.
# print(food_items.items())
print(describe_items(food_items, 'red'))