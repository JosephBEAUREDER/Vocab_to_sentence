# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import json
import os
import openai
from translate import Translator
from gtts import gTTS
import random


def home(request):
    return render(request, 'home.html')


# réception de la requête lorsque l'on veut générer une phrase
def analyze(request):

    # on va stocker les mots de la text-area (la liste de vocabulaire à travailler) dans une liste
    listvoca = []
    colis = json.loads(request.body)
    text = colis['inText']
    listvoca = text.split('\n')

    # on va créer deux variables pour choisir aléatoirement deux mots dans cette liste
    var1 = random.randint(0,(len(listvoca)-1))
    var2 = random.randint(0,(len(listvoca)-1))


    # on lance l'API d'OPEN AI
    openai.api_key = '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'

    # voici le prompt qui va nous permettre de générer une phrase avec nos deux mots de vocabulaire
    gpt_prompt = "Write an easy sentence with the words '" + listvoca[var1] + "' and '" + listvoca[var2] + "'."

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    
    # voilà la phrase générée en anglais
    rep1 = response.choices[0].text

    # on va lancer l'API de traduction
    translator= Translator(from_lang="english",to_lang="arabic")

    # voilà la phrase traduite en arabe
    rep = translator.translate(rep1)

    
    # maintenant on va lancer l'API de TTS
    
    # on va régler la langue dans lequel on veut l'audio
    language = 'ar'

    # on lance l'API de TTS
    myobj = gTTS(text=rep, lang=language, slow=False)
    
    # on sauvegarde l'audio dans un fichier
    myobj.save("static/welcome2.mp3")
 
    # on renvoie la réponse
    reponse = {
       "reponse":rep,
       "reponse1":rep1
     }
    return JsonResponse(reponse)