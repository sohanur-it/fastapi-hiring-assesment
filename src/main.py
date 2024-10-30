from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from src.routers.books_router import router as books_router

app = FastAPI(
    title="Books API",
    description="Get details for all the Books",
    terms_of_service="#",
    contact={
        "Developer name": "Sohanur Rahman",
    },
    license_info={
        "name": "spaceharpoon",
        "url": None 
    }
)

origins = [
    "http://localhost:3000",
    # Add other allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books_router, tags=['Books'])

@app.get("/")
def index():
    return {"message": "this is fastapi app"}

def start():
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()