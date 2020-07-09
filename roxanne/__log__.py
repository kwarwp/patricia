
{'date': 'Thu Jul 09 2020 15:32:37.534 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  def oi:
         ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Jul 09 2020 15:32:50.64 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 4
  print(f'Olá, {nome}, meu nome é doginho!')
  ^
IndentationError: unexpected indent
'''},
{'date': 'Thu Jul 09 2020 15:33:04.971 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 3
  nome = input("Digite o seu nome: ")
  ^
IndentationError: expected an indented block
'''},
{'date': 'Thu Jul 09 2020 15:34:16.85 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 6
    oi(nome)
TypeError: oi() takes 0 positional argument but more were given
'''},
{'date': 'Thu Jul 09 2020 15:54:24.783 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 9
  def sobre_pessoa(self)
                         ^
SyntaxError: invalid syntax
'''},