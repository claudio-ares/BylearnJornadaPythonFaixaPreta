# cod. de Claudio Soares (ByLearner)
from random import randint
from time import sleep

print('{:^30}'.format('*-*' * 15))
print('{:^40}'.format('JO-KEN-PO'))
print('{:^30}'.format('*-*' * 15))
s = '''Será que você é capaz de me vencer no JO KEN PO?'''
for c in s:
    sleep(0.1)
    print(c, end='')
sleep(1)
print('')
sleep(1)
print('Vamos começar!')
sleep(1)
s1 = 'Escolha sua jogada:'
for c in s1:
    sleep(0.03)
    print(c, end='')
print('''
[0]PEDRA
[1]PAPEL
[2]TESOURA''')

    #estas são as variaveis
cpt = randint(0, 2)
itens = ('pedra', 'papel', 'tesoura')
while True:
    jogador = int(input('Digite sua escolha:👉 '))
    if jogador >= 3:
        print('erro! Escolha uma opção válida!')
        continue
    computador = itens[cpt]
    jg = itens[jogador]

    #parte das escolas do jogador e do computador
    print('*-*' * 15)
    print('O COMPUTADOR escolheu {}'.format(computador))
    print('VOCÊ escolheu {}'.format(jg))
    print('*-*' * 15)

    sleep(3)
    #esta é a parte das condições
    if cpt == 0:
        if jogador == 0: #computador escolheu pedra
            print('EMPATE!')

        elif jogador == 1:
            print('Papel enrrola pedra. VOCÊ VENCEU!')

        elif jogador == 2:
            print('Pedra quebra tesoura. Computador VENCEU!')

    elif cpt == 1: #computador escolheu papel
        if jogador == 0:
            print('Papel enrrola pedra. Computador VENCEU!')

        elif jogador == 1:
            print('EMPATE!')

        elif jogador == 2:
            print('Tesoura corta papel. VOCÊ VENCEU!')

    elif cpt == 2:#computador escolheu tesoura
        if jogador == 0:
            print('Pedra quebra tesoura. VOCÊ VENCEU!')

        elif jogador == 1:
            print('Tesoura corta papel. O computador VENCEU!')

        elif jogador == 2:
            print('EMPATE!')

    sleep(3)
    print('*-*' * 15)
    print('Deseja tentar de novo?')
    print('''
    [1]Para tentar
    [2]Para sair''')
    opcao = int(input("👉 "))
    if opcao == 1:
        print('''
        [0]PEDRA
        [1]PAPEL
        [2]TESOURA
        ''')
        continue
    elif opcao == 2:
        print('OBRIGADO por jogar comigo! Volte sempre! ^^')
        break
    else:
        print('Opcão inválida!')
