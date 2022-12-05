import random
import string

def gerar_caracteres_aleatorios(frase_pretendida, caracteres):
    sequencia_caracteres = ""
    for i in range(len(frase_pretendida)):
        sequencia_caracteres += caracteres[random.randint(0, len(caracteres)-1)]
    return sequencia_caracteres

def mutacao_sequencia(sequencia_caracteres, caracteres):
    sequencia_mutada = ""
    for i in range(len(sequencia_caracteres)):
        if random.randint(0, 100) <= 5:
            sequencia_mutada += caracteres[random.randint(0, len(caracteres)-1)]
        else:
            sequencia_mutada += sequencia_caracteres[i]
    return sequencia_mutada

def multiplas_sequencias_mutacoes(sequencia_caracteres, caracteres):
    lista_de_sequencias = []
    for i in range(100):
        lista_de_sequencias.append(mutacao_sequencia(sequencia_caracteres, caracteres))
    return lista_de_sequencias

def score(sequencia_caracteres, frase_pretendida):
    score = 0
    for i in range(len(frase_pretendida)):
        if frase_pretendida[i] == sequencia_caracteres[i]:
            score += 1
    return score

def escolher_sequencia_mutada(sequencia_caracteres, frase_pretendida, caracteres):
    lista_de_sequencias = multiplas_sequencias_mutacoes(sequencia_caracteres, caracteres)
    sequencia_ideal = lista_de_sequencias[0]
    melhor_similar = score(sequencia_ideal, frase_pretendida)
    for sequencia in lista_de_sequencias:
        elem_similaridade = score(sequencia, frase_pretendida)
        if elem_similaridade > melhor_similar:
            melhor_similar = elem_similaridade
            sequencia_ideal = sequencia
    return sequencia_ideal


def main():
    caracteres = string.ascii_letters + " "
    frase_pretendida = str(input("O que o Macaco deve digitar? "))
    geracoes = 0
    sequencia_atual = gerar_caracteres_aleatorios(frase_pretendida, caracteres)
    print(f"Geração: {geracoes}")
    print(sequencia_atual)
    while sequencia_atual != frase_pretendida:
        sequencia_atual = escolher_sequencia_mutada(sequencia_atual, frase_pretendida, caracteres)
        geracoes += 1
        print(f"Geração: {geracoes}")
        print(sequencia_atual)

main()
condicao = str(input("Gostaria de executar novamente?(S/N) "))

while condicao != 'N':
    main()
    condicao = str(input("Gostaria de executar novamente?(S/N) "))