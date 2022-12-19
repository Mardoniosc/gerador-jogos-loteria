class Regra():
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def regraObjeto(self):
        return {self.titulo: self.descricao}


# LOTOFACIL
lotofacilAleatorio = Regra(
    'Lotofácil Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')
lotofacilNaoSorteado = Regra(
    'Lotofácil Não Sorteado', 'Números sorteados gerados através do algoritimo(random.sample), e verificado se já foram sorteados em algum concurso')
lotofacilBaseUltimo = Regra(
    'Lotofácil Base Último', 'São gerado 5 jogos com no mínimo 3 números que sairam no sorteio anterior')

# DUPLA SENA
duplasenaAleatorio = Regra(
    'DuplaSena Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')

# LOTOMANIA
lotomaniaAleatorio = Regra(
    'LotoMania Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')

# QUINA
quinaAleatorio = Regra(
    'Quina Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')

# MEGA SENA
megasenaAleatorio = Regra(
    'MegaSena Aleatória', 'Números sorteados gerados através do algoritimo(random.sample)')
megasenaDuque = Regra('MegaSena Duque',
                      '* 1 Numero baixo (1 e 10) * 1 Numero alto (51 e 60) * 2 Numero de trinta (30 e 39) * 2 Numero de aleatorios')

regrasFechamento = Regra('Fechamento', 'total_numeros_fechamento: numero total que vai ser feito o fechamento do jogo | para_acertar: o numero de dezenas que deseja acertar no jogo | geracao_numeros: o tipo de escolha dos numeros que formaram o fechamento')


def regras():
    listaRegrasAleatorios = []
    listaRegrasAleatorios.append(lotofacilAleatorio.regraObjeto())
    listaRegrasAleatorios.append(duplasenaAleatorio.regraObjeto())
    listaRegrasAleatorios.append(lotomaniaAleatorio.regraObjeto())
    listaRegrasAleatorios.append(megasenaAleatorio.regraObjeto())
    listaRegrasAleatorios.append(quinaAleatorio.regraObjeto())

    regras_json = {'Regras': {
        'Aleatorios': listaRegrasAleatorios,
        'Mega Sena Duque': megasenaDuque.regraObjeto(),
        'Lotofacil Não Sorteado': lotofacilNaoSorteado.regraObjeto(),
        'Lotofácil Base Ultimo': lotofacilBaseUltimo.regraObjeto(),
        'Fechamento': regrasFechamento.regraObjeto(),
    }}
    return regras_json


def regras_duplasena():
    regras = []
    regras.append(duplasenaAleatorio.regraObjeto())
    regras_json = {'Duplasena': regras}
    return regras_json


def regras_lotofacil():
    regras = []
    regras.append(lotofacilAleatorio.regraObjeto())
    regras.append(lotofacilNaoSorteado.regraObjeto())
    regras.append(lotofacilBaseUltimo.regraObjeto())
    regras_json = {'Lotofacil': regras}
    return regras_json


def regras_lotomania():
    regras = []
    regras.append(lotomaniaAleatorio.regraObjeto())
    regras_json = {'Lotomani': regras}
    return regras_json


def regras_megasena():
    regras = []
    regras.append(megasenaAleatorio.regraObjeto())
    regras.append(megasenaDuque.regraObjeto())

    regras_json = {'Megasena': regras}
    return regras_json


def regras_quina():
    regras = []
    regras.append(quinaAleatorio.regraObjeto())
    regras_json = {'Quina': regras}
    return regras_json
