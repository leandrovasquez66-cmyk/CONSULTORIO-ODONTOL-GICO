# ==============================================================================
# EDUARD LEANDRO VASQUEZ HIDALGO
# Código: 106202622568
# Universidad de Manizales
# ==============================================================================

# Programa para la gestión del consultorio odontológico

import datetime  # para validar las fechas reales del sistema

# Lista principal para guardar todos los clientes en memoria
lista_clientes = []

def calcular_precios(tipo_cliente, tipo_atencion):
    # Función que define los precios de la cita y del procedimiento según el tipo de cliente
    valor_cita = 0
    valor_atencion = 0
    
    # Revisamos las tarifas para cliente particular
    if tipo_cliente == "particular":
        valor_cita = 80000
        if tipo_atencion == "limpieza":
            valor_atencion = 60000
        elif tipo_atencion == "calzas":
            valor_atencion = 80000
        elif tipo_atencion == "extraccion":
            valor_atencion = 100000
        elif tipo_atencion == "diagnostico":
            valor_atencion = 50000
            
    # Tarifas si es por EPS
    elif tipo_cliente == "eps":
        valor_cita = 5000
        if tipo_atencion == "limpieza":
            valor_atencion = 0
        elif tipo_atencion == "calzas":
            valor_atencion = 40000
        elif tipo_atencion == "extraccion":
            valor_atencion = 40000
        elif tipo_atencion == "diagnostico":
            valor_atencion = 0
            
    # Tarifas si es medicina prepagada
    elif tipo_cliente == "prepagada":
        valor_cita = 30000
        if tipo_atencion == "limpieza":
            valor_atencion = 0
        elif tipo_atencion == "calzas":
            valor_atencion = 10000
        elif tipo_atencion == "extraccion":
            valor_atencion = 10000
        elif tipo_atencion == "diagnostico":
            valor_atencion = 0
            
    return valor_cita, valor_atencion

def capturar_cliente():
    # Pedimos los datos del cliente con ciclos while para que pida el dato de nuevo si se equivoca
    print("\n--- REGISTRO DE NUEVO CLIENTE ---")
    
    # Validar que la cédula sea solo números
    while True:
        cedula = input("Cédula: ").strip()
        if cedula.isdigit():
            break
        print("Opción inválida. La cédula debe contener únicamente números.")

    # Validar que el nombre solo tenga letras y espacios
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre and all(c.isalpha() or c.isspace() for c in nombre):
            break
        print("Opción inválida. El nombre debe contener únicamente letras.")

    # Validar que el teléfono sea solo números
    while True:
        telefono = input("Teléfono: ").strip()
        if telefono.isdigit():
            break
        print("Opción inválida. El teléfono debe contener únicamente números.")
    
    # Menú para el tipo de cliente
    mapa_cliente = {"1": "particular", "2": "eps", "3": "prepagada"}
    while True:
        print("\nTipo de Cliente: 1. Particular | 2. EPS | 3. Prepagada")
        opcion_cliente = input("Seleccione una opción (1-3): ").strip()
        if opcion_cliente in mapa_cliente:
            tipo_cliente = mapa_cliente[opcion_cliente]
            break
        print("Opción inválida. Seleccione un número de 1 a 3.")
    
    # Menú para el tipo de atención
    mapa_atencion = {"1": "limpieza", "2": "calzas", "3": "extraccion", "4": "diagnostico"}
    while True:
        print("\nTipo de Atención: 1. Limpieza | 2. Calzas | 3. Extracción | 4. Diagnóstico")
        opcion_atencion = input("Seleccione una opción (1-4): ").strip()
        if opcion_atencion in mapa_atencion:
            tipo_atencion = mapa_atencion[opcion_atencion]
            break
        print("Opción inválida. Seleccione un número de 1 a 4.")
    
    # Si es limpieza o diagnóstico la cantidad siempre es 1
    if tipo_atencion in ["limpieza", "diagnostico"]:
        cantidad = 1
        print(f"\nLa cantidad para {tipo_atencion} es fija: 1")
    else:
        # Para calzas o extracción pedimos la cantidad y validamos que sea mayor a 0
        while True:
            try:
                cantidad = int(input("Cantidad de procedimientos (mayor a 0): "))
                if cantidad > 0:
                    break
                print("Opción inválida. La cantidad debe ser un número entero mayor a 0.")
            except ValueError:
                print("Opción inválida. Ingrese un número entero válido.")
                
    # Menú de prioridad
    while True:
        print("\nPrioridad: 1. Normal | 2. Urgente")
        opcion_prioridad = input("Seleccione opción (1-2): ").strip()
        if opcion_prioridad in ["1", "2"]:
            prioridad = "Urgente" if opcion_prioridad == "2" else "Normal"
            break
        print("Opción inválida. Seleccione un número de 1 a 2.")
    
    # Validar que la fecha no sea una fecha pasada
    fecha_hoy = datetime.date.today()
    while True:
        fecha_str = input("\nFecha de la Cita (DD/MM/AAAA): ").strip()
        try:
            fecha_dt = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
            if fecha_dt >= fecha_hoy:
                fecha = fecha_str
                break
            else:
                print(f"Opción inválida. La fecha debe ser igual o posterior al día de hoy ({fecha_hoy.strftime('%d/%m/%Y')}).")
        except ValueError:
            print("Opción inválida. Formato incorrecto. Utilice el formato DD/MM/AAAA (Ejemplo: 25/11/2026).")
    
    # Calculamos totales
    valor_cita, valor_atencion = calcular_precios(tipo_cliente, tipo_atencion)
    total_atencion = valor_atencion * cantidad
    total_pagar = valor_cita + total_atencion
    
    # Guardamos todos los datos del cliente en un diccionario
    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "prioridad": prioridad,
        "fecha": fecha,
        "valor_cita": valor_cita,
        "valor_atencion": valor_atencion,
        "total_atencion": total_atencion,
        "total_pagar": total_pagar
    }
    
    # Lo agregamos a la lista general
    lista_clientes.append(cliente)
    print(f"\n¡Cliente {nombre} registrado con éxito! Total a pagar: ${total_pagar:,.0f}")

def mostrar_estadisticas():
    # Calcula el total de clientes, dinero total e inscritos a extracción
    total_clientes = len(lista_clientes)
    if total_clientes == 0:
        print("\nNo hay clientes registrados en el sistema.")
        return
        
    ingresos_totales = sum(c["total_pagar"] for c in lista_clientes)
    clientes_extraccion = sum(1 for c in lista_clientes if c["tipo_atencion"] == "extraccion")
    
    print("\n==========================================")
    print("        RESUMEN Y ESTADÍSTICAS")
    print("==========================================")
    print(f"Total Clientes registrados: {total_clientes}")
    print(f"Ingresos totales recibidos: ${ingresos_totales:,.0f}")
    print(f"Clientes citados para extracción: {clientes_extraccion}")
    print("==========================================")

def ordenar_y_mostrar():
    # Ordena la lista de mayor a menor según el valor de la atención
    if not lista_clientes:
        print("\nNo hay clientes para ordenar.")
        return
        
    lista_ordenada = sorted(lista_clientes, key=lambda x: x["total_atencion"], reverse=True)
    
    print("\n=========================================================================================")
    print("        LISTA DE CLIENTES ORDENADA POR VALOR DE ATENCIÓN (MAYOR A MENOR)")
    print("=========================================================================================")
    print(f"{'Cédula':<12} | {'Nombre':<20} | {'Atención':<12} | {'Cant.':<5} | {'Valor Atención Total':<20} | {'Total Pagar':<12}")
    print("-" * 90)
    
    for c in lista_ordenada:
        print(f"{c['cedula']:<12} | {c['nombre']:<20} | {c['tipo_atencion'].capitalize():<12} | {c['cantidad']:<5} | ${c['total_atencion']:<19,.0f} | ${c['total_pagar']:<11,.0f}")
    print("=========================================================================================")

def buscar_cliente_por_cedula():
    # Busca a un cliente recorriendo la lista por su cédula
    if not lista_clientes:
        print("\nNo hay clientes registrados en la base de datos.")
        return
        
    cedula_buscar = input("\nIngrese la Cédula a buscar: ").strip()
    encontrado = None
    
    for c in lista_clientes:
        if c["cedula"] == cedula_buscar:
            encontrado = c
            break
            
    if encontrado:
        print("\n--- CLIENTE ENCONTRADO ---")
        print(f"Nombre:           {encontrado['nombre']}")
        print(f"Cédula:           {encontrado['cedula']}")
        print(f"Teléfono:         {encontrado['telefono']}")
        print(f"Tipo Cliente:     {encontrado['tipo_cliente'].upper()}")
        print(f"Tipo Atención:    {encontrado['tipo_atencion'].capitalize()}")
        print(f"Cantidad:         {encontrado['cantidad']}")
        print(f"Prioridad:        {encontrado['prioridad']}")
        print(f"Fecha Cita:       {encontrado['fecha']}")
        print(f"Valor Cita:       ${encontrado['valor_cita']:,.0f}")
        print(f"Valor Atención:   ${encontrado['total_atencion']:,.0f}")
        print(f"TOTAL A PAGAR:    ${encontrado['total_pagar']:,.0f}")
    else:
        print(f"\nNo se encontró ningún cliente con la cédula {cedula_buscar}.")

def menu_principal():
    # Bucle del menú de opciones
    while True:
        print("\n--- MENÚ CONSULTORIO ODONTOLÓGICO ---")
        print("1. Registrar cita de cliente")
        print("2. Ver estadísticas generales")
        print("3. Ordenar lista de clientes por valor de atención")
        print("4. Buscar cliente por cédula")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            capturar_cliente()
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            ordenar_y_mostrar()
        elif opcion == "4":
            buscar_cliente_por_cedula()
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Por favor seleccione un número de 1 a 5.")

# Ejecución del programa
if __name__ == "__main__":
    menu_principal()
