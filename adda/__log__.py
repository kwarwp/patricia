
{'date': 'Mon Jul 13 2020 19:21:45.251 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 39
  keys = dict(x=+1, y=-1):
                          ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jul 13 2020 19:22:00.778 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 39
  keys = dict(x=1, y=-1):
                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jul 13 2020 19:22:10.619 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 177
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 51
    Eventos().vai()
  module <module> line 29
    self.cacada.elt.bind("keypressed", self.anda_banhista)
AttributeError: 'Eventos' object has no attribute 'cacada'
'''},
{'date': 'Mon Jul 13 2020 19:35:24.835 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 41
  keys = dict(37=1, 39=-1)
                ^
SyntaxError: keyword can't be an expression
'''},