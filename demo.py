'''
module demo: contiens des choses...
'''
import math

print('Hello, dans demo.py')

def est_premier(n):
    if n<2: return False
    if n==2: return True
    for i in range(3, n):
        print(f"{n} % {i} : {n % i}")
        if n % i == 0 : return False
    return True

def test1():
	""" Ne fait rien de spécial """
	print('methode test1 dans demo')

def fibonacci(n):
	"""Calcule la suite de Fibonacci (récursif pur)
    Utilise une version sans résultats intermédiaires
    Args:
    n (int): le chiffre dont on veut calculer le nbre de Fibonacci

    Returns:
    int : le résultat de Fibonacci
    """
	if n<=1: return n
	return fibonacci(n-1) + fibonacci(n-2)
	
if __name__ == '__main__':
	print('Ceci est le main de demo, je teste test1 !')
	test1()
	est_premier(6)
	
