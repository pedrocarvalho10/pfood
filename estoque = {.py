estoque = {
    "modelo1": 20,
    "modelo2": 15,
    "modelo3": 10,
    "modelo4": 30
}

def exibir_estoque():
    print("Estoque disponível:")
    for modelo, quantidade in estoque.items():
        print(f"{modelo}: {quantidade} unidades")

def adicionar_estoque(modelo, quantidade):
    if modelo in estoque:
        estoque[modelo] += quantidade
        print(f"{quantidade} unidades de {modelo} adicionadas ao estoque.")
    else:
        print(f"Modelo {modelo} não encontrado no estoque. Não foi possível adicionar.")

def vender(modelo, quantidade):
    if modelo in estoque and estoque[modelo] >= quantidade:
        estoque[modelo] -= quantidade
        print(f"{quantidade} unidades de {modelo} vendidas.")
    else:
        print(f"Estoque insuficiente para vender {quantidade} unidades de {modelo}.")