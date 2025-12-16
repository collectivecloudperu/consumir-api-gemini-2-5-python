from google import genai
from google.genai import types
import os

# Colocamos nuestra API KEY
GEMINI_API_KEY = "DFGDGEdfgggggggggggd54645645"
api_key = "DFGDGEdfgggggggggggd54645645"

# Crear cliente
cliente = genai.Client(api_key=api_key)

# Llamar al modelo Gemini 2.5 flash
response = cliente.models.generate_content(
    model="gemini-2.5-flash", contents="Donde esta Egipto?"
)

# Imprimimos la respuesta de Gemini 2.5
print(response.text)

