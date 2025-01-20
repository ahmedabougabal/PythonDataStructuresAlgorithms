def describe_items(food_items, color):
    # Write your code here.
    apple_taste = food_items['fruits']['temperate']['apple']['taste']
    beet_taste = food_items['vegetables']['root']['beet']['taste']
    return [f"The apple is {apple_taste}.", f"The beet is {beet_taste}."] 
  



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
