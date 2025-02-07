from fastapi import APIRouter
from models.model import TranslationRequest
from service.translate import Language_Translation,save_translation
from sqlalchemy.orm import Session
import logging

router = APIRouter(tags=['Translation'])

@router.get("/")
def home():
    return {"message": "Welcome to the Language Translation Service!"}


@router.post("/translate")
def translate(data:TranslationRequest):
    # get the text and target language from the request
    text = data.text
    target_language = data.target_language

    # make a object of langaue translation
    logging.info("Translating the text")
    translation = Language_Translation(text, target_language)
    response = translation.translate()
    
    logging.info("Translation done")
    # call the database and store the data and response
    save_translation(text=text, target_language=target_language ,translated_text = response,db=Session)
    logging.info("Data saved in database")
    return {"Text":text,"Translated Text":response}
