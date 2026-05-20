# Análise de Dados com Python

Este projeto demonstra duas formas de realizar análise de dados com Python, Pandas e Seaborn.

## Instalação das dependências

pip install pandas seaborn requests

## Arquivos do Projeto

extracao.py → Extrai os dados da API do Banco Central e gera o arquivo taxa-cdi.csv.
visualizacao.py → Lê o arquivo CSV e gera o gráfico em PNG.
analise.py → Executa todo o processo automaticamente.

## 1ª Forma: Executando pelo Terminal

Extrair os dados
python extracao.py

Gerar o gráfico
python visualizacao.py grafico-cdi

## 2ª Forma: Script Automatizado

Executar tudo de uma vez
python analise.py grafico-cdi

Arquivos Gerados
taxa-cdi.csv
grafico-cdi.png

## Resumo

Método Manual
python extracao.py
python visualizacao.py grafico-cdi

Método Automatizado
python analise.py grafico-cdi