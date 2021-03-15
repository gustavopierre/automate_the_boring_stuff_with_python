def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print (result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result


try:
    num = int(input('Digite um numero inteiro:'))
except ValueError:
    print('Tipo errado')
else:
    resultado = collatz(num)
    while resultado != 1:
        resultado = collatz(resultado)
        