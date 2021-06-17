from time import sleep


print('\033[1;94m-=-' * 20)
print('{:^60}'.format('Seja bem vindo, jogador!'))
print('-=-' * 20)

print('''\033[1;94m
 _                     _ _        _ 
| |                   (_) |      | |
| |__   ___  ___ _ __  _| |_ __ _| |
| '_ \ / _ \/ __| '_ \| | __/ _` | |
| | | | (_) \__ \ |_) | | || (_| | |
|_| |_|\___/|___/ .__/|_|\__\__,_|_|
                | |                 
                |_|
''')

nick_player = input('Escolha seu nickname: ')

sleep(1)
print(f'\n{nick_player}, você está em um hospital com milhares de pacientes e uma equipe de terroristas armou uma bomba em algum lugar do hospital. ')

sleep(4)
print('\ncorra, você precisa desarmar a bomba antes que todos morram.')

sleep(3)
print('\033[1;93m\nlembre-se, suas escolhas impactam seriamente o jogo.')

sleep(1.5)
escolha = input('\033[1;94m\nVocê está no centro do hospital, decide ir para direita ou para esquerda? direita[1], esquerda[2]: ')

if escolha == '1': 
    direita = input('\nSeguindo nesta direção você avista duas salas, em qual você quer entrar 1 ou 2? ')

    if direita == '1':
        print('\033[1;91m\nGAME OVER! Todos morreram, a bomba não estava nesta sala.')

    if direita == '2':
        print('\033[1;91m\nGAME OVER! Todos morreram, a bomba não estava nesta sala.')
        
if escolha == '2':
   esquerda = input('\nSeguinda nesta direção você avista duas salas, em qual pretende entrar 1 ou 2? ')

   if esquerda == '1':
        print('\033[1;91m\nGAME OVER! Todos morreram, a bomba não estava nesta sala.')

   if esquerda == '2':
       print('\n\033[1;92mVocê encontrou a bomba! calma, você precisa escolher a sequência certa para cortar os fios e assim desativa-la.')     
       sleep(1.7)
       desarmar_bomba = input('\n\033[1;35mSequência 1: fio roxo, azul e verde.\n\033[1;35mSequência 2: fio Vermelho, cinza e laranja. Qual você escolhe 1 ou 2? ')

       if desarmar_bomba == '1':
           for i in range(0, 6):
               sleep(1)
               print(i) 
           print('\033[1;91mGAME OVER!!! A bomba EXPLODIU, todos morreram.')

       if desarmar_bomba == '2':
            for i in range(0, 6):
                sleep(1)
                print(i) 
            print('\033[1;32mGAME WINS!!! A bomba foi desarmada com SUCESSO, você salvou todos!')
            print('\nFIM DE JOGO...')

           
