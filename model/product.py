from utils.formatters import formatar_preco, formatar_nota

class Produto:
    def __init__(self, nome: str, valor: float, nota: float, estrelas: str, img: str, marca: str = "", tipo: str = "",):
        self.nome = nome
        self.valor = valor
        self.nota = nota
        self.estrelas = estrelas
        self.img = img
        self.marca = marca
        self.tipo = tipo

    def to_dict(self):
        return {
            "nome": self.nome,
            "valor": formatar_preco(self.valor),
            "nota": formatar_nota(self.nota),
            "estrelas": self.estrelas,
            "img": self.img,
            "marca": self.marca,
            "tipo": self.tipo,
        }