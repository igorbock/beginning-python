def show_hierarchy(cls):
    # TODO: Print the class hierarchy for the given class
    # TODO: Print "Class hierarchy for [class name]:"
    # TODO: Use cls.__mro__ to iterate through and print each class name in the hierarchy
    print(f"Class hierarchy for {cls.__name__}:")
    for item in cls.__mro__:
        print(item.__name__)