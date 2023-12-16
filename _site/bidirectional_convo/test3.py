from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "ChatGPT (Chat Generative Pre-trained Transformer) is a large language model-based chatbot developed by OpenAI and launched on November 30, 2022, that enables users to refine and steer a conversation towards a desired length, format, style, level of detail, and language. Successive prompts and replies, known as prompt engineering, are considered at each conversation stage as a context.[2]   `ChatGPT is built upon either GPT-3.5 or GPT-4, both of which are members of OpenAI's proprietary series of generative pre-trained transformer (GPT) models, based on the transformer architecture developed by Google[3]—and is fine-tuned for conversational"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content)