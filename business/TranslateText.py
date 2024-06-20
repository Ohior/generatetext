import translators
from models.GenTextModel import GenTextModel


class TranslateText:
    def getTranslation(self, get_text: GenTextModel) -> str:
        text = translators.translate_text(
            query_text=get_text.text,
            to_language=get_text.to_lang.value,
            from_language=get_text.from_lang.value
        )
        return text

    def identifyLanguage(self, text: str) -> str:
        return translators.translate_text()
