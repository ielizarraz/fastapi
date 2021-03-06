
from fastapi import FastAPI , Response , status , Depends
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from pydantic import BaseModel
from starlette.status import HTTP_204_NO_CONTENT
from random import randrange
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


""" class Post(BaseModel):
    title: str 
    content: str
    published: bool = True """
while True:
    
    try: 
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Icryduringsex99', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful!")
        break
    except Exception as error:
        print(f"Connecting to database failed {error}")
        time.sleep(2)
    


#POSTS CRUD 



@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts =  db.query(models.Post).all()
    return {"data": posts}


#Create New Post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts():
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    
    conn.commit()
    
    return {"data":new_post}


#Read all posts
@app.get("/posts")
def read_posts():
    cursor.execute("""SELECT * FROM posts;""")
    posts = cursor.fetchall()
    return {"details: ": posts}


#Read specific post
@app.get("/posts/{id}")
def read_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = (%s) """, (str(id),))
    post = cursor.fetchone()
    if not post: 
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id: {id} was not found")
    return {"post details: ": post} 
    
    
#Update post
@app.put("/posts/{id}")
def update_post( id: int):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post: 
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id: {id} was not found")
    return {"data: ": updated_post}

#Delete a specific post 
@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post: raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id: {id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

