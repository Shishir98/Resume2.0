"""
A FastAPI application for serving static files and rendering Jinja2 templates.

This application uses FastAPI to serve static files from the "static" directory
and renders Jinja2 templates from the "templates" directory. It mounts the "/static"
route to serve static files and uses Jinja2Templates for rendering HTML templates.

Endpoints:
- GET /: Renders the "index.html" template.

Parameters:
    request (Request): A FastAPI Request instance used to render templates.

Returns:
    TemplateResponse: An HTML response rendered using Jinja2 templates.
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the "/static" route to serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2Templates to load templates from the "templates" directory
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    """
    Render the "index.html" template.

    Args:
        request (Request): A FastAPI Request instance used for rendering templates.

    Returns:
        TemplateResponse: An HTML response rendered using Jinja2 templates.
    """
    return templates.TemplateResponse("index.html", {"request": request})
