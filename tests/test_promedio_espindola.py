from funciones.promedio_espindola import promedio_espindola

def test_promedio_espindola():
    assert promedio_espindola([2, 4, 6]) == 4
    assert promedio_espindola([]) is None