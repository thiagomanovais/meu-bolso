def Gastos():
    gastos = {}
    categorias = {
    "1": "Alimentação",
    "2": "Transporte",
    "3": "Moradia",
    "4": "Lazer",
    "5": "Saúde",
    "6": "Educação",
    "7": "Outros"
}
    while True:
        gastos_id = len(gastos) + 1
        gasto_nome = str(input("Digite o nome do gasto: "))
        gasto_valor = float(input("Digite o valor do gasto: €"))
        gasto_tipo = str(input("Digite o tipo do gasto (fixo ou variável): ")).lower()
        gasto_descricao = str(input("Digite a descrição do gasto: "))
        gasto_categoria = str(input("Digite a categoria do gasto: 1- Alimentação, 2- Transporte, 3- Moradia, 4- Lazer, 5- Saúde, 6- Educação, 7- Outros: "))
        while gasto_categoria not in categorias:
            print("Categoria inválida. Por favor, escolha uma categoria válida.")
            gasto_categoria = str(input("Digite a categoria do gasto: 1- Alimentação, 2- Transporte, 3- Moradia, 4- Lazer, 5- Saúde, 6- Educação, 7- Outros: "))
        gasto_categoria = categorias[gasto_categoria]
        gastos[gastos_id] = {"nome": gasto_nome, "valor": gasto_valor, "tipo": gasto_tipo, "descrição": gasto_descricao, "categoria": gasto_categoria}
        print("Gasto adicionado com sucesso!")
        continuar = str(input("Deseja adicionar outro gasto? (s/n): ")).lower()
        if continuar != 's':
            break
    return gastos

if __name__ == "__main__":
    gastos_cadastrados = Gastos()
    print("Gastos registrados:")
    for id, gasto in gastos_cadastrados.items():
        print(f"ID: {id}, Nome: {gasto['nome']}, Valor: €{gasto['valor']:.2f}, Tipo: {gasto['tipo']}, Descrição: {gasto['descrição']}, Categoria: {gasto['categoria']}")