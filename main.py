import uvicorn
from business.TranslateText import TranslateText
from fastapi import FastAPI
from models.GenTextModel import GenTextModel

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello From generative text"}


@app.post("/gen_text")
def getText(gen_text: GenTextModel):
    translate_text = TranslateText()
    sentence = translate_text.getTranslation(gen_text)
    return GenTextModel(text=sentence, from_lang=gen_text.from_lang, to_lang=gen_text.to_lang)


# for vercel or AWS
# handler = Mangum(app, lifespan="off")


def main():
    # uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, workers=3)
    uvicorn.run("main:app", port=5000, reload=True, workers=3)


if __name__ == "__main__":
    main()
