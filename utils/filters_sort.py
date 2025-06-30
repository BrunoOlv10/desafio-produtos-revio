from typing import Optional

from model.product import Produto

def aplicar_filtros(
    produtos_cache: list[Produto],
    marca: Optional[str],
    tipo: Optional[str],
    valor_min: Optional[float],
    valor_max: Optional[float],
    nota_min: Optional[float],
    nota_max: Optional[float],
) -> list[Produto]:
    resultado = produtos_cache

    if marca is not None:
        marcas_lista = [m.strip().lower() for m in marca.split(',')]
        resultado = [p for p in resultado if any(m in p.nome.lower() for m in marcas_lista)]
    if tipo is not None:
        tipos_lista = [t.strip().lower() for t in tipo.split(',')]
        resultado = [p for p in resultado if any(t in p.nome.lower() for t in tipos_lista)]
    if valor_min is not None:
        resultado = [p for p in resultado if p.valor >= valor_min]
    if valor_max is not None:
        resultado = [p for p in resultado if p.valor <= valor_max]
    if nota_min is not None:
        resultado = [p for p in resultado if p.nota >= nota_min]
    if nota_max is not None:
        resultado = [p for p in resultado if p.nota <= nota_max]

    return resultado

def ordenar_produtos(produtos: list[Produto], sort: Optional[str]) -> list[Produto]:
    if sort == "valor_asc":
        produtos.sort(key=lambda x: x.valor)
    elif sort == "valor_desc":
        produtos.sort(key=lambda x: x.valor, reverse=True)
    elif sort == "nota_desc":
        produtos.sort(key=lambda x: x.nota, reverse=True)
    return produtos