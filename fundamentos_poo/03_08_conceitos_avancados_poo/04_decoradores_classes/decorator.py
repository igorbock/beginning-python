def add_counter(cls):
    # Inicializa os contadores na classe
    cls.call_counts = {"add": 0, "subtract": 0}

    # Guarda os métodos originais
    original_add = cls.add
    original_subtract = cls.subtract

    # Define wrappers que incrementam contadores e chamam o original
    def wrapped_add(self, a, b):
        self.__class__.call_counts["add"] += 1
        return original_add(self, a, b)

    def wrapped_subtract(self, a, b):
        self.__class__.call_counts["subtract"] += 1
        return original_subtract(self, a, b)

    # Substitui os métodos na classe
    cls.add = wrapped_add
    cls.subtract = wrapped_subtract

    return cls