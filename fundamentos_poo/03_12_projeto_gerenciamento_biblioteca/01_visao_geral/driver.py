# Neste desafio, você implementará a base para um Sistema de Gerenciamento de Biblioteca.

# Edite library.py para implementar as classes necessárias seguindo os comentários TODO. 
# O arquivo driver contém cenários de teste extensivos que validam sua implementação.

# Siga os comentários TODO em library.py para orientação passo a passo
# Implemente a classe Library com a inicialização e representação de string adequadas

# TODO: Import the Library class from library.py
# Use format: from library import Library
from library import Library

# Comprehensive test case handler
test_case = input()

if test_case == "basic_library_creation":
    # TODO: Create a library with name "Test Library"
    # TODO: Print the library object (this will call the __str__ method)
    lib = Library("Test Library")
    print(lib.__str__())
    
elif test_case == "library_attributes":
    # TODO: Create a library with name "Test Library"
    # TODO: Print the library's name attribute in the format: Name: Test Library
    # TODO: Print the length of the books list in the format: Books: 0
    # TODO: Print the length of the users list in the format: Users: 0
    # Hint: Use f-strings, e.g. print(f"Name: {library.name}")
    lib = Library("Test Library")
    print(f"Name: {lib.name}")
    print(f"Books: {len(lib.books)}")
    print(f"Users: {len(lib.users)}")

elif test_case == "multiple_libraries":
    # TODO: Create two different libraries with names "Library 1" and "Library 2"
    # TODO: Print both library objects
    lib1 = Library("Library 1")
    lib2 = Library("Library 2")
    print(lib1.__str__())
    print(lib2.__str__())

elif test_case == "empty_name":
    # TODO: Create a library with an empty string as the name
    # TODO: Print the library object
    lib = Library("")
    print(lib.__str__())

elif test_case == "special_characters":
    # TODO: Create a library with the name "!@#$%^&*()"
    # TODO: Print the library object
    lib = Library("!@#$%^&*()")
    print(lib.__str__())

elif test_case == "very_long_name":
    # TODO: Create a library with a name of exactly 100 'A' characters (use "A" * 100)
    # TODO: Print the library object
    lib = Library("A" * 100)
    print(lib.__str__())

elif test_case == "add_books_users":
    # TODO: Create a library with name "Test Library"
    # TODO: Add these items to the books list: ["Book1", "Book2", "Book3"]
    # TODO: Add these items to the users list: ["User1", "User2"]
    # TODO: Print the library object (should show updated counts)
    lib = Library("Test Library")
    lib.books = ["Book1", "Book2", "Book3"]
    lib.users = ["User1", "User2"]
    print(lib.__str__())

elif test_case == "empty_lists":
    # TODO: Create a library with name "Test Library"
    # TODO: Print the length of the books list in the format: Books length: 0
    # TODO: Print the length of the users list in the format: Users length: 0
    # Hint: Use f-strings, e.g. print(f"Books length: {len(library.books)}")
    lib = Library("Test Library")
    print(f"Books length: {len(lib.books)}")
    print(f"Users length: {len(lib.users)}")

elif test_case == "type_validation":
    # TODO: Create a library with the integer 123 as the name
    # TODO: Print the library object (should convert to string)
    lib = Library(123)
    print(lib.__str__())