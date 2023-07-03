import random

# manos.py
"""
td - todos diferentes
1p - 1 par
2p - 2 pares
tercia - 3 iguales
full - 1 trio y 1 par
poker - 4 iguales
quintilla - todos iguales
"""
probabilidad = {'td':0.30240, '1p':0.50400, '2p':0.10800, 'tercia':0.07200, 'full':0.00900, 'poker':0.00450, 'quintilla':0.00010}
def quintilla(numero):
    digito1 = numero[0]
    for digito in numero:
        if digito != digito1:
            return False
    return True
def full(numero):
    # Conteo
    guia = dict.fromkeys(numero, 0)
    for digito in numero:
        guia[digito]+=1
    if(2 in guia.values() and 3 in guia.values()):
        return True
    return False
def poker(numero):
    if(tercia(numero)):
        # Conteo
        guia = dict.fromkeys(numero, 0)
        for digito in numero:
            guia[digito]+=1
        for conteo in guia.values():
            if conteo >= 4:
                return True
        return False
    else:
        return False
def tercia(numero):
    # Conteo
    guia = dict.fromkeys(numero, 0)
    for digito in numero:
        guia[digito]+=1
    # Impar
    for conteo in guia.values():
        if conteo >= 3:
            return True
    return False
def onep(numero):
    # Conteo
    guia = dict.fromkeys(numero, 0)
    for digito in numero:
        guia[digito]+=1
    # Par
    for conteo in guia.values():
        if conteo >= 2:
            return True
    return False
def twop(numero):
    # Conteo
    guia = dict.fromkeys(numero, 0)
    for digito in numero:
        guia[digito]+=1
    # Primer par
    # Solo si sabemos que había uno
    if onep(numero):
        par = None
        for conteo in guia.items():
            if conteo[1] >= 2:
                par = conteo[0]
                break
        # Quitamos el que había
        del guia[par]
        # Segundo par
        for conteo in guia.values():
            if conteo >= 2:
                return True
        return False
    else:
        return False
def td(numero):
    return not (len(numero) != len(set(numero)))
def tipo(numero):
    if quintilla(numero):
        return 'quintilla'
    elif poker(numero):
        return 'poker'
    elif full(numero):
        return 'full'
    elif tercia(numero):
        return 'tercia'
    elif twop(numero):
        return '2p'
    elif onep(numero):
        return '1p'
    else:
        return 'td'
    

# Nivel de verbose
entrada = input("Desea ver todos los detalles?(Y/N) >")
IMPRIMIR = (entrada == 'Y' or entrada == 'y')

# Generando numeros aleatorios

def generar_numeros_aleatorios(n):
    numeros_aleatorios = []
    for _ in range(n):
        numero = random.random()
        numeros_aleatorios.append(str(numero))
    return numeros_aleatorios

numeros = generar_numeros_aleatorios(100000)

# Leyendo números
numeros = []
ruta = "./data/numeros-poker-2.txt"
# ruta = "numeros-poker-2.txt"
with open(ruta, "r") as archivo:
    for linea in archivo:
        numeros.append(linea[2:7])
    archivo.close()

# Mostrando números
if IMPRIMIR:
  print(numeros)

# Frecuencia observada
fo = {'td':0, '1p':0, '2p':0, 'tercia':0, 'full':0, 'poker':0, 'quintilla':0}
# Frecuencia esperada
fe = {'td':0, '1p':0, '2p':0, 'tercia':0, 'full':0, 'poker':0, 'quintilla':0}
# Calculando frecuencia esperada
for tipo_mano in fe.keys():
    fe[tipo_mano] = len(numeros) * probabilidad[tipo_mano]

# Contando la frecuencia observada
for numero in numeros:
    fo[tipo(numero)] += 1
    if IMPRIMIR:
        print("#", numero)
        print("quintilla:", quintilla(numero))
        print("poker:", poker(numero))
        print("full:", full(numero))
        print("tercia:", tercia(numero))
        print("2p:", twop(numero))
        print("1p:", onep(numero))
        print("td:", td(numero))
        print("-"*5)

# Mostrar la frecuencia esperada y observada obtenida
if IMPRIMIR:
    print("#"*5, "Frecuencias", "#"*5)
    print(fe, "=", sum(fe.values()))
    print(fo, "=", sum(fo.values()))

# Calculando X^2
sum = 0.0
for tipo_mano in fe.keys():
    sum += ((fo[tipo_mano]-fe[tipo_mano])**2)/fe[tipo_mano]

# Resultado
print(sum, "< 7.81")
if sum < 7.81:
    print("No se rechaza que los números siguen una distribución uniforme")
else:
    print("Se rechaza que los números siguen una distribución uniforme")