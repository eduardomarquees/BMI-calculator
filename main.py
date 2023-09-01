def calcular_imc(peso, altura):
    imc = peso /(altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso Normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obeso"

def main():
    print('Calculadora IMC')
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a sua altura: '))

    imc =calcular_imc(peso, altura)
    status = interpretar_imc(imc)

    print(f'Seu IMC é {imc:.2f}')
    print(f'Status: {status}')

if __name__ == "__main__":
    main()