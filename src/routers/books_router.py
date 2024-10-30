from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from typing import List
from src.models.books_models import Book 
from src.schemas.books_schemas import BookCreate, BookUpdate, DisplayBook 
from src.db.database import get_db 

router = APIRouter(
    prefix="/api/books",
    tags=["Books"]
)

@router.post('', response_model=DisplayBook, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    new_book = Book(**book.dict())
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book

@router.get('', response_model=List[DisplayBook])
async def books_list(is_available: bool = None, db: AsyncSession = Depends(get_db)):
    query = select(Book)
    
    if is_available is not None:
        query = query.filter(Book.is_available == is_available)
    
    result = await db.execute(query)
    return result.scalars().all() 


@router.get('/{book_id}', response_model=DisplayBook)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    try:
        query = select(Book).filter_by(id=book_id)
        result = await db.execute(query)
        book = result.scalar_one()
        return book
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@router.put('/{book_id}', response_model=DisplayBook)
async def update_book(book_id: int, book: BookUpdate, db: AsyncSession = Depends(get_db)):
    query = select(Book).filter_by(id=book_id)
    result = await db.execute(query)
    existing_book = result.scalar_one_or_none()
    if not existing_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    for key, value in book.dict(exclude_unset=True).items():
        setattr(existing_book, key, value)
    db.add(existing_book)
    await db.commit()
    await db.refresh(existing_book)
    return existing_book


@router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    query = select(Book).filter_by(id=book_id)
    result = await db.execute(query)
    existing_book = result.scalar_one_or_none()
    if not existing_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    await db.delete(existing_book)
    await db.commit()
