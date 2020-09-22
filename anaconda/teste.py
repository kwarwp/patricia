# patricia.anaconda.teste.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""
#from patricia.danae.circus import Letra, Piso, Aldeia, circus
from danae.circus import  circus

def desafio1():
    MASMORRA = [[ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"]
                ]

    circus(2, MASMORRA, 2)
        
    
if __name__ == "__main__":
    desafio1()