from utils.constants import MARCAS, TIPOS

def extrair_marca(nome: str) -> str:
    for marca in MARCAS:
        if marca in nome.lower():
            return marca

def extrair_tipo(nome: str) -> str:
    for tipo in TIPOS:
        if tipo in nome.lower():
            return tipo