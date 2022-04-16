import numpy as np
import random

pop = [np.random.randint(0,256,3) for _ in range(1000)]
geracoes = 1000
solucao_otima = False
solucao = None

def selecaoEReproducao(populacao):
    pontuados = [(funcaoFitness(individuo), individuo) for individuo in populacao]
    pontuados = [individuo[1] for individuo in sorted(pontuados, key = lambda i:i[0])]
    pontuados = pontuados[0:500]

    novaGeracao = []
    for i in range(0, len(pontuados), 2):
        filho1, filho2 = cruzamento(populacao[i], populacao[i+1])
        novaGeracao.append(filho1)
        novaGeracao.append(filho2)
    
    return novaGeracao   

def  funcaoFitness(individuo):
    return 255*3 - (individuo[0] + individuo[1] + individuo[2])

def cruzamento(individuo1, individuo2):
    filho1 = [individuo1[0], individuo1[1], individuo2[2]]
    filho2 = [individuo1[1], individuo1[0], individuo2[0]]

    return filho1, filho2

def mutacao(populacao):
    quantidade = int(0.01*len(populacao))
    escolhidos = np.random.randint(0, len(populacao)-1, quantidade)
    for escolhido in escolhidos:
        gene = np.random.randint(0,2)
        valor = np.random.randint(0,255)
        populacao[escolhido][gene] = valor

    return populacao

def calculaSolucaoOtima(pop):
    for individuo in pop:
        nota = funcaoFitness(individuo)

        if nota >= 750:
            return individuo

    return None
            



while geracoes > 0 and solucao_otima == False:
    pop = selecaoEReproducao(pop)
    pop = mutacao(pop)

    foiEncontradoSolucao = calculaSolucaoOtima(pop)
    if foiEncontradoSolucao != None:
        solucao_otima = True
        solucao = foiEncontradoSolucao

    geracoes -= 1

if(solucao_otima == True):
    solucaoString = ' ,'.join(map(str, solucao))
    print(f'Foi encontrada solução ótima! Individuo: {solucaoString} - pontuacao {funcaoFitness(solucao)}')
else:
    print('Top 10 soluções ótimas:')
    for individuo in sorted(pop, key=lambda i: funcaoFitness(i), reverse=True)[0:10]:
        solucaoString = ' ,'.join(map(str, individuo))
        print('\t- '+ solucaoString)
