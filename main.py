from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import employee
from router import earnings
from router import delivery_events
from router import operations

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(employee.router)
app.include_router(earnings.router)
app.include_router(delivery_events.router)
app.include_router(operations.router)
