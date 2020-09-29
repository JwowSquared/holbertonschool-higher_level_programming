def magic_string():
    magic_string.counter += 1
    return ("Holberton, " * magic_string.counter) + "Holberton"
magic_string.counter = -1
