from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Post, Role, Tag, User
from app.schemas import PostCreate, PostResponse, PostUpdate, UserResponse
from app import auth
from app.schemas import PostResponseWithAuthor


router = APIRouter(
    prefix = "/posts"
)


#Get all blog post
@router.get("",response_model=list[PostResponseWithAuthor])
def get_all_posts(db: Session = Depends(get_db)):
    posts =db.query(Post).all()
    return posts

# #Get a specified blog post
@router.get("/{post_id}", response_model=PostResponseWithAuthor)
def get_post(post_id : int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
#Create a blog post
@router.post("", response_model=PostResponseWithAuthor)
def create_post(post: PostCreate,current_user: UserResponse = Depends(auth.get_current_user),db:Session = Depends(get_db)):
    print(type(current_user.role))
    if current_user.role != Role.ADMIN.value and current_user.role !=Role.EDITOR.value:
        raise HTTPException(
            status_code=403,
            detail="Not authorized for creating"
        )
    new_post = Post(
        title=post.title,
        content=post.content,
        # category=post.category,
        # status=post.status,
        author_id=current_user.id,
        # tags=tag_objects
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    

#Update a blog post
@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id : int, updated_post: PostUpdate,current_user: UserResponse = Depends(auth.get_current_user) ,db:Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail= "post not found") 
    if post.author_id != current_user.id and current_user.role != Role.ADMIN.value:
        raise HTTPException(
            status_code=403,
            detail="Not authorized for updating"
        )

    post.title = updated_post.title
    post.content = updated_post.content 
    post.status = updated_post.status
    post.views = updated_post.views

    db.commit()
    db.refresh(post)
    return post

#Delete a blog post
@router.delete("/{post_id}",)
def delete_post(post_id : int,current_user: UserResponse = Depends(auth.get_current_user), db:Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post.author_id != current_user.id and current_user.role != Role.ADMIN.value:
        raise HTTPException(
            status_code=403,
            detail="Not authorized for updating"
        )
    
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {
        "message": "successful"
    }

  