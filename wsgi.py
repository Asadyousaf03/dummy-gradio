import gradio as gr
from gradio_app import app

# ASGI application for Uvicorn
application = app.queue()  # This makes it ASGI-compatible
