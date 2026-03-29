# Create a program that helps manage your diner's daily operations. You'll calculate the average customer
# satisfaction score from total points and review count, filter out dishes with ratings below your quality
# threshold, and determine how many positions the daily specials board was rotated when someone accidentally bumped it.

# Read the total satisfaction points and number of reviews
total_points = int(input())
review_count = int(input())

# TODO: Calculate the average satisfaction score (total_points / review_count)
# Store it in a variable called average_score
average_score = total_points / review_count

# Read the quality threshold
threshold = float(input())

# Read the number of dishes on the menu
num_dishes = int(input())

# Read each dish and its rating
dishes_above_threshold = []
for i in range(num_dishes):
    dish_info = input()  # Format: "DishName Rating"
    infos = dish_info.split(" ")
    name = infos[0]
    rating = float(infos[1])

    # Check if rating is >= threshold
    if rating >= threshold:
        dishes_above_threshold.append(name)

# Read the original order of daily specials (space-separated)
original_specials = input().split()

# Read the current order of daily specials (space-separated)
current_specials = input().split()

# TODO: Figure out how many positions the board was rotated
# Hint: Find where the first item of original_specials appears in current_specials
# Store the rotation count in a variable called rotation_positions
rotation_positions = current_specials.index(original_specials[0])

# Output the results
print(average_score)
print(len(dishes_above_threshold))
for dish in dishes_above_threshold:
    print(dish)
print(rotation_positions)