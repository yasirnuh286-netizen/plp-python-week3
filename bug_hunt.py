name = "Yasir"
age = 20

# BUG: Unclosed print string (missing closing quote)
print("Welcome to the Bug Hunt lab!")

# BUG: Misspelled variable name (was 'nam' instead of 'name')
print("Hello, " + name)

# BUG: Integer concatenation type mismatch (converted 'age' to string using str())
print("Next year you will be " + str(age + 1))