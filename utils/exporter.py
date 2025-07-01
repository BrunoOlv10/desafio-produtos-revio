from datetime import datetime
from io import BytesIO
import pandas as pd
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from fastapi.responses import StreamingResponse

from model.product import Produto
from utils.formatters import formatar_preco, formatar_nota

def montar_dados_exportacao(produtos: list[Produto]) -> list[dict]:
    return [{
        "nome": p.nome,
        "valor": formatar_preco(p.valor),
        "nota": formatar_nota(p.nota)
    } for p in produtos]

def montar_nome_arquivo(prefixo: str = "produtos", data: str = None) -> str:
    if data is None:
        return prefixo
    
    data_string = datetime.strptime(data, "%d/%m/%Y, %H:%M:%S")
    data_formatada = data_string.strftime('%d-%m-%y-%H-%M-%S')

    return f"{prefixo} {data_formatada}"

def exportar_dados_arquivo(produtos: list[Produto], tipo: str, data: str = None) -> StreamingResponse:
    output = BytesIO()
    dados = montar_dados_exportacao(produtos)
    df = pd.DataFrame(dados)
    nome_arquivo = montar_nome_arquivo(data=data)

    if tipo == "csv":
        df.to_csv(output, index=False, sep=";", encoding="utf-8")

        output.seek(0)

        return StreamingResponse(output, media_type="text/csv", headers={
            "Content-Disposition": f'attachment; filename="{nome_arquivo}.csv"'
        })

    elif tipo == "excel":
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Produtos")
            worksheet = writer.sheets["Produtos"]

            for col in worksheet.columns:
                max_length = 0
                col_letter = get_column_letter(col[0].column)
                for cell in col:
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                worksheet.column_dimensions[col_letter].width = max_length + 2

        output.seek(0)

        return StreamingResponse(output, media_type="application/vnd.openxmlformats-officedocument. spreadsheetml.sheet", headers={
            "Content-Disposition": f'attachment; filename="{nome_arquivo}.xlsx"'
        })