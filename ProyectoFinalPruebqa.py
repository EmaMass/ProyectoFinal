import ctypes as c

lib = c.CDLL(r'Debug\ProyectoFinal.dll')

print(lib.wincondition(11))