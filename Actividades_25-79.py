# TSMHSPMHMPCVMF2L - Colección de actividades con menú mejorado
# modelo preliminar
username = ("papu")
from random import random
import time 
import os
import math
import re

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def actividad1_funcionpieza():
    limpiar_pantalla ()
    print ("==============================")
    print ("         Calculo de X")
    print ("==============================")
    try:
        x = float(input("Ingrese el valor de x: "))
    except ValueError:
        print("Entrada inválida.")
        return
    if x <= 0:
        y = x**2 + 5
    elif x < 5:
        y = 3 * x - 1
    else:
        y = x**2 - 4 * x + 5
    
    limpiar_pantalla ()
    print(f"y = {y}")
    os.system ("Pause")

    

def actividad2_terrenos():
    limpiar_pantalla ()
    PRECIOS = {'A': 70, 'B': 60, 'C': 45, 'D': 30}
    print ("====================================")
    print ("    INMOBILARIA HERDIER SA DE CV")
    print ("====================================")
    print (f"¡Hola!: {username}")
    print ("")
    print ("Estas son las zonas disponibles:")
    print ("------------------------------------")
    print (f"ZONA A = ${PRECIOS['A']} m²")
    print (f"ZONA B = ${PRECIOS['B']} m²")
    print (f"ZONA C = ${PRECIOS['C']} m²")
    print (f"ZONA D = ${PRECIOS['D']} m²")
    print ("------------------------------------")
    zona = input("Favor de selecionar la deseada: ").strip().upper()
    if zona not in PRECIOS:
        print("Zona inválida.")
        return
    try:
        area = float(input("Área del terreno en m2: "))
    except ValueError:
        print("Área inválida.")
        return
    precio = PRECIOS[zona] * area
    limpiar_pantalla ()
    time.sleep(0.50)
    limpiar_pantalla ()
    print ("====================================")
    print ("             Cotización")
    print ("====================================")
    print ("Estimado usuario se le informa que")
    print ("de acuerdo a su eleccion el precio")
    print (f"de venta del terrero es de : ${precio:,.2f}")
    print ("Atentamente:")
    print ("INMOBILARIA HERDIER")
    print ("Gracias por su tiempo φ(*￣0￣)")
    os.system ("Pause")

def actividad3_numerosdel1al10conwhile():
    limpiar_pantalla ()
    i = 1
    while i <= 10:
        print(i)
        i += 1
    os.system ("Pause")

def actividad4_numerosdel1al10confor():
    limpiar_pantalla ()
    for i in range(1, 11):
        print(i)
    os.system ("Pause")

def actividad5_maximohasta99():
    limpiar_pantalla ()
    maximo = None
    while True:
        try:
            n = int(input("Ingrese un número (termine con -99): "))
        except ValueError:
            print("Número inválido")
            continue
        if n == -99:
            break
        if maximo is None or n > maximo:
            maximo = n
    if maximo is None:
        print("No se ingresaron números válidos.")
    else:
        print(f"Mayor: {maximo}")
    os.system ("Pause")

def actividad6_sumas_productos_impares_20_80():
    limpiar_pantalla ()
    impares = [n for n in range(21, 80) if n % 2 == 1]
    s = 0
    p = 1
    for n in impares:
        s += n
        p *= n
    print(f"Suma impares (20,80): {s}")
    print(f"Producto impares (20,80): {p}")
    os.system ("Pause")

def actividad7_conteorangos_naturales():
    limpiar_pantalla ()
    print("Ingrese números naturales. Finalice con vacío.")
    menores_15 = entre_25_45 = mayores_50 = 0
    while True:
        s = input("n = ")
        if not s:
            break
        if not s.isdigit():
            print("Solo naturales.")
            continue
        n = int(s)
        if n < 15:
            menores_15 += 1
        if 25 <= n <= 45:
            entre_25_45 += 1
        if n > 50:
            mayores_50 += 1
    print(f"Menores de 15: {menores_15}")
    print(f"Entre 25 y 45: {entre_25_45}")
    print(f"Mayores de 50: {mayores_50}")
    os.system ("Pause")

def actividad8_cadenasoperaciones():
    limpiar_pantalla ()
    s1 = input("Cadena 1: ")
    s2 = input("Cadena 2: ")

    print("Longitud s1:", len(s1))
    print("Longitud s2:", len(s2))

    print("Mayúsculas s1:", s1.upper())
    print("Mayúsculas s2:", s2.upper())

    print("Minúsculas s1:", s1.lower())
    print("Minúsculas s2:", s2.lower())

    print("s1 sin el primer carácter:", s1[1:] if len(s1) > 0 else s1)
    print("s1 sin la primera palabra:", " ".join(s1.split()[1:]) if s1.split() else "")

    print("s2 sin el último carácter:", s2[:-1] if len(s2) > 0 else s2)
    print("s2 sin la última palabra:", " ".join(s2.split()[:-1]) if s2.split() else "")

    palabras_s1 = [p for p in re.split(r"\s+", s1.strip()) if p]
    palabra_corta = min(palabras_s1, key=len) if palabras_s1 else ""
    print("Palabra más corta en s1:", palabra_corta)

    palabras_s2 = [p for p in re.split(r"\s+", s2.strip()) if p]
    palabra_larga = max(palabras_s2, key=len) if palabras_s2 else ""
    print("Palabra más larga en s2:", palabra_larga)

    print("s1 invertida:", s1[::-1])
    print("Unión s1+s2:", s1 + s2)

    conteo_vocales = {v: 0 for v in "aeiou"}
    for ch in s1.lower():
        if ch in conteo_vocales:
            conteo_vocales[ch] += 1
    print("Conteo de vocales en s1:", conteo_vocales)

    print("s1 sin espacios:", "".join(s1.split()))

    palabra = input("Palabra a invertir dentro de s2 (primera ocurrencia): ").strip()
    if palabra in s2:
        s2_invertida = s2.replace(palabra, palabra[::-1], 1)
        print("Resultado de s2 tras invertir la palabra:", s2_invertida)
    else:
        print("La palabra no se encuentra en s2.")
    os.system ("Pause")

def actividad9_sumaprimerosN():
    limpiar_pantalla ()
    try:
        N = int(input("N: "))
        if N < 0:
            raise ValueError
        suma = N * (N + 1) // 2
        print(f"Suma 1..N = {suma}")
    except ValueError:
        print("N inválido.")
    os.system ("Pause")

def actividad10_pulsaciones_por_edad_y_sexo():
    limpiar_pantalla ()
    print ("===========================================")
    print ("         Simulador de pulsaciones")
    print ("===========================================")
    nombre = input("Ingrese el nombre del encuestado: ")
    if nombre == ":v" :
        print ("Viva la grase xdddd :v")
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Edad inválida.")
        return
    while True :
        sexo = input("Sexo (F/M): ").strip().upper()
        if sexo.startswith('F'):
            resultado = (220 - edad) / 10.0
            break
        elif sexo.startswith('M'): 
            resultado = (210 - edad) / 10.0
            break
        elif sexo == "X" :
            print ("Esta bien pero.....")
            time.sleep(1)
            break
        elif sexo.startswith("0") :
            print ("Fracasado bro ༼ つ ◕_◕ ༽つ")
            time.sleep(1)
            continue
        elif sexo.startswith("1") :
            print ("Todo un semental ༼ つ ◕_◕ ༽つ")
            time.sleep(1)
            continue
        else :
            resultado = (210 - edad) / 10.0
    limpiar_pantalla ()
    time.sleep(0.50)
    print(f"Estimado : {nombre}, sus pulsaciones cada 10 s son de : {resultado:.2f}")
    print(f"Espero que te sirva :D")
    os.system ("Pause")

def actividad12_reforestacion():
    limpiar_pantalla ()
    print ("===================================================")
    print ("                 Fundacion Gea A.C                 ")
    print ("===================================================")
    print ("herramienta de de calculo de costo de reforestacion")
    print ("Copyright ©1993 Gea A.C")
    time.sleep(0.50)
    try:
        hectareas = float(input("Ingrese la superficie en hectáreas: "))
    except ValueError:
        print("Dato inválido.")
        return
    m2 = hectareas * 10_000
    if m2 > 1_000_000:
        pino_p, oyamel_p, cedro_p = 0.70, 0.20, 0.10
    else:
        pino_p, oyamel_p, cedro_p = 0.50, 0.30, 0.20

    sup_pino = m2 * pino_p
    sup_oyamel = m2 * oyamel_p
    sup_cedro = m2 * cedro_p

    n_pinos = int((sup_pino/10)*8)
    n_oyameles = int((sup_oyamel/15)*15)
    n_cedros = int((sup_cedro/18)*10)
    limpiar_pantalla ()
    time.sleep(0.50)
    print ("===================================================")
    print ("|                Operacion Gea                    |")
    print ("===================================================")
    print ("Ante los resultados se podra reforestar:")
    print ("-----------------------")
    print(f"Pinos: {n_pinos}")
    print(f"Oyameles: {n_oyameles}")
    print(f"Cedros: {n_cedros}")
    print ("-----------------------")
    print ("Por un mundo mas limpio siempre gea")
    print (f"Estimado {username} gracias por usarme.")
    os.system ("Pause")

def actividad13_imeca_sancion():
    print ("===================================================")
    print ("                 Fundacion Gea A.C                 ")
    print ("===================================================")
    lecturas = []
    for i in range(1, 6):
        while True:
            try:
                v = float(input(f"IMECA día {i}: "))
                break
            except ValueError:
                print("Valor inválido.")
        lecturas.append(v)
    promedio = sum(lecturas)/5
    print(f"Promedio IMECA: {promedio:.2f}")
    if promedio > 170:
        try:
            gan_dia = float(input("Ganancias diarias cuando no se detiene la producción: $"))
        except ValueError:
            print("Ganancias inválidas.")
            return
        multa = 0.5*gan_dia
        perdida = multa + 7*gan_dia
        print("Sanción: parar 1 semana + multa 50% de ganancias diarias")
        print(f"Multa: ${multa:,.2f}")
        print(f"Pérdida total estimada: ${perdida:,.2f}")
    else:
        print("Sin sanción ni multa.")

def actividad14_alturapelota_tabla():
    Vo = 96
    print("t (s)\t h(t) (m)")
    for t in range(1, 9):
        h = Vo * t - 5 * (t ** 2)
        print(f"{t}\t{h:.2f}")

def actividad15_banco_balances():
    try:
        n = int(input("Número de clientes a procesar (ej. 4000): "))
    except ValueError:
        print("Número inválido.")
        return
    for i in range(1, n+1):
        print(f"--- Cliente {i} ---")
        N = input("Número de cuenta: ").strip()
        try:
            BP = float(input("Balance previo: "))
        except ValueError:
            print("Balance inválido."); return
        try:
            NT = int(input("No. de transacciones: "))
        except ValueError:
            print("Número inválido."); return
        balance = BP
        for j in range(NT):
            tipo = input("Transacción (D=depósito/R=retiro): ").strip().upper()
            try:
                monto = float(input("Monto: "))
            except ValueError:
                print("Monto inválido."); return
            if tipo == 'D':
                balance += monto
            elif tipo == 'R':
                balance -= monto
            else:
                print("Tipo inválido."); return
        if balance < 50000:
            balance -= 1000
        print(f"Cuenta {N}, Balance final: ${balance:,.2f}")
    print("Fin.")

def actividad16_personas_promedios():
    total = 0
    edades_no_mayores_45 = []
    alturas_no_mayores_45 = []
    print("Ingrese nombre vacío para terminar.")
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            break
        try:
            edad = int(input("Edad: "))
            altura = float(input("Altura (m): "))
        except ValueError:
            print("Dato inválido."); continue
        total += 1
        if edad <= 45:
            edades_no_mayores_45.append(edad)
            alturas_no_mayores_45.append(altura)
    print(f"Personas consideradas: {total}")
    if edades_no_mayores_45:
        print(f"Edad promedio (<=45): {sum(edades_no_mayores_45)/len(edades_no_mayores_45):.2f}")
        print(f"Altura promedio (<=45): {sum(alturas_no_mayores_45)/len(alturas_no_mayores_45):.2f}")
    else:
        print("No hubo personas con edad <= 45.")

def actividad17_empleados_sueldos():
    entre_100_300 = 0
    mas_300 = 0
    total_sueldos = 0.0
    print("Empleado vacío para terminar.")
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            break
        _ = input("Categoría/Puesto: ").strip()
        try:
            sueldo = float(input("Sueldo: "))
        except ValueError:
            print("Sueldo inválido."); continue
        total_sueldos += sueldo
        if 100 <= sueldo <= 300:
            entre_100_300 += 1
        elif sueldo > 300:
            mas_300 += 1
    print(f"Empleados $100-$300: {entre_100_300}")
    print(f"Empleados > $300: {mas_300}")
    print(f"Total sueldos: ${total_sueldos:,.2f}")

def actividad18_factura_productos():
    print("Producto vacío para terminar.")
    total = 0.0
    while True:
        desc = input("Descripción: ").strip()
        if not desc:
            break
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Dato inválido."); continue
        sub = precio*cantidad
        total += sub
        print(f"{desc} | ${precio:.2f} x {cantidad} = ${sub:.2f}")
    print(f"TOTAL: ${total:.2f}")

def actividad19_circunferencia():
    try:
        r = float(input("Radio: "))
    except ValueError:
        print("Radio inválido."); return
    L = 2*math.pi*r
    A = math.pi*(r**2)
    print(f"Longitud: {L:.4f}")
    print(f"Área: {A:.4f}")

def actividad20_kmh_a_ms():
    try:
        v_kmh = float(input("Velocidad (km/h): "))
    except ValueError:
        print("Dato inválido."); return
    v_ms = v_kmh * 1000/3600
    print(f"{v_kmh} km/h = {v_ms:.4f} m/s")

def actividad21_hipotenusa():
    try:
        a = float(input("Cateto a: "))
        b = float(input("Cateto b: "))
    except ValueError:
        print("Dato inválido."); return
    c = math.hypot(a, b)
    print(f"Hipotenusa: {c:.4f}")

def actividad22_area_triangulo_lados():
    try:
        a = float(input("Lado a: "))
        b = float(input("Lado b: "))
        c = float(input("Lado c: "))
    except ValueError:
        print("Dato inválido."); return
    p = (a + b + c) / 2
    area = math.sqrt(max(p*(p-a)*(p-b)*(p-c), 0.0))
    print(f"Área: {area:.4f}")

def actividad23_numero_suerte():
    def suma_de_cifras(n: int) -> int:
        return sum(int(d) for d in str(abs(n)))
    try:
        d = int(input("Día: "))
        m = int(input("Mes: "))
        a = int(input("Año: "))
    except ValueError:
        print("Dato inválido."); return
    s = d + m + a
    lucky = suma_de_cifras(s)
    print(f"Número de la suerte: {lucky}")

def actividad24_numero_producto_o_suma():
    while True:
        try:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
        except ValueError:
            print("Dato inválido."); continue
        if a > 0:
            print(f"Producto b*c = {b*c}")
        else:
            print(f"Suma b+c = {b+c}")
        otra = input("¿Desea repetir? (s/n): ").strip().lower()
        if otra != 's':
            break

def actividad25_leerint():
    mensaje = "Ingrese un entero válido: "
    n = input("Ingrese un entero (sin validar): ")
    print("Usted ingresó:", n)
    while True:
        s = input(mensaje)
        try:
            n2 = int(s)
            print("Entero válido:", n2)
            return
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def actividad26_estadistica_N_numeros():
    try:
        N = int(input("Cantidad N (>0): "))
        if N <= 0:
            raise ValueError
    except ValueError:
        print("N inválido."); return
    nums = []
    for i in range(N):
        while True:
            try:
                nums.append(float(input(f"n{i+1}: ")))
                break
            except ValueError:
                print("Dato inválido.")
    print("Mayor:", max(nums))
    print("Menor:", min(nums))
    print("Media:", sum(nums)/len(nums))

def actividad27_precio_zapatos_tallas():
    PRECIOS_8 = {'A': 345.50, 'B': 298.70, 'C': 246.00}
    modelo = input("Modelo (A=Ejecutivo, B=Premier, C=Emperador): ").strip().upper()
    if modelo not in PRECIOS_8:
        print("Modelo inválido."); return
    try:
        talla = int(input("Talla (8/9/10): "))
        if talla not in (8, 9, 10):
            raise ValueError
    except ValueError:
        print("Talla inválida."); return
    base = PRECIOS_8[modelo]
    incremento = (talla - 8) * 10
    precio = base + incremento
    print(f"Precio: ${precio:.2f}")

def actividad28_interes_mensual_capital():
    try:
        capital = float(input("Capital: "))
    except ValueError:
        print("Dato inválido."); return
    if capital < 500:
        tasa = 0.02
    elif capital <= 1500:
        tasa = 0.045
    else:
        tasa = 0.09
    interes = capital * tasa
    print(f"Interés mensual: ${interes:,.2f}")

def actividad29_digitos_pares():
    def todos_pares(n: int) -> bool:
        s = str(abs(n))
        return (len(s) == 4) and all(int(d) % 2 == 0 for d in s)
    try:
        n = int(input("Número entero de 4 dígitos: "))
    except ValueError:
        print("Dato inválido."); return
    if todos_pares(n):
        print("Todos los dígitos son pares.")
    else:
        print("No cumple.")

def actividad30_reparto_de_herencia():
    try:
        herencia = float(input("Monto total de la herencia: "))
        hijos = int(input("Número de hijos: "))
    except ValueError:
        print("Dato inválido."); return
    if hijos <= 0:
        print("Sin hijos."); return
    if hijos < 4:
        por_hijo = herencia / hijos
        partes = [por_hijo] * hijos
    else:
        mayor = herencia / 2
        resto = herencia - mayor
        por_cada = resto / (hijos - 1)
        partes = [mayor] + [por_cada] * (hijos - 1)
    for i, monto in enumerate(partes, start=1):
        print(f"Hijo {i}: ${monto:,.2f}")

def actividad31_descuento_por_importe():
    def descuento_por_importe(importe: float) -> float:
        if importe >= 1000:
            return 0.20
        elif importe >= 800:
            return 0.16
        elif importe >= 300:
            return 0.12
        else:
            return 0.08
    try:
        unidades = int(input("Unidades: "))
        precio = float(input("Precio unitario: "))
    except ValueError:
        print("Dato inválido."); return
    importe = unidades * precio
    desc = descuento_por_importe(importe)
    desc_monto = importe * desc
    total = importe - desc_monto
    print(f"Importe: ${importe:,.2f}")
    print(f"Descuento ({desc*100:.0f}%): ${desc_monto:,.2f}")
    print(f"Total a pagar: ${total:,.2f}")

def actividad32_pago_trabajador_bonif_desc():
    BONIF = {
        'A': {'E': 0.20, 'N': 0.17},
        'B': {'E': 0.18, 'N': 0.15},
        'C': {'E': 0.15, 'N': 0.14},
        'D': {'E': 0.12, 'N': 0.10},
    }
    DESC = {'E': 0.06, 'N': 0.04}
    try:
        sueldo = float(input("Sueldo: "))
    except ValueError:
        print("Dato inválido."); return
    cat = input("Categoría (A/B/C/D): ").strip().upper()
    if cat not in BONIF:
        print("Categoría inválida."); return
    cond = input("Condición (E=Estable / N=No estable): ").strip().upper()
    if cond not in ('E', 'N'):
        print("Condición inválida."); return
    bonificacion = sueldo * BONIF[cat][cond]
    bruto = sueldo + bonificacion
    descuento = bruto * DESC[cond]
    total = bruto - descuento
    print(f"Bonificación: ${bonificacion:,.2f}")
    print(f"Descuento: ${descuento:,.2f}")
    print(f"Pago total: ${total:,.2f}")

def actividad33_estimulo_academico_unidades():
    try:
        prom = float(input("Promedio: "))
    except ValueError:
        print("Dato inválido."); return
    nivel = input("Nivel (P=Preparatoria, otro = sin estímulo): ").strip().upper()
    unidades = 0
    desc = 0.0
    if nivel == 'P':
        if prom >= 9.5:
            unidades, desc = 55, 0.25
        elif prom >= 9.0:
            unidades, desc = 50, 0.10
        elif 7.0 < prom < 9.0:
            unidades, desc = 50, 0.0
        else:
            try:
                reprob = int(input("Materias reprobadas (0-3): "))
            except ValueError:
                print("Dato inválido."); return
            if 0 <= reprob <= 3:
                unidades, desc = 45, 0.0
    print(f"Unidades permitidas: {unidades}")
    print(f"Descuento: {desc*100:.0f}%")

def actividad34_tipo_caracter():
    s = input("Ingrese un carácter: ")
    if not s:
        print("Vacío.")
        return
    c = s[0]
    if c.isdigit():
        print("número")
    elif 'a' <= c <= 'z':
        print("letra minúscula")
    elif 'A' <= c <= 'Z':
        print("letra mayúscula")
    else:
        print("Carácter no válido")

def actividad35_contar_20_numeros():
    pos = neg = cero = 0
    for i in range(20):
        while True:
            try:
                n = float(input(f"n{i+1}: "))
                break
            except ValueError:
                print("Dato inválido.")
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            cero += 1
    print(f"Positivos: {pos}, Negativos: {neg}, Ceros: {cero}")

def actividad36_ordenadas_pares_funcion():
    def f(x): 
        return x**3 + 1
    print("x\ty")
    for x in range(0, 31, 2):
        print(f"{x}\t{f(x)}")

def main():
    limpiar_pantalla ()
    time.sleep(0.50)   
    username = input ("Ingrese su nombre: ")
    while True:
        limpiar_pantalla ()
        print("\n===== MENÚ DE OPCIONES =====")
        print("1. Función a trozos")
        print("2. Precio de terrenos")
        print("3. Números del 1 al 10 (while)")
        print("4. Números del 1 al 10 (for)")
        print("5. Máximo hasta -99")
        print("6. Suma y producto impares (20,80)")
        print("7. Conteo por rangos (naturales)")
        print("8. Operaciones con cadenas")
        print("9. Suma 1..N")
        print("10. Pulsaciones (edad/sexo)")
        print("11. Reforestación")
        print("12. IMECA y sanción")
        print("13. Altura de pelota (tabla)")
        print("14. Banco (balances)")
        print("15. Promedios (<=45 años)")
        print("16. Empleados y sueldos")
        print("17. Factura de productos")
        print("18. Circunferencia (L y A)")
        print("19. km/h → m/s")
        print("20. Hipotenusa")
        print("21. Área de triángulo (lados)")
        print("22. Número de la suerte")
        print("23. Producto o suma (según a)")
        print("24. Leer entero validado")
        print("25. Estadística N números")
        print("26. Precio zapatos por talla")
        print("27. Interés mensual por capital")
        print("28. ¿Todos los dígitos pares?")
        print("29. Reparto de herencia")
        print("30. Descuento por importe")
        print("31. Pago trabajador (bonif/desc)")
        print("32. Estímulo académico")
        print("33. Tipo de carácter")
        print("34. Contar 20 números")
        print("35. Pares (0..30) y f(x)=x^3+1")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            actividad1_funcionpieza()
        elif opcion == "2":
            actividad2_terrenos()
        elif opcion == "3":
            actividad3_numerosdel1al10conwhile()
        elif opcion == "4":
            actividad4_numerosdel1al10confor()
        elif opcion == "5":
            actividad5_maximohasta99()
        elif opcion == "6":
            actividad6_sumas_productos_impares_20_80()
        elif opcion == "7":
            actividad7_conteorangos_naturales()
        elif opcion == "8":
            actividad8_cadenasoperaciones()
        elif opcion == "9":
            actividad9_sumaprimerosN()
        elif opcion == "10":
            actividad10_pulsaciones_por_edad_y_sexo()
        elif opcion == "11":
            actividad12_reforestacion()
        elif opcion == "12":
            actividad13_imeca_sancion()
        elif opcion == "13":
            actividad14_alturapelota_tabla()
        elif opcion == "14":
            actividad15_banco_balances()
        elif opcion == "15":
            actividad16_personas_promedios()
        elif opcion == "16":
            actividad17_empleados_sueldos()
        elif opcion == "17":
            actividad18_factura_productos()
        elif opcion == "18":
            actividad19_circunferencia()
        elif opcion == "19":
            actividad20_kmh_a_ms()
        elif opcion == "20":
            actividad21_hipotenusa()
        elif opcion == "21":
            actividad22_area_triangulo_lados()
        elif opcion == "22":
            actividad23_numero_suerte()
        elif opcion == "23":
            actividad24_numero_producto_o_suma()
        elif opcion == "24":
            actividad25_leerint()
        elif opcion == "25":
            actividad26_estadistica_N_numeros()
        elif opcion == "26":
            actividad27_precio_zapatos_tallas()
        elif opcion == "27":
            actividad28_interes_mensual_capital()
        elif opcion == "28":
            actividad29_digitos_pares()
        elif opcion == "29":
            actividad30_reparto_de_herencia()
        elif opcion == "30":
            actividad31_descuento_por_importe()
        elif opcion == "31":
            actividad32_pago_trabajador_bonif_desc()
        elif opcion == "32":
            actividad33_estimulo_academico_unidades()
        elif opcion == "33":
            actividad34_tipo_caracter()
        elif opcion == "34":
            actividad35_contar_20_numeros()
        elif opcion == "35":
            actividad36_ordenadas_pares_funcion()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()

        

