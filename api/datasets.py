import requests
import pandas as pd
import json
import csv
import io

base_url = "https://api.beta.ons.gov.uk/v1"

class Error(Exception):
    """ Base class for exceptions """
    pass

class HTTPError(Error):
    def __init__(self, message):
        self.message = message

class Datasets(object):
    def __init__(self):
        """ Returns a list of datasets. This endpoint supports pagination per the below parameters """
        self.r = requests.get(base_url + '/datasets')
        status_code = self.r.status_code

        if (status_code == 500):
            raise HTTPError("Server Error")

        if (status_code == 404):
            raise HTTPError("The requested resource does not exist")

    def as_json(self):
        r = self.r
        response = r.json()
        return response   

    def as_DataFrame(self):
        r = self.r
        response = pd.DataFrame(r.json()['items'])
        return response

    class Dataset(object):
        def __init__(self, dataset_id):
            self.dataset_id = dataset_id
            r = requests.get(base_url + '/datasets/' + dataset_id)
            self.r = r
            status_code = r.status_code

            if (status_code == 500):
                raise HTTPError("Server Error")

            if (status_code == 404):
                raise HTTPError("The requested resource does not exist")
        
        def getLatest(self):
            dataset_id = self.dataset_id
            r = requests.get(base_url + '/datasets/' + dataset_id)
            

            response = r.json()
            latest_version_href = response['links']['latest_version']['href']
            
            r = requests.get(latest_version_href)
            response = r.json()
            csv_url  = response['downloads']['csv']['href']
    
            r = requests.get(csv_url)
            r = r.content.decode('utf8')
            df = pd.read_csv(io.StringIO(r))

            return df

        def edition(self):
            return Datasets.edition(self.dataset_id)
           

    class edition: 
        def __init__(self, dataset_id ):
            r = requests.get(base_url + '/datasets/' + dataset_id + '/editions')
            self.r = r
          
        def get(self):
            editions = self.r.json()['items']
            return editions

