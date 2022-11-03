from fastapi import FastAPI
from router import blog_get
from router import blog_post


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/blog/all', tags=['blog'])
def get_all_blogs():
    return {'message': 'All blogs provided'}