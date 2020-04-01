# MonetDB CSV Loader From S3 buckets

This tiny project provides some small python scripts as examples and for testing purposes.
The preferable way to load an CSV from a s3 bucket is to use COPY INTO FROM url which will be soon
ready. As an alternative, a python script can be used, especially since MonetDB integrates python.

## Requirements

The python scripts use the smart_open and the pymonetdb libraries.
The authentication of AWS must be done by `aws configure` or by exporting the keys.
More information can be found here:

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

## copy_from_s3.py

This is the first python script showing an example of how you could use the smart_open library.
The script streams the one column .csv file from s3 and inserts the that column into table `gama`.

## s3_loader.sql

That is the main script. It uses the embedded python of MonetDB. To enable python 3 in MonetDB make
sure that you have installed along with MonetDB:

1. monetdb-python3
2. python3-numpy
3. pymonetdb
4. smart_open

Stop the monetdbd. Start it and then:

`monetdb set embedpy3=true <db>`

In mclient copy and paste the s3_loader.sql. Then you can use the:

```
sql> COPY LOADER INTO < TABLE > FROM csv_loader('{"< Link to s3 bucket> ": "< TYPE >", "< First column>": "< TYPE >"}', buffer_line);
sql> COPY LOADER INTO gama FROM csv_loader('{"'s3://my-monetdb-temp-csv-s3bucket/example.csv'": "STRING", "data": "INTEGER"}', 10000);
```

If you want to test or change the script there is also the same script but in vanilla python the
`s3_loader_temp.py` to run your own experiments. The only difference is that the method will print
the results and not save it in the database.

Loader info: https://www.monetdb.org/blog/monetdbpython-loader-functions
