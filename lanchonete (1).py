print("=== Lá no Charuri ===")
print(" " * 4, "Lanchonete" )

nome_cliente = input ("Por favor digite o seu nome ")
print (f"Olá, {nome_cliente}")

print ("=== NOSSO CARDÁPIO ===")
print ("1. Hamburguer Matador - R$ 39.59")
print ("2. Podrão - R$ 22.00")
print ("3. Misto Quente - R$ 12.00")
print ("4. Batata Frita 100gr - R$ 9.00")
# Recebendo dados do pedido
print ("\n Faça o seu pedido")
qtd_hamburguer = int (input("Quantos Hamburgueres você deseja? "))
qtd_podrao = int (input("Quantos Podrao você deseja? "))
qtd_misto = int (input("Quantos Misto Quente você deseja? "))
qtd_batata = int (input("Quantas Batata Frita de 100gr você deseja? "))
# Fechando a conta
total_hamburguer = qtd_hamburguer * 39.00
total_podrao = qtd_podrao * 22.00
total_misto = qtd_misto * 12.00
total_batata = qtd_batata * 9.00
# Exibindo o cupom fiscal
print ("\n" + "="*30)
print (" " * 8 + "Cupom Fiscal" + " " * 8)
print ("=" * 30)
print (f"Cliente: {nome_cliente}")
print (f"Hamburguer Matador: {total_hamburguer}")
print (f"Podrão: {total_podrao}")
print (f"MIsto Quente: {total_misto}")
print (f"Batata Frita: {total_batata}")
print ("Total do Pedido: {total_hamburguer+total_podrao+total_misto+total_batata}")
