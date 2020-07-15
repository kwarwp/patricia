
{'date': 'Wed Jul 15 2020 15:35:50.493 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  cena1.vai()
  ^
IndentationError: unexpected indent
'''},
{'date': 'Wed Jul 15 2020 15:36:12.131 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  cena1.vai()
  ^
IndentationError: unexpected indent
'''},
{'date': 'Wed Jul 15 2020 15:36:36.717 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 20
    teste()    
  module <module> line 18
    	cena1 = Cena(link_fundo)
TypeError: 'module' object is not callable
'''},