# patricia.alpha.hotel.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Monica Novellino <monicanovellino@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""
from _spy.circus.circus import circus
# faça aqui a sua implementação do desafio
#if __name__ == "__main__":
    #circus(<ponha aqui o número do desafio e descomente a linha>, <parâmetro indicado>)
f = open("names.txt", "w")
name = input("Hello, what is your name? ")
print("Hello " + name)
f.write(name)
f.close()
