def noNegativo(n: int | float) -> bool:
    if (n < 0):
        return False
    return True

def igual(n: int | float, p: int | float) -> int:
    if (n == p):
        return True
    return False

def comprobarCedula(n: str) -> bool:
    if (len(n) == 8):
        return True
    return False

def noVacio(n: str) -> bool:
    if (len(n) <= 0):
        return False
    return True

def noNumeros(n: str) -> bool:
    s = "1234567890"
    for e in n:
        if e in s:
            return False
    return True