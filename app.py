import logging  # 📌 Importamos logging para depuración
from flask import Flask, request, jsonify  # 🌐 Flask para crear el servicio web
from flask_cors import CORS  # 🔄 Permite habilitar CORS y evitar problemas con peticiones externas
from transformers import MarianMTModel, MarianTokenizer  # 🤖 Cargar el modelo de traducción
import torch  # 🔥 PyTorch para manejar el modelo de Hugging Face

# 📌 Configurar logging para depuración y monitoreo del servicio
logging.basicConfig(level=logging.DEBUG)

# 🚀 Crear la aplicación Flask
app = Flask(__name__)
CORS(app)  # 🔄 Habilita CORS para permitir peticiones desde cualquier origen

### 📌 MODELO DE TRADUCCIÓN (Inglés ➡ Español)
model_translation_name = "Helsinki-NLP/opus-mt-en-es"
logging.info("🔄 Cargando el modelo de traducción...")  # 🛠️ Mensaje de inicio de carga

# 🤖 Cargamos el modelo de traducción desde Hugging Face
model_translation = MarianMTModel.from_pretrained(model_translation_name)
tokenizer_translation = MarianTokenizer.from_pretrained(model_translation_name)

logging.info("✅ Modelo de traducción cargado correctamente.")  # ✔️ Confirmación de carga exitosa


### 🌍 Endpoint de traducción 📌
@app.route("/translate", methods=["POST", "OPTIONS"])  # 🚀 Endpoint accesible en /translate
def translate():
    """📢 Recibe un texto en inglés y lo traduce al español"""
    
    logging.info(f"📨 Solicitud recibida en /translate con método {request.method}")

    # 🌍 Manejo de preflight request de CORS (cuando el frontend verifica permisos antes de enviar datos)
    if request.method == "OPTIONS":
        response = jsonify({"message": "✅ CORS preflight request successful"})  # 🟢 Respuesta exitosa
        response.headers.add("Access-Control-Allow-Origin", "*")  # 🌍 Permitir todas las solicitudes
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")  # 📌 Métodos permitidos
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")  # 📜 Cabecera permitida
        return response, 200  # ✅ Respuesta HTTP 200 OK

    try:
        # 📥 Obtener los datos enviados en la solicitud (esperamos JSON)
        data = request.get_json()
        
        # 🚨 Verificar si el JSON es válido y contiene el campo "text"
        if not data or "text" not in data or not data["text"].strip():
            logging.warning("⚠️ Texto vacío en la solicitud de traducción")  # ⚠️ Advertencia en logs
            return jsonify({"error": "No text provided"}), 400  # ⛔ Devolver error 400 (Bad Request)

        logging.info(f"📜 Texto recibido para traducción: {data['text']}")  # 📜 Log del texto de entrada

        # 🔠 Tokenizar el texto antes de pasarlo al modelo
        inputs = tokenizer_translation(data["text"], return_tensors="pt", truncation=True, padding=True)

        # 🔄 Generar la traducción sin necesidad de calcular gradientes
        with torch.no_grad():
            translated_tokens = model_translation.generate(**inputs)

        # 📝 Decodificar el resultado de la traducción
        translated_text = tokenizer_translation.decode(translated_tokens[0], skip_special_tokens=True)

        logging.info(f"✅ Texto traducido: {translated_text}")  # ✔️ Confirmación de traducción exitosa

        # 📤 Devolver la traducción en formato JSON
        return jsonify({"translated_text": translated_text})

    except Exception as e:
        # 🚨 Capturar cualquier error y loguearlo
        logging.error(f"❌ Error en la traducción: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500  # ⛔ Error 500 (Internal Server Error)


### 🚀 Iniciar el servidor Flask
if __name__ == "__main__":
    logging.info("🚀 Servidor Flask iniciándose en http://127.0.0.1:5555")  # 🔥 Mensaje de inicio
    app.run(host="0.0.0.0", port=5555, debug=True)  # 🌍 Iniciar servidor en localhost:5555 con depuración activada