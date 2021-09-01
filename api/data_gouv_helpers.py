import math
from urllib.parse import urlencode
from django.shortcuts import redirect


def manage_multiple_address_reponses(baseurl: str, locations: dict) -> list:
    """
    The function build a json containing possible address matching requests
    """
    json_instructions = []
    base_url = baseurl.split("?q")

    # TODO: Comprehensive list
    for location in locations:
        json_instruction = {}
        json_instruction["address"] = str(location.get("properties").get("label"))
        json_instruction["url"] = (
            str(base_url[0]) + "?q=" + str(location.get("properties").get("label"))
        )
        json_instructions.append(json_instruction)

    json_content = {
        "message": "Your address was not precise enough please choose from the following and put back address",
        "possible_address": json_instructions,
    }

    return json_content


def truncate(number: float, digits: int) -> float:
    """
    Simple function to truncate float number
    """
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def redirect_params(url: str, params: object = None):
    """
    A wrapper around django redirect to easily pass params
    """
    response = redirect(url)
    if params:
        query_string = urlencode(params)
        response["Location"] += "?" + query_string
    print(response)
    return response
