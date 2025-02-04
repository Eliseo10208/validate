import re

# Definición de patrones léxicos
TOKENS = [
    ("PALABRA_CLAVE", r"\b(if|else|then|int|float|string)\b"),  # Palabras clave
    ("IDENTIFICADOR", r"[a-zA-Z_][a-zA-Z0-9_]*"),               # Identificadores
    ("NUMERO_REAL", r"\b\d+\.\d+\b"),                            # Números reales
    ("NUMERO", r"\b\d+\b"),                                      # Números enteros
    ("LITERAL_CADENA", r"\".*?\""),                               # Literales de cadena
    ("OPERADOR_LOGICO", r"(==|!=|<=|>=|<|>)"),                   # Operadores lógicos
    ("OPERADOR_ARITMETICO", r"[+\-*/=]"),                         # Operadores aritméticos y asignación
    ("DELIMITADOR", r"[;{}()]"),                                 # Delimitadores
    ("ESPACIO", r"[ \t\n]+"),                                    # Espacios en blanco (ignorar)
]

# Función del analizador léxico
def analizador_lexico(codigo_fuente):
    tokens = []
    pos = 0

    while pos < len(codigo_fuente):
        match = None
        for token_tipo, patron in TOKENS:
            regex = re.compile(patron)
            match = regex.match(codigo_fuente, pos)

            if match:
                lexema = match.group(0)
                if token_tipo != "ESPACIO":  # Ignorar espacios en blanco
                    tokens.append((token_tipo, lexema))
                pos = match.end()
                break

        if not match:
            raise ValueError(f"Error léxico: carácter inesperado en posición {pos} ('{codigo_fuente[pos]}')")

    return tokens

# Ejemplo de entrada
codigo_fuente = """
int x = 10;
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
