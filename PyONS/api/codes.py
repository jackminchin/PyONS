""" Used to get details about codes and code lists stored by ONS. Codes are used to provide a common definition when presenting statistics 
with related categories. Codes are gathered in code lists, which may change over time to include new or different codes. 
The meaning of a code should not change over time, but new codes may be created where new meaning is required. """

import requests
import json
import csv

base_url = "https://api.beta.ons.gov.uk/v1"

class Codes():
    def __init__(self, id=None):
        self.id = id


    # /code-lists

    def list(self):
        r = requests.get(base_url + '/code-lists')
        response = r.json()['items']
        data = []
        for code in response: 
            data.append(code['links']['self']['id'])
        return data

    # Instantiate Classes
    def editions(self, edition=None):
        return Editions(self.id, edition)

    # /code-lists/{id}

    # /code-lists/{id}/editions

    # /code-lists/{id}/editions/{edition}

    # /code-lists/{id}/editions/{edition}/codes

    # /code-lists/{id}/editions/{edition}/codes/{code_id}

    # /code-lists/{id}/editions/{edition}/codes/{code_id}/datasets

class Editions:
    def __init__(self, id, edition=None):
        self.id = id

    def list(self):
        r = requests.get(base_url + '/code-lists/{id}/editions'.format(id=self.id))
        response = r.json()
        return response
