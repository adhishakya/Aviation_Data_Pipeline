# Aviation_Data_Pipeline
Automated aviation data extraction from Aviation Stack, insertion using Python and MySQL, data cleaning and storage using Pandas library and MySQL, and task automation using Apache Airflow.


## Flow Diagram

![AviationFlow](https://github.com/user-attachments/assets/3bf0cc22-c537-4f54-ada4-d488584fecf3)

## Installation and Setup

- Install dependencies

```bash
pip install -e .
```

- Configure environment variables
- Ensure database and table creation. Link to query listed below <br>
  [- Raw Table](https://github.com/adhishakya/Aviation_Data_Pipeline/blob/main/aviation_package/create_table.sql)
  <br>
  [- Cleaned Table](https://github.com/adhishakya/Aviation_Data_Pipeline/blob/main/aviation_package/create_cleaned_table.sql)

## Running the Pipeline

- Test the Extraction Script
```bash
python main.py
```
This should fetch aviation data and store it in one of the MySQL databases. Next the data will be cleaned and stored into another MySQL database as cleaned data.

- Set Up Apache Airflow
Ensure Airflow is installed and properly configured.
```bash
export AIRFLOW_HOME=~/airflow
airflow db init
airflow scheduler & airflow webserver
```

- Move DAG to Airflow DAGs Folder
```bash
cp dags/aviation_etl_dag.py ~/airflow/dags/
```
Now, the DAG should be visible in the Airflow UI.

- Start Airflow Scheduler
```bash
airflow scheduler
```

## Demo

- DAG Logs
  
  ![AviationDagLogs](https://github.com/user-attachments/assets/bd5d67bf-eeb8-4618-b596-5994a7eb789a)

- DAG Status and Run Type
  
  ![AviationDagStatus](https://github.com/user-attachments/assets/17928eff-c7fb-4dbb-8bb8-df0616f2da1a)


- Data Insertion in MySQL

  ![AviationRawData1](https://github.com/user-attachments/assets/1648a8e0-f558-427c-8ad1-7e60707a0b46)

  ![AviationRawData2](https://github.com/user-attachments/assets/d6fe3790-01d8-490d-9869-01db0cd51dda)

  ![AviationCleanedData1](https://github.com/user-attachments/assets/ccc2908c-3f36-4079-b5d4-6aa61eb6e056)

  ![AviationCleanedData2](https://github.com/user-attachments/assets/18013e36-e1ef-40a3-b38e-4c33f8266a58)


## Troubleshooting
- ModuleNotFoundError: If Airflow can’t find the package, add the project path:
```bash
export PYTHONPATH=$PYTHONPATH:path_to_Aviation_Data_Pipeline
```

## API source
- [Aviation Stack](https://aviationstack.com/)

## Note
- Project switched from using `sqlalchemy` to `mysql.connector` for data cleaning due to version conflicts with pandas 2.2 and SQLAlchemy 1.4.
  More details about the issue [here](https://github.com/pandas-dev/pandas/issues/57049) 






