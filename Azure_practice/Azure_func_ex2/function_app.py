import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="convert_temperature", auth_level=func.AuthLevel.ANONYMOUS)
def convert_temperature(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    temp = req.params.get('temp')
    unit = req.params.get('unit')
    if not temp or not unit:
        try:
            req_body = req.get_json()
        except ValueError:
            return func.HttpResponse(
             "Temperature and unit needed as parameters",
             status_code=400
        )
        else:
            temp = req_body.get('temp')
            unit = req_body.get('unit')

    if (type(temp) is float or type(temp) is int) and type(unit) is str:
        if unit.lower() == 'fahreinheit':
            temp_converted = temp * 9/5 + 32
        elif unit.lower() == 'celsius':
            temp_converted = (temp - 32) * 5/9
        else:
            return func.HttpResponse(
                "Bad Parameters",
                status_code=400
            )
        temperature = f"The temperature in {unit} is {temp_converted}"
        return func.HttpResponse(
            temperature,
            status_code=200
        )
    else:
        return func.HttpResponse(
             "Temperature and unit needed",
             status_code=400
        )