import azure.functions as func
import datetime
import json
import logging
from random import randint
import os
import base64
from azure.storage.blob import BlobServiceClient

app = func.FunctionApp()

@app.route(route="beautiful_quotes", auth_level=func.AuthLevel.ANONYMOUS)
def beautiful_quotes(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    type_ = req.params.get('type')
    if not type_:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            type_ = req_body.get('type')

    if type_:
        with open("quotes.json", "r") as f:
            all_quotes = json.loads(f.read())
            quote = all_quotes.get(type_)[randint(0, 19)]
        person = ""
        i = 0
        while quote[len(quote) - 1 - i] != "-":
            person += quote[len(quote) - 1 - i]
            i += 1
        person = person[-2::-1]
        base64_image = get_image(person)
        response_json = {"quote": f"Here is your quote: {quote}", "image": base64_image}
        response_body = json.dumps(response_json)
        return func.HttpResponse(
            body=response_body,
            status_code=200,
            headers={"Content-Type": "application/json"}
        )

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a quote type in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
 
def get_image(person):
    connect_str = os.environ["AzureWebJobsStorage"]
    container_name = "data"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)
    blob_list = list(container_client.list_blobs(name_starts_with=f"images/{person}"))
    rand_image = blob_list[randint(0, len(blob_list) - 1)]
    blob_client = container_client.get_blob_client(rand_image)
    stream = blob_client.download_blob()
    image = base64.b64encode(stream.readall()).decode('utf-8')
    return image

    