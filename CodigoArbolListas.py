# Cada nodo se representa como: [valor, hijo_izquierdo, hijo_derecho]

def crear_arbol(valor):
    return [valor, [], []]  # Nodo con valor, hijo izquierdo vacío, hijo derecho vacío

def insertar_izquierda(nodo, nuevo_valor):
    subarbol_izq = nodo[1]
    if subarbol_izq:  # Si ya hay algo a la izquierda
        nodo[1] = [nuevo_valor, subarbol_izq, []]  # Se inserta como nueva raíz, el árbol viejo queda colgado
    else:
        nodo[1] = [nuevo_valor, [], []]  # Inserta directamente si no hay hijo izquierdo

def insertar_derecha(nodo, nuevo_valor):
    subarbol_der = nodo[2]
    if subarbol_der:  # Si ya hay algo a la derecha
        nodo[2] = [nuevo_valor, [], subarbol_der]  # Se inserta como nueva raíz, el árbol viejo queda colgado
    else:
        nodo[2] = [nuevo_valor, [], []]  # Inserta directamente si no hay hijo derecho

# Recorrido Preorden: raíz - izquierda - derecha
def preorden(arbol):
    if arbol:
        print(arbol[0], end=' ')
        preorden(arbol[1])
        preorden(arbol[2])

# Recorrido Inorden: izquierda - raíz - derecha
def inorden(arbol):
    if arbol:
        inorden(arbol[1])
        print(arbol[0], end=' ')
        inorden(arbol[2])

# Recorrido Postorden: izquierda - derecha - raíz
def postorden(arbol):
    if arbol:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0], end=' ')

# Impresión visual del árbol (rotado 90°)
def imprimir_arbol(arbol, nivel=0):
    if arbol:
        imprimir_arbol(arbol[2], nivel + 1)  # Hijo derecho
        print(' ' * nivel + str(arbol[0]))   # Nodo actual
        imprimir_arbol(arbol[1], nivel + 1)  # Hijo izquierdo

# -----------------------

# Ejemplo de uso

# Crear nodo raíz
arbol = crear_arbol('A')

# Insertar hijos
insertar_izquierda(arbol, 'B')
insertar_derecha(arbol, 'C')
insertar_izquierda(arbol[1], 'D')
insertar_derecha(arbol[1], 'E')
insertar_izquierda(arbol[2], 'F')
insertar_derecha(arbol[2], 'G')

# Visualización del árbol
print("Árbol visualizado (rotado 90°):")
imprimir_arbol(arbol)

# Recorridos
print("\nRecorrido Preorden:")
preorden(arbol)

print("\nRecorrido Inorden:")
inorden(arbol)

print("\nRecorrido Postorden:")
postorden(arbol)