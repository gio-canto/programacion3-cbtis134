print ("--" * 20)
print ("FERRETERÍA 'EL MARTILLO DE ORO'")
print ("Sistema de venta con descuentos")
print("--" * 20)
products = []
while True:
    name = input("Ingrese el nombre del producto (0 para terminar): ")
    if name == "0":
        break
    try:
        price = float(input(f"Ingrese el precio del producto '{name}': "))
    except ValueError:
        print("Precio inválido. Intente de nuevo.")
        continue
    products.append((name, price))

nopro = len(products)
total = sum(price for _, price in products)

if nopro > 10:
    descuento = total * 0.40
elif 5 <= nopro <= 9:
    descuento = total * 0.30
elif 3 <= nopro <= 4:
    descuento = total * 0.20
else:
    descuento = 0

total_pagar = total - descuento

print("-----------------------------------")
print("           TICKET DE COMPRA        ")
print("-----------------------------------")
for idx, (name, price) in enumerate(products, 1):
    print(f"{idx}. {name:20} ${price:8.2f}")
print("-----------------------------------")
print(f"Cantidad de productos distintos: {nopro}")
print(f"Total sin descuento:           ${total:8.2f}")
print(f"Descuento aplicado:            ${descuento:8.2f}")
print(f"Total a pagar:                 ${total_pagar:8.2f}")
print("-----------------------------------")
