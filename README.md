# PythonONSAPIWrapper


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


*Not affiliated with the Office for National Statistics* 
