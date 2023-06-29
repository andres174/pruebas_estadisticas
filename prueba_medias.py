import random
import math
from scipy.stats import norm

def generar_numeros_aleatorios(n):
    numeros_aleatorios = []
    for _ in range(n):
        numero = random.random()
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

def media(X):
    return sum(X)/len(X)

def limite_inferior_media(alfa, n):
    alpha_limite = 1 - alpha + alpha / 2
    z = norm.ppf(alpha_limite, loc=0, scale=1)
    return 0.5 - z * (1 / math.sqrt(12 * n))

def limite_superior_media(alfa, n):
    alpha_limite = 1 - alpha + alpha / 2
    z = norm.ppf(alpha_limite, loc=0, scale=1)
    return 0.5 + z * (1 / math.sqrt(12 * n))

def get_limites_media(li, ls):
    print(f'EL valor del limite inferior de la media es {li}')
    print(f'EL valor del limite superior de la media es {ls}')

def prueba_medias(X, alpha):
    mu_x = media(X)
    li_mu = limite_inferior_media(alpha, len(X))
    ls_mu = limite_superior_media(alpha, len(X))
    if li_mu <= mu_x <= ls_mu:
        print(f'El valor de la media = {mu_x} se encuentra entre los limites de aceptación')
    else:
        print(f'El valor de la media = {mu_x} NO se encuentra entre los limites de aceptación')
    get_limites_media(li_mu, ls_mu)

if __name__ == '__main__':
    X = generar_numeros_aleatorios(100)
    print(X)
    aceptacion = 95
    alpha = 1 - (aceptacion / 100)

    prueba_medias(X, alpha)
