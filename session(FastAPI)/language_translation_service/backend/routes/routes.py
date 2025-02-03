from fastapi import APIRouter
from models.model import TranslationRequest
from service.translate import Language_Translation

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
    translation = Language_Translation(text, target_language)
    response = translation.translate()
    return {"Text":text,"Translated Text":response}
