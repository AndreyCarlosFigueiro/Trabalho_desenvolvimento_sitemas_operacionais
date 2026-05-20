#usado ia claude/ajuda de colegas para descobrir em como deixar aleatorio
import random
class Processo:
    def __init__(self, tempo_execucao, tempo_chegada, prioridade):
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.tempo_chegada = tempo_chegada
        self.prioridade = prioridade
        self.finalizado = False

def gerar_processos_aleatorio():
    lista = []
    total = random.randint(2, 10)
    print(f"Quantidade de processos gerada: {total}")
    for i in range(total):
        tempo_execucao = random.randint(1, 10)
        tempo_chegada = random.randint(1, 10)
        prioridade = random.randint(1, 10)
        processo = Processo(tempo_execucao, tempo_chegada, prioridade)
        lista.append(processo)
        print(f"Processo [{i}]: tempo de execução={tempo_execucao} tempo restante={tempo_execucao} tempo de chegada={tempo_chegada} Prioridade={prioridade}")
    return lista, total

lista_processo = []
flag = True
acumulador = 0
lista_espera = []
total_processo = 0
aleatorio = int(input("Sera aleatorio? SIM(1) NÃO(2): "))


if aleatorio == 1:
    lista_processo, total_processo = gerar_processos_aleatorio()

elif aleatorio == 2:
    total_processo = int(input("Quantos processos? "))
    for i in range(total_processo):
        tempo_execucao = int(input(f"Tempo de execução do processo {i}: "))
        tempo_chegada = int(input(f"Tempo chegada do processo {i}: "))
        prioridade = int(input(f"Prioridade do processo {i}: "))
        processo = Processo(tempo_execucao, tempo_chegada, prioridade)
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
        acumulador = 0
        lista_espera = []
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
#Ambos os SJF teve ajuda de ia e colegas para tentar entender a logica e como fazer (ia usada copilot)
    #codigo da opção 2
    elif algoritimo == 2:
        tempo = 0
        finalizados = 0
        # reset dos processos
        for p in lista_processo:
            p.tempo_restante = p.tempo_execucao
            p.finalizado = False
            p.tempo_termino = 0
        while finalizados < total_processo:
            escolhido = -1
            existe_pronto = False
            # procurar algum processo pronto
            for i in range(total_processo):
                p = lista_processo[i]
                if p.tempo_chegada <= tempo:
                    if p.finalizado == False:
                        escolhido = i
                        existe_pronto = True
            if existe_pronto == False:
                tempo += 1
                print(f"tempo [{tempo}]: nenhum processo está pronto")
            else:
                #escolher o menor tempo restante
                for i in range(total_processo):
                    p = lista_processo[i]
                    if p.tempo_chegada <= tempo:
                        if p.finalizado == False:
                            if p.tempo_restante < lista_processo[escolhido].tempo_restante:
                                escolhido = i
                tempo += 1
                lista_processo[escolhido].tempo_restante -= 1
                print(f"tempo [{tempo}]: processo[{escolhido}] restante={lista_processo[escolhido].tempo_restante}")
                if lista_processo[escolhido].tempo_restante == 0:
                    lista_processo[escolhido].finalizado = True
                    lista_processo[escolhido].tempo_termino = tempo
                    finalizados += 1
        # cálculo do tempo de espera
        print("")
        soma = 0
        for i in range(total_processo):
            p = lista_processo[i]
            espera = p.tempo_termino - p.tempo_chegada - p.tempo_execucao
            print(f"Processo[{i}]: tempo_espera={espera}")
            soma += espera
        print(f"Tempo médio de espera: {soma / total_processo}")
        input("Clique enter para voltar ao menu")
    
    #codigo da opção 3
    elif algoritimo == 3:
        tempo = 0
        finalizados = 0
        # reset dos processos
        for p in lista_processo:
            p.tempo_restante = p.tempo_execucao
            p.finalizado = False
            p.tempo_termino = 0
        while finalizados < total_processo:
            escolhido = -1
            existe_pronto = False
            # procurar algum processo pronto
            for i in range(total_processo):
                p = lista_processo[i]
                if p.tempo_chegada <= tempo:
                    if p.finalizado == False:
                        escolhido = i
                        existe_pronto = True
            if existe_pronto == False:
                tempo += 1
                print(f"tempo [{tempo}]: nenhum processo está pronto")
            else:
                for i in range(total_processo):
                    p = lista_processo[i]
                    if p.tempo_chegada <= tempo:
                        if p.finalizado == False:
                            if p.tempo_execucao < lista_processo[escolhido].tempo_execucao:
                                escolhido = i
                while lista_processo[escolhido].tempo_restante > 0:
                    tempo += 1
                    lista_processo[escolhido].tempo_restante -= 1
                    print(f"tempo [{tempo}]: processo[{escolhido}] restante= {lista_processo[escolhido].tempo_restante}")
                lista_processo[escolhido].finalizado = True
                lista_processo[escolhido].tempo_termino = tempo
                finalizados += 1
        # cálculo do tempo de espera
        print("")
        soma = 0
        for i in range(total_processo):
            p = lista_processo[i]
            espera = p.tempo_termino - p.tempo_chegada - p.tempo_execucao
            print(f"Processo[{i}]: tempo_espera={espera}")
            soma += espera
        print(f"Tempo médio de espera: {soma / total_processo}")
        input("Clique enter para voltar ao menu")
#AS PRIORIADDES USAM QUANTO MENOR O NUMERO MAIOR A PRIORIDADE        
    #codigo da opção 4
    elif algoritimo == 4:
        tempo = 0
        finalizados = 0

        # reset dos processos
        for p in lista_processo:
            p.tempo_restante = p.tempo_execucao
            p.finalizado = False
            p.tempo_termino = 0

        while finalizados < total_processo:
            escolhido = -1
            existe_pronto = False

            # procurar algum processo pronto
            for i in range(total_processo):
                p = lista_processo[i]
                if p.tempo_chegada <= tempo:
                    if p.finalizado == False:
                        escolhido = i
                        existe_pronto = True

            if existe_pronto == False:
                tempo += 1
                print(f"tempo [{tempo}]: nenhum processo está pronto")
            else:
                # escolher o processo de MAIOR prioridade
                # menor número = maior prioridade
                for i in range(total_processo):
                    p = lista_processo[i]
                    if p.tempo_chegada <= tempo:
                        if p.finalizado == False:
                            if p.prioridade < lista_processo[escolhido].prioridade:
                                escolhido = i
                tempo += 1
                lista_processo[escolhido].tempo_restante -= 1
                print(
                    f"tempo [{tempo}]: processo[{escolhido}] restante={lista_processo[escolhido].tempo_restante}")
                if lista_processo[escolhido].tempo_restante == 0:
                    lista_processo[escolhido].finalizado = True
                    lista_processo[escolhido].tempo_termino = tempo
                    finalizados += 1

        # cálculo do tempo de espera
        print("")
        soma = 0
        for i in range(total_processo):
            p = lista_processo[i]
            espera = p.tempo_termino - p.tempo_chegada - p.tempo_execucao
            print(f"Processo[{i}]: tempo_espera={espera}")
            soma += espera
        print(f"Tempo médio de espera: {soma / total_processo}")
        input("Clique enter para voltar ao menu")

    #codigo da opção 5 - Prioridade Não Preemptivo
    elif algoritimo == 5:
        tempo = 0
        finalizados = 0
        # reset dos processos
        for p in lista_processo:
            p.tempo_restante = p.tempo_execucao
            p.finalizado = False
            p.tempo_termino = 0

        while finalizados < total_processo:
            escolhido = -1
            existe_pronto = False
            # procurar algum processo pronto
            for i in range(total_processo):
                p = lista_processo[i]
                if p.tempo_chegada <= tempo:
                    if p.finalizado == False:
                        escolhido = i
                        existe_pronto = True
            if existe_pronto == False:
                tempo += 1
                print(f"tempo [{tempo}]: nenhum processo está pronto")
            else:
                # escolher o processo de MAIOR prioridade
                for i in range(total_processo):
                    p = lista_processo[i]
                    if p.tempo_chegada <= tempo:
                        if p.finalizado == False:
                            if p.prioridade < lista_processo[escolhido].prioridade:
                                escolhido = i

                # executa ATÉ TERMINAR (não-preemptivo)
                while lista_processo[escolhido].tempo_restante > 0:
                    tempo += 1
                    lista_processo[escolhido].tempo_restante -= 1
                    print(
                        f"tempo [{tempo}]: processo[{escolhido}] restante={lista_processo[escolhido].tempo_restante}")
                lista_processo[escolhido].finalizado = True
                lista_processo[escolhido].tempo_termino = tempo
                finalizados += 1

        # cálculo do tempo de espera
        print("")
        soma = 0
        for i in range(total_processo):
            p = lista_processo[i]
            espera = p.tempo_termino - p.tempo_chegada - p.tempo_execucao
            print(f"Processo[{i}]: tempo_espera={espera}")
            soma += espera

        print(f"Tempo médio de espera: {soma / total_processo}")
        input("Clique enter para voltar ao menu")
    
    #ROUND ROBIN(ajuda de ia para pensar no codigo e vericar em linguagem falada)
    elif algoritimo == 6:
        tempo = 0
        finalizados = 0
        fila = []

        time_slice = int(input("Escolha o time slice: "))

        #reseta os processos
        for p in lista_processo:
            p.tempo_restante = p.tempo_execucao
            p.finalizado = False
            p.tempo_termino = 0

        #vai continuar a rodar todos os processos terminarem
        while finalizados < total_processo:
            #verifica quem chegou e quem ainda não terminou
            for i in range(total_processo):
                p = lista_processo[i]
                if p.tempo_chegada <= tempo:
                    if p.finalizado == False:
                        if i not in fila:
                            fila.append(i)


            if len(fila) == 0:
                tempo += 1
                print(f"tempo [{tempo}]: nenhum processo está pronto")
            else:
                #remove o primeiro da fila e faz ele ser o que vai executar
                atual = fila.pop(0)
                
                contador_time_slice = 0
                # executa até o tempo permitido e ainda n terminou
                while contador_time_slice < time_slice and lista_processo[atual].tempo_restante > 0:
                    tempo += 1
                    contador_time_slice += 1
                    lista_processo[atual].tempo_restante -= 1

                    print(f"tempo [{tempo}]: processo[{atual}] restante={lista_processo[atual].tempo_restante}")

                    # adicionar novos processos na fila
                    for i in range(total_processo):
                        p = lista_processo[i]
                        if p.tempo_chegada <= tempo:
                            if p.finalizado == False:
                                if i not in fila and i != atual:
                                    fila.append(i)

                #guarda se terminou se não volta pra fila
                if lista_processo[atual].tempo_restante == 0:
                    lista_processo[atual].finalizado = True
                    lista_processo[atual].tempo_termino = tempo
                    finalizados += 1
                else:
                    fila.append(atual)

        # cálculo do tempo de espera
        print("")
        soma = 0
        for i in range(total_processo):
            p = lista_processo[i]
            espera = p.tempo_termino - p.tempo_chegada - p.tempo_execucao
            print(f"Processo[{i}]: tempo_espera={espera}")
            soma += espera

        print(f"Tempo médio de espera: {soma / total_processo}")
        input("Clique enter para voltar ao menu")

    #codigo da opção 7
    elif algoritimo == 7:
        print("Lista de processos:")
        for i, p in enumerate(lista_processo):
            print(f"Processo [{i}]: tempo de execução={p.tempo_execucao} tempo de chegada={p.tempo_chegada} prioridade={p.prioridade}")
        input("Clique enter para voltar ao menu")


    #codigo da opção 8    
    elif algoritimo == 8:
        lista_processo = []
        acumulador = 0
        lista_espera = []
        aleatorio = int(input("Sera aleatorio novamente? SIM(1) NÃO(2): "))

        if aleatorio == 1:
            lista_processo, total_processo = gerar_processos_aleatorio()
    
        elif aleatorio == 2:
            total_processo = int(input("Quantos processos? "))
            for i in range(total_processo):
                tempo_execucao = int(input(f"Tempo de execução do processo {i}: "))
                tempo_chegada = int(input(f"Tempo chegada do processo {i}: "))
                prioridade = int(input(f"Prioridade do processo {i}: "))
                processo = Processo(tempo_execucao, tempo_chegada, prioridade)
                lista_processo.append(processo)

    #codigo da opção 9   
    elif algoritimo == 9:
        print("adeus...")
        flag = False
    else:
        print("ainda não inserido ou opção invalida")
        input("Clque enter para voltar ao menu")
