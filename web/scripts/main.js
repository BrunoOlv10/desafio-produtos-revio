import { API_BASE } from './config.js';

const sortSelect = document.querySelector('.sort-options select')
const container = document.getElementById('products-container')
const countResults = document.querySelector('.results-count')

document.getElementById('export-excel').addEventListener('click', () => exportarDados('excel'))
document.getElementById('export-csv').addEventListener('click', () => exportarDados('csv'))

const filtros = {
    precos: document.querySelectorAll('.price-filters input'),
    marcas: document.querySelectorAll('.brand-filters input'),
    tipos: document.querySelectorAll('.type-filters input'),
    notas: document.querySelectorAll('.grade-filters input'),
}

function obterValorMarcado(valor) {
    return Array.from(valor)
        .filter(input => input.checked)
        .map(input => input.value)
}

function parsePreco(values) {
    let precoMin = Infinity
    let precoMax = 0

    values.forEach(val => {
        if (val.includes('-')) {
            const [min, max] = val.split('-').map(n => parseInt(n))
            precoMin = Math.min(precoMin, min);
            precoMax = Math.max(precoMax, max);
        } else {
            const valor = parseInt(val);

            if (valor === 5000) {
                precoMin = Math.min(precoMin, valor)
            } else {
                precoMax = Math.max(precoMax, valor);
            }
        }
    })

  return [isFinite(precoMin) ? precoMin : null, precoMax > 0 ? precoMax : null]
}

function parseNota(inputs) {
    let notaMin = Infinity
    let notaMax = 0

    Array.from(inputs)
        .filter(input => input.checked)
        .forEach(input => {
            const [min, max] = input.value.split('-').map(n => parseFloat(n))
            notaMin = Math.min(notaMin, min)
            notaMax = Math.max(notaMax, max)
        })

    return [isFinite(notaMin) ? notaMin : null, notaMax > 0 ? notaMax : null]
}

function montarQuery() {
    const params = new URLSearchParams()

    const marcas = obterValorMarcado(filtros.marcas)
    const tipos = obterValorMarcado(filtros.tipos)
    const precos = obterValorMarcado(filtros.precos)
    const notas = filtros.notas

    if (marcas.length > 0) params.set('marca', marcas.join(','))
    if (tipos.length > 0) params.set('tipo', tipos.join(','))

    const [valor_min, valor_max] = parsePreco(precos)
    if (valor_min !== null) params.set('valor_min', valor_min)
    if (valor_max !== null) params.set('valor_max', valor_max)

    const [nota_min, nota_max] = parseNota(notas)
    if (nota_min !== null) params.set('nota_min', nota_min)
    if (nota_max !== null) params.set('nota_max', nota_max)

    const sortOption = sortSelect.value
    if (sortOption === 'avaliacao-maior') params.set('sort', 'nota_desc')
    if (sortOption === 'valor-menor') params.set('sort', 'valor_asc')
    if (sortOption === 'valor-maior') params.set('sort', 'valor_desc')

    return `/listar_produtos?${params.toString()}`
}

function mostrarProdutos(produtos) {
    container.innerHTML = ''
    const exportExcel = document.getElementById('export-excel')
    const exportCsv = document.getElementById('export-csv')

    if (produtos.length === 0) {
        exportExcel.disabled = true
        exportCsv.disabled = true
    } else {
        exportExcel.disabled = false
        exportCsv.disabled = false
    }

    produtos.forEach(p => {
        const html = `
            <div class="product-card">
                <div class="product-image"><img src="${p.img}" alt="${p.nome}"></div>
                <div class="product-info">
                    <h3>${p.nome}</h3>
                    <div class="price"><span class="current-price">R$ ${p.valor}</span></div>
                    <div class="rating">
                        <span class="stars">${p.estrelas}</span>
                        <span class="rating-value">${p.nota}</span>
                    </div>
                </div>
            </div>`
        container.insertAdjacentHTML('beforeend', html)
    })
    
    countResults.textContent = `${produtos.length} produtos encontrados`
}

function exportarDados(tipo) {
    const query = montarQuery()
    const params = new URLSearchParams(query.slice(query.indexOf('?')))
    params.set('tipo_export', tipo)

    const dataHora = new Date().toLocaleString('pt-BR') 
    params.set('data_hora', dataHora)

    const url = `${API_BASE}/exportar_dados?${params.toString()}`

    window.open(url)
}

async function buscarExibir() {
    try {
        const url = API_BASE + montarQuery()
        const resp = await fetch(url)
        const data = await resp.json()
        mostrarProdutos(data.produtos || [])
    } catch (e) {
        console.error('Erro ao buscar produtos:', e)
    }
}

Object.values(filtros).forEach(f =>
    f.forEach(input => input.addEventListener('change', buscarExibir))
)
sortSelect.addEventListener('change', buscarExibir)

buscarExibir()