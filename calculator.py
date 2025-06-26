def add (i, j): 
    return i + j

def sub (i, j):
    return i - j

def mult (i, j):
    return i * j

def div (i, j):
    if j == 0:
        raise ValueError("Cannot divide by 0")
    return i / j

