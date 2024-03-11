import azure.functions as func
import datetime
import json
import logging
import requests
from PIL import Image
from io import BytesIO

app = func.FunctionApp()

@app.route(route="process_image", auth_level=func.AuthLevel.ANONYMOUS)
def image_processing(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Request is being processed')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
             "Image url needed",
             status_code=400
        )
    r = requests.get(req_body["url"])
    r.raise_for_status()
    with Image.open(BytesIO(r.content)) as img:
        # Convert the image to grayscale
        img = img.convert("L")
        image_bytes = BytesIO()
        img.save(image_bytes, format='PNG')
        image_bytes.seek(0)

    return func.HttpResponse(
        image_bytes.read(),
        mimetype="image/png",
        status_code=200
    )