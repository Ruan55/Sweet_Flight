avioes = []
assentos_disponiveis = []
limite_reservas = 10
import os

class Aviao:
    def __init__(self, numerodoaviao: int, nomedopassageiro: str) -> None:
        self.numerodoaviao = numerodoaviao
        self.nomedopassageiro = nomedopassageiro

while True:

    print('1 - Registrar o número de cada avião')
    print('2 - Registrar o quantitativo de assentos disponíveis em cada avião')
    print('3 - Reservar passagem aérea')
    print('4 - Realizar consulta do avião')
    print('5 - Realizar consulta por passageiro')
    print('6 - Encerrar programa')
    opcoes_companhia = int(input('Escolha um das opções acima: '))

    match opcoes_companhia:

            case 1:
                os.system('cls || clear')
                for i in range(4):
                    numerodoaviao = int(input(f'Digite o número do {i+1}º avião disponível: '))
                    avioes.append(numerodoaviao)
                print(avioes)
            case 2:
                os.system('cls || clear')
                for i in range(4):
                    assentosDisponiveis = int(input('Digite o número de assentos disponiveis: '))
                    assentos_disponiveis.append(assentosDisponiveis)
                print(assentos_disponiveis)
            case 3:
                os.system('cls || clear')
                numerodoaviao = int(input('Digite o número do avião: '))
                avioes.append(numerodoaviao)
                if numerodoaviao not in avioes:
                    print('Este avião não existe!')
                else:
                    if assentos_disponiveis[numerodoaviao] <= 0:
                        print('Não há assentos neste avião!')
                    else:
                        if assentos_disponiveis[numerodoaviao] > limite_reservas:
                            print('Limite de reservas atingido!')                            
                        else:
                            nomedopassageiro = str(input('Digite o nome do passageiro: '))
                            assentos_disponiveis[numerodoaviao] -= 1
                            print('Reserva realizada com sucesso!')
            case 4:
                os.system('cls || clear')
                numerodoaviao = int(input('Digite o número do avião: '))
                avioes.append(numerodoaviao)
                print(f'Avião de interesse: {numerodoaviao}')
                print(f'Reservas feitas neste avião: {assentos_disponiveis[numerodoaviao]}')
                if numerodoaviao not in avioes:
                    print('Este avião não existe!')
                if assentos_disponiveis[numerodoaviao] <= 0:
                    print('Não há reservas realizadas para este avião!')
            case 5:
                os.system('cls || clear')
                numerodoaviao = int(input('Digite o número do avião: '))
                avioes.append(numerodoaviao)
                nomedopassageiro = str(input('Digite o nome do passageiro: '))
                print(f'Reservas feitas por este passageiro: {avioes[numerodoaviao]}')
                if assentos_disponiveis[numerodoaviao] <= 0:
                    print('Não há reservas realizadas para este passageiro!')
                
            case 6:
                break