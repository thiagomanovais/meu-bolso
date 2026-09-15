def cadastro():
    import time
    print("Bem-vindo ao MeuBolso! Aqui você pode cadastrar seus gastos e acompanhar suas finanças de forma prática e eficiente.")
    time.sleep(2)
    print("Do seu bolso, para seus sonhos!")
    time.sleep(2)
    nome = str(input("Para começar, como você se chama? "))
    while not nome.strip():
        print("Nome inválido. Por favor, digite um nome válido.")
        nome = str(input("Para começar, como você se chama? "))
    print(f"Olá, {nome}! Prazer em conhecê-lo(a).")
    time.sleep(1)
    print("Antes de começarmos, vamos cadastrar seus gastos. Você poderá adicionar informações como nome, valor, tipo, descrição e categoria do gasto.")
    time.sleep(2)
    salario = float(input("Qual é o seu salário anual? €"))
    while salario <= 0:
        print("Salário inválido. Por favor, digite um valor maior que zero.")
        salario = float(input("Qual é o seu salário anual? €"))
    
    estado_civil = str(input("Você vai fazer seu controle financeiro sozinho(a), ou com seu parceiro(a)? Digite 's' para sozinho(a) ou 'p' para parceiro(a): ")).lower()
    while estado_civil not in ['s', 'p']:
        print("Opção inválida. Por favor, digite 's' para sozinho(a) ou 'p' para parceiro(a).")
        estado_civil = str(input("Você vai fazer seu controle financeiro sozinho(a), ou com seu parceiro(a)? Digite 's' para sozinho(a) ou 'p' para parceiro(a): ")).lower()
    if estado_civil == 'p':
        parceiro_nome = str(input("Qual é o nome do seu parceiro(a)? "))
        while not parceiro_nome.strip():
            print("Nome inválido. Por favor, digite um nome válido.")
            parceiro_nome = str(input("Qual é o nome do seu parceiro(a)? "))
        print(f"Ótimo! Agora você e {parceiro_nome} podem cadastrar seus gastos juntos.")
        salario_parceiro = float(input("Qual é o salário do seu parceiro(a)? €"))
        while salario_parceiro <= 0:
            print("Salário inválido. Por favor, digite um valor maior que zero.")
            salario_parceiro = float(input("Qual é o salário do seu parceiro(a)? €"))
        salario_total = salario + salario_parceiro
        print(f"Salário total do casal: €{salario_total:.2f} e mensal é: €{salario_total/12:.2f}")
    if estado_civil == 's':
        print("Ótimo! Agora você pode cadastrar seus gastos sozinho(a).")
        print(f"Seu salário anual é: €{salario:.2f} e mensal é: €{salario/12:.2f}")


if __name__ == "__main__":
    cadastro()