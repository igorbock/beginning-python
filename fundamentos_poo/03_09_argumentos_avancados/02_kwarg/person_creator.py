def create_person(**kwargs):
    # Note: kwargs is already a dictionary — no need to convert it!
    # TODO: Print "Person created with properties:"
    # TODO: Loop through each key-value pair in kwargs
    # TODO: Print each key-value pair on a new line in the format "key: value"
    print("Person created with properties:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")