import gradio as gr

def dummy_model(text):
    return f"Echo: {text}"

app = gr.Interface(fn=dummy_model, inputs="text", outputs="text")
app.launch(server_name="0.0.0.0", server_port=8080)
