import random
from time import sleep

alunos = [{'Nome': 'Ryan', 'id': 1, 'Xp': 10, 'Nivel': 1}]

# Adiciona os dados do aluno dentro de um dicionário,
# que por sua vez é acrescentado em uma lista chamada "alunos".
def adiciona_aluno(nome, identificacao_aluno, xp, nivel):
    aluno = {
        'Nome': nome,
        'Id': identificacao_aluno,
        'Xp': xp,
        'Nível': nivel
    }
    alunos.append(aluno)

# Função responsável por gerar as questões do aluno,
# Bem como por retornar os valores do seu xp e nível de acordo com suas respostas.
def detector_nivel(nome, nivel, xp):
    if nivel == 1 and xp == 0:
        print("Boas vindas {}!" .format(nome))
    if nivel == 1:
        if xp >= 50:
            nivel, xp = boss_lv1(nome, nivel, xp)
        else:
            xp = gerador_questoes_lv1(nome, nivel, xp)
        return xp, nivel
    elif nivel == 2:
        if xp >= 200:
            nivel, xp = boss_lv2(nome, nivel, xp)
        else:
            xp = gerador_questoes_lv2(nome, nivel, xp)
        return xp, nivel
    elif nivel == 3:
        if xp >= 500:
            nivel, xp = boss_lv3(nome, nivel, xp)
        else:
            xp = gerador_questoes_lv3(nome, nivel, xp)
        return xp, nivel

def gerador_questoes_lv1(nome, nivel, xp):
    while xp <= 50:
        v1 = random.randint(2, 10)
        v2 = random.randint(1, 10)
        # Isso aqui vai garantir que não tenham contas com o resultado negativo
        while True:
            if (v2 == v1):
                v2 = random.randint(1, 10)
                continue
            else:
                break
        operacoes = random.randint(1, 2)
        print("Qual o resultado da seguinte operação?")
        if operacoes == 1:
            print("{} + {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 + v2):
                print("Correto")
                print("{} ganhou +10 de XP" .format(nome))
                xp += 10
                if xp >= 50:
                    return xp
                else:
                    continue
            else:
                print("Incorreto")
                continue
        elif operacoes == 2:
            while True:
                if (v2 > v1) or (v2 == v1):
                    v2 = random.randint(1, 10)
                    continue
                else:
                    break
            print("{} - {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 - v2):
                print("Correto")
                print("{} ganhou +10 de XP" .format(nome))
                xp += 10
                if xp >= 50:
                    return xp
                else:
                    continue
            else:
                print("Incorreto")
                continue


#Boss 1
def boss_lv1(nome, nivel, xp):
    while True:
        print("Marcia tem 15 laranjas, que ela vende por 0,50 R$ cada, João comprou 6 dessas laranjas.")
        print("Quantas laranjas sobraram para Marcia?")
        r1 = int(input(">>>"" "))
        if r1 == 9:
            print("Correto!")
            print("Agora")
            print("Quanto João R$ pagou pelas 6 laranjas?")
            r2 = int(input(">>>"" "))
            if r2 == 3 or r2 == 3.00:
                print("Correto!")
                print("Parabéns {}, você alcançou o Nivel 2!" .format(nome))
                nivel = 2
                return nivel, xp
            else:
                print("Incorreto")
                nivel = 1
                return nivel, xp
        else:
                print("Incorreto")
                nivel = 1
                return nivel, xp



# Gerador de questôes nivel 2
def gerador_questoes_lv2(nome, nivel, xp):
    while xp <= 200:
        v1 = random.randint(2, 30)
        v2 = random.randint(1, 30)
        # Isso aqui vai garantir que não tenham contas com o resultado negativo
        while True:
            if (v2 == v1):
                v2 = random.randint(1, 30)
                continue
            else:
                break
        operacoes = random.randint(1, 2)
        print("Qual o resultado da seguinte operação?")
        if operacoes == 1:
            print("{} + {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 + v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 200:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue
        elif operacoes == 2:
            while True:
                if (v2 > v1) or (v2 == v1):
                    v2 = random.randint(1, 30)
                    continue
                else:
                    break
            print("{} - {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 - v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 200:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue

# Boss 2
def boss_lv2(nome, nivel, xp):
    while True:
        print("Davi tem 3 barracas de doce e cada barraca produz 20 balas por dia.")
        print("Quantas balas são feitas por dia?")
        r1 = int(input(">>>"" "))
        if r1 == 60:
            print("Correto!")
            print("Quantas balas seriam feitas em 3 dias?")
            r2 = int(input(">>>"" "))
            if r2 == 180:
                print("Correto!")
                print("Se Davi fizesse outra barraca que também produz 20 balas todo dia, quantas seriam produzidas em 2 dias?")
                r3 = int(input(">>>"" "))
                if r3 == 160:
                    print("Parabéns {}, você alcançou o Nivel 3!" .format(nome))
                    nivel = 3
                    return nivel, xp
                else:
                    print("Incorreto")
                    nivel = 2
                    return nivel, xp
            else:
                print("Incorreto")
                nivel = 2
                return nivel, xp
        else:
            print("Incorreto")
            nivel = 2
            return nivel, xp


# Gerador de questôes nivel 3
def gerador_questoes_lv3(nome, nivel, xp):
    while xp <= 500:
        v1 = random.randint(11, 30)
        v2 = random.randint(10, 30)
        # Isso aqui vai garantir que não tenham contas com o resultado negativo
        while True:
            if (v2 == v1):
                v2 = random.randint(10, 30)
                continue
            else:
                break
        operacoes = random.randint(1, 3)
        print("Qual o resultado da seguinte operação?")
        if operacoes == 1:
            print("{} + {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 + v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 200:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue
        elif operacoes == 2:
            while True:
                if (v2 > v1) or (v2 == v1):
                    v2 = random.randint(10, 30)
                    continue
                else:
                    break
            print("{} - {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 - v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 500:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue
        elif operacoes == 3:
            #Isso aqui serve para balancear as opercaoes com multiplicação
            v1 = random.randint(2, 30)
            v2 = random.randint(1, 10)
            print("{} x {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 * v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 500:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue

# Boss 3
def boss_lv3(nome, nivel, xp):
    while True:
        print("Marcos quer comprar parte de um terreno, o terreno é dividido em 12 partes cada parte custando R$ 180,00.")
        print("Quantas partes Marcos pode comprar por R$ 800,00?")
        r1 = int(input(">>>"" "))
        if r1 == 4:
            print("Correto!")
            print("E quanto dinherio sobraria?")
            r2 = int(input(">>>"" "))
            if r2 == 80 or r2 == 80.00:
                print("Correto!")
                print("Se marcos quisesse comprar todo o terreno de quanto ele precisaria no minimo?")
                r3 = int(input(">>>"" "))
                if r3 == 2160 or r3 == 2160.00:
                    print("Parabéns {}, você alcançou o Nivel 4!" .format(nome))
                    nivel = 4
                    return nivel, xp
                else:
                   print("Incorreto")
                   nivel = 3
                   return nivel, xp
            else:
                print("Incorreto")
                nivel = 3
                return nivel, xp
        else:
                print("Incorreto")
                nivel = 3
                return nivel, xp

# Loop principal, coleta o nome do aluno e víncula a ele os dados iniciais do jogo.
while True:
    nomeAluno = str(input('Digite o seu nome: '))
    id_aluno = len(alunos) + 1
    print('')
    # Valores iniciais
    nivel_aluno = 1
    xp_aluno = 0
    xp_aluno, nivel_aluno = detector_nivel(nomeAluno, nivel_aluno, xp_aluno)
    adiciona_aluno(nomeAluno, id_aluno, xp_aluno, nivel_aluno)

    # Fazendo com que os alunos fiquem ordenados dentro da lista de acordo com o seu XP (ORDEM DECRESCENTE)
    alunos.sort(key=lambda item: item['Xp'], reverse=True)

    posicao = 0
    print(f'{"=-" * 4}RANKING DE ALUNOS{"-=" * 4}')
    for aluno in alunos:
        posicao += 1
        print(f'{posicao}° {aluno}')
    
    while True:
        funcao = str(input('Você deseja continuar[S/N]: ')).upper()
        if funcao == 'S':
            xp_aluno, nivel_aluno = detector_nivel(nomeAluno, nivel_aluno, xp_aluno)
        elif funcao == 'N':
            print('Finalizando...')
            sleep(1)
            print('Volte logo!')
            break