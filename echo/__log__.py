
{'date': 'Wed Jul 15 2020 19:00:06.222 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 12
  dado_1 = "https://i.imgur.com/eEqs1z7.png"
  ^
IndentationError: unexpected indent
'''},
{'date': 'Wed Jul 15 2020 19:00:16.574 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 14
  dado_1.vai()
  ^
IndentationError: unexpected indent
'''},
{'date': 'Wed Jul 15 2020 19:00:33.427 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 13
  dado_1.vai()
  ^
IndentationError: unexpected indent
'''},
{'date': 'Wed Jul 15 2020 19:16:00.400 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 15
    self.dado_1.vai()
AttributeError: 'GUI' object has no attribute 'dado_1'
'''},