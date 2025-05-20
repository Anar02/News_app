from script.getNews import obtenir_news
from fastapi import FastAPI
from pydantic import BaseModel

import logging
import warnings

logging.basicConfig(level=logging.ERROR)
warnings.filterwarnings("ignore", category=FutureWarning)

app = FastAPI()
cle_api = "8aa122f0353a4570870cd29baf246587"

# Exemple de route GET
@app.get("/news/{topics}")
def get_news(topcis: str):
    print("\nNews sur les jeux vidéo :")
    text = obtenir_news(cle_api, topcis, 5)
    return {"message": text}

# Modèle de données pour POST
class Message(BaseModel):
    nom: str
    message: str

# Exemple de route POST
@app.post("/echo")
def echo_message(data: Message):
    return {"recu": data}