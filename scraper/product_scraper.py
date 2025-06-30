import bs4

from model.product import Produto
from utils.extractors import extrair_marca, extrair_tipo

def listar_produtos() -> list[Produto]:
    html_pagina = open("mock/revio-e-commerce.html", encoding="utf-8")

    soup = bs4.BeautifulSoup(html_pagina, "html.parser")

    grid_de_produtos = soup.find("div", class_="products-grid")

    produtos = grid_de_produtos.find_all("div", attrs={"class":"product-card"})

    lista_produtos = []
    for produto in produtos:
        nome = produto.find("h3").text.strip()
        valor = float(produto.find("span", class_="current-price")
                      .text.strip()
                      .replace("R$", "")
                      .replace(".", "")
                      .replace(",", ".")
                )
        nota = float(produto.find("span", class_="rating-value").text.strip())
        estrelas = produto.find("span", class_="stars").text.strip()
        img = produto.find("img")["src"]
        marca = extrair_marca(nome)
        tipo = extrair_tipo(nome)
        lista_produtos.append(Produto(nome, valor, nota, estrelas, img, marca, tipo))

    return lista_produtos