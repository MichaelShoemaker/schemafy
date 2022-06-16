to install simply use:
pip install SparkSchemafy

## Usage
from schemafy import make_spark_schema, make_delta_schema


#Make a Spark DataFrame Schema from a Pandas DataFrame
make_spark_schema(str(spark.sql.DataFram(<Pandas DataFrame>).schema))

#Make a delta table schema from parquet file
make_delta_schema('<your file>.parquet')