# Implemente o template.py e o driver.py com encapsulamento e métodos adequados. 
# Siga os comentários TODO para orientação passo a passo.

from template import Template

# Test case handler
test_case = input()

if test_case == "basic_test":
    # TODO: Create a Template object with name "Test Name"
    # TODO: Call the display_info() method on the object
    test = Template("Test Name")
    test.display_info()
elif test_case == "validation_test":
    # TODO: Create a Template object with name "Validation Test"
    # TODO: Print the name using the name property in format: "Name: {obj.name}"
    ttest = Template("Validation Test")
    print(f"Name: {ttest.name}")