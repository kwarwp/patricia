
{'date': 'Sat Aug 29 2020 17:35:28.604 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 71
    Kwarwp(Jogo).cria()
  module <module> line 48
    self.cena = self.cria(cenario=cenario) if vitollino else None
  module <module> line 52
    cena = self.v.c(self.SOLO)
AttributeError: 'Kwarwp' object has no attribute 'SOLO'
'''},
{'date': 'Sat Aug 29 2020 17:38:32.416 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 47
  self.v = vitollino()
  ^
IndentationError: expected an indented block
'''},