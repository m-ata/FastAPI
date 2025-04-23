from fastapi import FastAPI , UploadFile 

app = FastAPI()

blogs = [
    {"id": 1, "title": "First Blog", "content": "This is the content of the first blog."},
    {"id": 2, "title": "Second Blog", "content": "Content of the second blog."},
    {"id": 3, "title": "Third Blog", "content": "Here is the content of the third blog."},
]

@app.get("/")
def home():
    return {"data": "Welcome to blog backend"}

@app.get("/blogs")
def get_blogs():
    return {"blogs": blogs}

@app.post("/blogs")
def post_blog(title: str, content: str):
    new_blog = {"id": len(blogs) + 1, "title": title, "content": content}
    blogs.append(new_blog)
    return {"message": "Blog added successfully!", "blog": new_blog}

@app.get("/blogs/{blog_id}")
def get_blog(blog_id: int):
    blog = next((blog for blog in blogs if blog["id"] == blog_id), None)
    if blog is None:
        return {"error": "Blog not found!"}
    return {"blog": blog}

@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int):
    blog = next((blog for blog in blogs if blog["id"] == blog_id), None)
    if blog is None:
        return {"error": "Blog not found!"}
    
    blogs.remove(blog) 
    return {"message": f"Blog with id {blog_id} deleted successfully!"}


@app.post("/upload")
def uploadFile(files:list[UploadFile]):
    print(files)
    return {"data:" : "Got the file"}

import uvicorn  # type:ignore
uvicorn.run(app)
