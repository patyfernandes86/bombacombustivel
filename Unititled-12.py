class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecer_por_litro(self, litros):
        valor_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"O valor a pagar é R$ {valor_pagar:.2f}.")
        else:
            print("Não há combustível suficiente na bomba.")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

bomba = BombaCombustivel("Gasolina", 4.50, 1000)

print("Abastecimento por valor:")
bomba.abastecer_por_valor(100)  

print("\nAbastecimento por litro:")
bomba.abastecer_por_litro(35) 

print("\nAlteração de valor do litro:")
bomba.alterar_valor(4.70)  

print("\nAlteração do tipo de combustível:")
bomba.alterar_combustivel("Álcool")  

print("\nAlteração da quantidade de combustível na bomba:")
bomba.alterar_quantidade_combustivel(2200)  

print("\nAbastecimento por valor:")
bomba.abastecer_por_valor(90) 