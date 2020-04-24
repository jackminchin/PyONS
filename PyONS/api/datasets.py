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

        def edition(self, edition=None):
            return Datasets.edition(self.dataset_id, edition)
           

    class edition: 
        def __init__(self, dataset_id, edition=None):
            self.dataset_id = dataset_id
            self.edition = edition
            r = requests.get(base_url + '/datasets/' + dataset_id + '/editions')
            self.r = r

        def list(self):
            """ List all editions of the Dataset """
            editions = self.r.json()['items']
            return editions
                       
        def get(self):
            r = requests.get(base_url + '/datasets/' + self.dataset_id + '/editions/' + self.edition)
            r = r.json()
            return r

        def version(self, version=None):
            return Datasets.version(self.dataset_id, self.edition, version)

    class version:
        def __init__(self, dataset_id, edition, version=None):
            self.dataset_id = dataset_id
            self.edition = edition
            self.version = version

            r = requests.get(base_url + '/datasets/' + dataset_id + '/editions/' + edition + '/versions')
            self.r = r
        
        def list(self):
            """ List all versions in the edition """ 
            versions = self.r.json()['items']
            df = pd.DataFrame(versions)
            return df

        def metadata(self):
            """ Get specified version """
            r = requests.get(base_url + '/datasets/' + self.dataset_id + '/editions/' + self.edition + '/versions/' + self.version)
            response = r.json()
            return response

        def as_csv(self):
            pass
    
        def as_DataFrame(self):
            r = requests.get(base_url + '/datasets/' + self.dataset_id + '/editions/' + self.edition + '/versions/' + self.version)
            response = r.json()
            csv_download_link = response['downloads']['csv']['href']
            df = dfFromURL(csv_download_link)
            return df

        def dimensions(self, dimensions=None):
            return Datasets.dimensions(self.dataset_id, self.edition, self.version, dimensions)


        def observation(self, dimensions=None):
            return Datasets.observation(self.dataset_id, self.edition, self.version, dimensions)

    class dimensions:
        def __init__(self, dataset_id, edition, version, dimensions=None):
            version = str(version)
            self.dataset_id = dataset_id
            self.edition = edition
            self.version = version
        
        def list(self):
            """ List all dimensions in version """
            r = requests.get(base_url + '/datasets/' + self.dataset_id + '/editions/' + self.edition + '/versions/' + self.version +'/dimensions')
            data = r.json()['items']
            dimensions = []
            for item in data:
                dimensions.append(item['name'])
            return dimensions


    class observation:
        """" /datasets/{id}/editions/{edition}/versions/{version}/observations """
        def __init__(self, dataset_id, edition, version, dimensions=None):
            self.edition = edition
            self.dataset_id = dataset_id
            self.version = version
            self.dimensions = dimensions

        def get(self):
            r = requests.get(
               base_url + '/datasets/{id}/editions/{edition}/versions/{version}/observations'.format(id = self.dataset_id, edition = self.edition, version = self.version), params = self.dimensions)
            print(r.url)
            response = r.json()
            return response

def dfFromURL(csv_url):
    r = requests.get(csv_url)
    r = r.content.decode('utf8')
    df = pd.read_csv(io.StringIO(r))
    return df
