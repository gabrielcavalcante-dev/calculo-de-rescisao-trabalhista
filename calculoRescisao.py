print('Olá, bem vindo ao CDR! (Calculadora de Rescisão)\n')

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

while True:
    print('Selecione a opção desejada:')
    print('1 - Fui demitido')
    print('2 - Pedi demissão')
    print('3 - Sair\n')

    opcao = valida_int('Qual sua opcão?: ',1,3)
    if opcao == 1:
        print('Vamos iniciar o calculo da sua rescisão de contrato!\n')

        # Nome
        nome = input('Digite seu nome: ')
        print('Salvando dados...\n')

        # Salário base
        salario = float(input('Digite seu salário?: '))
        print('Salvando dados...\n')

        # FGTS
        fgts = float(input('Digite o saldo do seu FGTS?: '))
        multa_rescisoria = float(fgts / 10 * 4)
        print(f'Multa rescisória de 40%: R$ {multa_rescisoria:,.2f}\n')

        # Opção Saque Aniversário
        print('1 - Saque Aniversário')
        print('2 - Saque Rescisão')

        saque_aniversario = valida_int('Digite a modalidade vigente: ', 1, 2)

        if saque_aniversario == 1:
            fgts = 0
            print('Você não poderá retirar o FGTS! \n')

        if saque_aniversario == 2:
            print('Vocé poderá retirar o FGTS \n')

        # Férias
        ferias = valida_int('Possui férias vencidas? (1 - Sim / 2 - Não): ', 1, 2)
        ferias_1 = float(salario / 3 + salario)

        if ferias == 1:
            ferias_2 = ferias_1
            print(f'O total a receber é: R$ {ferias_2:,.2f}\n')

        elif ferias == 2:
            ferias_2 = 0
            print('Você não tem ferias a receber \n')

        # Férias Proporcional
        ferias_proporcional = valida_int('Possui Férias proporcional? (Digite a quantidade dos meses): ', 1, 11)
        ferias_3 = 0

        if ferias_proporcional == 0:
            ferias_3 = 0

        elif 0 < ferias_proporcional < 12:
            ferias_3 = float((salario / 12) * ferias_proporcional)
            ferias_3 = float(ferias_3 + ferias_3 / 3)
            print(f'O saldo proporcional é: R$ {ferias_3:,.2f}\n')

        # 13° salário
        print('1 - Janeiro | 2 - Fevereiro | 3 - Março | 4 - Abril')
        print('5 - Maio | 6 - Junho | 7 - Julho | 8 - Agosto')
        print('9 - Setembro | 10 - Outubro | 11 - Novembro | 12 - Dezembro')

        salario_13 = valida_int('Digite o número correspondente ao mês do ano: ', 1, 12)
        salario_13 = float(salario / 12 * salario_13)
        print(f'Saldo porpocional do 13° salário é: R$ {salario_13:,.2f}\n')

        # Aviso prévio
        aviso_previo = valida_int('Está cumprindo aviso prévio? (1 - Sim / 2 - Não): ', 1, 2)

        if aviso_previo == 1:
            aviso_previo1 = 0
            print('Você não tem direito a indenização! \n')

        elif aviso_previo == 2:
            print('Você tem direito a indenização no valor de: R$ {} \n'.format(salario))
            aviso_previo1 = salario

        # Montante total
        print(f'{nome}, motante total a receber é: R$ {aviso_previo1 + salario_13 + ferias_2 + ferias_3 + fgts + multa_rescisoria:,.2f}\n')

        montante_total = salario + salario_13 + ferias_2 + fgts + multa_rescisoria + ferias_3

        # Base salárial para o seguro desemprego
        print('Digite seus 3 últimos salários para calcularmos o valor da parcela do seu seguro desemprego, caso você tenha direito')
        salario_retrasado = int(input('Digite o valor do seu salário do mês retrasado: '))
        salario_anterior = int(input('Digite o valor do seu salário do mês anterior: '))
        salario_atual = int(input('Digite o valor do seu salário do mês atual: '))

        salario_seguro = (salario_atual + salario_anterior + salario_retrasado) / 3

        # Seguro desemprego
        seguro_desemprego = int(input('Quantos meses trabalhados na empresa?: '))
        seguro_desemprego1 = salario_seguro / 100
        seguro_desemprego1 = int(seguro_desemprego1 * 80)

        x = 0

        if 0 <= seguro_desemprego < 9:
            print('Você não tem direito ao seguro desemprego! \n')
            x = 0

        elif 9 <= seguro_desemprego < 13:
            print('Você ira receber 3 parcelas de: R$ {} \n'.format(seguro_desemprego1))
            x = 3



        elif 12 <= seguro_desemprego < 24:
            print('Você ira receber 4 parcelas de: R$ {} \n'.format(seguro_desemprego1))
            x = 4

        else:
            print('Você ira receber 5 parcelas de: R$ {} \n'.format(seguro_desemprego1))
            x = 5

        # Criar e salvar relatório

        z = valida_int('Deseja salvar o relatório? (1 - Sim / 2 - Não): ', 1, 2)

        if z == 1:

            print('Relatório salvo com sucesso!')

            arquivo = open('relatório_fuidemitido.txt', 'w+')
            arquivo.write('{}, segue abaixo as informações sobre sua rescisão contratual\n'.format(nome))
            arquivo.write(f'Aviso previo: R$ {aviso_previo1:,.2f}\n')
            arquivo.write(f'FGTS: R${fgts:,.2f}\n')
            arquivo.write(f'Multa de 40% sobre FGTS: R${multa_rescisoria:,.2f}\n')
            arquivo.write(f'Férias: R${ferias_2:,.2f}\n')
            arquivo.write(f'Férias proporcional: R${ferias_3:,.2f}\n')
            arquivo.write(f'13º Salário: R${salario_13:,.2f}\n')
            arquivo.write(f'O total a receber será: R${montante_total:,.2f}\n')
            arquivo.write('E você ira receber {} parcelas de: R$ {} \n'.format(x, seguro_desemprego1))
            arquivo.close()

        else:
            print('Processo finalizado!')

        print('Programa Encerrado...\n')

    elif opcao == 2:
        print('Você não terá direito ao FGTS e seguro desemprego!')
        print('Vamos iniciar o calculo da sua rescisão de contrato!\n')

        # Nome
        nome = input('Digite seu nome: ')
        print('Salvando dados... \n')

        # Salário base
        salario = float(input('Digite seu salário?: '))
        print('Salvando dados... \n')

        # Férias
        ferias = valida_int('Possui férias vencidas? (1 - Sim / 2 - Não): ',1,2)
        ferias_1 = float(salario / 3 + salario)

        if ferias == 1:
            ferias_2 = ferias_1
            print(f'O total a receber é: R$ {ferias_2:,.2f}\n')

        elif ferias == 2:
            ferias_2 = 0
            print('Você não tem ferias a receber \n')

        # Férias Proporcional
        ferias_proporcional = valida_int('Possui Férias proporcional? (Digite a quantidade dos meses): ',1,11)
        ferias_3 = 0

        if ferias_proporcional == 0:
            ferias_3 = 0

        elif 0 < ferias_proporcional < 12:
            ferias_3 = float((salario / 12) * ferias_proporcional)
            ferias_3 = float(ferias_3 + ferias_3 / 3)
            print(f'O saldo proporcional é: R$ {ferias_3:,.2f}\n')


        # 13° salário
        print('1 - Janeiro | 2 - Fevereiro | 3 - Março | 4 - Abril')
        print('5 - Maio | 6 - Junho | 7 - Julho | 8 - Agosto')
        print('9 - Setembro | 10 - Outubro | 11 - Novembro | 12 - Dezembro')

        salario_13 = valida_int('Digite o número correspondente ao mês do ano: ', 1, 12)
        salario_13 = float(salario / 12 * salario_13)
        print(f'Saldo porpocional do 13° salário é: R$ {salario_13:,.2f}\n')

        # Aviso prévio
        desconto = 0
        aviso_previo = valida_int('Cumpriu ou irá cumprir o aviso prévio? (1 - Sim / 2 - Não): ', 1, 2)

        if aviso_previo == 1:
            desconto = 0
            print('Você não tem direito a indenização! \n')

        elif aviso_previo == 2:
            desconto = salario
            print('Será descontado R$ {} sobre o montante da sua rescisão\n'.format(salario))


        # Montante total
        montante_total = (salario_13 + ferias_2 + ferias_3) - desconto
        print(f'{nome}, o total a receber é: {montante_total:,.2f}\n')

        # Criar e salvar relatório
        z = valida_int('Deseja salvar o relatório? (1 - Sim / 2 - Não): ', 1, 2)

        if z == 1:

            print('Relatório salvo com sucesso!')

            arquivo = open('relatório_pedidemissão.txt', 'w+')
            arquivo.write('{}, segue abaixo as informações sobre sua rescisão contratual\n'.format(nome))
            arquivo.write(f'Desconto do aviso previo: R${desconto:,.2f}\n')
            arquivo.write(f'Férias: R${ferias_2:,.2f}\n')
            arquivo.write(f'Férias proporcional: R${ferias_3:,.2f}\n')
            arquivo.write(f'13º Salário: R${salario_13:,.2f}\n')
            arquivo.write(f'O total a receber será: R${montante_total:,.2f}\n')
            arquivo.close()

        else:
            print('Processo finalizado!')

    else:
        print('Programa Encerrado...\n')
        break



