import random
from enum import Enum
from .classes.operators.equation import Equation
from .classes.operators.addition import Addition
from .classes.operators.multiplication import Multiplication
from .classes.operators.subtraction import Subtraction

class Equation_Type(Enum):
    ADDITION = "Addition",
    MULTIPLICATION = "Multiplication",
    SUBTRACTION = "Subtraction"

def get_equation_types(has_addition: bool, has_multiplication: bool, has_subtraction: bool) -> list[Equation_Type]:
    types = []
    if has_addition:
        types.append(Equation_Type.ADDITION)
    if has_multiplication:
        types.append(Equation_Type.MULTIPLICATION)
    if has_subtraction:
        types.append(Equation_Type.SUBTRACTION)
    return types

def get_equation_by_type(type: Equation_Type, left: int, right: int) -> Equation:
    match type:
        case Equation_Type.ADDITION:
            return Addition(left, right)
        case Equation_Type.MULTIPLICATION:
            return Multiplication(left, right)
        case Equation_Type.SUBTRACTION:
            return Subtraction(left, right)

# Creates a list of all possible equations with a given max integer
# If max = 2 => [(1,1), (1,2), (2,1), (2,2)]
def create_equation_table(max: int, has_addition: bool, has_multiplication: bool, has_subtraction: bool) -> list[Equation]:
    if not has_addition and not has_multiplication and not has_subtraction:
        raise Exception("At least one equation type must be true")
    table = []
    equation_types = get_equation_types(has_addition, has_multiplication, has_subtraction)
    for i in range(1, max + 1):
        for j in range(1, max + 1):
            equation_type = equation_types[random.randint(0, len(equation_types) - 1)]
            table.append(get_equation_by_type(equation_type, i, j))
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