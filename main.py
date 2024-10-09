from leitura_pagina_playwright import submit_cnpj_and_calculate_rentabilidade

def main():
    resp = 1
    while resp == 1:
        cnpj = input("Digite o CNPJ do fundo que deseja consultar: ")
        submit_cnpj_and_calculate_rentabilidade(cnpj)
        resp = int(input("Deseja consultar outro fundo? (1 - Sim, 0 - Não): "))



if __name__ == '__main__':
    main()


