class Regra():
  def __init__(self, titulo, descricao):
    self.titulo = titulo
    self.descricao = descricao

  def regraObjeto(self):
    return { self.titulo : self.descricao }

# ALEATORIOS
lotofacilAleatorio = Regra('Lotofácil Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')
duplasenaAleatorio = Regra('DuplaSena Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')
lotomaniaAleatorio = Regra('LotoMania Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')
megasenaAleatorio = Regra('MegaSena Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')
quinaAleatorio = Regra('Quina Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')




def regras_aleatorio():
  listaRegrasAleatorios = []
  listaRegrasAleatorios.append(lotofacilAleatorio.regraObjeto())
  listaRegrasAleatorios.append(duplasenaAleatorio.regraObjeto())
  listaRegrasAleatorios.append(lotomaniaAleatorio.regraObjeto())
  listaRegrasAleatorios.append(megasenaAleatorio.regraObjeto())
  listaRegrasAleatorios.append(quinaAleatorio.regraObjeto())
  jogo = { 'Regras' : {
    'Aleatorios': listaRegrasAleatorios
  }}
  return jogo