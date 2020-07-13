# patricia.danae.open.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Classe para criar um substituto para open no vitolino.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.07
        classe Open.

"""
from browser.local_storage import storage
class Open:
    def __init__(self, filename, mode="r"):
        def create(n):
            storage[n] = ""
            return storage[n]
        self.filename, self.mode = filename, mode
        if mode not in "rwa".split():
            raise ValueError("must have exactly one of create/read/write/append mode")
        self.__enter = dict(
            r=lambda n: raise FileNotFoundError(n)
            w=create
            a=create
        self.filehandle = None
        self.__enter__()

    def __enter__(self):
        try:
            self.filehandle = storage[self.filename]
        except:
            self.filehandle = self.__enter[self.mode](self.filename)
            

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.close()
            
    def write(self, content):
        storage[self.filename] += content
        
    def read(self):
        return storage[self.filename]
        
    def close(self):
        return True

f = Open("nome.txt")
f.write("carlo")
f.close()
print (f.read())
with Open("nome.txt") as no:
    no.write("jo")
    print(no.read())
