import random
import math
from scipy.stats import norm, chi2

def generar_numeros_aleatorios(n):
    numeros_aleatorios = []
    for _ in range(n):
        numero = random.random()
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

def media(X):
    return sum(X)/len(X)



#########################################################################

def limite_inferior_varianza(alpha, n):
    chi2_li = chi2.ppf(alpha/2, n-1)
    return chi2_li / (12* (n - 1))

def limite_superior_varianza(alpha, n):
    chi2_ls = chi2.ppf(1 - (alpha/2), n-1)
    return chi2_ls / (12* (n - 1))


def varianza(X):
    mu_var = media(X)
    acumulado = 0
    for x in X:
        acumulado += (x - mu_var)**2
    return acumulado / (len(X) - 1)

def get_limites_varianza(li, ls):
    print(f'EL valor del limite inferior de la varianza es {li}')
    print(f'EL valor del limite superior de la varianza es {ls}')

def prueba_varianza(X, alpha):
    var = varianza(X)
    li_var = limite_inferior_varianza(alpha, len(X))
    ls_var = limite_superior_varianza(alpha, len(X))

    if li_var <= var <= ls_var:
        print(f'El valor de la varianza = {var} se encuentra entre los limites de aceptación')
    else:
        print(f'El valor de la varianza = {var} NO se encuentra entre los limites de aceptación')

    get_limites_varianza(li_var, ls_var)


if __name__ == '__main__':
    X = generar_numeros_aleatorios(100)
    print(X)
    aceptacion = 95
    alpha = 1 - (aceptacion / 100)

    prueba_varianza(X, alpha)