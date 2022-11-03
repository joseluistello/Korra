from fastapi import FastAPI
from router import blog_get


app = FastAPI()
app.include_router(blog_get.router)


@app.get('/blog/all', tags=['blog'])
def get_all_blogs():
    return {'message': 'All blogs provided'}