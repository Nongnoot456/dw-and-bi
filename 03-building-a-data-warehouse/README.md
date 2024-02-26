# Building a Data Warehouse with BigQuery (GCP)

## Started
### Getting Started
```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

### Running ETL Script
```sh
python etl.py
```

### Set def main(dataset_id, table_id, file_path)
```sh
main(dataset_id="github", table_id="events", file_path="github_events.csv")
```

![def main](https://github.com/Nongnoot456/dw-and-bi/blob/main/03-building-a-data-warehouse/Image/Def%20main.png)


### Set Project ID
```sh
project_ID = ""YOUR_GCP_PROJECT""
```


### Set Keyfile Path
```sh
keyfile = ""YOUR_KEYFILE_PATH""
```

### Keyfile Path in GCP
```sh
IAM & Admin --> Service Accounts
Create Service Accounts : 
    Service accounts details: Service account name
    Grant account access to project: Role
    Grant user access to service account: Done
    Create private key type: JSON
```

![Keyfile Path](https://github.com/Nongnoot456/dw-and-bi/blob/main/03-building-a-data-warehouse/Image/Key%20file%20path.png)


### Load data to BigQuery
```sh
python etl.py
```
![BigQuery](https://github.com/Nongnoot456/dw-and-bi/blob/main/03-building-a-data-warehouse/Image/Load%20data%20to%20bigquery.png)


### Add Actor in etl and show in bigquery
```sh
Delete events
python etl.py
Create new events
```

![Actor in etl0](https://github.com/Nongnoot456/dw-and-bi/blob/main/03-building-a-data-warehouse/Image/Python%20etl%20add%20actor.png)

![Actor in etl1](https://github.com/Nongnoot456/dw-and-bi/blob/main/03-building-a-data-warehouse/Image/Python%20etl%20add%20login%20.png)


![Actor in BigQuery](https://github.com/Nongnoot456/dw-and-bi/blob/main/03-building-a-data-warehouse/Image/Load%20data%20to%20bigquery.png)


### Query Data

![Query Data](https://github.com/Nongnoot456/dw-and-bi/blob/main/03-building-a-data-warehouse/Image/Query.png)