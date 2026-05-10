# Write a function analyzePhotoCollection that takes an array of brightness values (0-100) and a 
# scanner purchase date string (format: "YYYY-MM-DD"), then returns a dictionary with three 
# pieces of information about your photo collection.

# Calculate the average brightness of all photos, check if more than five photos are worth 
# keeping (brightness > 30), and determine if the scanner is still under warranty 
# (purchased within the last 2 years from today's date "2024-01-15").

from datetime import datetime, timedelta
import ast

def analyzePhotoCollection(brightness_values, purchase_date):
    # Write code here 
    # Calculate average brightness
    average_brightness = sum(brightness_values) / len(brightness_values) 

    # Check if more than five photos are worth keeping
    photos_to_keep = [value for value in brightness_values if value > 30]
    more_than_five = len(photos_to_keep) > 5

    # Determine if the scanner is still under warranty
    today = datetime.strptime("2024-01-15", "%Y-%m-%d")
    purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
    warranty_period = timedelta(days=365 * 2)
    under_warranty = (today - purchase_date) <= warranty_period

    # Return the results as a dictionary
    return {
        "average_brightness": average_brightness,
        "more_than_five_worth_keeping": more_than_five,
        "under_warranty": under_warranty
    }

# Example usage:
brightness_values = ast.literal_eval(input())
purchase_date = input()
result = analyzePhotoCollection(brightness_values, purchase_date)
print(result)