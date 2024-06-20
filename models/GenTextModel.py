from pydantic import BaseModel
from utils.project_enums import Language


class GenTextModel(BaseModel):
    text: str
    from_lang: Language
    to_lang: Language
    error: str | None = None
