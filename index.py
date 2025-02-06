import re

# Definición de patrones léxicos
TOKENS = [
    ("COMENTARIO_LINEA", r"//.*"),                                 # Comentarios de línea
    ("COMENTARIO_BLOQUE", r"/\*.*?\*/", re.DOTALL),                # Comentarios de bloque
    ("PALABRA_CLAVE", r"\b(if|else|then|int|float|string)\b"),     # Palabras clave
    ("IDENTIFICADOR", r"[a-zA-Z_][a-zA-Z0-9_]*"),                  # Identificadores
    ("NUMERO_REAL", r"\b\d+\.\d+\b"),                              # Números reales
    ("NUMERO", r"\b\d+\b"),                                        # Números enteros
    ("LITERAL_CADENA", r"\".*?\""),                                # Literales de cadena
    ("OPERADOR_LOGICO", r"(==|!=|<=|>=|<|>)"),                     # Operadores lógicos
    ("OPERADOR_ARITMETICO", r"[+\-*/=]"),                          # Operadores aritméticos y asignación
    ("DELIMITADOR", r"[;{}()]"),                                   # Delimitadores
    ("ESPACIO", r"[ \t\n]+"),                                      # Espacios en blanco (ignorar)
]

# Función del analizador léxico
def analizador_lexico(codigo_fuente):
    tokens = []
    lineas = codigo_fuente.splitlines()
    patron_global = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron, *_ in TOKENS)

    for numero_linea, linea in enumerate(lineas, start=1):
        pos = 0
        while pos < len(linea):
            match = re.match(patron_global, linea[pos:])
            if not match:
                raise ValueError(f"Error léxico: carácter inesperado en línea {numero_linea}, posición {pos + 1} ('{linea[pos]}')")

            for nombre, lexema in match.groupdict().items():
                if lexema:
                    if nombre not in ["ESPACIO", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE"]:
                        tokens.append((nombre, lexema, numero_linea, pos + 1))
                    pos += len(lexema)
                    break

    return tokens

# Ejemplo de entrada
codigo_fuente = """
// Comentario de prueba
int x = 10;
/* Comentario en bloque
   que abarca varias líneas */
if (x > 5) {
    x = x + 1;
} else {
    x = x - 1;
}
"""

# Analizar el código fuente
try:
    tokens = analizador_lexico(codigo_fuente)
    print("Tokens generados:")
    for token in tokens:
        print(token)
except ValueError as e:
    print(e)
