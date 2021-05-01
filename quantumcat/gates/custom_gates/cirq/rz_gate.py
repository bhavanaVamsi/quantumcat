# (C) Copyright Artificial Brain 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import cirq
import numpy as np


class RZGate(cirq.Gate):
    def __init__(self, phi):
        super(RZGate, self).__init__()
        self.phi = phi

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        ilam2 = 0.5j * float(self.phi)
        return np.array([[np.exp(-ilam2), 0],
                         [0, np.exp(ilam2)]])


    def _circuit_diagram_info_(self, args):
        return "RZ"
