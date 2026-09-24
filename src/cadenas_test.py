#from cadenas import estiliza_mensaje
def invierte_cadena():
    cadena_invertida = ""
    cadena = input("Ingrese una cadena para invertirla: ")
    for i in range(0,len(cadena)):
        cadena_invertida += cadena[-(1+i)]
    print (cadena_invertida)
invierte_cadena()
"""
def test_estiliza_mensaje():
    print("Probando estiliza_mensaje...")
    assert estiliza_mensaje("Fundamentos de programación 1") == "FuNdAmEnToS dE pRoGrAmAcIóN 1"
    assert estiliza_mensaje("Murciélago", usa_dieresis=True) == "MüRcÏéLäGö"
    assert estiliza_mensaje("Soy un programador experto", sustituye_espacios="*") == "SoY*uN*pRoGrAmAdOr*ExPeRtO"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=False, usa_dieresis=True, sustituye_espacios="-") == "Hölä-Mündö"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=True, usa_dieresis=False, sustituye_espacios="_") == "HoLa_MuNdO"

test_estiliza_mensaje()
print("Todas las pruebas pasaron correctamente.")
"""