from pydantic import BaseModel
from utils.project_enums import Language


class GenTextModel(BaseModel):
    text: str
    to_lang: Language
    from_lang: Language = Language.AUTOMATIC
    error: str | None = None
