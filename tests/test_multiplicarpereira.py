from funciones.multiplicarpereira import multiplicarpereira

def test_multiplicarpereira():
    assert multiplicarpereira(3, 4) == 12
    assert multiplicarpereira(-2, 5) == -10
