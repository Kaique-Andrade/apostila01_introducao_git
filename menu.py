import calculadora

def menu():
    while True:
        print("\nMenu:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                print(f"Resultado: {calculadora.somar (num1, num2)}")
            elif opcao == "2":
                print(f"Resultado: {calculadora.subtrair (num1, num2)}")
            elif opcao == "3":
                print(f"Resultado: {calculadora.multiplicar (num1, num2)}")
            elif opcao == "4":
                print(f"Resultado: {calculadora.dividir (num1, num2)}")
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()