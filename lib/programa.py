from time import sleep
from typing import Dict, List

from .codificadores import cod_cesar, cod_vigenere, cod_onetimepad, cod_morse, cod_tapcode, cod_autokey, cod_niilista
from .decodificadores import decod_cesar, decod_vigenere, decod_onetimepad, decod_morse, decod_tapcode, decod_autokey, decod_niilista

# Lista contendo o nome da criptografia e suas funções
opcoes_cripto: List[list] = [
    ['Cifra de César', cod_cesar, decod_cesar],
    ['Cifra de Vigenère', cod_vigenere, decod_vigenere],
    ['One-time pad (Cifra de uso único)', cod_onetimepad, decod_onetimepad],
    ['Código morse', cod_morse, decod_morse],
    ['Tap code (Código da batida)', cod_tapcode, decod_tapcode],
    ['Autokey cipher (Cifra de autochave)', cod_autokey, decod_autokey],
    ['Cifra niilista', cod_niilista, decod_niilista]
]


def programa() -> None:
    """Função que recebe qual das opções de criptografias o usuário quer executar"""
    print('Menu principal\n')
    print('1 - Cifra de César')
    print('2 - Cifra de Vigenère')
    print('3 - One-time pad (Cifra de uso único)')
    print('4 - Código morse')
    print('5 - Tap code (Código da batida)')
    print('6 - Autokey cipher (Cifra de autochave)')
    print('7 - Cifra niilista')
    print('8 - Sair do programa\n')

    try:
        opcao_escolhida: int = int(input('Digite umas da opções: '))

        if opcao_escolhida == 8:
            print('Programa finalizado')
            exit()

        else:
            print(f'Resultado: {efetuar_opcao(opcoes_cripto[opcao_escolhida - 1])}')

    except (ValueError):
        print('Opção inválida.')

    sleep(3)
    print('\n' * 15)
    programa()


def receber_operacao() -> int:
    """Função para saber se o usuário deseja codificar ou decodificar"""
    print('Codificar ou decodificar\n')
    print('1 - Codificar')
    print('2 - Decodificar')
    escolha: int = int(input('Digite uma das opções: '))

    if escolha == 1 or escolha == 2:
        return escolha

    else:
        print('Opção inválida.')
        return False


def receber_dados(criptografia: list, operacao: int) -> list:
    opcoes_operacoes: Dict[int, str] = {1: 'Codificador', 2: 'Decodificador'}
    indice_cripto: int = opcoes_cripto.index(criptografia)
    lista_dados: list = []
    nome_operacao: str = opcoes_operacoes.get(operacao)

    print(f'{nome_operacao} de {criptografia[0].lower()}' )
    mensagem: str = input('Digite a mensagem: ')
    lista_dados.append(mensagem)

    if indice_cripto != 3 and indice_cripto != 4:
        chave: str = input('Digite a chave: ')
        lista_dados.append(chave)

    if indice_cripto == 4:
        print('\nEscolha uma das opções\n')
        print('1 - Mensagem em pares de números')
        print('2 - Mensagem em pontos')
        tipo_cod: int = int(input('Digite uma das opções: '))
        lista_dados.append(tipo_cod)
    
    elif indice_cripto == 6:
        palavra_chave: str = input('Digite a palavra-chave: ')
        lista_dados.append(palavra_chave)

    return lista_dados


def efetuar_opcao(escolha_cripto: list) -> str:
    """Função que verifica se o usuário escolheu uma opção válida, e se sim, ela é executada"""
    escolha_operacao: int = 0
    while not escolha_operacao:
        escolha_operacao = receber_operacao()

    dados: list = receber_dados(escolha_cripto, escolha_operacao)
    return escolha_cripto[escolha_operacao](*dados)
