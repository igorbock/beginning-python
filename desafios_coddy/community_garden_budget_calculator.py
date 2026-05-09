# Write a function calculate_garden_budget that takes soil_cost, seeds_cost, and tools_cost and returns 
# the total cost needed for setting up a community garden plot.

# Arthur, the mustachioed volunteer coordinator, needs to calculate the total budget required for 
# each new garden plot including soil preparation, fiddleneck seeds, and basic gardening tools.

# Parameters:

# soil_cost (float): Cost of soil preparation
# seeds_cost (float): Cost of seeds and plants
# tools_cost (float): Cost of basic gardening tools
# Returns: Total cost as a float. Format: 125.50

def calculate_garden_budget(soil_cost, seeds_cost, tools_cost):
    # Write code here 
    total_cost = soil_cost + seeds_cost + tools_cost
    return float(total_cost)

num1 = input()
num2 = input()
num3 = input()

result = calculate_garden_budget(float(num1), float(num2), float(num3))
print(result)