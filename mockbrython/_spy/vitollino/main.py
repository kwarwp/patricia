from unittest.mock import MagicMock, ANY
class BrythonMock(MagicMock):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg) 
        self.__le__ = MagicMock()
Cena = BrythonMock()
Elemento = BrythonMock()
INVENTARIO = BrythonMock()
STYLE = BrythonMock()
Labirinto = BrythonMock()
Sala = BrythonMock()
Musica = BrythonMock()
Inventario = BrythonMock()
Codigo = BrythonMock()
Portal = BrythonMock()

Salao = BrythonMock()
Popup = BrythonMock()
Texto = BrythonMock()
Point = BrythonMock()

Cursor = BrythonMock()
Dragger = BrythonMock()
Dropper = BrythonMock()
Droppable = BrythonMock()

Folha = BrythonMock()
Suporte = BrythonMock()
Bloco = BrythonMock()
Jogo = BrythonMock()
JOGO = BrythonMock()


