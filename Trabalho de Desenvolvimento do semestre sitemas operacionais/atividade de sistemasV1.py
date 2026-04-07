#usado ia claude/ajuda de colegas para descobrir em como deixar aleatorio
import random
class Processo:
    def __init__(self, tempo_exec):
        self.tempo_execucao = tempo_exec

lista_processo = []
flag = True
acumulador = 0
lista_espera = []
aleatorio = int(input("Sera aleatorio? SIM(1) NÃO(2): "))

if aleatorio == 1:
    total_processo = random.randint(2, 10)
    print(f"Quantidade de processos gerada: {total_processo}")
    for i in range(total_processo):
        tempo_exec = random.randint(1, 10)
        processo = Processo(tempo_exec)
        lista_processo.append(processo)
        print(f"Processo {i} criado com tempo de execução: {tempo_exec}")

elif aleatorio == 2:
    total_processo = int(input("Quantos processos? "))
    for i in range(total_processo):
        tempo_exec = int(input(f"Tempo de execução do processo {i}: "))
        processo = Processo(tempo_exec)
        lista_processo.append(processo)

while flag == True:
    print("1=FCFS")
    print("2=SJF Preemptivo")
    print("3=SJF Não Preemptivo")
    print("4=Prioridade Preemptivo")
    print("5=Prioridade Não Preemptivo")
    print("6=Round_Robin")
    print("7=Imprime lista de processos")
    print("8=Popular processos novamente")
    print("9=Sair:")
    algoritimo = int(input("Escolha o algoritmo: "))
    #codigo do FCFS
    if algoritimo == 1:
        for processo in range(total_processo):
            lista_espera.append(acumulador)
            for tempo in range(lista_processo[processo].tempo_execucao):
                acumulador += 1
                print(f"tempo [{acumulador}] processo[{processo}] restante=[{lista_processo[processo].tempo_execucao - (tempo + 1)}]")

        print("")
        for espera in range(len(lista_espera)):
            print(f"processo[{espera}]: tempo espera={lista_espera[espera]}")

        tempo_soma = sum(lista_espera)
        tempo_media = tempo_soma / len(lista_espera)
        print(f"Tempo médio de espera: {tempo_media}")
        input("Clque enter para voltar ao menu")

    #codigo da opção 7
    elif algoritimo == 7:
        print("Lista de processos:")
        for i, p in enumerate(lista_processo):
            print(f"  Processo {i}: tempo de execução = {p.tempo_execucao}")
        input("Clique enter para voltar ao menu")

    #codigo da opção 8    
    elif algoritimo == 8:
        lista_processo = []
        aleatorio = int(input("Sera aleatorio novamente? SIM(1) NÃO(2): "))
        if aleatorio == 1:
            total_processo = random.randint(2, 10)
            print(f"Quantidade de processos gerada: {total_processo}")
            for i in range(total_processo):
                tempo_exec = random.randint(1, 10)
                processo = Processo(tempo_exec)
                lista_processo.append(processo)
                print(f"Processo {i} criado com tempo de execução: {tempo_exec}")
        elif aleatorio == 2:
            total_processo = int(input("Quantos processos? "))
            for i in range(total_processo):
                tempo_exec = int(input(f"Tempo de execução do processo {i}: "))
                processo = Processo(tempo_exec)
                lista_processo.append(processo)
        input("Clique enter para voltar ao menu")

    #codigo da opção 9   
    elif algoritimo == 9:
        print("adeus...")
        flag = False
    else:
        print("ainda não inserido ou opção invalida")
        input("Clque enter para voltar ao menu")