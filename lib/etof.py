from qiskit import QuantumCircuit
from qiskit.circuit.gate import Gate
from typing import List, Optional


def etof(controls: List[Optional[bool]]) -> Gate:
    n = len(controls)
    qc = QuantumCircuit(n + 1, name="ETOFF")

    for qubit, control in zip(range(n), controls):
        if control is not None and not control:
            qc.x(qubit)

    controlling_qubits = []
    for qubit, control in zip(range(n), controls):
        if control is not None:
            controlling_qubits.append(qubit)

    qc.mct(controlling_qubits, n, mode="noancilla")

    for qubit, control in zip(range(n), controls):
        if control is not None and not control:
            qc.x(qubit)

    return qc.to_gate()
