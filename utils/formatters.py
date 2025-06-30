def formatar_preco(valor: float) -> str:
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_nota(nota: float) -> str:
    return f"{nota:.1f}"