# Flask API: Traducción Inglés - Español

Este proyecto es una aplicación **Flask** que proporciona una funcionalidad principal:

1. **Traducción de Texto**: Traduce un texto de inglés a español.

El modelo utilizado está basado en **Hugging Face Transformers** y se expone a través de una API REST.

---

## 1. Requerimientos de Instalación

Antes de ejecutar la aplicación, asegúrate de tener instalado:

- **Python 3.8+** ([Descargar aquí](https://www.python.org/downloads/))
- **pip** (Gestor de paquetes de Python)
- **Virtualenv** (opcional, pero recomendado)

### 1.1 Instalar dependencias

#### Clonar este repositorio:
```bash
git clone https://github.com/crisrodriguez1993/flask-sentiment-translator.git
cd tu-repositorio
```

#### Crear y activar un entorno virtual:
```bash
python -m venv env  # Crear entorno virtual
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows
```

#### Instalar las dependencias:
```bash
pip install -r requirements.txt
```

---

## 2. Cómo Ejecutar la Aplicación

Ejecuta la API Flask:
```bash
python app.py
```

Si todo funciona correctamente, verás algo como esto:
```
Servidor Flask iniciándose en http://127.0.0.1:5555
```

---

## 3. Endpoints Disponibles

### 3.1 Traducción de Inglés a Español
- **Modelo:** Helsinki-NLP Opus MT
- **Ruta:** `/translate`
- **Método:** `POST`
- **Descripción:** Recibe un texto en inglés y lo traduce al español.

#### Ejemplo de solicitud:
```bash
curl -X POST "http://127.0.0.1:5555/translate" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, how are you?"}'
```
#### Respuesta esperada:
```json
{"translated_text": "Hola, ¿cómo estás?"}
```

---

## 4. Interfaz Web

El proyecto incluye una interfaz web (`index.html`) donde puedes:
- Traducir texto de inglés a español.

### Pasos para usar la interfaz:
1. **Ejecuta `app.py`** para levantar el servidor.
2. **Abre `index.html` en tu navegador** (doble clic o `Ctrl + O` en Chrome).
3. **Prueba ingresando texto** en los campos correspondientes.

---

## 5. Posibles Errores y Soluciones

❌ **Error: "sentencepiece not found"**
- **Solución:** Instalar la librería necesaria:
  ```bash
  pip install sentencepiece
  ```

❌ **Error: "Port 5555 already in use"**
- **Solución:** Detener el proceso que usa ese puerto:
  ```bash
  lsof -i :5555  # Identificar proceso (Mac/Linux)
  kill -9 <PID>  # Matar proceso en el puerto 5555
  ```

---

## 6. Tecnologías Utilizadas
- **Flask**: Framework backend en Python.
- **Hugging Face Transformers**: Modelos de IA para NLP.
- **Torch**: Librería para modelos de aprendizaje profundo.
- **JavaScript + HTML**: Para la interfaz web.
- **cURL**: Para pruebas en la terminal.

---

## 7. Contribuciones y Contacto
Si quieres mejorar este proyecto o tienes preguntas:
📧 **Email:** cristian.rodriguezbarba@gmail.com  

¡Gracias por usar esta aplicación!