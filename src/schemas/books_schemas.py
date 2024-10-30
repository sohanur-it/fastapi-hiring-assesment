from pydantic import BaseModel
from typing import Optional

class DisplayBook(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    price: float
    is_available: Optional[bool] = True

class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float
    is_available: Optional[bool] = True

class BookUpdate(BookCreate):
    pass

class BookResponse(BookCreate):
    id: int
