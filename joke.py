import gradio as gr
import requests
import os
FastAPI_URL = "https://joke-proj.onrender.com/joke"
def joke(prompt, category, language):
    try:
        response = requests.post(
            FastAPI_URL,
            json={
                "prompt": prompt,
                "category": category,
                "language": language
            },
            timeout=60
        )

        return f"Status Code: {response.status_code}\n\nResponse:\n{response.text}"

    except Exception as e:
        return f"Exception: {e}"
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
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
