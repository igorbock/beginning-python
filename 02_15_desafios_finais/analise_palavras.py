# Crie uma função chamada analyze_text que analisa palavras em uma string de texto.

# Sua função deve:

# Contar palavras únicas (insensível a maiúsculas e minúsculas)
# Encontrar todas as palavras que aparecem mais de uma vez
# Identificar todas as palavras palíndromas (palavras que se leem da mesma forma de frente para trás, como "level")
# Retorne um dicionário com três chaves:

# unique_count: o número de palavras únicas (conte também palavras repetidas uma vez cada)
# repeated_words: uma lista ordenada de palavras que aparecem mais de uma vez
# palindromes: uma lista ordenada de palavras palíndromas
# Notas:

# Trate as palavras como insensíveis a maiúsculas e minúsculas (ex.: "Hello" e "hello" são a mesma palavra)
# Remova qualquer pontuação (.,!?:;"()) das palavras
# Ordene alfabeticamente tanto as listas repeated_words quanto palindromes
# Exemplo de Entrada:
# "Madam saw a racecar. Dad said hello hello to mom."

# Saída Esperada:
# {
#     'unique_count': 9,
#     'repeated_words': ['hello'],
#     'palindromes': ['a', 'dad', 'madam', 'mom', 'racecar']
# }

def analyze_text(text):
    # 1. Split the text into words and normalize them
    # Remove pontuação e converte para minúsculas
    punctuation = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    normalized_text = ''.join(char.lower() if char not in punctuation else ' ' for char in text)
    words = normalized_text.split()

    # 2. Count the occurrences of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # 3. Find the number of unique words
    unique_count = len(word_count)

    # 4. Identify repeated words (appearing more than once)
    repeated_words = sorted([word for word, count in word_count.items() if count > 1])

    # 5. Find palindrome words
    palindromes = sorted([word for word in word_count.keys() if word == word[::-1]])

    # 6. Return the results in a dictionary with sorted lists
    return {
        'unique_count': unique_count,
        'repeated_words': repeated_words,
        'palindromes': palindromes
    }

print(analyze_text("Wow! Did Hannah see that Race car? Mom was there too. Hannah did see it!"))
print(analyze_text("Madam in Eden, I'm Adam! Eve saw diamond? Madam saw live evil. Live not on evil, madam, live not on evil."))