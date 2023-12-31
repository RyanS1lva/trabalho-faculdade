import random
from time import sleep

alunos = [{'Nome': 'Ryan', 'id': 1, 'Xp': 10, 'Nivel': 1},
          {'Nome': 'Lara', 'id': 2, 'Xp': 50, 'Nivel': 2}]

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
        while True:
            v1 = random.randint(2, 10)
            v2 = random.randint(1, 10)
            # Isso aqui vai garantir que não tenham contas com o resultado negativo
            if v2 != v1:
                break

        operacoes = random.randint(1, 2)
        print("Qual o resultado da seguinte operação?")
        if operacoes == 1:
            print("{} + {} = ?".format(v1, v2))
            while True: #Laço caso o usuário insira uma string no lugar de um number
                try:
                    resultado = int(input('>>> '))
                    if resultado == (v1 + v2):
                        print("Correto")
                        print("{} ganhou +10 de XP".format(nome))
                        xp += 10
                        if xp >= 50:
                            return xp
                        break  # Sai do loop interno e faz a próxima pergunta
                    else:
                        print("Incorreto")
                        break  # Sai do loop interno e faz a próxima pergunta
                except ValueError:
                    print('Por favor, digite um número.')
        elif operacoes == 2:
            while True:
                if v2 <= v1:
                    break
                else:
                    v2 = random.randint(1, 10)

            print("{} - {} = ?".format(v1, v2))
            while True: #Laço igual ao de cima
                try:
                    resultado = int(input('>>> '))
                    if resultado == (v1 - v2):
                        print("Correto")
                        print("{} ganhou +10 de XP".format(nome))
                        xp += 10
                        if xp >= 50:
                            return xp
                        break  # Sai do loop interno e faz a próxima pergunta
                    else:
                        print("Incorreto")
                        break  # Sai do loop interno e faz a próxima pergunta
                except ValueError:
                    print('Por favor, digite um número.')
    return xp #tentei alterar o nivel e o xp no ranking dos alunos, mas sem sucesso




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
#Iicio da interface
print('''
|====================================|
|       BEM VINDO AO DRAW-MATH       |
|====================================|
''')

def mural_opções (): #resolvi fazer só para esse caso seja necesário chamar somente esse.
    print ('Escolha uma das opções abaixo:\n'
        '1 - Entrar\n'
        '2 - Cadastrar\n'
        '3 - Mural de XP\n'
        '4 - Sair')
def interface_inicial (): #input e suas opções
    while True: #laço caso o usuário coloque uma opção inexistente
        login = input('>>')
        if login == '1':
            for aluno in alunos:
                print(aluno)
            while True: #laço para caso coloque um número ou id invalido
                try:
                    login_aluno = int(input('Digite o número do seu id: '))
                except ValueError:
                    print('Por favor, insira um número válido para o ID')
                    continue
                if 1 <= login_aluno <= len(alunos):
                    # ID válido, obter dados do aluno
                    for chave, valor in alunos[login_aluno - 1].items():
                        if chave == 'Nome':
                            nomeAluno = valor
                        elif chave == 'id':
                            id_aluno = valor
                        elif chave == 'Xp':
                            xp_aluno = valor
                        elif chave == 'Nivel':
                            nivel_aluno = valor
                    xp_aluno, nivel_aluno = detector_nivel(nomeAluno, nivel_aluno, xp_aluno)
                    break  # Sai do loop interno, pois temos um ID válido
                else:
                    print('ID inválido. Tente novamente.')
            break
        if login == '2': #criação de usuário
                nomeAluno = str(input('Digite o seu nome: '))
                id_aluno = len(alunos) + 1
                print('')
                # Valores iniciais
                nivel_aluno = 1
                xp_aluno = 0
                xp_aluno, nivel_aluno = detector_nivel(nomeAluno, nivel_aluno, xp_aluno)
                adiciona_aluno(nomeAluno, id_aluno, xp_aluno, nivel_aluno)
                break
        if login == '3': #mural de XP
            alunos.sort(key=lambda item: item['Xp'], reverse=True)

            posicao = 0
            print(f'{"=-" * 4}RANKING DE ALUNOS{"-=" * 4}')
            for aluno in alunos:
                    posicao += 1
                    print(f'{posicao}° {aluno}')
            mural_opções()
        elif login == '4': #fecha o código
            return
        else:
            print ('Valor não encontrado, tente novamente.')
            continue

    while True: #laço caso insira uma opção inexistente
        funcao = input('Você deseja continuar [S/N]: ')
        if funcao == 'S' or funcao == 's':
            xp_aluno, nivel_aluno = detector_nivel(nomeAluno, nivel_aluno, xp_aluno)
        elif funcao == 'N' or funcao == 'n':
            print(f'Você chegou até o nível {nivel_aluno}, e terminou com {xp_aluno} de xp, parábens!')
        else:
            print('Insira "S" para SIM e "N" para NÃO')

mural_opções()
interface_inicial()
print('Finalizando...')
sleep(1)
print('Volte logo!')