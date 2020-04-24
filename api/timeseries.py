import requests

base_url = "https://api.ons.gov.uk"


class Error(Exception):
    """ Base class for exceptions """
    pass


class HTTPError(Error):
    def __init__(self, message):
        self.message = message


def timeseries(start="", limit=""):
    """ Returns a list of datasets. This endpoint supports pagination per the below parameters """
    r = requests.get(base_url + '/timeseries',
                     params={'start': start, 'limit': limit})
    print(r.url)
    status_code = r.status_code

    if (status_code == 500):
        raise HTTPError("Server Error")

    if (status_code == 404):
        raise HTTPError("The requested resource does not exist")

    response = r.json()
    return response
