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
        quote, image = get_quote_image(type_)
        response_json = {"quote": f"Here is your quote: {quote}", "image": image}
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
    
 
def get_quote_image(type_):
    connect_str = os.environ["AzureWebJobsStorage"]
    container_name = "data"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client1 = container_client.get_blob_client("quotes.json")
    stream1 = blob_client1.download_blob()
    quotes = json.loads(stream1.readall())
    quote = quotes.get(type_)[randint(0, 19)]
    person = ""
    i = 0
    while quote[len(quote) - 1 - i] != "-":
        person += quote[len(quote) - 1 - i]
        i += 1
    person = person[-2::-1]
    blob_list = list(container_client.list_blobs(name_starts_with=f"images/{person}"))
    rand_image = blob_list[randint(0, len(blob_list) - 1)]
    blob_client2 = container_client.get_blob_client(rand_image)
    stream2 = blob_client2.download_blob()
    image = base64.b64encode(stream2.readall()).decode('utf-8')
    return quote, image

    