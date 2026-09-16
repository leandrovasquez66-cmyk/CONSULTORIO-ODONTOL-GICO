# ==============================================================================
# EDUARD LEANDRO VASQUEZ HIDALGO
# Código: 106202622568
# Universidad de Manizales
# ==============================================================================

# ==============================================================================
# PROGRAMA DE GESTIÓN CONSULTORIO ODONTOLÓGICO
# Conceptos aplicados: Variables, Condicionales, Ciclos, Excepciones y Colecciones
# ==============================================================================

# ESTRUCTURA DE DATOS / ARREGLO EN MEMORIA: 
# Lista global para almacenar la información de los clientes registrados.
lista_clientes = []

def calcular_precios(tipo_cliente, tipo_atencion):
    """
    Función que recibe el tipo de cliente y atención,
    y retorna el valor base de la cita y el valor del servicio por unidad.
    APLICA: Toma de decisiones mediante ESTRUCTURAS CONDICIONALES ANIDADAS (if / elif).
    """
    # VARIABLES LOCALES PARA VALORES MONETARIOS
    valor_cita = 0
    valor_atencion = 0
    
    # CONDICIONAL: Evaluación de tarifas según el Tipo de Cliente
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
    """
    Función para registrar un nuevo cliente con validaciones.
    APLICA: Lectura de datos por consola, diccionarios, validación de reglas de negocio
    y manejo de excepciones/bucles de rebote para evitar datos inválidos.
    """
    print("\n--- REGISTRO DE NUEVO CLIENTE ---")
    
    # VALIDACIÓN: Cédula no vacía
    while True:
        cedula = input("Cédula: ").strip()
        if cedula:
            break
        print("Error: La cédula no puede estar vacía.")

    nombre = input("Nombre completo: ").strip()
    telefono = input("Teléfono: ").strip()
    
    # VALIDACIÓN DE REBOTE: Tipo de Cliente
    mapa_cliente = {"1": "particular", "2": "eps", "3": "prepagada"}
    while True:
        print("\nTipo de Cliente: 1. Particular | 2. EPS | 3. Prepagada")
        opcion_cliente = input("Seleccione una opción (1-3): ").strip()
        if opcion_cliente in mapa_cliente:
            tipo_cliente = mapa_cliente[opcion_cliente]
            break
        print("Error: Opción inválida. Seleccione un número entre 1 y 3.")
    
    # VALIDACIÓN DE REBOTE: Tipo de Atención
    mapa_atencion = {"1": "limpieza", "2": "calzas", "3": "extraccion", "4": "diagnostico"}
    while True:
        print("\nTipo de Atención: 1. Limpieza | 2. Calzas | 3. Extracción | 4. Diagnóstico")
        opcion_atencion = input("Seleccione una opción (1-4): ").strip()
        if opcion_atencion in mapa_atencion:
            tipo_atencion = mapa_atencion[opcion_atencion]
            break
        print("Error: Opción inválida. Seleccione un número entre 1 y 4.")
    
    # REGLA DE NEGOCIO Y MANEJO DE ERRORES (CICLO WHILE + TRY / EXCEPT)
    if tipo_atencion in ["limpieza", "diagnostico"]:
        cantidad = 1
        print(f"\nLa cantidad para {tipo_atencion} es fija: 1")
    else:
        # CICLO REPETITIVO para validar la cantidad ingresada
        while True:
            try:
                # ERROR HANDLING: Intenta convertir la entrada a número entero (int)
                cantidad = int(input("Cantidad de procedimientos (mayor a 0): "))
                if cantidad > 0:
                    break  # Sale del ciclo si el dato cumple la condición
                print("Error: La cantidad debe ser un número entero mayor a 0.")
            except ValueError:
                # Se activa si el usuario escribe letras o caracteres especiales
                print("Error: Ingrese un número entero válido.")
                
    # VALIDACIÓN DE REBOTE: Prioridad de Atención
    while True:
        print("\nPrioridad: 1. Normal | 2. Urgente")
        opcion_prioridad = input("Seleccione opción (1-2): ").strip()
        if opcion_prioridad in ["1", "2"]:
            prioridad = "Urgente" if opcion_prioridad == "2" else "Normal"
            break
        print("Error: Opción inválida. Seleccione 1 o 2.")
    
    fecha = input("Fecha de la Cita (DD/MM/AAAA): ").strip()
    
    # CÁLCULOS MATEMÁTICOS DE TARIFA Y TOTALES
    valor_cita, valor_atencion = calcular_precios(tipo_cliente, tipo_atencion)
    total_atencion = valor_atencion * cantidad
    total_pagar = valor_cita + total_atencion
    
    # ESTRUCTURA DICCIONARIO: Agrupa todos los atributos del cliente en un solo registro
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
    
    # GUARDAR EN MEMORIA: Añadir elemento a la lista principal
    lista_clientes.append(cliente)
    print(f"\n¡Cliente {nombre} registrado con éxito! Total a pagar: ${total_pagar:,.0f}")

def mostrar_estadisticas():
    """
    Calcula e imprime los totales solicitados.
    APLICA: Funciones acumuladoras, conteo filtrado y validación de lista vacía.
    """
    total_clientes = len(lista_clientes)  # Función integrada len() para contar elementos
    if total_clientes == 0:
        print("\nNo hay clientes registrados en el sistema.")
        return
        
    # ACUMULADORES DE INFORMACIÓN
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
    """
    Ordena los clientes por valor de la atención de mayor a menor.
    APLICA: ORDENAMIENTO DE DATOS mediante la función sorted() y expresión lambda.
    """
    if not lista_clientes:
        print("\nNo hay clientes para ordenar.")
        return
        
    # ORDENAMIENTO DESCENDENTE (reverse=True) según la clave 'total_atencion'
    lista_ordenada = sorted(lista_clientes, key=lambda x: x["total_atencion"], reverse=True)
    
    print("\n=========================================================================================")
    print("        LISTA DE CLIENTES ORDENADA POR VALOR DE ATENCIÓN (MAYOR A MENOR)")
    print("=========================================================================================")
    print(f"{'Cédula':<12} | {'Nombre':<20} | {'Atención':<12} | {'Cant.':<5} | {'Valor Atención Total':<20} | {'Total Pagar':<12}")
    print("-" * 90)
    
    # CICLO FOR: Recorre e imprime la lista ordenada con formato visual
    for c in lista_ordenada:
        print(f"{c['cedula']:<12} | {c['nombre']:<20} | {c['tipo_atencion'].capitalize():<12} | {c['cantidad']:<5} | ${c['total_atencion']:<19,.0f} | ${c['total_pagar']:<11,.0f}")
    print("=========================================================================================")

def buscar_cliente_por_cedula():
    """
    Busca a un cliente específico por su número de cédula.
    APLICA: BÚSQUEDA SECUENCIAL mediante recorrido con ciclo FOR y comparación directa.
    """
    if not lista_clientes:
        print("\nNo hay clientes registrados en la base de datos.")
        return
        
    cedula_buscar = input("\nIngrese la Cédula a buscar: ").strip()
    encontrado = None
    
    # CICLO REPETITIVO Y CONDICIONAL DE BÚSQUEDA
    for c in lista_clientes:
        if c["cedula"] == cedula_buscar:
            encontrado = c
            break  # Detiene la búsqueda al encontrar la primera coincidencia
            
    # CONDICIONAL: Muestra resultado si se halló el registro
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

# ==============================================================================
# MENÚ PRINCIPAL: CONTROL DE FLUJO DEL PROGRAMA
# APLICA: CICLO REPETITIVO INFINITO (while True) Y ESTRUCTURA CONDICIONAL MÚLTIPLE
# ==============================================================================
def menu_principal():
    while True:
        print("\n--- MENÚ CONSULTORIO ODONTOLÓGICO ---")
        print("1. Registrar cita de cliente")
        print("2. Ver estadísticas generales")
        print("3. Ordenar lista de clientes por valor de atención")
        print("4. Buscar cliente por cédula")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        # CONDICIONALES PARA NAVEGACIÓN EN EL MENÚ
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
            break  # Interrumpe el ciclo while para finalizar el programa
        else:
            print("Opción inválida. Por favor seleccione un número de 1 a 5.")

# PUNTO DE ENTRADA AL PROGRAMA
if __name__ == "__main__":
    menu_principal()
