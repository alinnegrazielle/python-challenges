'''
Bin2Dec permite ao usuário inserir strings de até 8 dígitos binários, 0's e 1's,
em qualquer sequência e, em seguida, exibe seu equivalente decimal.

Esse desafio requer que o desenvolvedor que o está implementando siga estas restrições:

     * Os arrays não podem ser usados para conter os dígitos binários inseridos pelo usuário.
     * Determinar o equivalente decimal de um dígito binário particular na sequência
         deve ser calculado usando uma única função matemática, por exemplo, o natural
         logaritmo. Depende de você descobrir qual função usar.

Requisitos de sistema:

     * O usuário pode inserir até 8 dígitos binários em um campo de entrada.
     * O usuário deve ser notificado se algo diferente de 0 ou 1 for inserido.
     * O usuário visualiza os resultados em um único campo de saída contendo o decimal (base 10)
         equivalente ao número binário inserido.

'''


binNum = str(input('Enter a number in binary, up to eight digits: '))

i = 0
tsum = 0
for bin in range(len(binNum) - 1, -1, -1):
    dec = (binNum[bin] * (2**i))
    i += 1
    # print(dec)
    sum = 0
    for contents in dec:
        if contents.isdigit():
            sum += int(contents)
    # print(sum)
    tsum += sum

print('The number {} is equivalent to {} in decimal.'.format(binNum, tsum))
