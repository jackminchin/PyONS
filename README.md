# PyONS
**Python wrapper for the Office for National Statistics API**
![Upload Python Package](https://github.com/jackminchin/PythonONSAPIWrapper/workflows/Upload%20Python%20Package/badge.svg)

## Installation

        pip install pyONS


## Usage

## Datasets

### Get List of Available Datasets

* The ONS do not seem to provide their full range of datasets through their BETA API. 

#### As Pandas DataFrame

```python
from pyONS import api.Datasets

datasets_df = Datasets().as_DataFrame()
```

#### As JSON

```python
from pyONS import api.Datasets

datasets_json = Datasets().as_Json()
```

### Get Latest Dataset Version

```python
from pyONS import api.Datasets

dataset = Datasets().Dataset(dataset_id).getLatest()
```

### Interacting with Datasets

#### List Editions

#### List Versions

#### List Dimensions

```python
from pyONS import api.Datasets

dimensions = x = Datasets().Dataset(dataset_id).edition(edition).version(version).dimensions().list()
print(dimensions)
```



*Not affiliated with the Office for National Statistics* 
