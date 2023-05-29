from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# create an interface for the model
iface = gr.Interface(fn=predict, inputs=gr.inputs.Textbox(lines=4, placeholder="Enter text block to summarize"), outputs="text")

iface.launch()