# 🛒 Desafio Revio - Scraping de Produtos com Visualização e Exportação

> Projeto desenvolvido como parte do processo seletivo para a vaga de **Desenvolvedor Python** na empresa **Revio**.

---

## 📌 Objetivo

Realizar **web scraping** com **Python** em um e-commerce específico, com o objetivo de coletar informações de determinados produtos.

---

## 📄 Funcionalidades

- ✅ Extração automática de dados dos produtos
- ✅ Interface web intuitiva para:
  - Listar produtos  
  - Filtrar por valor, nome (marca e/ou tipo) e nota
  - Ordenar por valor (ascendente/descendente) ou maior nota
- ✅ Geração de relatórios com base nos filtros e ordenação aplicados:
- `.xlsx` (Excel)
- `.csv`

---

## 💬 Destaque

Este desafio me permitiu demonstrar habilidades em scraping, manipulação de dados, desenvolvimento de API com FastAPI e integração com front-end. Além disso, implementei filtros, ordenação dinâmica e exportação de dados. Um diferencial importante está na geração de relatórios que respeitam os filtros e a ordenação aplicados na interface web, permitindo ao usuário visualizar previamente os dados que serão exportados.

---

## 🛠 Tecnologias Utilizadas

### 🔎 Scraping
- `beautifulsoup4`

### 💻 Back-end
- `Python`
- `FastAPI`
- `uvicorn`
- `pandas`
- `openpyxl`

### 🌐 Front-end
- `HTML`
- `CSS`
- `JavaScript`

---

## 🌍 Projeto Online
- Você pode testar a aplicação hospedada: <br>
🔗 [Acessar Projeto](https://revio-desafio-produtos.vercel.app)
> ⚠️ Atenção: O back-end está hospedado gratuitamente no **Render**, o que pode causar **demora no primeiro carregamento** dos dados.

---

## 🧪 Como Testar Localmente

### 1. Clonar o Repositório
```
git clone https://github.com/BrunoOlv10/revio-desafio-produtos.git
cd revio-desafio-produtos
```

### 2. Instalar Dependências
```
pip install -r requirements.txt
```

### 3. Rodar o Back-end
```
uvicorn api.app:app --reload
```

<br>

### ⚙️ Configurações para Ambiente Local

### 1. Alterar a URL da API no Front-end
- No arquivo **config.js**, comente o back-end hospedado (prod) e descomente o local:
```
const API_BASE = 'http://localhost:8000'
```

### 2. Ajustar CORS (autorização para requisições) no Back-end
- No arquivo **app.py**, comente a linha com o domínio específico (prod) e libere todas as origens ou insira a url do localhost:
```
allow_origins=["*"]
```

<br>

### 🖼️ Executar o Front-end
- Abra o arquivo **index.html** diretamente ou utilize alguma extensão como o Live Server do VS Code.
