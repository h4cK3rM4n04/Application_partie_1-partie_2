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

from importer.importation import Fibonacci as h4cK3rM4n04

nombre_0 = True
nombre_1 = False
nombre_2 = 10.2
nombre_3 = "h4cK3rM4n04"
nombre_4 = 10
file = "file.txt"
with open(file, "a+") as x:
	pass
	x.write(h4cK3rM4n04.suite_F(nombre_0) + "\n")
	x.write(h4cK3rM4n04.suite_F(nombre_1)+ "\n")
	x.write(h4cK3rM4n04.suite_F(nombre_2)+ "\n")
	x.write(h4cK3rM4n04.suite_F(nombre_3)+ "\n")
	x.write(h4cK3rM4n04.suite_F(nombre_4)+ "\n")
	x.close()