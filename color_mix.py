r = 'Red'         # Assigns 'Red' to variable r
g = 'Green'       # Assigns 'Green' to variable g
b = 'Blue'        # Assigns 'Blue' to variable b
Dot = '.'         # Assigns '.' (dot symbol) to variable Dot

# This line prints multiple elements separated by spaces
print(
    r,            # → 'Red'
    b,            # → 'Blue'
    g,            # → 'Green'
    b,            # → 'Blue'
    r + g + b,    # Concatenates strings → 'RedGreenBlue'
    b,            # → 'Blue'
    g + b + Dot   # Concatenates → 'GreenBlue.'
)

print('')         # Adds an empty line at the end
