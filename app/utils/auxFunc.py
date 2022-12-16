def resultado_lista_inteiro(jogo):
    jogo = list(map(int, jogo))
    return jogo

def compara_resultado(jogo1, jogo2):
    resultado = set(jogo1).intersection(jogo2)
    acertos = len(resultado)
    return acertos

# valida se na lista exite 5 numeros em sequencia
def valida_sequencia(lista_int):
  for i, v in enumerate(lista_int[:-4]):  
    if (lista_int[i:i+5]) == [*range(v, v+5)]:     
      return True
  
  return False