import random
from .classes.equation import Equation

# Creates a list of all possible equations with a given max mulitplier
# If max = 2 => [(1,1), (1,2), (2,1), (2,2)]
def create_times_table(max: int) -> list[Equation]:
    table = []
    for i in range(1, max + 1):
        for j in range(1, max + 1):
            table.append(Equation(i, j))
    return table

# Gets the list of equations for the game using a times table
# Interates through the given times_table to prevent repeating equations
def get_equation_list(times_table: list[Equation], count: int):
    i = 0
    equation_list = []
    times_table_copy = times_table[:]
    while i < count:
        # Reset the table if all options have been used
        if (len(times_table_copy) == 0):
            times_table_copy = times_table[:]
        index = random.randint(0, len(times_table_copy) - 1)
        equation_list.append(times_table_copy[index])
        del times_table_copy[index]
        i += 1
    return equation_list