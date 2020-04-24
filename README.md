# PyONS
** Python wrapper for the Office for National Statistics API **


## Get List of Datasets

### As Pandas DataFrame

```python
from pyONS import api.Datasets

datasets_df = Datasets().as_DataFrame()
```

### As JSON

```python
from pyONS import api.Datasets

datasets_json = Datasets().as_Json()
```

## Get Latest Dataset Version

```python
from pyONS import api.Datasets

dataset = Datasets().Dataset(dataset_id).getLatest()
```

## Interacting with Datasets

### List Editions

### List Versions

### List Dimensions

```python
from pyONS import api.Datasets

dimensions = x = Datasets().Dataset(dataset_id).edition(edition).version(version).dimensions().list()
print(dimensions)
```



*Not affiliated with the Office for National Statistics* 
