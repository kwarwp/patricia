# patricia.samantha.kwarwp4.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Testando - EMPURRA A TORA

.. codeauthor:: Raquel M. M. Fernandes <raquelmachado4993@gmail.com>

Changelog
---------
.. versionadded::    10.09
        

"""
class Nulo:
    """Objeto nulo que responde passivamente a todas as requisições."""
    def __init__(self):
        self.pegar = self.ocupa = self.empurrar = self.nulo
        
    def nulo(self, *_, **__):
        """Método nulo, responde passivamente a todas as chamadas.
        
        :param _: aceita todos os argumentos posicionais.
        :param __: aceita todos os argumentos nomeados.
        :return: retorna o próprio objeto nulo.
        """
        return self 

NULO = Nulo()