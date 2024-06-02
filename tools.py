import ctypes
from typing import Any
class Cpp_tools:
    def __init__(self):
        self.l = {}
    def append(self, x,y):
        self.l[y] = x
    def __getattr__(self, name) -> ctypes.CDLL|Any:
        return self.l[name]