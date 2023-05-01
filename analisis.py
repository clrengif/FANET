with open("evaluacion.py", "r") as archivo:
    contenido = archivo.read()

import openai
openai.api_key = "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"

# Enviar el contenido del archivo a ChatGPT

pregunta = "¿Cómo puedo eliminar la creación de archivos y guardar las variables en un archivo en el siguiente código?\n\n"
respuesta = openai.Completion.create(
    engine="davinci", 
    prompt=pregunta+contenido, 
    max_tokens=150, 
    n=1, 
    stop=None, 
    temperature=0.5
)

# Imprimir la respuesta de ChatGPT
print(respuesta.choices[0].text)
