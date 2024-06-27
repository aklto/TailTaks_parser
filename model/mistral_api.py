from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from keys.key import MISTRAL_API
def generate_summary(text):
    model = "mistral-large-latest"

    client = MistralClient(api_key=MISTRAL_API)
    messages = [
        ChatMessage(role="user", content=f"Пожалуйста, сформулируйте краткое содержание текста, НА РУССКОМ ЯЗЫКЕ, используя литературные нормы и не превышая 240 символов при это текст должен быть уникальны, НО ПОЛНОСТЬЮ СОХРАНИВ ИЗНАЧАЛЬНЫЙ СМЫСЛ. Так же создай заголовок, формат должен быть: заголовок \n краткое содержание  {text}")
    ]

    chat_response = client.chat(
        model=model,
        messages=messages,
    )

    return chat_response.choices[0].message.content

