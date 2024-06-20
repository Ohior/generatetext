from googletrans import Translator
from models.GenTextModel import GenTextModel


class TranslateText:
    def __init__(self):
        self.translator = Translator()

    def getTranslation(self, get_text: GenTextModel) -> str:
        text = self.translator.translate(
            text=get_text.text,
            dest=get_text.to_lang.value,
            src=get_text.from_lang.value
        )
        return text.text

    def getTranslationMultiple(self, get_text: list[GenTextModel]) -> list[GenTextModel]:
        translate_list: list[GenTextModel] = []
        for i in get_text:
            translate_list.append(self.translator.translate(
                text=i.text,
                dest=i.to_lang.value,
                src=i.from_lang.value
            ))
        return translate_list

    def getLanguage(self, text: str) -> str:
        return self.translator.detect(text).lang
