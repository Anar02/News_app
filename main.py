from script.getNews import obtenir_news
import logging
import warnings


logging.basicConfig(level=logging.ERROR)
warnings.filterwarnings("ignore", category=FutureWarning)

cle_api = "8aa122f0353a4570870cd29baf246587"

print("\nNews sur les jeux vidéo :")
obtenir_news(cle_api, "Jeux Vidéo", 5)