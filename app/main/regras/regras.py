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


# MEGA SENA
megasenaDuque = Regra('MegaSena Aleatória', '* 1 Numero baixo (1 e 10) * 1 Numero alto (51 e 60) * 2 Numero de trinta (30 e 39) * 2 Numero de aleatorios')

def regras_aleatorio():
  listaRegrasAleatorios = []
  listaRegrasAleatorios.append(lotofacilAleatorio.regraObjeto())
  listaRegrasAleatorios.append(duplasenaAleatorio.regraObjeto())
  listaRegrasAleatorios.append(lotomaniaAleatorio.regraObjeto())
  listaRegrasAleatorios.append(megasenaAleatorio.regraObjeto())
  listaRegrasAleatorios.append(quinaAleatorio.regraObjeto())
  jogo = { 'Regras' : {
    'Aleatorios': listaRegrasAleatorios,
    'Mega Sena Duque': megasenaDuque.regraObjeto()
  }}
  return jogo