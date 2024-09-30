# STITCHeD
 STITCHED - *Standardized Tool for Integrating and Transforming Hate Speech Datasets into an established Database*, is a data tool integrating different datasets in the research domain of Hate Speech, whose schemas often differ greatly, into a SQL database, while preserving the original label name and label definition. The design allows for a more flexible way of dataset combination and data extraction.

## Install the Package

```bash
pip install STITCHED==0.1.0
```

## Generate Config File

Configuration File for the database can be either supplied or created with our `Config` tool. However, it is crucial for the later stages that supplied config file conform to the following manuals:

Manual for the Config file：
- `dataset_file_name`: Please include the **full** file name including the datatype, e.g. data.csv, data.tsv. If the datasets are splitted into different sets, seperate the names with a comma(`,`).
- `dataset_name`: The short name for the dataset.
- `label_name_definition`: Please write the label name and corresponding definition in a `JSON` format.
- `source`: For data with a single source, please state the source name, e.g. Twitter, Facebook, etc. Add an `@` symbol in-front, e.g. *@Twitter*. If of multi-source, please provide a column name.
- `language`: For single language, language code as stipulated in ISO 639-2 are recognized, e.g. eng, spa, chi, ger, fre, ita, etc (). Add an `@` symbol in-front, e.g. *@eng*. For multi-language contents, please provide a column name describing this property, e.g. languages.
- `text`: The column name of text.

**Note**:
1. Only datasets that are in CSV(comma-seperated) or TSV formats are supported.


```python
from STITCHED import tool
from tool.config.generator import Config
```

To avoid problems in later stages, we advise to create the config file using our tool `Config`, which is modularly structured, easy to use and reliable for the following stages. 

Config file generator (Config) takes two parameters during initialization: `name` of the config file, and `mode` of either `create` or `append`, for the creation and append of dataset item. A mode switch function needs to be called explicitly when switching modes. In the example, two toy datasets will be added into config with the tools:


```python
config = Config("toy_config", mode = 'create')
```

```python
config.add_entry(
    dataset_file_name='toy_data/toy_dataset_1_eng_twitter.csv',
    dataset_name='toy_data_1',
    label_name_definition={'Label1': 'Definition Label 1',
                           'Label2': 'Definition Label 2'},  # two label columns
    text='Text',
    source='@Twitter',
    language='@eng'
)
```


```python
config.switch_mode('append')
```


```python
config.add_entry(    
    dataset_file_name='toy_dataset_2_ger_reddit.csv',
    dataset_name= 'toy_data_2',
    label_name_definition={'Label':'Definition Label'},
    text='Text',
    source='@Reddit',
    language='@ger')
```

## Validate the Datasets
`ConfigValidator` compares the `config` file with the provided data folder path, to see if everything listed on `config` matches the dataset provided. If some check fails, detailed error message will also be helpful to locate and correct the problem.


```python
from tool.loader.validator import ConfigValidator
```


```python
config_validator = ConfigValidator('toy_config','../toy_data')
config_validator.final_config()
```

## Load Data into Database
`DataLoader` takes two inputs, a `conn` from the established empty database and an instance of `validator`. Its member function of `storage_datasets()` will process and commit the data change to the database.

Set up a database connection

```python
import sqlite3
from tool.database.setup import setupSchema
from tool.loader.loader import DataLoader

path = 'toy_database.db'
conn = sqlite3.connect(path)
setupSchema(conn)
```

```python
loader = DataLoader(conn=conn, validator=config_validator)
```

```python
loader.storage_datasets()
```    

## Check the data
`QueryInterface` provides many options to look into the dataset, `get_dataset_text_labels()` function extracts information from the text label pairs. More flexible way is also provided in the repository.


```python
from tool.database.queryInterface import QueryInterface
```


```python
queryer = QueryInterface(conn)
```


```python
queryer.get_dataset_text_labels(10, file_path='result.csv')
```

## Extras

The `utils` module includes a set of helpful tools for data analysis and selection during the dataset preparation phase:

- **Distribute Tool**: Analyzes the distribution of one column relative to another, helping users identify balanced or imbalanced data points, useful for dataset selection.
- **Fuzzysearch Tool**: Allows approximate matching within the dataset, helping locate relevant data, such as label definitions or metadata, without requiring exact queries.
- **Sampling Tool**: Provides three pre-configured sampling strategies to ensure balanced and representative data subsets for experimental setups.

