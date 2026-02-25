import requests
from bs4 import BeautifulSoup
import csv

def extrair_citacoes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar o site.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    dados = []

    for quote, author in zip(quotes, authors):
        dados.append({
            "citacao": quote.text,
            "autor": author.text
        })

    return dados


def salvar_csv(dados):
    with open("citacoes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["citacao", "autor"])
        writer.writeheader()
        writer.writerows(dados)

    print("Arquivo citacoes.csv criado com sucesso!")


if __name__ == "__main__":
    dados = extrair_citacoes()
    if dados:
        salvar_csv(dados)
