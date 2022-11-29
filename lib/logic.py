from typing import List


class Variable(object):
    def __init__(self, index, inv=False):
        self.index: int = index
        self.inv: bool = inv

    def __str__(self) -> str:
        return f"x{self.index}" + ("'" if self.inv else "")

    def __repr__(self) -> str:
        return str(self)

    def to_latex(self) -> str:
        if self.inv:
            return f"\overline{{x_{self.index}}}"
        else:
            return f"x_{self.index}"


class Disjunction(list):
    def __str__(self) -> str:
        if len(self) == 1:
            return str(self[0])
        return "(%s)" % " + ".join([el.to_latex() for el in self])

    def __repr__(self) -> str:
        return str(self)

    def to_latex(self) -> str:
        if len(self) == 1:
            return self[0].to_latex()
        return "(%s)" % " \lor ".join([el.to_latex() for el in self])


class ExclusiveDisjunction(list):
    def __str__(self) -> str:
        if len(self) == 1:
            return str(self[0])
        return "(%s)" % " ^ ".join([el.to_latex() for el in self])

    def __repr__(self) -> str:
        return str(self)

    def to_latex(self) -> str:
        if len(self) == 1:
            return self[0].to_latex()
        return "(%s)" % " \oplus ".join([el.to_latex() for el in self])


class Conjunction(list):
    def __str__(self) -> str:
        if len(self) == 1:
            return str(self[0])
        return "(%s)" % " * ".join([el.to_latex() for el in self])

    def __repr__(self) -> str:
        return str(self)

    def to_latex(self) -> str:
        if len(self) == 1:
            return self[0].to_latex()
        return "(%s)" % " \land ".join([el.to_latex() for el in self])


class CNF(Conjunction):
    def __init__(self, clauses: List[List[Variable]]):
        super().__init__()
        for clause in clauses:
            self.append(Disjunction(clause))


V = Variable


def dj_to_xdj(disj: Disjunction):
    mut = disj.copy()
    while len(mut) > 1:
        xdj = ExclusiveDisjunction()
        xdj.append(mut[0])
        xdj.append(mut[1])
        xdj.append(Conjunction([mut[0], mut[1]]))
        mut = [xdj] + mut[2:]
    return mut[0]


def cnf_to_cxf(cnf: CNF):
    cxf = Conjunction()
    for disjunction in cnf:
        cxf.append(dj_to_xdj(disjunction))
    return cxf
