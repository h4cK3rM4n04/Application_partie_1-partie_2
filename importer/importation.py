#coding:utf-8

"""	Voici un exemple d'exercice qui utilise les notions suivantes :

				Variables
				Opérateurs
				Conditions
				Boucles
				Fonctions
Enoncé :
			Écrire une fonction Python qui prend un nombre entier en entrée et qui affiche les "n" premiers nombres de la suite de Fibonacci.

			La suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent. La suite commence généralement par les nombres 0 et 1, et les termes suivants sont obtenus en additionnant les deux termes précédents :

			0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Indications :

			Vous pouvez utiliser une boucle while pour générer les termes de la suite jusqu'au nombre voulu.
			Vous pouvez utiliser des variables pour stocker les deux termes précédents de la suite et pour calculer le terme suivant.
			Vous pouvez utiliser une condition if pour traiter le cas où l'entrée est inférieure ou égale à zéro.

"""

class Fibonacci:

	"""docstring for Fibonacci by h4cK3rM4n04"""

	def __init__(self):
		raise NotImplementedError

	def suite_F(nombre):

		try:
			if type(nombre) == bool:
				raise AssertionError
			res = [x for x in range(nombre)]
			cpt = 2
			while cpt < nombre:
				if not res[0]:
					res[0] = 0
				elif res[1]:
					res[1] = 1
				elif res[2]:
					res[2] = 1
				res[cpt] = res[cpt-1] + res[cpt-2]
				cpt += 1
			x = f"Les {nombre} nombres de la suite Fibonacci sont:	{res}"

		except TypeError:
			return f"Le chiffre ({nombre}) est invalide elle est de la {type(nombre)} !!!"

		except AssertionError:
			return f"Le chiffre ({nombre}) est un booléens il prend comme valeur {1 if nombre == True else 0}. Voici les ({nombre}) premier de la suite Fibonacci: {nombre} !!!"

		else:
			return x
		finally:
                        print("============================================================h4cK3rM4n04's Space=====================================================================\n")


if __name__ == "__main__":

	print(Fibonacci.suite_F(10))
	print(Fibonacci.suite_F(10.2))
	print(Fibonacci.suite_F("Bonjour"))
	print(Fibonacci.suite_F(True))
	print(Fibonacci.suite_F([12,15,20]))