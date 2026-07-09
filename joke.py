import gradio as gr
import requests
import os
FastAPI_URL = "https://joke-proj.onrender.com/joke"
def joke(prompt,category,language):
    response=requests.post(FastAPI_URL,json={"prompt":prompt,
    "category":category,
    "language":language})
    if response.status_code==200:
        return response.json()["answer"]
    else:
        return "Error conecting FastAPI"
demo=gr.Interface(
    fn=joke,
    inputs=[gr.Textbox(label="Enter prompt"),
    gr.Dropdown(
        choices=[
            "Programming",
            "Dad Joke",
            "Animal",
            "School",
            "Office",
            "Random"
        ],
        label="Choose category"),
    gr.Dropdown(
        choices=[
            "Telugu",
            "Hindi",
            "English" 
        ],
        label="choose Language"
    )
    ],
outputs=gr.Textbox(label="Anser here",lines=20))
demo.launch()
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
