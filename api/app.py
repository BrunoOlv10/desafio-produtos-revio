from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Literal

from model.product import Produto
from scraper.product_scraper import listar_produtos
from utils.filters_sort import aplicar_filtros, ordenar_produtos
from utils.exporter import exportar_dados_arquivo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

produtos_cache: list[Produto] = listar_produtos()

@app.get("/listar_produtos")
def listar_produtos_e_commerce(
    marca: Optional[str] = None,
    tipo: Optional[str] = None,
    valor_min: Optional[float] = None,
    valor_max: Optional[float] = None,
    nota_min: Optional[float] = None,
    nota_max: Optional[float] = None,
    sort: Optional[str] = None
):
    produtos = aplicar_filtros(produtos_cache, marca, tipo, valor_min, valor_max, nota_min, nota_max)

    produtos = ordenar_produtos(produtos, sort)

    return {
        "produtos": [
            p.to_dict() for p in produtos
        ]
    }

@app.get("/exportar_dados")
def exportar_dados(
    tipo_export: Literal["csv", "excel"],
    marca: Optional[str] = None,
    tipo: Optional[str] = None,
    valor_min: Optional[float] = None,
    valor_max: Optional[float] = None,
    nota_min: Optional[float] = None,
    nota_max: Optional[float] = None,
    sort: Optional[str] = None
):
    produtos = aplicar_filtros(produtos_cache, marca, tipo, valor_min, valor_max, nota_min, nota_max)
    
    produtos = ordenar_produtos(produtos, sort)

    return exportar_dados_arquivo(produtos, tipo_export)