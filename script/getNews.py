import requests
from bs4 import BeautifulSoup
from transformers import pipeline, AutoTokenizer, logging
from datetime import datetime, timedelta




def obtenir_news(api_key, sujet, nombre, langue="fr"):
    date_to = datetime.now().date()
    date_from = date_to - timedelta(days=3)

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": sujet,
        "language": langue,
        "pageSize": nombre,
        "from": date_from.isoformat(),  # format YYYY-MM-DD
        "to": date_to.isoformat(),
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"data: {data}")
        articles = data.get("articles", [])
        for i, article in enumerate(articles, 1):
            if "live" not in article['url']:
                print(f"{i}. {article['title']}")
                texte = recuperer_texte(article['url'])

                if texte:
                    print(f"   Résumé : {resumer_texte(texte)}")
                else:
                    print(f"   Bug rien de trouvé donc résumé basique")
                    print(f"   Résumé : {extraire_resume(article['url'])}")
                print(f"   Source : {article['source']['name']}")
                print(f"   URL : {article['url']}\n")
    else:
        print(f"Erreur lors de la récupération des news : {response.status_code}")


def recuperer_texte(url):
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        

        if "lemonde.fr" in url:
            paragraphes = soup.find_all('p', class_='article__paragraph')
        else:
            paragraphes = soup.find_all('p')
        # Extraire tout le texte des balises <p>
        texte = ' '.join(p.get_text() for p in paragraphes)
        return texte
    except Exception as e:
        print(f"Erreur lors du scraping : {e}")
        return None
    
def resumer_texte(texte):
    tokenizer = AutoTokenizer.from_pretrained("plguillou/t5-base-fr-sum-cnndm", use_fast=False)
    summarizer = pipeline("summarization", model="plguillou/t5-base-fr-sum-cnndm", tokenizer=tokenizer, device=0)

    max_chunk = 1024
    if len(texte) > max_chunk:
        texte = texte[:max_chunk]

    resultat = summarizer(texte, max_length=300, min_length=30, do_sample=False)
    return resultat[0]['summary_text']

def extraire_resume(url):
    try:
        response = requests.get(url, timeout=5)
        response.encoding = 'utf-8'
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Chercher le premier paragraphe <p>
        paragraphe = soup.find('p')
        if paragraphe:
            return paragraphe.get_text(strip=True)
        else:
            return "Pas de résumé trouvé."
    except Exception as e:
        return f"Erreur lors du scraping : {e}"
    
def nettoyer_texte(texte, url):
    return texte
