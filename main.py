from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from db import models
from db.database import engine
from routers import user
from routers import post
from routers import comment
from auth import authentication
import uvicorn
import os

app = FastAPI()

@app.get('/alive')
def alive():
  return {
    'message': 'I am alive'
  }
  
app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)
app.include_router(comment.router)

origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware, 
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ['*'],
  allow_headers = ['*']
)

models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')

if __name__ == "__main__":
  uvicorn.run(app, host="localhost", port=int(8001))
