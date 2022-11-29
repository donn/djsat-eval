from numpy import (
    sqrt,
    transpose as t,
    array as a,
    matmul as mm,
    concatenate as cat,
    kron as tp,
)
from sympy import Matrix

from types import SimpleNamespace


def display_matrix(m):
    try:
        display(Matrix(m))
    except NameError:
        None


# Bras
k0 = a([[1], [0]])
k1 = a([[0], [1]])
kplus = (k0 + k1) / sqrt(2)
kminus = (k0 - k1) / sqrt(2)

# Kets
b0 = t(k0)[0]
b1 = t(k1)[0]
bplus = t(kplus)[0]
bminus = t(kminus)[0]

Bases = SimpleNamespace(
    zero=k0,
    one=k1,
    plus=kplus,
    minus=kminus,
    bras=SimpleNamespace(zero=b0, one=b1, plus=bplus, minus=bminus),
)

Gates = SimpleNamespace(
    h=a([[1, 1], [1, -1]]) / sqrt(2),
    cz=a([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]),
)

__all__ = ["Bases", "Gates", "mm", "cat", "tp", "display_matrix"]
