from pydantic import BaseModel


class ImageModel(BaseModel):
    image: str
    error: str | None = None