# create-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# create-endpoint

## Description

Creates an endpoint using the provided settings.

### Note

For a MySQL source or target endpoint, donât explicitly specify the database using the `DatabaseName` request parameter on the `CreateEndpoint` API call. Specifying `DatabaseName` when you create a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the DMS task.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateEndpoint)

## Synopsis

```
create-endpoint
--endpoint-identifier <value>
--endpoint-type <value>
--engine-name <value>
[--username <value>]
[--password <value>]
[--server-name <value>]
[--port <value>]
[--database-name <value>]
[--extra-connection-attributes <value>]
[--kms-key-id <value>]
[--tags <value>]
[--certificate-arn <value>]
[--ssl-mode <value>]
[--service-access-role-arn <value>]
[--external-table-definition <value>]
[--dynamo-db-settings <value>]
[--s3-settings <value>]
[--dms-transfer-settings <value>]
[--mongo-db-settings <value>]
[--kinesis-settings <value>]
[--kafka-settings <value>]
[--elasticsearch-settings <value>]
[--neptune-settings <value>]
[--redshift-settings <value>]
[--postgre-sql-settings <value>]
[--my-sql-settings <value>]
[--oracle-settings <value>]
[--sybase-settings <value>]
[--microsoft-sql-server-settings <value>]
[--ibm-db2-settings <value>]
[--resource-identifier <value>]
[--doc-db-settings <value>]
[--redis-settings <value>]
[--gcp-my-sql-settings <value>]
[--timestream-settings <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--endpoint-identifier` (string)

The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They canât end with a hyphen, or contain two consecutive hyphens.

`--endpoint-type` (string)

The type of endpoint. Valid values are `source` and `target` .

Possible values:

- `source`
- `target`

`--engine-name` (string)

The type of engine for the endpoint. Valid values, depending on the `EndpointType` value, include `"mysql"` , `"oracle"` , `"postgres"` , `"mariadb"` , `"aurora"` , `"aurora-postgresql"` , `"opensearch"` , `"redshift"` , `"s3"` , `"db2"` , `"db2-zos"` , `"azuredb"` , `"sybase"` , `"dynamodb"` , `"mongodb"` , `"kinesis"` , `"kafka"` , `"elasticsearch"` , `"docdb"` , `"sqlserver"` , `"neptune"` , `"babelfish"` , `redshift-serverless` , `aurora-serverless` , `aurora-postgresql-serverless` , `gcp-mysql` , `azure-sql-managed-instance` , `redis` , `dms-transfer` .

`--username` (string)

The user name to be used to log in to the endpoint database.

`--password` (string)

The password to be used to log in to the endpoint database.

`--server-name` (string)

The name of the server where the endpoint database resides.

`--port` (integer)

The port used by the endpoint database.

`--database-name` (string)

The name of the endpoint database. For a MySQL source or target endpoint, do not specify DatabaseName. To migrate to a specific database, use this setting and `targetDbType` .

`--extra-connection-attributes` (string)

Additional attributes associated with the connection. Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see [Working with DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html) in the *Database Migration Service User Guide.*

`--kms-key-id` (string)

An KMS key identifier that is used to encrypt the connection parameters for the endpoint.

If you donât specify a value for the `KmsKeyId` parameter, then DMS uses your default encryption key.

KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

`--tags` (list)

One or more tags to be assigned to the endpoint.

(structure)

A user-defined key-value pair that describes metadata added to an DMS resource and that is used by operations such as the following:

- `AddTagsToResource`
- `ListTagsForResource`
- `RemoveTagsFromResource`

Key -> (string)

A key is the required name of the tag. The string value can be 1-128 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be 1-256 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

ResourceArn -> (string)

The Amazon Resource Name (ARN) string that uniquely identifies the resource for which the tag is created.

Shorthand Syntax:

```
Key=string,Value=string,ResourceArn=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "ResourceArn": "string"
  }
  ...
]
```

`--certificate-arn` (string)

The Amazon Resource Name (ARN) for the certificate.

`--ssl-mode` (string)

The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is `none`

Possible values:

- `none`
- `require`
- `verify-ca`
- `verify-full`

`--service-access-role-arn` (string)

The Amazon Resource Name (ARN) for the service access role that you want to use to create the endpoint. The role must allow the `iam:PassRole` action.

`--external-table-definition` (string)

The external table definition.

`--dynamo-db-settings` (structure)

Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see [Using Object Mapping to Migrate Data to DynamoDB](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping) in the *Database Migration Service User Guide.*

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.

Shorthand Syntax:

```
ServiceAccessRoleArn=string
```

JSON Syntax:

```
{
  "ServiceAccessRoleArn": "string"
}
```

`--s3-settings` (structure)

Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see [Extra Connection Attributes When Using Amazon S3 as a Target for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring) in the *Database Migration Service User Guide.*

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action. It is a required parameter that enables DMS to write and read objects from an S3 bucket.

ExternalTableDefinition -> (string)

Specifies how tables are defined in the S3 source files only.

CsvRowDelimiter -> (string)

The delimiter used to separate rows in the .csv file for both source and target. The default is a carriage return (`\n` ).

CsvDelimiter -> (string)

The delimiter used to separate columns in the .csv file for both source and target. The default is a comma.

BucketFolder -> (string)

An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this parameter isnât specified, then the path used is `` *schema_name* /*table_name* /`` .

BucketName -> (string)

The name of the S3 bucket.

CompressionType -> (string)

An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or donât use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats.

EncryptionMode -> (string)

The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either `SSE_S3` (the default) or `SSE_KMS` .

### Note

For the `ModifyEndpoint` operation, you can change the existing value of the `EncryptionMode` parameter from `SSE_KMS` to `SSE_S3` . But you canât change the existing value from `SSE_S3` to `SSE_KMS` .

To use `SSE_S3` , you need an Identity and Access Management (IAM) role with permission to allow `"arn:aws:s3:::dms-*"` to use the following actions:

- `s3:CreateBucket`
- `s3:ListBucket`
- `s3:DeleteBucket`
- `s3:GetBucketLocation`
- `s3:GetObject`
- `s3:PutObject`
- `s3:DeleteObject`
- `s3:GetObjectVersion`
- `s3:GetBucketPolicy`
- `s3:PutBucketPolicy`
- `s3:DeleteBucketPolicy`

ServerSideEncryptionKmsKeyId -> (string)

If you are using `SSE_KMS` for the `EncryptionMode` , provide the KMS key ID. The key that you use needs an attached policy that enables Identity and Access Management (IAM) user permissions and allows use of the key.

Here is a CLI example: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html#id1)aws dms create-endpoint âendpoint-identifier *value* âendpoint-type target âengine-name s3 âs3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

DataFormat -> (string)

The format of the data that you want to use for output. You can choose one of the following:

- `csv` : This is a row-based file format with comma-separated values (.csv).
- `parquet` : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.

EncodingType -> (string)

The type of encoding you are using:

- `RLE_DICTIONARY` uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.
- `PLAIN` doesnât use encoding at all. Values are stored as they are.
- `PLAIN_DICTIONARY` builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.

DictPageSizeLimit -> (integer)

The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of `PLAIN` . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to `PLAIN` encoding. This size is used for .parquet file format only.

RowGroupLength -> (integer)

The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.

If you choose a value larger than the maximum, `RowGroupLength` is set to the max row group length in bytes (64 * 1024 * 1024).

DataPageSize -> (integer)

The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.

ParquetVersion -> (string)

The version of the Apache Parquet format that you want to use: `parquet_1_0` (the default) or `parquet_2_0` .

EnableStatistics -> (boolean)

A value that enables statistics for Parquet pages and row groups. Choose `true` to enable statistics, `false` to disable. Statistics include `NULL` , `DISTINCT` , `MAX` , and `MIN` values. This parameter defaults to `true` . This value is used for .parquet file format only.

IncludeOpForFullLoad -> (boolean)

A value that enables a full load to write INSERT operations to the comma-separated value (.csv) or .parquet output files only to indicate how the rows were added to the source database.

### Note

DMS supports the `IncludeOpForFullLoad` parameter in versions 3.1.4 and later.

DMS supports the use of the .parquet files with the `IncludeOpForFullLoad` parameter in versions 3.4.7 and later.

For full load, records can only be inserted. By default (the `false` setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If `IncludeOpForFullLoad` is set to `true` or `y` , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.

### Note

This setting works together with the `CdcInsertsOnly` and the `CdcInsertsAndUpdates` parameters for output to .csv files only. For more information about how these settings work together, see [Indicating Source DB Operations in Migrated S3 Data](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps) in the *Database Migration Service User Guide.* .

CdcInsertsOnly -> (boolean)

A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the `false` setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.

If `CdcInsertsOnly` is set to `true` or `y` , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of `IncludeOpForFullLoad` . If `IncludeOpForFullLoad` is set to `true` , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If `IncludeOpForFullLoad` is set to `false` , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see [Indicating Source DB Operations in Migrated S3 Data](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps) in the *Database Migration Service User Guide.* .

### Note

DMS supports the interaction described preceding between the `CdcInsertsOnly` and `IncludeOpForFullLoad` parameters in versions 3.1.4 and later.

`CdcInsertsOnly` and `CdcInsertsAndUpdates` canât both be set to `true` for the same endpoint. Set either `CdcInsertsOnly` or `CdcInsertsAndUpdates` to `true` for the same endpoint, but not both.

TimestampColumnName -> (string)

A value that when nonblank causes DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.

### Note

DMS supports the `TimestampColumnName` parameter in versions 3.1.4 and later.

DMS includes an additional `STRING` column in the .csv or .parquet object files of your migrated data when you set `TimestampColumnName` to a nonblank value.

For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.

For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.

The string format for this timestamp column value is `yyyy-MM-dd HH:mm:ss.SSSSSS` . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.

When the `AddColumnName` parameter is set to `true` , DMS also includes a name for the timestamp column that you set with `TimestampColumnName` .

ParquetTimestampInMillisecond -> (boolean)

A value that specifies the precision of any `TIMESTAMP` column values that are written to an Amazon S3 object file in .parquet format.

### Note

DMS supports the `ParquetTimestampInMillisecond` parameter in versions 3.1.4 and later.

When `ParquetTimestampInMillisecond` is set to `true` or `y` , DMS writes all `TIMESTAMP` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.

Currently, Amazon Athena and Glue can handle only millisecond precision for `TIMESTAMP` values. Set this parameter to `true` for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or Glue.

### Note

DMS writes any `TIMESTAMP` column values written to an S3 file in .csv format with microsecond precision.

Setting `ParquetTimestampInMillisecond` has no effect on the string format of the timestamp column value that is inserted by setting the `TimestampColumnName` parameter.

CdcInsertsAndUpdates -> (boolean)

A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is `false` , but when `CdcInsertsAndUpdates` is set to `true` or `y` , only INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.

### Warning

DMS supports the use of the .parquet files in versions 3.4.7 and later.

How these INSERTs and UPDATEs are recorded depends on the value of the `IncludeOpForFullLoad` parameter. If `IncludeOpForFullLoad` is set to `true` , the first field of every CDC record is set to either `I` or `U` to indicate INSERT and UPDATE operations at the source. But if `IncludeOpForFullLoad` is set to `false` , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see [Indicating Source DB Operations in Migrated S3 Data](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps) in the *Database Migration Service User Guide.* .

### Note

DMS supports the use of the `CdcInsertsAndUpdates` parameter in versions 3.3.1 and later.

`CdcInsertsOnly` and `CdcInsertsAndUpdates` canât both be set to `true` for the same endpoint. Set either `CdcInsertsOnly` or `CdcInsertsAndUpdates` to `true` for the same endpoint, but not both.

DatePartitionEnabled -> (boolean)

When set to `true` , this parameter partitions S3 bucket folders based on transaction commit dates. The default value is `false` . For more information about date-based folder partitioning, see [Using date-based folder partitioning](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.DatePartitioning) .

DatePartitionSequence -> (string)

Identifies the sequence of the date format to use during folder partitioning. The default value is `YYYYMMDD` . Use this parameter when `DatePartitionedEnabled` is set to `true` .

DatePartitionDelimiter -> (string)

Specifies a date separating delimiter to use during folder partitioning. The default value is `SLASH` . Use this parameter when `DatePartitionedEnabled` is set to `true` .

UseCsvNoSupValue -> (boolean)

This setting applies if the S3 output files during a change data capture (CDC) load are written in .csv format. If set to `true` for columns not included in the supplemental log, DMS uses the value specified by ` `CsvNoSupValue` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-CsvNoSupValue`__ . If not set or set to `false` , DMS uses the null value for these columns.

### Note

This setting is supported in DMS versions 3.4.1 and later.

CsvNoSupValue -> (string)

This setting only applies if your Amazon S3 output files during a change data capture (CDC) load are written in .csv format. If ` `UseCsvNoSupValue` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-UseCsvNoSupValue`__ is set to true, specify a string value that you want DMS to use for all columns not included in the supplemental log. If you do not specify a string value, DMS uses the null value for these columns regardless of the `UseCsvNoSupValue` setting.

### Note

This setting is supported in DMS versions 3.4.1 and later.

PreserveTransactions -> (boolean)

If set to `true` , DMS saves the transaction order for a change data capture (CDC) load on the Amazon S3 target specified by ` `CdcPath` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-CdcPath`__ . For more information, see [Capturing data changes (CDC) including transaction order on the S3 target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath) .

### Note

This setting is supported in DMS versions 3.4.2 and later.

CdcPath -> (string)

Specifies the folder path of CDC files. For an S3 source, this setting is required if a task captures change data; otherwise, itâs optional. If `CdcPath` is set, DMS reads CDC files from this path and replicates the data changes to the target endpoint. For an S3 target if you set ` `PreserveTransactions` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-PreserveTransactions`__ to `true` , DMS verifies that you have set this parameter to a folder path on your S3 target where DMS can save the transaction order for the CDC load. DMS creates this CDC folder path in either your S3 target working directory or the S3 target location specified by ` `BucketFolder` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-BucketFolder`__ and ` `BucketName` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-BucketName`__ .

For example, if you specify `CdcPath` as `MyChangedData` , and you specify `BucketName` as `MyTargetBucket` but do not specify `BucketFolder` , DMS creates the CDC folder path following: `MyTargetBucket/MyChangedData` .

If you specify the same `CdcPath` , and you specify `BucketName` as `MyTargetBucket` and `BucketFolder` as `MyTargetData` , DMS creates the CDC folder path following: `MyTargetBucket/MyTargetData/MyChangedData` .

For more information on CDC including transaction order on an S3 target, see [Capturing data changes (CDC) including transaction order on the S3 target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath) .

### Note

This setting is supported in DMS versions 3.4.2 and later.

UseTaskStartTimeForFullLoadTimestamp -> (boolean)

When set to true, this parameter uses the task start time as the timestamp column value instead of the time data is written to target. For full load, when `useTaskStartTimeForFullLoadTimestamp` is set to `true` , each row of the timestamp column contains the task start time. For CDC loads, each row of the timestamp column contains the transaction commit time.

When `useTaskStartTimeForFullLoadTimestamp` is set to `false` , the full load timestamp in the timestamp column increments with the time data arrives at the target.

CannedAclForObjects -> (string)

A value that enables DMS to specify a predefined (canned) access control list for objects created in an Amazon S3 bucket as .csv or .parquet files. For more information about Amazon S3 canned ACLs, see [Canned ACL](http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) in the *Amazon S3 Developer Guide.*

The default value is NONE. Valid values include NONE, PRIVATE, PUBLIC_READ, PUBLIC_READ_WRITE, AUTHENTICATED_READ, AWS_EXEC_READ, BUCKET_OWNER_READ, and BUCKET_OWNER_FULL_CONTROL.

AddColumnName -> (boolean)

An optional parameter that, when set to `true` or `y` , you can use to add column name information to the .csv output file.

The default value is `false` . Valid values are `true` , `false` , `y` , and `n` .

CdcMaxBatchInterval -> (integer)

Maximum length of the interval, defined in seconds, after which to output a file to Amazon S3.

When `CdcMaxBatchInterval` and `CdcMinFileSize` are both specified, the file write is triggered by whichever parameter condition is met first within an DMS CloudFormation template.

The default value is 60 seconds.

CdcMinFileSize -> (integer)

Minimum file size, defined in kilobytes, to reach for a file output to Amazon S3.

When `CdcMinFileSize` and `CdcMaxBatchInterval` are both specified, the file write is triggered by whichever parameter condition is met first within an DMS CloudFormation template.

The default value is 32 MB.

CsvNullValue -> (string)

An optional parameter that specifies how DMS treats null values. While handling the null value, you can use this parameter to pass a user-defined string as null when writing to the target. For example, when target columns are nullable, you can use this option to differentiate between the empty string value and the null value. So, if you set this parameter value to the empty string (ââ or ââ), DMS treats the empty string as the null value instead of `NULL` .

The default value is `NULL` . Valid values include any valid string.

IgnoreHeaderRows -> (integer)

When this value is set to 1, DMS ignores the first row header in a .csv file. A value of 1 turns on the feature; a value of 0 turns off the feature.

The default is 0.

MaxFileSize -> (integer)

A value that specifies the maximum size (in KB) of any .csv file to be created while migrating to an S3 target during full load.

The default value is 1,048,576 KB (1 GB). Valid values include 1 to 1,048,576.

Rfc4180 -> (boolean)

For an S3 source, when this value is set to `true` or `y` , each leading double quotation mark has to be followed by an ending double quotation mark. This formatting complies with RFC 4180. When this value is set to `false` or `n` , string literals are copied to the target as is. In this case, a delimiter (row or column) signals the end of the field. Thus, you canât use a delimiter as part of the string, because it signals the end of the value.

For an S3 target, an optional parameter used to set behavior to comply with RFC 4180 for data migrated to Amazon S3 using .csv file format only. When this value is set to `true` or `y` using Amazon S3 as a target, if the data has quotation marks or newline characters in it, DMS encloses the entire column with an additional pair of double quotation marks (â). Every quotation mark within the data is repeated twice.

The default value is `true` . Valid values include `true` , `false` , `y` , and `n` .

DatePartitionTimezone -> (string)

When creating an S3 target endpoint, set `DatePartitionTimezone` to convert the current UTC time into a specified time zone. The conversion occurs when a date partition folder is created and a CDC filename is generated. The time zone format is Area/Location. Use this parameter when `DatePartitionedEnabled` is set to `true` , as shown in the following example.

`s3-settings='{"DatePartitionEnabled": true, "DatePartitionSequence": "YYYYMMDDHH", "DatePartitionDelimiter": "SLASH", "DatePartitionTimezone":"*Asia/Seoul* ", "BucketName": "dms-nattarat-test"}'`

AddTrailingPaddingCharacter -> (boolean)

Use the S3 target endpoint setting `AddTrailingPaddingCharacter` to add padding on string data. The default value is `false` .

ExpectedBucketOwner -> (string)

To specify a bucket owner and prevent sniping, you can use the `ExpectedBucketOwner` endpoint setting.

Example: `--s3-settings='{"ExpectedBucketOwner": "*AWS_Account_ID* "}'`

When you make a request to test a connection or perform a migration, S3 checks the account ID of the bucket owner against the specified parameter.

GlueCatalogGeneration -> (boolean)

When true, allows Glue to catalog your S3 bucket. Creating an Glue catalog lets you use Athena to query your data.

Shorthand Syntax:

```
ServiceAccessRoleArn=string,ExternalTableDefinition=string,CsvRowDelimiter=string,CsvDelimiter=string,BucketFolder=string,BucketName=string,CompressionType=string,EncryptionMode=string,ServerSideEncryptionKmsKeyId=string,DataFormat=string,EncodingType=string,DictPageSizeLimit=integer,RowGroupLength=integer,DataPageSize=integer,ParquetVersion=string,EnableStatistics=boolean,IncludeOpForFullLoad=boolean,CdcInsertsOnly=boolean,TimestampColumnName=string,ParquetTimestampInMillisecond=boolean,CdcInsertsAndUpdates=boolean,DatePartitionEnabled=boolean,DatePartitionSequence=string,DatePartitionDelimiter=string,UseCsvNoSupValue=boolean,CsvNoSupValue=string,PreserveTransactions=boolean,CdcPath=string,UseTaskStartTimeForFullLoadTimestamp=boolean,CannedAclForObjects=string,AddColumnName=boolean,CdcMaxBatchInterval=integer,CdcMinFileSize=integer,CsvNullValue=string,IgnoreHeaderRows=integer,MaxFileSize=integer,Rfc4180=boolean,DatePartitionTimezone=string,AddTrailingPaddingCharacter=boolean,ExpectedBucketOwner=string,GlueCatalogGeneration=boolean
```

JSON Syntax:

```
{
  "ServiceAccessRoleArn": "string",
  "ExternalTableDefinition": "string",
  "CsvRowDelimiter": "string",
  "CsvDelimiter": "string",
  "BucketFolder": "string",
  "BucketName": "string",
  "CompressionType": "none"|"gzip",
  "EncryptionMode": "sse-s3"|"sse-kms",
  "ServerSideEncryptionKmsKeyId": "string",
  "DataFormat": "csv"|"parquet",
  "EncodingType": "plain"|"plain-dictionary"|"rle-dictionary",
  "DictPageSizeLimit": integer,
  "RowGroupLength": integer,
  "DataPageSize": integer,
  "ParquetVersion": "parquet-1-0"|"parquet-2-0",
  "EnableStatistics": true|false,
  "IncludeOpForFullLoad": true|false,
  "CdcInsertsOnly": true|false,
  "TimestampColumnName": "string",
  "ParquetTimestampInMillisecond": true|false,
  "CdcInsertsAndUpdates": true|false,
  "DatePartitionEnabled": true|false,
  "DatePartitionSequence": "YYYYMMDD"|"YYYYMMDDHH"|"YYYYMM"|"MMYYYYDD"|"DDMMYYYY",
  "DatePartitionDelimiter": "SLASH"|"UNDERSCORE"|"DASH"|"NONE",
  "UseCsvNoSupValue": true|false,
  "CsvNoSupValue": "string",
  "PreserveTransactions": true|false,
  "CdcPath": "string",
  "UseTaskStartTimeForFullLoadTimestamp": true|false,
  "CannedAclForObjects": "none"|"private"|"public-read"|"public-read-write"|"authenticated-read"|"aws-exec-read"|"bucket-owner-read"|"bucket-owner-full-control",
  "AddColumnName": true|false,
  "CdcMaxBatchInterval": integer,
  "CdcMinFileSize": integer,
  "CsvNullValue": "string",
  "IgnoreHeaderRows": integer,
  "MaxFileSize": integer,
  "Rfc4180": true|false,
  "DatePartitionTimezone": "string",
  "AddTrailingPaddingCharacter": true|false,
  "ExpectedBucketOwner": "string",
  "GlueCatalogGeneration": true|false
}
```

`--dms-transfer-settings` (structure)

The settings in JSON format for the DMS transfer type of source endpoint.

Possible settings include the following:

- `ServiceAccessRoleArn` - The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the `iam:PassRole` action.
- `BucketName` - The name of the S3 bucket to use.

Shorthand syntax for these settings is as follows: `ServiceAccessRoleArn=string,BucketName=string`

JSON syntax for these settings is as follows: `{ "ServiceAccessRoleArn": "string", "BucketName": "string", }`

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the `iam:PassRole` action.

BucketName -> (string)

The name of the S3 bucket to use.

Shorthand Syntax:

```
ServiceAccessRoleArn=string,BucketName=string
```

JSON Syntax:

```
{
  "ServiceAccessRoleArn": "string",
  "BucketName": "string"
}
```

`--mongo-db-settings` (structure)

Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see [Endpoint configuration settings when using MongoDB as a source for Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration) in the *Database Migration Service User Guide.*

Username -> (string)

The user name you use to access the MongoDB source endpoint.

Password -> (string)

The password for the user account you use to access the MongoDB source endpoint.

ServerName -> (string)

The name of the server on the MongoDB source endpoint. For MongoDB Atlas, provide the server name for any of the servers in the replication set.

Port -> (integer)

The port value for the MongoDB source endpoint.

DatabaseName -> (string)

The database name on the MongoDB source endpoint.

AuthType -> (string)

The authentication type you use to access the MongoDB source endpoint.

When when set to `"no"` , user name and password parameters are not used and can be empty.

AuthMechanism -> (string)

The authentication mechanism you use to access the MongoDB source endpoint.

For the default value, in MongoDB version 2.x, `"default"` is `"mongodb_cr"` . For MongoDB version 3.x or later, `"default"` is `"scram_sha_1"` . This setting isnât used when `AuthType` is set to `"no"` .

NestingLevel -> (string)

Specifies either document or table mode.

Default value is `"none"` . Specify `"none"` to use document mode. Specify `"one"` to use table mode.

ExtractDocId -> (string)

Specifies the document ID. Use this setting when `NestingLevel` is set to `"none"` .

Default value is `"false"` .

DocsToInvestigate -> (string)

Indicates the number of documents to preview to determine the document organization. Use this setting when `NestingLevel` is set to `"one"` .

Must be a positive value greater than `0` . Default value is `1000` .

AuthSource -> (string)

The MongoDB database name. This setting isnât used when `AuthType` is set to `"no"` .

The default is `"admin"` .

KmsKeyId -> (string)

The KMS key identifier that is used to encrypt the content on the replication instance. If you donât specify a value for the `KmsKeyId` parameter, then DMS uses your default encryption key. KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the MongoDB endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the MongoDB endpoint connection details.

UseUpdateLookUp -> (boolean)

If `true` , DMS retrieves the entire document from the MongoDB source during migration. This may cause a migration failure if the server response exceeds bandwidth limits. To fetch only updates and deletes during migration, set this parameter to `false` .

ReplicateShardCollections -> (boolean)

If `true` , DMS replicates data to shard collections. DMS only uses this setting if the target endpoint is a DocumentDB elastic cluster.

When this setting is `true` , note the following:

- You must set `TargetTablePrepMode` to `nothing` .
- DMS automatically sets `useUpdateLookup` to `false` .

Shorthand Syntax:

```
Username=string,Password=string,ServerName=string,Port=integer,DatabaseName=string,AuthType=string,AuthMechanism=string,NestingLevel=string,ExtractDocId=string,DocsToInvestigate=string,AuthSource=string,KmsKeyId=string,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string,UseUpdateLookUp=boolean,ReplicateShardCollections=boolean
```

JSON Syntax:

```
{
  "Username": "string",
  "Password": "string",
  "ServerName": "string",
  "Port": integer,
  "DatabaseName": "string",
  "AuthType": "no"|"password",
  "AuthMechanism": "default"|"mongodb_cr"|"scram_sha_1",
  "NestingLevel": "none"|"one",
  "ExtractDocId": "string",
  "DocsToInvestigate": "string",
  "AuthSource": "string",
  "KmsKeyId": "string",
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string",
  "UseUpdateLookUp": true|false,
  "ReplicateShardCollections": true|false
}
```

`--kinesis-settings` (structure)

Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about the available settings, see [Using object mapping to migrate data to a Kinesis data stream](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping) in the *Database Migration Service User Guide.*

StreamArn -> (string)

The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

MessageFormat -> (string)

The output format for the records created on the endpoint. The message format is `JSON` (default) or `JSON_UNFORMATTED` (a single line with no tab).

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Kinesis data stream. The role must allow the `iam:PassRole` action.

IncludeTransactionDetails -> (boolean)

Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for `transaction_id` , previous `transaction_id` , and `transaction_record_id` (the record offset within a transaction). The default is `false` .

IncludePartitionValue -> (boolean)

Shows the partition value within the Kinesis message output, unless the partition type is `schema-table-type` . The default is `false` .

PartitionIncludeSchemaTable -> (boolean)

Prefixes schema and table names to partition values, when the partition type is `primary-key-type` . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is `false` .

IncludeTableAlterOperations -> (boolean)

Includes any data definition language (DDL) operations that change the table in the control data, such as `rename-table` , `drop-table` , `add-column` , `drop-column` , and `rename-column` . The default is `false` .

IncludeControlDetails -> (boolean)

Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is `false` .

IncludeNullAndEmpty -> (boolean)

Include NULL and empty columns for records migrated to the endpoint. The default is `false` .

NoHexPrefix -> (boolean)

Set this optional parameter to `true` to avoid adding a â0xâ prefix to raw data in hexadecimal format. For example, by default, DMS adds a â0xâ prefix to the LOB column type in hexadecimal format moving from an Oracle source to an Amazon Kinesis target. Use the `NoHexPrefix` endpoint setting to enable migration of RAW data type columns without adding the â0xâ prefix.

UseLargeIntegerValue -> (boolean)

Specifies using the large integer value with Kinesis.

Shorthand Syntax:

```
StreamArn=string,MessageFormat=string,ServiceAccessRoleArn=string,IncludeTransactionDetails=boolean,IncludePartitionValue=boolean,PartitionIncludeSchemaTable=boolean,IncludeTableAlterOperations=boolean,IncludeControlDetails=boolean,IncludeNullAndEmpty=boolean,NoHexPrefix=boolean,UseLargeIntegerValue=boolean
```

JSON Syntax:

```
{
  "StreamArn": "string",
  "MessageFormat": "json"|"json-unformatted",
  "ServiceAccessRoleArn": "string",
  "IncludeTransactionDetails": true|false,
  "IncludePartitionValue": true|false,
  "PartitionIncludeSchemaTable": true|false,
  "IncludeTableAlterOperations": true|false,
  "IncludeControlDetails": true|false,
  "IncludeNullAndEmpty": true|false,
  "NoHexPrefix": true|false,
  "UseLargeIntegerValue": true|false
}
```

`--kafka-settings` (structure)

Settings in JSON format for the target Apache Kafka endpoint. For more information about the available settings, see [Using object mapping to migrate data to a Kafka topic](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping) in the *Database Migration Service User Guide.*

Broker -> (string)

A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance. Specify each broker location in the form `` *broker-hostname-or-ip* :*port* `` . For example, `"ec2-12-345-678-901.compute-1.amazonaws.com:2345"` . For more information and examples of specifying a list of broker locations, see [Using Apache Kafka as a target for Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html) in the *Database Migration Service User Guide* .

Topic -> (string)

The topic to which you migrate the data. If you donât specify a topic, DMS specifies `"kafka-default-topic"` as the migration topic.

MessageFormat -> (string)

The output format for the records created on the endpoint. The message format is `JSON` (default) or `JSON_UNFORMATTED` (a single line with no tab).

IncludeTransactionDetails -> (boolean)

Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for `transaction_id` , previous `transaction_id` , and `transaction_record_id` (the record offset within a transaction). The default is `false` .

IncludePartitionValue -> (boolean)

Shows the partition value within the Kafka message output unless the partition type is `schema-table-type` . The default is `false` .

PartitionIncludeSchemaTable -> (boolean)

Prefixes schema and table names to partition values, when the partition type is `primary-key-type` . Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is `false` .

IncludeTableAlterOperations -> (boolean)

Includes any data definition language (DDL) operations that change the table in the control data, such as `rename-table` , `drop-table` , `add-column` , `drop-column` , and `rename-column` . The default is `false` .

IncludeControlDetails -> (boolean)

Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output. The default is `false` .

MessageMaxBytes -> (integer)

The maximum size in bytes for records created on the endpoint The default is 1,000,000.

IncludeNullAndEmpty -> (boolean)

Include NULL and empty columns for records migrated to the endpoint. The default is `false` .

SecurityProtocol -> (string)

Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS). Options include `ssl-encryption` , `ssl-authentication` , and `sasl-ssl` . `sasl-ssl` requires `SaslUsername` and `SaslPassword` .

SslClientCertificateArn -> (string)

The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.

SslClientKeyArn -> (string)

The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.

SslClientKeyPassword -> (string)

The password for the client private key used to securely connect to a Kafka target endpoint.

SslCaCertificateArn -> (string)

The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that DMS uses to securely connect to your Kafka target endpoint.

SaslUsername -> (string)

The secure user name you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.

SaslPassword -> (string)

The secure password you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.

NoHexPrefix -> (boolean)

Set this optional parameter to `true` to avoid adding a â0xâ prefix to raw data in hexadecimal format. For example, by default, DMS adds a â0xâ prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the `NoHexPrefix` endpoint setting to enable migration of RAW data type columns without adding the â0xâ prefix.

SaslMechanism -> (string)

For SASL/SSL authentication, DMS supports the `SCRAM-SHA-512` mechanism by default. DMS versions 3.5.0 and later also support the `PLAIN` mechanism. To use the `PLAIN` mechanism, set this parameter to `PLAIN.`

SslEndpointIdentificationAlgorithm -> (string)

Sets hostname verification for the certificate. This setting is supported in DMS version 3.5.1 and later.

UseLargeIntegerValue -> (boolean)

Specifies using the large integer value with Kafka.

Shorthand Syntax:

```
Broker=string,Topic=string,MessageFormat=string,IncludeTransactionDetails=boolean,IncludePartitionValue=boolean,PartitionIncludeSchemaTable=boolean,IncludeTableAlterOperations=boolean,IncludeControlDetails=boolean,MessageMaxBytes=integer,IncludeNullAndEmpty=boolean,SecurityProtocol=string,SslClientCertificateArn=string,SslClientKeyArn=string,SslClientKeyPassword=string,SslCaCertificateArn=string,SaslUsername=string,SaslPassword=string,NoHexPrefix=boolean,SaslMechanism=string,SslEndpointIdentificationAlgorithm=string,UseLargeIntegerValue=boolean
```

JSON Syntax:

```
{
  "Broker": "string",
  "Topic": "string",
  "MessageFormat": "json"|"json-unformatted",
  "IncludeTransactionDetails": true|false,
  "IncludePartitionValue": true|false,
  "PartitionIncludeSchemaTable": true|false,
  "IncludeTableAlterOperations": true|false,
  "IncludeControlDetails": true|false,
  "MessageMaxBytes": integer,
  "IncludeNullAndEmpty": true|false,
  "SecurityProtocol": "plaintext"|"ssl-authentication"|"ssl-encryption"|"sasl-ssl",
  "SslClientCertificateArn": "string",
  "SslClientKeyArn": "string",
  "SslClientKeyPassword": "string",
  "SslCaCertificateArn": "string",
  "SaslUsername": "string",
  "SaslPassword": "string",
  "NoHexPrefix": true|false,
  "SaslMechanism": "scram-sha-512"|"plain",
  "SslEndpointIdentificationAlgorithm": "none"|"https",
  "UseLargeIntegerValue": true|false
}
```

`--elasticsearch-settings` (structure)

Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see [Extra Connection Attributes When Using OpenSearch as a Target for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration) in the *Database Migration Service User Guide* .

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.

EndpointUri -> (string)

The endpoint for the OpenSearch cluster. DMS uses HTTPS if a transport protocol (http/https) is not specified.

FullLoadErrorPercentage -> (integer)

The maximum percentage of records that can fail to be written before a full load operation stops.

To avoid early failure, this counter is only effective after 1000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops.

ErrorRetryDuration -> (integer)

The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.

UseNewMappingType -> (boolean)

Set this option to `true` for DMS to migrate documentation using the documentation type `_doc` . OpenSearch and an Elasticsearch cluster only support the _doc documentation type in versions 7. x and later. The default value is `false` .

Shorthand Syntax:

```
ServiceAccessRoleArn=string,EndpointUri=string,FullLoadErrorPercentage=integer,ErrorRetryDuration=integer,UseNewMappingType=boolean
```

JSON Syntax:

```
{
  "ServiceAccessRoleArn": "string",
  "EndpointUri": "string",
  "FullLoadErrorPercentage": integer,
  "ErrorRetryDuration": integer,
  "UseNewMappingType": true|false
}
```

`--neptune-settings` (structure)

Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see [Specifying graph-mapping rules using Gremlin and R2RML for Amazon Neptune as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings) in the *Database Migration Service User Guide.*

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of the service role that you created for the Neptune target endpoint. The role must allow the `iam:PassRole` action. For more information, see [Creating an IAM Service Role for Accessing Amazon Neptune as a Target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole) in the *Database Migration Service User Guide.*

S3BucketName -> (string)

The name of the Amazon S3 bucket where DMS can temporarily store migrated graph data in .csv files before bulk-loading it to the Neptune target database. DMS maps the SQL source data to graph data before storing it in these .csv files.

S3BucketFolder -> (string)

A folder path where you want DMS to store migrated graph data in the S3 bucket specified by `S3BucketName`

ErrorRetryDuration -> (integer)

The number of milliseconds for DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.

MaxFileSize -> (integer)

The maximum size in kilobytes of migrated graph data stored in a .csv file before DMS bulk-loads the data to the Neptune target database. The default is 1,048,576 KB. If the bulk load is successful, DMS clears the bucket, ready to store the next batch of migrated graph data.

MaxRetryCount -> (integer)

The number of times for DMS to retry a bulk load of migrated graph data to the Neptune target database before raising an error. The default is 5.

IamAuthEnabled -> (boolean)

If you want Identity and Access Management (IAM) authorization enabled for this endpoint, set this parameter to `true` . Then attach the appropriate IAM policy document to your service role specified by `ServiceAccessRoleArn` . The default is `false` .

Shorthand Syntax:

```
ServiceAccessRoleArn=string,S3BucketName=string,S3BucketFolder=string,ErrorRetryDuration=integer,MaxFileSize=integer,MaxRetryCount=integer,IamAuthEnabled=boolean
```

JSON Syntax:

```
{
  "ServiceAccessRoleArn": "string",
  "S3BucketName": "string",
  "S3BucketFolder": "string",
  "ErrorRetryDuration": integer,
  "MaxFileSize": integer,
  "MaxRetryCount": integer,
  "IamAuthEnabled": true|false
}
```

`--redshift-settings` (structure)

Provides information that defines an Amazon Redshift endpoint.

AcceptAnyDate -> (boolean)

A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose `true` or `false` (the default).

This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesnât match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

AfterConnectScript -> (string)

Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.

BucketFolder -> (string)

An S3 folder where the comma-separated-value (.csv) files are stored before being uploaded to the target Redshift cluster.

For full load mode, DMS converts source records into .csv files and loads them to the *BucketFolder/TableID* path. DMS uses the Redshift `COPY` command to upload the .csv files to the target table. The files are deleted once the `COPY` operation has finished. For more information, see [COPY](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html) in the *Amazon Redshift Database Developer Guide* .

For change-data-capture (CDC) mode, DMS creates a *NetChanges* table, and loads the .csv files to this *BucketFolder/NetChangesTableID* path.

BucketName -> (string)

The name of the intermediate S3 bucket used to store .csv files before uploading data to Redshift.

CaseSensitiveNames -> (boolean)

If Amazon Redshift is configured to support case sensitive schema names, set `CaseSensitiveNames` to `true` . The default is `false` .

CompUpdate -> (boolean)

If you set `CompUpdate` to `true` Amazon Redshift applies automatic compression if the table is empty. This applies even if the table columns already have encodings other than `RAW` . If you set `CompUpdate` to `false` , automatic compression is disabled and existing column encodings arenât changed. The default is `true` .

ConnectionTimeout -> (integer)

A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.

DatabaseName -> (string)

The name of the Amazon Redshift data warehouse (service) that you are working with.

DateFormat -> (string)

The date format that you are using. Valid values are `auto` (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of âYYYY-MM-DDâ. Using `auto` recognizes most strings, even some that arenât supported when you use a date format string.

If your date and time values use formats different from each other, set this to `auto` .

EmptyAsNull -> (boolean)

A value that specifies whether DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of `true` sets empty CHAR and VARCHAR fields to null. The default is `false` .

EncryptionMode -> (string)

The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either `SSE_S3` (the default) or `SSE_KMS` .

### Note

For the `ModifyEndpoint` operation, you can change the existing value of the `EncryptionMode` parameter from `SSE_KMS` to `SSE_S3` . But you canât change the existing value from `SSE_S3` to `SSE_KMS` .

To use `SSE_S3` , create an Identity and Access Management (IAM) role with a policy that allows `"arn:aws:s3:::*"` to use the following actions: `"s3:PutObject", "s3:ListBucket"`

ExplicitIds -> (boolean)

This setting is only valid for a full-load migration task. Set `ExplicitIds` to `true` to have tables with `IDENTITY` columns override their auto-generated values with explicit values loaded from the source data files used to populate the tables. The default is `false` .

FileTransferUploadStreams -> (integer)

The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.

The number of parallel streams used to upload a single .csv file to an S3 bucket using S3 Multipart Upload. For more information, see [Multipart upload overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html) .

`FileTransferUploadStreams` accepts a value from 1 through 64. It defaults to 10.

LoadTimeout -> (integer)

The amount of time to wait (in milliseconds) before timing out of operations performed by DMS on a Redshift cluster, such as Redshift COPY, INSERT, DELETE, and UPDATE.

MaxFileSize -> (integer)

The maximum size (in KB) of any .csv file used to load data on an S3 bucket and transfer data to Amazon Redshift. It defaults to 1048576KB (1 GB).

Password -> (string)

The password for the user named in the `username` property.

Port -> (integer)

The port number for Amazon Redshift. The default value is 5439.

RemoveQuotes -> (boolean)

A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose `true` to remove quotation marks. The default is `false` .

ReplaceInvalidChars -> (string)

A list of characters that you want to replace. Use with `ReplaceChars` .

ReplaceChars -> (string)

A value that specifies to replaces the invalid characters specified in `ReplaceInvalidChars` , substituting the specified characters instead. The default is `"?"` .

ServerName -> (string)

The name of the Amazon Redshift cluster you are using.

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service. The role must allow the `iam:PassRole` action.

ServerSideEncryptionKmsKeyId -> (string)

The KMS key ID. If you are using `SSE_KMS` for the `EncryptionMode` , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

TimeFormat -> (string)

The time format that you want to use. Valid values are `auto` (case-sensitive), `'timeformat_string'` , `'epochsecs'` , or `'epochmillisecs'` . It defaults to 10. Using `auto` recognizes most strings, even some that arenât supported when you use a time format string.

If your date and time values use formats different from each other, set this parameter to `auto` .

TrimBlanks -> (boolean)

A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose `true` to remove unneeded white space. The default is `false` .

TruncateColumns -> (boolean)

A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose `true` to truncate data. The default is `false` .

Username -> (string)

An Amazon Redshift user name for a registered user.

WriteBufferSize -> (integer)

The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk at the DMS replication instance. The default value is 1000 (buffer size is 1000KB).

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the Amazon Redshift endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Amazon Redshift endpoint connection details.

MapBooleanAsBoolean -> (boolean)

When true, lets Redshift migrate the boolean type as boolean. By default, Redshift migrates booleans as `varchar(1)` . You must set this setting on both the source and target endpoints for it to take effect.

Shorthand Syntax:

```
AcceptAnyDate=boolean,AfterConnectScript=string,BucketFolder=string,BucketName=string,CaseSensitiveNames=boolean,CompUpdate=boolean,ConnectionTimeout=integer,DatabaseName=string,DateFormat=string,EmptyAsNull=boolean,EncryptionMode=string,ExplicitIds=boolean,FileTransferUploadStreams=integer,LoadTimeout=integer,MaxFileSize=integer,Password=string,Port=integer,RemoveQuotes=boolean,ReplaceInvalidChars=string,ReplaceChars=string,ServerName=string,ServiceAccessRoleArn=string,ServerSideEncryptionKmsKeyId=string,TimeFormat=string,TrimBlanks=boolean,TruncateColumns=boolean,Username=string,WriteBufferSize=integer,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string,MapBooleanAsBoolean=boolean
```

JSON Syntax:

```
{
  "AcceptAnyDate": true|false,
  "AfterConnectScript": "string",
  "BucketFolder": "string",
  "BucketName": "string",
  "CaseSensitiveNames": true|false,
  "CompUpdate": true|false,
  "ConnectionTimeout": integer,
  "DatabaseName": "string",
  "DateFormat": "string",
  "EmptyAsNull": true|false,
  "EncryptionMode": "sse-s3"|"sse-kms",
  "ExplicitIds": true|false,
  "FileTransferUploadStreams": integer,
  "LoadTimeout": integer,
  "MaxFileSize": integer,
  "Password": "string",
  "Port": integer,
  "RemoveQuotes": true|false,
  "ReplaceInvalidChars": "string",
  "ReplaceChars": "string",
  "ServerName": "string",
  "ServiceAccessRoleArn": "string",
  "ServerSideEncryptionKmsKeyId": "string",
  "TimeFormat": "string",
  "TrimBlanks": true|false,
  "TruncateColumns": true|false,
  "Username": "string",
  "WriteBufferSize": integer,
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string",
  "MapBooleanAsBoolean": true|false
}
```

`--postgre-sql-settings` (structure)

Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see [Extra connection attributes when using PostgreSQL as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib) and [Extra connection attributes when using PostgreSQL as a target for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib) in the *Database Migration Service User Guide.*

AfterConnectScript -> (string)

For use with change data capture (CDC) only, this attribute has DMS bypass foreign keys and user triggers to reduce the time it takes to bulk load data.

Example: `afterConnectScript=SET session_replication_role='replica'`

CaptureDdls -> (boolean)

To capture DDL events, DMS creates various artifacts in the PostgreSQL database when the task starts. You can later remove these artifacts.

The default value is `true` .

If this value is set to `N` , you donât have to create tables or triggers on the source database.

MaxFileSize -> (integer)

Specifies the maximum size (in KB) of any .csv file used to transfer data to PostgreSQL.

The default value is 32,768 KB (32 MB).

Example: `maxFileSize=512`

DatabaseName -> (string)

Database name for the endpoint.

DdlArtifactsSchema -> (string)

The schema in which the operational DDL database artifacts are created.

The default value is `public` .

Example: `ddlArtifactsSchema=xyzddlschema;`

ExecuteTimeout -> (integer)

Sets the client statement timeout for the PostgreSQL instance, in seconds. The default value is 60 seconds.

Example: `executeTimeout=100;`

FailTasksOnLobTruncation -> (boolean)

When set to `true` , this value causes a task to fail if the actual size of a LOB column is greater than the specified `LobMaxSize` .

The default value is `false` .

If task is set to Limited LOB mode and this option is set to true, the task fails instead of truncating the LOB data.

HeartbeatEnable -> (boolean)

The write-ahead log (WAL) heartbeat feature mimics a dummy transaction. By doing this, it prevents idle logical replication slots from holding onto old WAL logs, which can result in storage full situations on the source. This heartbeat keeps `restart_lsn` moving and prevents storage full scenarios.

The default value is `false` .

HeartbeatSchema -> (string)

Sets the schema in which the heartbeat artifacts are created.

The default value is `public` .

HeartbeatFrequency -> (integer)

Sets the WAL heartbeat frequency (in minutes).

The default value is 5 minutes.

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port. The default is 5432.

ServerName -> (string)

The host name of the endpoint database.

For an Amazon RDS PostgreSQL instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) , in the `` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

For an Aurora PostgreSQL instance, this is the output of [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) , in the `Endpoint` field.

Username -> (string)

Endpoint connection user name.

SlotName -> (string)

Sets the name of a previously created logical replication slot for a change data capture (CDC) load of the PostgreSQL source instance.

When used with the `CdcStartPosition` request parameter for the DMS API , this attribute also makes it possible to use native CDC start points. DMS verifies that the specified logical replication slot exists before starting the CDC load task. It also verifies that the task was created with a valid setting of `CdcStartPosition` . If the specified slot doesnât exist or the task doesnât have a valid `CdcStartPosition` setting, DMS raises an error.

For more information about setting the `CdcStartPosition` request parameter, see [Determining a CDC native start point](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native) in the *Database Migration Service User Guide* . For more information about using `CdcStartPosition` , see [CreateReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html) , [StartReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html) , and [ModifyReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html) .

PluginName -> (string)

Specifies the plugin to use to create a replication slot.

The default value is `pglogical` .

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the PostgreSQL endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the PostgreSQL endpoint connection details.

TrimSpaceInChar -> (boolean)

Use the `TrimSpaceInChar` source endpoint setting to trim data on CHAR and NCHAR data types during migration. The default value is `true` .

MapBooleanAsBoolean -> (boolean)

When true, lets PostgreSQL migrate the boolean type as boolean. By default, PostgreSQL migrates booleans as `varchar(5)` . You must set this setting on both the source and target endpoints for it to take effect.

The default value is `false` .

MapJsonbAsClob -> (boolean)

When true, DMS migrates JSONB values as CLOB.

The default value is `false` .

MapLongVarcharAs -> (string)

Sets what datatype to map LONG values as.

The default value is `wstring` .

DatabaseMode -> (string)

Specifies the default behavior of the replicationâs handling of PostgreSQL- compatible endpoints that require some additional configuration, such as Babelfish endpoints.

BabelfishDatabaseName -> (string)

The Babelfish for Aurora PostgreSQL database name for the endpoint.

DisableUnicodeSourceFilter -> (boolean)

Disables the Unicode source filter with PostgreSQL, for values passed into the Selection rule filter on Source Endpoint column values. By default DMS performs source filter comparisons using a Unicode string which can cause look ups to ignore the indexes in the text columns and slow down migrations.

Unicode support should only be disabled when using a selection rule filter is on a text column in the Source database that is indexed.

ServiceAccessRoleArn -> (string)

The IAM role arn you can use to authenticate the connection to your endpoint. Ensure to include `iam:PassRole` and `rds-db:connect` actions in permission policy.

AuthenticationMethod -> (string)

This attribute allows you to specify the authentication method as âiam authâ.

Shorthand Syntax:

```
AfterConnectScript=string,CaptureDdls=boolean,MaxFileSize=integer,DatabaseName=string,DdlArtifactsSchema=string,ExecuteTimeout=integer,FailTasksOnLobTruncation=boolean,HeartbeatEnable=boolean,HeartbeatSchema=string,HeartbeatFrequency=integer,Password=string,Port=integer,ServerName=string,Username=string,SlotName=string,PluginName=string,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string,TrimSpaceInChar=boolean,MapBooleanAsBoolean=boolean,MapJsonbAsClob=boolean,MapLongVarcharAs=string,DatabaseMode=string,BabelfishDatabaseName=string,DisableUnicodeSourceFilter=boolean,ServiceAccessRoleArn=string,AuthenticationMethod=string
```

JSON Syntax:

```
{
  "AfterConnectScript": "string",
  "CaptureDdls": true|false,
  "MaxFileSize": integer,
  "DatabaseName": "string",
  "DdlArtifactsSchema": "string",
  "ExecuteTimeout": integer,
  "FailTasksOnLobTruncation": true|false,
  "HeartbeatEnable": true|false,
  "HeartbeatSchema": "string",
  "HeartbeatFrequency": integer,
  "Password": "string",
  "Port": integer,
  "ServerName": "string",
  "Username": "string",
  "SlotName": "string",
  "PluginName": "no-preference"|"test-decoding"|"pglogical",
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string",
  "TrimSpaceInChar": true|false,
  "MapBooleanAsBoolean": true|false,
  "MapJsonbAsClob": true|false,
  "MapLongVarcharAs": "wstring"|"clob"|"nclob",
  "DatabaseMode": "default"|"babelfish",
  "BabelfishDatabaseName": "string",
  "DisableUnicodeSourceFilter": true|false,
  "ServiceAccessRoleArn": "string",
  "AuthenticationMethod": "password"|"iam"
}
```

`--my-sql-settings` (structure)

Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see [Extra connection attributes when using MySQL as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib) and [Extra connection attributes when using a MySQL-compatible database as a target for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib) in the *Database Migration Service User Guide.*

AfterConnectScript -> (string)

Specifies a script to run immediately after DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails.

For this parameter, provide the code of the script itself, not the name of a file containing the script.

CleanSourceMetadataOnMismatch -> (boolean)

Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.

DatabaseName -> (string)

Database name for the endpoint. For a MySQL source or target endpoint, donât explicitly specify the database using the `DatabaseName` request parameter on either the `CreateEndpoint` or `ModifyEndpoint` API call. Specifying `DatabaseName` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the DMS task.

EventsPollInterval -> (integer)

Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds.

Example: `eventsPollInterval=5;`

In the example, DMS checks for changes in the binary logs every five seconds.

TargetDbType -> (string)

Specifies where to migrate source tables on the target, either to a single database or multiple databases. If you specify `SPECIFIC_DATABASE` , specify the database name using the `DatabaseName` parameter of the `Endpoint` object.

Example: `targetDbType=MULTIPLE_DATABASES`

MaxFileSize -> (integer)

Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.

Example: `maxFileSize=512`

ParallelLoadThreads -> (integer)

Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.

Example: `parallelLoadThreads=1`

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port.

ServerName -> (string)

The host name of the endpoint database.

For an Amazon RDS MySQL instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) , in the `` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

For an Aurora MySQL instance, this is the output of [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) , in the `Endpoint` field.

ServerTimezone -> (string)

Specifies the time zone for the source MySQL database.

Example: `serverTimezone=US/Pacific;`

Note: Do not enclose time zones in single quotes.

Username -> (string)

Endpoint connection user name.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the MySQL endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the MySQL endpoint connection details.

ExecuteTimeout -> (integer)

Sets the client statement timeout (in seconds) for a MySQL source endpoint.

ServiceAccessRoleArn -> (string)

The IAM role you can use to authenticate when connecting to your endpoint. Ensure to include `iam:PassRole` and `rds-db:connect` actions in permission policy.

AuthenticationMethod -> (string)

This attribute allows you to specify the authentication method as âiam authâ.

Shorthand Syntax:

```
AfterConnectScript=string,CleanSourceMetadataOnMismatch=boolean,DatabaseName=string,EventsPollInterval=integer,TargetDbType=string,MaxFileSize=integer,ParallelLoadThreads=integer,Password=string,Port=integer,ServerName=string,ServerTimezone=string,Username=string,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string,ExecuteTimeout=integer,ServiceAccessRoleArn=string,AuthenticationMethod=string
```

JSON Syntax:

```
{
  "AfterConnectScript": "string",
  "CleanSourceMetadataOnMismatch": true|false,
  "DatabaseName": "string",
  "EventsPollInterval": integer,
  "TargetDbType": "specific-database"|"multiple-databases",
  "MaxFileSize": integer,
  "ParallelLoadThreads": integer,
  "Password": "string",
  "Port": integer,
  "ServerName": "string",
  "ServerTimezone": "string",
  "Username": "string",
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string",
  "ExecuteTimeout": integer,
  "ServiceAccessRoleArn": "string",
  "AuthenticationMethod": "password"|"iam"
}
```

`--oracle-settings` (structure)

Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see [Extra connection attributes when using Oracle as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib) and [Extra connection attributes when using Oracle as a target for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib) in the *Database Migration Service User Guide.*

AddSupplementalLogging -> (boolean)

Set this attribute to set up table-level supplemental logging for the Oracle database. This attribute enables PRIMARY KEY supplemental logging on all tables selected for a migration task.

If you use this option, you still need to enable database-level supplemental logging.

ArchivedLogDestId -> (integer)

Specifies the ID of the destination for the archived redo logs. This value should be the same as a number in the dest_id column of the v$archived_log view. If you work with an additional redo log destination, use the `AdditionalArchivedLogDestId` option to specify the additional destination ID. Doing this improves performance by ensuring that the correct logs are accessed from the outset.

AdditionalArchivedLogDestId -> (integer)

Set this attribute with `ArchivedLogDestId` in a primary/ standby setup. This attribute is useful in the case of a switchover. In this case, DMS needs to know which destination to get archive redo logs from to read changes. This need arises because the previous primary instance is now a standby instance after switchover.

Although DMS supports the use of the Oracle `RESETLOGS` option to open the database, never use `RESETLOGS` unless necessary. For additional information about `RESETLOGS` , see [RMAN Data Repair Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B) in the *Oracle Database Backup and Recovery Userâs Guide* .

ExtraArchivedLogDestIds -> (list)

Specifies the IDs of one more destinations for one or more archived redo logs. These IDs are the values of the `dest_id` column in the `v$archived_log` view. Use this setting with the `archivedLogDestId` extra connection attribute in a primary-to-single setup or a primary-to-multiple-standby setup.

This setting is useful in a switchover when you use an Oracle Data Guard database as a source. In this case, DMS needs information about what destination to get archive redo logs from to read changes. DMS needs this because after the switchover the previous primary is a standby instance. For example, in a primary-to-single standby setup you might apply the following settings.

`archivedLogDestId=1; ExtraArchivedLogDestIds=[2]`

In a primary-to-multiple-standby setup, you might apply the following settings.

`archivedLogDestId=1; ExtraArchivedLogDestIds=[2,3,4]`

Although DMS supports the use of the Oracle `RESETLOGS` option to open the database, never use `RESETLOGS` unless itâs necessary. For more information about `RESETLOGS` , see [RMAN Data Repair Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B) in the *Oracle Database Backup and Recovery Userâs Guide* .

(integer)

AllowSelectNestedTables -> (boolean)

Set this attribute to `true` to enable replication of Oracle tables containing columns that are nested tables or defined types.

ParallelAsmReadThreads -> (integer)

Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 2 (the default) and 8 (the maximum). Use this attribute together with the `readAheadBlocks` attribute.

ReadAheadBlocks -> (integer)

Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 1000 (the default) and 200,000 (the maximum).

AccessAlternateDirectly -> (boolean)

Set this attribute to `false` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to not access redo logs through any specified path prefix replacement using direct file access.

UseAlternateFolderForOnline -> (boolean)

Set this attribute to `true` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to use any specified prefix replacement to access all online redo logs.

OraclePathPrefix -> (string)

Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the default Oracle root used to access the redo logs.

UsePathPrefix -> (string)

Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the path prefix used to replace the default Oracle root to access the redo logs.

ReplacePathPrefix -> (boolean)

Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This setting tells DMS instance to replace the default Oracle root with the specified `usePathPrefix` setting to access the redo logs.

EnableHomogenousTablespace -> (boolean)

Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target.

DirectPathNoLog -> (boolean)

When set to `true` , this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs.

ArchivedLogsOnly -> (boolean)

When this field is set to `True` , DMS only accesses the archived redo logs. If the archived redo logs are stored on Automatic Storage Management (ASM) only, the DMS user account needs to be granted ASM privileges.

AsmPassword -> (string)

For an Oracle source endpoint, your Oracle Automatic Storage Management (ASM) password. You can set this value from the `` *asm_user_password* `` value. You set this value as part of the comma-separated value that you set to the `Password` request parameter when you create the endpoint to access transaction logs using Binary Reader. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration) .

AsmServer -> (string)

For an Oracle source endpoint, your ASM server address. You can set this value from the `asm_server` value. You set `asm_server` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration) .

AsmUser -> (string)

For an Oracle source endpoint, your ASM user name. You can set this value from the `asm_user` value. You set `asm_user` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration) .

CharLengthSemantics -> (string)

Specifies whether the length of a character column is in bytes or in characters. To indicate that the character column length is in characters, set this attribute to `CHAR` . Otherwise, the character column length is in bytes.

Example: `charLengthSemantics=CHAR;`

DatabaseName -> (string)

Database name for the endpoint.

DirectPathParallelLoad -> (boolean)

When set to `true` , this attribute specifies a parallel load when `useDirectPathFullLoad` is set to `Y` . This attribute also only applies when you use the DMS parallel load feature. Note that the target table cannot have any constraints or indexes.

FailTasksOnLobTruncation -> (boolean)

When set to `true` , this attribute causes a task to fail if the actual size of an LOB column is greater than the specified `LobMaxSize` .

If a task is set to limited LOB mode and this option is set to `true` , the task fails instead of truncating the LOB data.

NumberDatatypeScale -> (integer)

Specifies the number scale. You can select a scale up to 38, or you can select FLOAT. By default, the NUMBER data type is converted to precision 38, scale 10.

Example: `numberDataTypeScale=12`

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port.

ReadTableSpaceName -> (boolean)

When set to `true` , this attribute supports tablespace replication.

RetryInterval -> (integer)

Specifies the number of seconds that the system waits before resending a query.

Example: `retryInterval=6;`

SecurityDbEncryption -> (string)

For an Oracle source endpoint, the transparent data encryption (TDE) password required by AWM DMS to access Oracle redo logs encrypted by TDE using Binary Reader. It is also the `` *TDE_Password* `` part of the comma-separated value you set to the `Password` request parameter when you create the endpoint. The `SecurityDbEncryptian` setting is related to this `SecurityDbEncryptionName` setting. For more information, see [Supported encryption methods for using Oracle as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption) in the *Database Migration Service User Guide* .

SecurityDbEncryptionName -> (string)

For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE. The key value is the value of the `SecurityDbEncryption` setting. For more information on setting the key name value of `SecurityDbEncryptionName` , see the information and example for setting the `securityDbEncryptionName` extra connection attribute in [Supported encryption methods for using Oracle as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption) in the *Database Migration Service User Guide* .

ServerName -> (string)

Fully qualified domain name of the endpoint.

For an Amazon RDS Oracle instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) , in the `` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

SpatialDataOptionToGeoJsonFunctionName -> (string)

Use this attribute to convert `SDO_GEOMETRY` to `GEOJSON` format. By default, DMS calls the `SDO2GEOJSON` custom function if present and accessible. Or you can create your own custom function that mimics the operation of `SDOGEOJSON` and set `SpatialDataOptionToGeoJsonFunctionName` to call it instead.

StandbyDelayTime -> (integer)

Use this attribute to specify a time in minutes for the delay in standby sync. If the source is an Oracle Active Data Guard standby database, use this attribute to specify the time lag between primary and standby databases.

In DMS, you can create an Oracle CDC task that uses an Active Data Guard standby instance as a source for replicating ongoing changes. Doing this eliminates the need to connect to an active database that might be in production.

Username -> (string)

Endpoint connection user name.

UseBFile -> (boolean)

Set this attribute to True to capture change data using the Binary Reader utility. Set `UseLogminerReader` to False to set this attribute to True. To use Binary Reader with Amazon RDS for Oracle as the source, you set additional attributes. For more information about using this setting with Oracle Automatic Storage Management (ASM), see [Using Oracle LogMiner or DMS Binary Reader for CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC) .

UseDirectPathFullLoad -> (boolean)

Set this attribute to True to have DMS use a direct path full load. Specify this value to use the direct path protocol in the Oracle Call Interface (OCI). By using this OCI protocol, you can bulk-load Oracle target tables during a full load.

UseLogminerReader -> (boolean)

Set this attribute to True to capture change data using the Oracle LogMiner utility (the default). Set this attribute to False if you want to access the redo logs as a binary file. When you set `UseLogminerReader` to False, also set `UseBfile` to True. For more information on this setting and using Oracle ASM, see [Using Oracle LogMiner or DMS Binary Reader for CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC) in the *DMS User Guide* .

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the Oracle endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Oracle endpoint connection details.

SecretsManagerOracleAsmAccessRoleArn -> (string)

Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the `SecretsManagerOracleAsmSecret` . This `SecretsManagerOracleAsmSecret` has the secret value that allows access to the Oracle ASM of the endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerOracleAsmSecretId` . Or you can specify clear-text values for `AsmUser` , `AsmPassword` , and `AsmServerName` . You canât specify both. For more information on creating this `SecretsManagerOracleAsmSecret` and the `SecretsManagerOracleAsmAccessRoleArn` and `SecretsManagerOracleAsmSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerOracleAsmSecretId -> (string)

Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the `SecretsManagerOracleAsmSecret` that contains the Oracle ASM connection details for the Oracle endpoint.

TrimSpaceInChar -> (boolean)

Use the `TrimSpaceInChar` source endpoint setting to trim data on CHAR and NCHAR data types during migration. The default value is `true` .

ConvertTimestampWithZoneToUTC -> (boolean)

When true, converts timestamps with the `timezone` datatype to their UTC value.

OpenTransactionWindow -> (integer)

The timeframe in minutes to check for open transactions for a CDC-only task.

You can specify an integer value between 0 (the default) and 240 (the maximum).

### Note

This parameter is only valid in DMS version 3.5.0 and later.

AuthenticationMethod -> (string)

Specifies the authentication method to be used with Oracle.

Shorthand Syntax:

```
AddSupplementalLogging=boolean,ArchivedLogDestId=integer,AdditionalArchivedLogDestId=integer,ExtraArchivedLogDestIds=integer,integer,AllowSelectNestedTables=boolean,ParallelAsmReadThreads=integer,ReadAheadBlocks=integer,AccessAlternateDirectly=boolean,UseAlternateFolderForOnline=boolean,OraclePathPrefix=string,UsePathPrefix=string,ReplacePathPrefix=boolean,EnableHomogenousTablespace=boolean,DirectPathNoLog=boolean,ArchivedLogsOnly=boolean,AsmPassword=string,AsmServer=string,AsmUser=string,CharLengthSemantics=string,DatabaseName=string,DirectPathParallelLoad=boolean,FailTasksOnLobTruncation=boolean,NumberDatatypeScale=integer,Password=string,Port=integer,ReadTableSpaceName=boolean,RetryInterval=integer,SecurityDbEncryption=string,SecurityDbEncryptionName=string,ServerName=string,SpatialDataOptionToGeoJsonFunctionName=string,StandbyDelayTime=integer,Username=string,UseBFile=boolean,UseDirectPathFullLoad=boolean,UseLogminerReader=boolean,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string,SecretsManagerOracleAsmAccessRoleArn=string,SecretsManagerOracleAsmSecretId=string,TrimSpaceInChar=boolean,ConvertTimestampWithZoneToUTC=boolean,OpenTransactionWindow=integer,AuthenticationMethod=string
```

JSON Syntax:

```
{
  "AddSupplementalLogging": true|false,
  "ArchivedLogDestId": integer,
  "AdditionalArchivedLogDestId": integer,
  "ExtraArchivedLogDestIds": [integer, ...],
  "AllowSelectNestedTables": true|false,
  "ParallelAsmReadThreads": integer,
  "ReadAheadBlocks": integer,
  "AccessAlternateDirectly": true|false,
  "UseAlternateFolderForOnline": true|false,
  "OraclePathPrefix": "string",
  "UsePathPrefix": "string",
  "ReplacePathPrefix": true|false,
  "EnableHomogenousTablespace": true|false,
  "DirectPathNoLog": true|false,
  "ArchivedLogsOnly": true|false,
  "AsmPassword": "string",
  "AsmServer": "string",
  "AsmUser": "string",
  "CharLengthSemantics": "default"|"char"|"byte",
  "DatabaseName": "string",
  "DirectPathParallelLoad": true|false,
  "FailTasksOnLobTruncation": true|false,
  "NumberDatatypeScale": integer,
  "Password": "string",
  "Port": integer,
  "ReadTableSpaceName": true|false,
  "RetryInterval": integer,
  "SecurityDbEncryption": "string",
  "SecurityDbEncryptionName": "string",
  "ServerName": "string",
  "SpatialDataOptionToGeoJsonFunctionName": "string",
  "StandbyDelayTime": integer,
  "Username": "string",
  "UseBFile": true|false,
  "UseDirectPathFullLoad": true|false,
  "UseLogminerReader": true|false,
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string",
  "SecretsManagerOracleAsmAccessRoleArn": "string",
  "SecretsManagerOracleAsmSecretId": "string",
  "TrimSpaceInChar": true|false,
  "ConvertTimestampWithZoneToUTC": true|false,
  "OpenTransactionWindow": integer,
  "AuthenticationMethod": "password"|"kerberos"
}
```

`--sybase-settings` (structure)

Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see [Extra connection attributes when using SAP ASE as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib) and [Extra connection attributes when using SAP ASE as a target for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib) in the *Database Migration Service User Guide.*

DatabaseName -> (string)

Database name for the endpoint.

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port. The default is 5000.

ServerName -> (string)

Fully qualified domain name of the endpoint.

Username -> (string)

Endpoint connection user name.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the SAP ASE endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the SAP SAE endpoint connection details.

Shorthand Syntax:

```
DatabaseName=string,Password=string,Port=integer,ServerName=string,Username=string,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string
```

JSON Syntax:

```
{
  "DatabaseName": "string",
  "Password": "string",
  "Port": integer,
  "ServerName": "string",
  "Username": "string",
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string"
}
```

`--microsoft-sql-server-settings` (structure)

Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see [Extra connection attributes when using SQL Server as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib) and [Extra connection attributes when using SQL Server as a target for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib) in the *Database Migration Service User Guide.*

Port -> (integer)

Endpoint TCP port.

BcpPacketSize -> (integer)

The maximum size of the packets (in bytes) used to transfer data using BCP.

DatabaseName -> (string)

Database name for the endpoint.

ControlTablesFileGroup -> (string)

Specifies a file group for the DMS internal tables. When the replication task starts, all the internal DMS control tables ([awsdms_](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html#id5) apply_exception, awsdms_apply, awsdms_changes) are created for the specified file group.

Password -> (string)

Endpoint connection password.

QuerySingleAlwaysOnNode -> (boolean)

Cleans and recreates table metadata information on the replication instance when a mismatch occurs. An example is a situation where running an alter DDL statement on a table might result in different information about the table cached in the replication instance.

ReadBackupOnly -> (boolean)

When this attribute is set to `Y` , DMS only reads changes from transaction log backups and doesnât read from the active transaction log file during ongoing replication. Setting this parameter to `Y` enables you to control active transaction log file growth during full load and ongoing replication tasks. However, it can add some source latency to ongoing replication.

SafeguardPolicy -> (string)

Use this attribute to minimize the need to access the backup log and enable DMS to prevent truncation using one of the following two methods.

*Start transactions in the database:* This is the default method. When this method is used, DMS prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started arenât truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method.

*Exclusively use sp_repldone within a single task* : When this method is used, DMS reads the changes and then uses sp_repldone to mark the TLOG transactions as ready for truncation. Although this method doesnât involve any transactional activities, it can only be used when Microsoft Replication isnât running. Also, when using this method, only one DMS task can access the database at any given time. Therefore, if you need to run parallel DMS tasks against the same database, use the default method.

ServerName -> (string)

Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) , in the `` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

Username -> (string)

Endpoint connection user name.

UseBcpFullLoad -> (boolean)

Use this to attribute to transfer data for full-load operations using BCP. When the target table contains an identity column that does not exist in the source table, you must disable the use BCP for loading table option.

UseThirdPartyBackupDevice -> (boolean)

When this attribute is set to `Y` , DMS processes third-party transaction log backups if they are created in native format.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the SQL Server endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the SQL Server endpoint connection details.

TrimSpaceInChar -> (boolean)

Use the `TrimSpaceInChar` source endpoint setting to right-trim data on CHAR and NCHAR data types during migration. Setting `TrimSpaceInChar` does not left-trim data. The default value is `true` .

TlogAccessMode -> (string)

Indicates the mode used to fetch CDC data.

ForceLobLookup -> (boolean)

Forces LOB lookup on inline LOB.

AuthenticationMethod -> (string)

Specifies the authentication method to be used with Microsoft SQL Server.

Shorthand Syntax:

```
Port=integer,BcpPacketSize=integer,DatabaseName=string,ControlTablesFileGroup=string,Password=string,QuerySingleAlwaysOnNode=boolean,ReadBackupOnly=boolean,SafeguardPolicy=string,ServerName=string,Username=string,UseBcpFullLoad=boolean,UseThirdPartyBackupDevice=boolean,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string,TrimSpaceInChar=boolean,TlogAccessMode=string,ForceLobLookup=boolean,AuthenticationMethod=string
```

JSON Syntax:

```
{
  "Port": integer,
  "BcpPacketSize": integer,
  "DatabaseName": "string",
  "ControlTablesFileGroup": "string",
  "Password": "string",
  "QuerySingleAlwaysOnNode": true|false,
  "ReadBackupOnly": true|false,
  "SafeguardPolicy": "rely-on-sql-server-replication-agent"|"exclusive-automatic-truncation"|"shared-automatic-truncation",
  "ServerName": "string",
  "Username": "string",
  "UseBcpFullLoad": true|false,
  "UseThirdPartyBackupDevice": true|false,
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string",
  "TrimSpaceInChar": true|false,
  "TlogAccessMode": "BackupOnly"|"PreferBackup"|"PreferTlog"|"TlogOnly",
  "ForceLobLookup": true|false,
  "AuthenticationMethod": "password"|"kerberos"
}
```

`--ibm-db2-settings` (structure)

Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see [Extra connection attributes when using Db2 LUW as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib) in the *Database Migration Service User Guide.*

DatabaseName -> (string)

Database name for the endpoint.

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port. The default value is 50000.

ServerName -> (string)

Fully qualified domain name of the endpoint.

SetDataCaptureChanges -> (boolean)

Enables ongoing replication (CDC) as a BOOLEAN value. The default is true.

CurrentLsn -> (string)

For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.

MaxKBytesPerRead -> (integer)

Maximum number of bytes per read, as a NUMBER value. The default is 64 KB.

Username -> (string)

Endpoint connection user name.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the Db2 LUW endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Db2 LUW endpoint connection details.

LoadTimeout -> (integer)

The amount of time (in milliseconds) before DMS times out operations performed by DMS on the Db2 target. The default value is 1200 (20 minutes).

WriteBufferSize -> (integer)

The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk on the DMS replication instance. The default value is 1024 (1 MB).

MaxFileSize -> (integer)

Specifies the maximum size (in KB) of .csv files used to transfer data to Db2 LUW.

KeepCsvFiles -> (boolean)

If true, DMS saves any .csv files to the Db2 LUW target that were used to replicate data. DMS uses these files for analysis and troubleshooting.

The default value is false.

Shorthand Syntax:

```
DatabaseName=string,Password=string,Port=integer,ServerName=string,SetDataCaptureChanges=boolean,CurrentLsn=string,MaxKBytesPerRead=integer,Username=string,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string,LoadTimeout=integer,WriteBufferSize=integer,MaxFileSize=integer,KeepCsvFiles=boolean
```

JSON Syntax:

```
{
  "DatabaseName": "string",
  "Password": "string",
  "Port": integer,
  "ServerName": "string",
  "SetDataCaptureChanges": true|false,
  "CurrentLsn": "string",
  "MaxKBytesPerRead": integer,
  "Username": "string",
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string",
  "LoadTimeout": integer,
  "WriteBufferSize": integer,
  "MaxFileSize": integer,
  "KeepCsvFiles": true|false
}
```

`--resource-identifier` (string)

A friendly name for the resource identifier at the end of the `EndpointArn` response parameter that is returned in the created `Endpoint` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen (â-â). Also, it canât end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as `Example-App-ARN1` . For example, this value might result in the `EndpointArn` value `arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1` . If you donât specify a `ResourceIdentifier` value, DMS generates a default identifier value for the end of `EndpointArn` .

`--doc-db-settings` (structure)

Provides information that defines a DocumentDB endpoint.

Username -> (string)

The user name you use to access the DocumentDB source endpoint.

Password -> (string)

The password for the user account you use to access the DocumentDB source endpoint.

ServerName -> (string)

The name of the server on the DocumentDB source endpoint.

Port -> (integer)

The port value for the DocumentDB source endpoint.

DatabaseName -> (string)

The database name on the DocumentDB source endpoint.

NestingLevel -> (string)

Specifies either document or table mode.

Default value is `"none"` . Specify `"none"` to use document mode. Specify `"one"` to use table mode.

ExtractDocId -> (boolean)

Specifies the document ID. Use this setting when `NestingLevel` is set to `"none"` .

Default value is `"false"` .

DocsToInvestigate -> (integer)

Indicates the number of documents to preview to determine the document organization. Use this setting when `NestingLevel` is set to `"one"` .

Must be a positive value greater than `0` . Default value is `1000` .

KmsKeyId -> (string)

The KMS key identifier that is used to encrypt the content on the replication instance. If you donât specify a value for the `KmsKeyId` parameter, then DMS uses your default encryption key. KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the DocumentDB endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the DocumentDB endpoint connection details.

UseUpdateLookUp -> (boolean)

If `true` , DMS retrieves the entire document from the DocumentDB source during migration. This may cause a migration failure if the server response exceeds bandwidth limits. To fetch only updates and deletes during migration, set this parameter to `false` .

ReplicateShardCollections -> (boolean)

If `true` , DMS replicates data to shard collections. DMS only uses this setting if the target endpoint is a DocumentDB elastic cluster.

When this setting is `true` , note the following:

- You must set `TargetTablePrepMode` to `nothing` .
- DMS automatically sets `useUpdateLookup` to `false` .

Shorthand Syntax:

```
Username=string,Password=string,ServerName=string,Port=integer,DatabaseName=string,NestingLevel=string,ExtractDocId=boolean,DocsToInvestigate=integer,KmsKeyId=string,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string,UseUpdateLookUp=boolean,ReplicateShardCollections=boolean
```

JSON Syntax:

```
{
  "Username": "string",
  "Password": "string",
  "ServerName": "string",
  "Port": integer,
  "DatabaseName": "string",
  "NestingLevel": "none"|"one",
  "ExtractDocId": true|false,
  "DocsToInvestigate": integer,
  "KmsKeyId": "string",
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string",
  "UseUpdateLookUp": true|false,
  "ReplicateShardCollections": true|false
}
```

`--redis-settings` (structure)

Settings in JSON format for the target Redis endpoint.

ServerName -> (string)

Fully qualified domain name of the endpoint.

Port -> (integer)

Transmission Control Protocol (TCP) port for the endpoint.

SslSecurityProtocol -> (string)

The connection to a Redis target endpoint using Transport Layer Security (TLS). Valid values include `plaintext` and `ssl-encryption` . The default is `ssl-encryption` . The `ssl-encryption` option makes an encrypted connection. Optionally, you can identify an Amazon Resource Name (ARN) for an SSL certificate authority (CA) using the `SslCaCertificateArn` setting. If an ARN isnât given for a CA, DMS uses the Amazon root CA.

The `plaintext` option doesnât provide Transport Layer Security (TLS) encryption for traffic between endpoint and database.

AuthType -> (string)

The type of authentication to perform when connecting to a Redis target. Options include `none` , `auth-token` , and `auth-role` . The `auth-token` option requires an `AuthPassword` value to be provided. The `auth-role` option requires `AuthUserName` and `AuthPassword` values to be provided.

AuthUserName -> (string)

The user name provided with the `auth-role` option of the `AuthType` setting for a Redis target endpoint.

AuthPassword -> (string)

The password provided with the `auth-role` and `auth-token` options of the `AuthType` setting for a Redis target endpoint.

SslCaCertificateArn -> (string)

The Amazon Resource Name (ARN) for the certificate authority (CA) that DMS uses to connect to your Redis target endpoint.

Shorthand Syntax:

```
ServerName=string,Port=integer,SslSecurityProtocol=string,AuthType=string,AuthUserName=string,AuthPassword=string,SslCaCertificateArn=string
```

JSON Syntax:

```
{
  "ServerName": "string",
  "Port": integer,
  "SslSecurityProtocol": "plaintext"|"ssl-encryption",
  "AuthType": "none"|"auth-role"|"auth-token",
  "AuthUserName": "string",
  "AuthPassword": "string",
  "SslCaCertificateArn": "string"
}
```

`--gcp-my-sql-settings` (structure)

Settings in JSON format for the source GCP MySQL endpoint.

AfterConnectScript -> (string)

Specifies a script to run immediately after DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails.

For this parameter, provide the code of the script itself, not the name of a file containing the script.

CleanSourceMetadataOnMismatch -> (boolean)

Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.

DatabaseName -> (string)

Database name for the endpoint. For a MySQL source or target endpoint, donât explicitly specify the database using the `DatabaseName` request parameter on either the `CreateEndpoint` or `ModifyEndpoint` API call. Specifying `DatabaseName` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the DMS task.

EventsPollInterval -> (integer)

Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds.

Example: `eventsPollInterval=5;`

In the example, DMS checks for changes in the binary logs every five seconds.

TargetDbType -> (string)

Specifies where to migrate source tables on the target, either to a single database or multiple databases.

Example: `targetDbType=MULTIPLE_DATABASES`

MaxFileSize -> (integer)

Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.

Example: `maxFileSize=512`

ParallelLoadThreads -> (integer)

Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.

Example: `parallelLoadThreads=1`

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port.

ServerName -> (string)

The MySQL host name.

ServerTimezone -> (string)

Specifies the time zone for the source MySQL database.

Example: `serverTimezone=US/Pacific;`

Note: Do not enclose time zones in single quotes.

Username -> (string)

Endpoint connection user name.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret.` The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the MySQL endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the Database Migration Service User Guide.

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the MySQL endpoint connection details.

Shorthand Syntax:

```
AfterConnectScript=string,CleanSourceMetadataOnMismatch=boolean,DatabaseName=string,EventsPollInterval=integer,TargetDbType=string,MaxFileSize=integer,ParallelLoadThreads=integer,Password=string,Port=integer,ServerName=string,ServerTimezone=string,Username=string,SecretsManagerAccessRoleArn=string,SecretsManagerSecretId=string
```

JSON Syntax:

```
{
  "AfterConnectScript": "string",
  "CleanSourceMetadataOnMismatch": true|false,
  "DatabaseName": "string",
  "EventsPollInterval": integer,
  "TargetDbType": "specific-database"|"multiple-databases",
  "MaxFileSize": integer,
  "ParallelLoadThreads": integer,
  "Password": "string",
  "Port": integer,
  "ServerName": "string",
  "ServerTimezone": "string",
  "Username": "string",
  "SecretsManagerAccessRoleArn": "string",
  "SecretsManagerSecretId": "string"
}
```

`--timestream-settings` (structure)

Settings in JSON format for the target Amazon Timestream endpoint.

DatabaseName -> (string)

Database name for the endpoint.

MemoryDuration -> (integer)

Set this attribute to specify the length of time to store all of the tables in memory that are migrated into Amazon Timestream from the source database. Time is measured in units of hours. When Timestream data comes in, it first resides in memory for the specified duration, which allows quick access to it.

MagneticDuration -> (integer)

Set this attribute to specify the default magnetic duration applied to the Amazon Timestream tables in days. This is the number of days that records remain in magnetic store before being discarded. For more information, see [Storage](https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html) in the [Amazon Timestream Developer Guide](https://docs.aws.amazon.com/timestream/latest/developerguide/) .

CdcInsertsAndUpdates -> (boolean)

Set this attribute to `true` to specify that DMS only applies inserts and updates, and not deletes. Amazon Timestream does not allow deleting records, so if this value is `false` , DMS nulls out the corresponding record in the Timestream database rather than deleting it.

EnableMagneticStoreWrites -> (boolean)

Set this attribute to `true` to enable memory store writes. When this value is `false` , DMS does not write records that are older in days than the value specified in `MagneticDuration` , because Amazon Timestream does not allow memory writes by default. For more information, see [Storage](https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html) in the [Amazon Timestream Developer Guide](https://docs.aws.amazon.com/timestream/latest/developerguide/) .

Shorthand Syntax:

```
DatabaseName=string,MemoryDuration=integer,MagneticDuration=integer,CdcInsertsAndUpdates=boolean,EnableMagneticStoreWrites=boolean
```

JSON Syntax:

```
{
  "DatabaseName": "string",
  "MemoryDuration": integer,
  "MagneticDuration": integer,
  "CdcInsertsAndUpdates": true|false,
  "EnableMagneticStoreWrites": true|false
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create an endpoint**

The following `create-endpoint` example creates an endpoint for an Amazon S3 source.

```
aws dms create-endpoint \
    --endpoint-type source \
    --engine-name s3 \
    --endpoint-identifier src-endpoint \
    --s3-settings file://s3-settings.json
```

Contents of `s3-settings.json`:

```
{
    "BucketName":"my-corp-data",
    "BucketFolder":"sourcedata",
    "ServiceAccessRoleArn":"arn:aws:iam::123456789012:role/my-s3-access-role"
}
```

Output:

```
{
    "Endpoint": {
        "EndpointIdentifier": "src-endpoint",
        "EndpointType": "SOURCE",
        "EngineName": "s3",
        "EngineDisplayName": "Amazon S3",
        "ExtraConnectionAttributes": "bucketFolder=sourcedata;bucketName=my-corp-data;compressionType=NONE;csvDelimiter=,;csvRowDelimiter=\\n;",
        "Status": "active",
        "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:GUVAFG34EECUOJ6QVZ56DAHT3U",
        "SslMode": "none",
        "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role",
        "S3Settings": {
            "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role",
            "CsvRowDelimiter": "\\n",
            "CsvDelimiter": ",",
            "BucketFolder": "sourcedata",
            "BucketName": "my-corp-data",
            "CompressionType": "NONE",
            "EnableStatistics": true
        }
    }
}
```

For more information, see [Working with AWS DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html) in the *AWS Database Migration Service User Guide*.

## Output

Endpoint -> (structure)

The endpoint that was created.

EndpointIdentifier -> (string)

The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They canât end with a hyphen or contain two consecutive hyphens.

EndpointType -> (string)

The type of endpoint. Valid values are `source` and `target` .

EngineName -> (string)

The database engine name. Valid values, depending on the EndpointType, include `"mysql"` , `"oracle"` , `"postgres"` , `"mariadb"` , `"aurora"` , `"aurora-postgresql"` , `"redshift"` , `"redshift-serverless"` , `"s3"` , `"db2"` , `"db2-zos"` , `"azuredb"` , `"sybase"` , `"dynamodb"` , `"mongodb"` , `"kinesis"` , `"kafka"` , `"elasticsearch"` , `"documentdb"` , `"sqlserver"` , `"neptune"` , and `"babelfish"` .

EngineDisplayName -> (string)

The expanded name for the engine name. For example, if the `EngineName` parameter is âauroraâ, this value would be âAmazon Aurora MySQLâ.

Username -> (string)

The user name used to connect to the endpoint.

ServerName -> (string)

The name of the server at the endpoint.

Port -> (integer)

The port value used to access the endpoint.

DatabaseName -> (string)

The name of the database at the endpoint.

ExtraConnectionAttributes -> (string)

Additional connection attributes used to connect to the endpoint.

Status -> (string)

The status of the endpoint.

KmsKeyId -> (string)

An KMS key identifier that is used to encrypt the connection parameters for the endpoint.

If you donât specify a value for the `KmsKeyId` parameter, then DMS uses your default encryption key.

KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

EndpointArn -> (string)

The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

CertificateArn -> (string)

The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

SslMode -> (string)

The SSL mode used to connect to the endpoint. The default value is `none` .

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.

ExternalTableDefinition -> (string)

The external table definition.

ExternalId -> (string)

Value returned by a call to CreateEndpoint that can be used for cross-account validation. Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

DynamoDbSettings -> (structure)

The settings for the DynamoDB target endpoint. For more information, see the `DynamoDBSettings` structure.

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.

S3Settings -> (structure)

The settings for the S3 target endpoint. For more information, see the `S3Settings` structure.

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action. It is a required parameter that enables DMS to write and read objects from an S3 bucket.

ExternalTableDefinition -> (string)

Specifies how tables are defined in the S3 source files only.

CsvRowDelimiter -> (string)

The delimiter used to separate rows in the .csv file for both source and target. The default is a carriage return (`\n` ).

CsvDelimiter -> (string)

The delimiter used to separate columns in the .csv file for both source and target. The default is a comma.

BucketFolder -> (string)

An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this parameter isnât specified, then the path used is `` *schema_name* /*table_name* /`` .

BucketName -> (string)

The name of the S3 bucket.

CompressionType -> (string)

An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or donât use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats.

EncryptionMode -> (string)

The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either `SSE_S3` (the default) or `SSE_KMS` .

### Note

For the `ModifyEndpoint` operation, you can change the existing value of the `EncryptionMode` parameter from `SSE_KMS` to `SSE_S3` . But you canât change the existing value from `SSE_S3` to `SSE_KMS` .

To use `SSE_S3` , you need an Identity and Access Management (IAM) role with permission to allow `"arn:aws:s3:::dms-*"` to use the following actions:

- `s3:CreateBucket`
- `s3:ListBucket`
- `s3:DeleteBucket`
- `s3:GetBucketLocation`
- `s3:GetObject`
- `s3:PutObject`
- `s3:DeleteObject`
- `s3:GetObjectVersion`
- `s3:GetBucketPolicy`
- `s3:PutBucketPolicy`
- `s3:DeleteBucketPolicy`

ServerSideEncryptionKmsKeyId -> (string)

If you are using `SSE_KMS` for the `EncryptionMode` , provide the KMS key ID. The key that you use needs an attached policy that enables Identity and Access Management (IAM) user permissions and allows use of the key.

Here is a CLI example: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html#id3)aws dms create-endpoint âendpoint-identifier *value* âendpoint-type target âengine-name s3 âs3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

DataFormat -> (string)

The format of the data that you want to use for output. You can choose one of the following:

- `csv` : This is a row-based file format with comma-separated values (.csv).
- `parquet` : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.

EncodingType -> (string)

The type of encoding you are using:

- `RLE_DICTIONARY` uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.
- `PLAIN` doesnât use encoding at all. Values are stored as they are.
- `PLAIN_DICTIONARY` builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.

DictPageSizeLimit -> (integer)

The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of `PLAIN` . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to `PLAIN` encoding. This size is used for .parquet file format only.

RowGroupLength -> (integer)

The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.

If you choose a value larger than the maximum, `RowGroupLength` is set to the max row group length in bytes (64 * 1024 * 1024).

DataPageSize -> (integer)

The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.

ParquetVersion -> (string)

The version of the Apache Parquet format that you want to use: `parquet_1_0` (the default) or `parquet_2_0` .

EnableStatistics -> (boolean)

A value that enables statistics for Parquet pages and row groups. Choose `true` to enable statistics, `false` to disable. Statistics include `NULL` , `DISTINCT` , `MAX` , and `MIN` values. This parameter defaults to `true` . This value is used for .parquet file format only.

IncludeOpForFullLoad -> (boolean)

A value that enables a full load to write INSERT operations to the comma-separated value (.csv) or .parquet output files only to indicate how the rows were added to the source database.

### Note

DMS supports the `IncludeOpForFullLoad` parameter in versions 3.1.4 and later.

DMS supports the use of the .parquet files with the `IncludeOpForFullLoad` parameter in versions 3.4.7 and later.

For full load, records can only be inserted. By default (the `false` setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If `IncludeOpForFullLoad` is set to `true` or `y` , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.

### Note

This setting works together with the `CdcInsertsOnly` and the `CdcInsertsAndUpdates` parameters for output to .csv files only. For more information about how these settings work together, see [Indicating Source DB Operations in Migrated S3 Data](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps) in the *Database Migration Service User Guide.* .

CdcInsertsOnly -> (boolean)

A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the `false` setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.

If `CdcInsertsOnly` is set to `true` or `y` , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of `IncludeOpForFullLoad` . If `IncludeOpForFullLoad` is set to `true` , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If `IncludeOpForFullLoad` is set to `false` , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see [Indicating Source DB Operations in Migrated S3 Data](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps) in the *Database Migration Service User Guide.* .

### Note

DMS supports the interaction described preceding between the `CdcInsertsOnly` and `IncludeOpForFullLoad` parameters in versions 3.1.4 and later.

`CdcInsertsOnly` and `CdcInsertsAndUpdates` canât both be set to `true` for the same endpoint. Set either `CdcInsertsOnly` or `CdcInsertsAndUpdates` to `true` for the same endpoint, but not both.

TimestampColumnName -> (string)

A value that when nonblank causes DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.

### Note

DMS supports the `TimestampColumnName` parameter in versions 3.1.4 and later.

DMS includes an additional `STRING` column in the .csv or .parquet object files of your migrated data when you set `TimestampColumnName` to a nonblank value.

For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.

For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.

The string format for this timestamp column value is `yyyy-MM-dd HH:mm:ss.SSSSSS` . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.

When the `AddColumnName` parameter is set to `true` , DMS also includes a name for the timestamp column that you set with `TimestampColumnName` .

ParquetTimestampInMillisecond -> (boolean)

A value that specifies the precision of any `TIMESTAMP` column values that are written to an Amazon S3 object file in .parquet format.

### Note

DMS supports the `ParquetTimestampInMillisecond` parameter in versions 3.1.4 and later.

When `ParquetTimestampInMillisecond` is set to `true` or `y` , DMS writes all `TIMESTAMP` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.

Currently, Amazon Athena and Glue can handle only millisecond precision for `TIMESTAMP` values. Set this parameter to `true` for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or Glue.

### Note

DMS writes any `TIMESTAMP` column values written to an S3 file in .csv format with microsecond precision.

Setting `ParquetTimestampInMillisecond` has no effect on the string format of the timestamp column value that is inserted by setting the `TimestampColumnName` parameter.

CdcInsertsAndUpdates -> (boolean)

A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is `false` , but when `CdcInsertsAndUpdates` is set to `true` or `y` , only INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.

### Warning

DMS supports the use of the .parquet files in versions 3.4.7 and later.

How these INSERTs and UPDATEs are recorded depends on the value of the `IncludeOpForFullLoad` parameter. If `IncludeOpForFullLoad` is set to `true` , the first field of every CDC record is set to either `I` or `U` to indicate INSERT and UPDATE operations at the source. But if `IncludeOpForFullLoad` is set to `false` , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see [Indicating Source DB Operations in Migrated S3 Data](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps) in the *Database Migration Service User Guide.* .

### Note

DMS supports the use of the `CdcInsertsAndUpdates` parameter in versions 3.3.1 and later.

`CdcInsertsOnly` and `CdcInsertsAndUpdates` canât both be set to `true` for the same endpoint. Set either `CdcInsertsOnly` or `CdcInsertsAndUpdates` to `true` for the same endpoint, but not both.

DatePartitionEnabled -> (boolean)

When set to `true` , this parameter partitions S3 bucket folders based on transaction commit dates. The default value is `false` . For more information about date-based folder partitioning, see [Using date-based folder partitioning](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.DatePartitioning) .

DatePartitionSequence -> (string)

Identifies the sequence of the date format to use during folder partitioning. The default value is `YYYYMMDD` . Use this parameter when `DatePartitionedEnabled` is set to `true` .

DatePartitionDelimiter -> (string)

Specifies a date separating delimiter to use during folder partitioning. The default value is `SLASH` . Use this parameter when `DatePartitionedEnabled` is set to `true` .

UseCsvNoSupValue -> (boolean)

This setting applies if the S3 output files during a change data capture (CDC) load are written in .csv format. If set to `true` for columns not included in the supplemental log, DMS uses the value specified by ` `CsvNoSupValue` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-CsvNoSupValue`__ . If not set or set to `false` , DMS uses the null value for these columns.

### Note

This setting is supported in DMS versions 3.4.1 and later.

CsvNoSupValue -> (string)

This setting only applies if your Amazon S3 output files during a change data capture (CDC) load are written in .csv format. If ` `UseCsvNoSupValue` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-UseCsvNoSupValue`__ is set to true, specify a string value that you want DMS to use for all columns not included in the supplemental log. If you do not specify a string value, DMS uses the null value for these columns regardless of the `UseCsvNoSupValue` setting.

### Note

This setting is supported in DMS versions 3.4.1 and later.

PreserveTransactions -> (boolean)

If set to `true` , DMS saves the transaction order for a change data capture (CDC) load on the Amazon S3 target specified by ` `CdcPath` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-CdcPath`__ . For more information, see [Capturing data changes (CDC) including transaction order on the S3 target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath) .

### Note

This setting is supported in DMS versions 3.4.2 and later.

CdcPath -> (string)

Specifies the folder path of CDC files. For an S3 source, this setting is required if a task captures change data; otherwise, itâs optional. If `CdcPath` is set, DMS reads CDC files from this path and replicates the data changes to the target endpoint. For an S3 target if you set ` `PreserveTransactions` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-PreserveTransactions`__ to `true` , DMS verifies that you have set this parameter to a folder path on your S3 target where DMS can save the transaction order for the CDC load. DMS creates this CDC folder path in either your S3 target working directory or the S3 target location specified by ` `BucketFolder` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-BucketFolder`__ and ` `BucketName` [https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings](https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings)-BucketName`__ .

For example, if you specify `CdcPath` as `MyChangedData` , and you specify `BucketName` as `MyTargetBucket` but do not specify `BucketFolder` , DMS creates the CDC folder path following: `MyTargetBucket/MyChangedData` .

If you specify the same `CdcPath` , and you specify `BucketName` as `MyTargetBucket` and `BucketFolder` as `MyTargetData` , DMS creates the CDC folder path following: `MyTargetBucket/MyTargetData/MyChangedData` .

For more information on CDC including transaction order on an S3 target, see [Capturing data changes (CDC) including transaction order on the S3 target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath) .

### Note

This setting is supported in DMS versions 3.4.2 and later.

UseTaskStartTimeForFullLoadTimestamp -> (boolean)

When set to true, this parameter uses the task start time as the timestamp column value instead of the time data is written to target. For full load, when `useTaskStartTimeForFullLoadTimestamp` is set to `true` , each row of the timestamp column contains the task start time. For CDC loads, each row of the timestamp column contains the transaction commit time.

When `useTaskStartTimeForFullLoadTimestamp` is set to `false` , the full load timestamp in the timestamp column increments with the time data arrives at the target.

CannedAclForObjects -> (string)

A value that enables DMS to specify a predefined (canned) access control list for objects created in an Amazon S3 bucket as .csv or .parquet files. For more information about Amazon S3 canned ACLs, see [Canned ACL](http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) in the *Amazon S3 Developer Guide.*

The default value is NONE. Valid values include NONE, PRIVATE, PUBLIC_READ, PUBLIC_READ_WRITE, AUTHENTICATED_READ, AWS_EXEC_READ, BUCKET_OWNER_READ, and BUCKET_OWNER_FULL_CONTROL.

AddColumnName -> (boolean)

An optional parameter that, when set to `true` or `y` , you can use to add column name information to the .csv output file.

The default value is `false` . Valid values are `true` , `false` , `y` , and `n` .

CdcMaxBatchInterval -> (integer)

Maximum length of the interval, defined in seconds, after which to output a file to Amazon S3.

When `CdcMaxBatchInterval` and `CdcMinFileSize` are both specified, the file write is triggered by whichever parameter condition is met first within an DMS CloudFormation template.

The default value is 60 seconds.

CdcMinFileSize -> (integer)

Minimum file size, defined in kilobytes, to reach for a file output to Amazon S3.

When `CdcMinFileSize` and `CdcMaxBatchInterval` are both specified, the file write is triggered by whichever parameter condition is met first within an DMS CloudFormation template.

The default value is 32 MB.

CsvNullValue -> (string)

An optional parameter that specifies how DMS treats null values. While handling the null value, you can use this parameter to pass a user-defined string as null when writing to the target. For example, when target columns are nullable, you can use this option to differentiate between the empty string value and the null value. So, if you set this parameter value to the empty string (ââ or ââ), DMS treats the empty string as the null value instead of `NULL` .

The default value is `NULL` . Valid values include any valid string.

IgnoreHeaderRows -> (integer)

When this value is set to 1, DMS ignores the first row header in a .csv file. A value of 1 turns on the feature; a value of 0 turns off the feature.

The default is 0.

MaxFileSize -> (integer)

A value that specifies the maximum size (in KB) of any .csv file to be created while migrating to an S3 target during full load.

The default value is 1,048,576 KB (1 GB). Valid values include 1 to 1,048,576.

Rfc4180 -> (boolean)

For an S3 source, when this value is set to `true` or `y` , each leading double quotation mark has to be followed by an ending double quotation mark. This formatting complies with RFC 4180. When this value is set to `false` or `n` , string literals are copied to the target as is. In this case, a delimiter (row or column) signals the end of the field. Thus, you canât use a delimiter as part of the string, because it signals the end of the value.

For an S3 target, an optional parameter used to set behavior to comply with RFC 4180 for data migrated to Amazon S3 using .csv file format only. When this value is set to `true` or `y` using Amazon S3 as a target, if the data has quotation marks or newline characters in it, DMS encloses the entire column with an additional pair of double quotation marks (â). Every quotation mark within the data is repeated twice.

The default value is `true` . Valid values include `true` , `false` , `y` , and `n` .

DatePartitionTimezone -> (string)

When creating an S3 target endpoint, set `DatePartitionTimezone` to convert the current UTC time into a specified time zone. The conversion occurs when a date partition folder is created and a CDC filename is generated. The time zone format is Area/Location. Use this parameter when `DatePartitionedEnabled` is set to `true` , as shown in the following example.

`s3-settings='{"DatePartitionEnabled": true, "DatePartitionSequence": "YYYYMMDDHH", "DatePartitionDelimiter": "SLASH", "DatePartitionTimezone":"*Asia/Seoul* ", "BucketName": "dms-nattarat-test"}'`

AddTrailingPaddingCharacter -> (boolean)

Use the S3 target endpoint setting `AddTrailingPaddingCharacter` to add padding on string data. The default value is `false` .

ExpectedBucketOwner -> (string)

To specify a bucket owner and prevent sniping, you can use the `ExpectedBucketOwner` endpoint setting.

Example: `--s3-settings='{"ExpectedBucketOwner": "*AWS_Account_ID* "}'`

When you make a request to test a connection or perform a migration, S3 checks the account ID of the bucket owner against the specified parameter.

GlueCatalogGeneration -> (boolean)

When true, allows Glue to catalog your S3 bucket. Creating an Glue catalog lets you use Athena to query your data.

DmsTransferSettings -> (structure)

The settings for the DMS Transfer type source. For more information, see the DmsTransferSettings structure.

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the `iam:PassRole` action.

BucketName -> (string)

The name of the S3 bucket to use.

MongoDbSettings -> (structure)

The settings for the MongoDB source endpoint. For more information, see the `MongoDbSettings` structure.

Username -> (string)

The user name you use to access the MongoDB source endpoint.

Password -> (string)

The password for the user account you use to access the MongoDB source endpoint.

ServerName -> (string)

The name of the server on the MongoDB source endpoint. For MongoDB Atlas, provide the server name for any of the servers in the replication set.

Port -> (integer)

The port value for the MongoDB source endpoint.

DatabaseName -> (string)

The database name on the MongoDB source endpoint.

AuthType -> (string)

The authentication type you use to access the MongoDB source endpoint.

When when set to `"no"` , user name and password parameters are not used and can be empty.

AuthMechanism -> (string)

The authentication mechanism you use to access the MongoDB source endpoint.

For the default value, in MongoDB version 2.x, `"default"` is `"mongodb_cr"` . For MongoDB version 3.x or later, `"default"` is `"scram_sha_1"` . This setting isnât used when `AuthType` is set to `"no"` .

NestingLevel -> (string)

Specifies either document or table mode.

Default value is `"none"` . Specify `"none"` to use document mode. Specify `"one"` to use table mode.

ExtractDocId -> (string)

Specifies the document ID. Use this setting when `NestingLevel` is set to `"none"` .

Default value is `"false"` .

DocsToInvestigate -> (string)

Indicates the number of documents to preview to determine the document organization. Use this setting when `NestingLevel` is set to `"one"` .

Must be a positive value greater than `0` . Default value is `1000` .

AuthSource -> (string)

The MongoDB database name. This setting isnât used when `AuthType` is set to `"no"` .

The default is `"admin"` .

KmsKeyId -> (string)

The KMS key identifier that is used to encrypt the content on the replication instance. If you donât specify a value for the `KmsKeyId` parameter, then DMS uses your default encryption key. KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the MongoDB endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the MongoDB endpoint connection details.

UseUpdateLookUp -> (boolean)

If `true` , DMS retrieves the entire document from the MongoDB source during migration. This may cause a migration failure if the server response exceeds bandwidth limits. To fetch only updates and deletes during migration, set this parameter to `false` .

ReplicateShardCollections -> (boolean)

If `true` , DMS replicates data to shard collections. DMS only uses this setting if the target endpoint is a DocumentDB elastic cluster.

When this setting is `true` , note the following:

- You must set `TargetTablePrepMode` to `nothing` .
- DMS automatically sets `useUpdateLookup` to `false` .

KinesisSettings -> (structure)

The settings for the Amazon Kinesis target endpoint. For more information, see the `KinesisSettings` structure.

StreamArn -> (string)

The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

MessageFormat -> (string)

The output format for the records created on the endpoint. The message format is `JSON` (default) or `JSON_UNFORMATTED` (a single line with no tab).

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Kinesis data stream. The role must allow the `iam:PassRole` action.

IncludeTransactionDetails -> (boolean)

Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for `transaction_id` , previous `transaction_id` , and `transaction_record_id` (the record offset within a transaction). The default is `false` .

IncludePartitionValue -> (boolean)

Shows the partition value within the Kinesis message output, unless the partition type is `schema-table-type` . The default is `false` .

PartitionIncludeSchemaTable -> (boolean)

Prefixes schema and table names to partition values, when the partition type is `primary-key-type` . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is `false` .

IncludeTableAlterOperations -> (boolean)

Includes any data definition language (DDL) operations that change the table in the control data, such as `rename-table` , `drop-table` , `add-column` , `drop-column` , and `rename-column` . The default is `false` .

IncludeControlDetails -> (boolean)

Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is `false` .

IncludeNullAndEmpty -> (boolean)

Include NULL and empty columns for records migrated to the endpoint. The default is `false` .

NoHexPrefix -> (boolean)

Set this optional parameter to `true` to avoid adding a â0xâ prefix to raw data in hexadecimal format. For example, by default, DMS adds a â0xâ prefix to the LOB column type in hexadecimal format moving from an Oracle source to an Amazon Kinesis target. Use the `NoHexPrefix` endpoint setting to enable migration of RAW data type columns without adding the â0xâ prefix.

UseLargeIntegerValue -> (boolean)

Specifies using the large integer value with Kinesis.

KafkaSettings -> (structure)

The settings for the Apache Kafka target endpoint. For more information, see the `KafkaSettings` structure.

Broker -> (string)

A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance. Specify each broker location in the form `` *broker-hostname-or-ip* :*port* `` . For example, `"ec2-12-345-678-901.compute-1.amazonaws.com:2345"` . For more information and examples of specifying a list of broker locations, see [Using Apache Kafka as a target for Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html) in the *Database Migration Service User Guide* .

Topic -> (string)

The topic to which you migrate the data. If you donât specify a topic, DMS specifies `"kafka-default-topic"` as the migration topic.

MessageFormat -> (string)

The output format for the records created on the endpoint. The message format is `JSON` (default) or `JSON_UNFORMATTED` (a single line with no tab).

IncludeTransactionDetails -> (boolean)

Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for `transaction_id` , previous `transaction_id` , and `transaction_record_id` (the record offset within a transaction). The default is `false` .

IncludePartitionValue -> (boolean)

Shows the partition value within the Kafka message output unless the partition type is `schema-table-type` . The default is `false` .

PartitionIncludeSchemaTable -> (boolean)

Prefixes schema and table names to partition values, when the partition type is `primary-key-type` . Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is `false` .

IncludeTableAlterOperations -> (boolean)

Includes any data definition language (DDL) operations that change the table in the control data, such as `rename-table` , `drop-table` , `add-column` , `drop-column` , and `rename-column` . The default is `false` .

IncludeControlDetails -> (boolean)

Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output. The default is `false` .

MessageMaxBytes -> (integer)

The maximum size in bytes for records created on the endpoint The default is 1,000,000.

IncludeNullAndEmpty -> (boolean)

Include NULL and empty columns for records migrated to the endpoint. The default is `false` .

SecurityProtocol -> (string)

Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS). Options include `ssl-encryption` , `ssl-authentication` , and `sasl-ssl` . `sasl-ssl` requires `SaslUsername` and `SaslPassword` .

SslClientCertificateArn -> (string)

The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.

SslClientKeyArn -> (string)

The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.

SslClientKeyPassword -> (string)

The password for the client private key used to securely connect to a Kafka target endpoint.

SslCaCertificateArn -> (string)

The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that DMS uses to securely connect to your Kafka target endpoint.

SaslUsername -> (string)

The secure user name you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.

SaslPassword -> (string)

The secure password you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.

NoHexPrefix -> (boolean)

Set this optional parameter to `true` to avoid adding a â0xâ prefix to raw data in hexadecimal format. For example, by default, DMS adds a â0xâ prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the `NoHexPrefix` endpoint setting to enable migration of RAW data type columns without adding the â0xâ prefix.

SaslMechanism -> (string)

For SASL/SSL authentication, DMS supports the `SCRAM-SHA-512` mechanism by default. DMS versions 3.5.0 and later also support the `PLAIN` mechanism. To use the `PLAIN` mechanism, set this parameter to `PLAIN.`

SslEndpointIdentificationAlgorithm -> (string)

Sets hostname verification for the certificate. This setting is supported in DMS version 3.5.1 and later.

UseLargeIntegerValue -> (boolean)

Specifies using the large integer value with Kafka.

ElasticsearchSettings -> (structure)

The settings for the OpenSearch source endpoint. For more information, see the `ElasticsearchSettings` structure.

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.

EndpointUri -> (string)

The endpoint for the OpenSearch cluster. DMS uses HTTPS if a transport protocol (http/https) is not specified.

FullLoadErrorPercentage -> (integer)

The maximum percentage of records that can fail to be written before a full load operation stops.

To avoid early failure, this counter is only effective after 1000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops.

ErrorRetryDuration -> (integer)

The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.

UseNewMappingType -> (boolean)

Set this option to `true` for DMS to migrate documentation using the documentation type `_doc` . OpenSearch and an Elasticsearch cluster only support the _doc documentation type in versions 7. x and later. The default value is `false` .

NeptuneSettings -> (structure)

The settings for the Amazon Neptune target endpoint. For more information, see the `NeptuneSettings` structure.

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of the service role that you created for the Neptune target endpoint. The role must allow the `iam:PassRole` action. For more information, see [Creating an IAM Service Role for Accessing Amazon Neptune as a Target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole) in the *Database Migration Service User Guide.*

S3BucketName -> (string)

The name of the Amazon S3 bucket where DMS can temporarily store migrated graph data in .csv files before bulk-loading it to the Neptune target database. DMS maps the SQL source data to graph data before storing it in these .csv files.

S3BucketFolder -> (string)

A folder path where you want DMS to store migrated graph data in the S3 bucket specified by `S3BucketName`

ErrorRetryDuration -> (integer)

The number of milliseconds for DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.

MaxFileSize -> (integer)

The maximum size in kilobytes of migrated graph data stored in a .csv file before DMS bulk-loads the data to the Neptune target database. The default is 1,048,576 KB. If the bulk load is successful, DMS clears the bucket, ready to store the next batch of migrated graph data.

MaxRetryCount -> (integer)

The number of times for DMS to retry a bulk load of migrated graph data to the Neptune target database before raising an error. The default is 5.

IamAuthEnabled -> (boolean)

If you want Identity and Access Management (IAM) authorization enabled for this endpoint, set this parameter to `true` . Then attach the appropriate IAM policy document to your service role specified by `ServiceAccessRoleArn` . The default is `false` .

RedshiftSettings -> (structure)

Settings for the Amazon Redshift endpoint.

AcceptAnyDate -> (boolean)

A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose `true` or `false` (the default).

This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesnât match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

AfterConnectScript -> (string)

Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.

BucketFolder -> (string)

An S3 folder where the comma-separated-value (.csv) files are stored before being uploaded to the target Redshift cluster.

For full load mode, DMS converts source records into .csv files and loads them to the *BucketFolder/TableID* path. DMS uses the Redshift `COPY` command to upload the .csv files to the target table. The files are deleted once the `COPY` operation has finished. For more information, see [COPY](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html) in the *Amazon Redshift Database Developer Guide* .

For change-data-capture (CDC) mode, DMS creates a *NetChanges* table, and loads the .csv files to this *BucketFolder/NetChangesTableID* path.

BucketName -> (string)

The name of the intermediate S3 bucket used to store .csv files before uploading data to Redshift.

CaseSensitiveNames -> (boolean)

If Amazon Redshift is configured to support case sensitive schema names, set `CaseSensitiveNames` to `true` . The default is `false` .

CompUpdate -> (boolean)

If you set `CompUpdate` to `true` Amazon Redshift applies automatic compression if the table is empty. This applies even if the table columns already have encodings other than `RAW` . If you set `CompUpdate` to `false` , automatic compression is disabled and existing column encodings arenât changed. The default is `true` .

ConnectionTimeout -> (integer)

A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.

DatabaseName -> (string)

The name of the Amazon Redshift data warehouse (service) that you are working with.

DateFormat -> (string)

The date format that you are using. Valid values are `auto` (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of âYYYY-MM-DDâ. Using `auto` recognizes most strings, even some that arenât supported when you use a date format string.

If your date and time values use formats different from each other, set this to `auto` .

EmptyAsNull -> (boolean)

A value that specifies whether DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of `true` sets empty CHAR and VARCHAR fields to null. The default is `false` .

EncryptionMode -> (string)

The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either `SSE_S3` (the default) or `SSE_KMS` .

### Note

For the `ModifyEndpoint` operation, you can change the existing value of the `EncryptionMode` parameter from `SSE_KMS` to `SSE_S3` . But you canât change the existing value from `SSE_S3` to `SSE_KMS` .

To use `SSE_S3` , create an Identity and Access Management (IAM) role with a policy that allows `"arn:aws:s3:::*"` to use the following actions: `"s3:PutObject", "s3:ListBucket"`

ExplicitIds -> (boolean)

This setting is only valid for a full-load migration task. Set `ExplicitIds` to `true` to have tables with `IDENTITY` columns override their auto-generated values with explicit values loaded from the source data files used to populate the tables. The default is `false` .

FileTransferUploadStreams -> (integer)

The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.

The number of parallel streams used to upload a single .csv file to an S3 bucket using S3 Multipart Upload. For more information, see [Multipart upload overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html) .

`FileTransferUploadStreams` accepts a value from 1 through 64. It defaults to 10.

LoadTimeout -> (integer)

The amount of time to wait (in milliseconds) before timing out of operations performed by DMS on a Redshift cluster, such as Redshift COPY, INSERT, DELETE, and UPDATE.

MaxFileSize -> (integer)

The maximum size (in KB) of any .csv file used to load data on an S3 bucket and transfer data to Amazon Redshift. It defaults to 1048576KB (1 GB).

Password -> (string)

The password for the user named in the `username` property.

Port -> (integer)

The port number for Amazon Redshift. The default value is 5439.

RemoveQuotes -> (boolean)

A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose `true` to remove quotation marks. The default is `false` .

ReplaceInvalidChars -> (string)

A list of characters that you want to replace. Use with `ReplaceChars` .

ReplaceChars -> (string)

A value that specifies to replaces the invalid characters specified in `ReplaceInvalidChars` , substituting the specified characters instead. The default is `"?"` .

ServerName -> (string)

The name of the Amazon Redshift cluster you are using.

ServiceAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service. The role must allow the `iam:PassRole` action.

ServerSideEncryptionKmsKeyId -> (string)

The KMS key ID. If you are using `SSE_KMS` for the `EncryptionMode` , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

TimeFormat -> (string)

The time format that you want to use. Valid values are `auto` (case-sensitive), `'timeformat_string'` , `'epochsecs'` , or `'epochmillisecs'` . It defaults to 10. Using `auto` recognizes most strings, even some that arenât supported when you use a time format string.

If your date and time values use formats different from each other, set this parameter to `auto` .

TrimBlanks -> (boolean)

A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose `true` to remove unneeded white space. The default is `false` .

TruncateColumns -> (boolean)

A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose `true` to truncate data. The default is `false` .

Username -> (string)

An Amazon Redshift user name for a registered user.

WriteBufferSize -> (integer)

The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk at the DMS replication instance. The default value is 1000 (buffer size is 1000KB).

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the Amazon Redshift endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Amazon Redshift endpoint connection details.

MapBooleanAsBoolean -> (boolean)

When true, lets Redshift migrate the boolean type as boolean. By default, Redshift migrates booleans as `varchar(1)` . You must set this setting on both the source and target endpoints for it to take effect.

PostgreSQLSettings -> (structure)

The settings for the PostgreSQL source and target endpoint. For more information, see the `PostgreSQLSettings` structure.

AfterConnectScript -> (string)

For use with change data capture (CDC) only, this attribute has DMS bypass foreign keys and user triggers to reduce the time it takes to bulk load data.

Example: `afterConnectScript=SET session_replication_role='replica'`

CaptureDdls -> (boolean)

To capture DDL events, DMS creates various artifacts in the PostgreSQL database when the task starts. You can later remove these artifacts.

The default value is `true` .

If this value is set to `N` , you donât have to create tables or triggers on the source database.

MaxFileSize -> (integer)

Specifies the maximum size (in KB) of any .csv file used to transfer data to PostgreSQL.

The default value is 32,768 KB (32 MB).

Example: `maxFileSize=512`

DatabaseName -> (string)

Database name for the endpoint.

DdlArtifactsSchema -> (string)

The schema in which the operational DDL database artifacts are created.

The default value is `public` .

Example: `ddlArtifactsSchema=xyzddlschema;`

ExecuteTimeout -> (integer)

Sets the client statement timeout for the PostgreSQL instance, in seconds. The default value is 60 seconds.

Example: `executeTimeout=100;`

FailTasksOnLobTruncation -> (boolean)

When set to `true` , this value causes a task to fail if the actual size of a LOB column is greater than the specified `LobMaxSize` .

The default value is `false` .

If task is set to Limited LOB mode and this option is set to true, the task fails instead of truncating the LOB data.

HeartbeatEnable -> (boolean)

The write-ahead log (WAL) heartbeat feature mimics a dummy transaction. By doing this, it prevents idle logical replication slots from holding onto old WAL logs, which can result in storage full situations on the source. This heartbeat keeps `restart_lsn` moving and prevents storage full scenarios.

The default value is `false` .

HeartbeatSchema -> (string)

Sets the schema in which the heartbeat artifacts are created.

The default value is `public` .

HeartbeatFrequency -> (integer)

Sets the WAL heartbeat frequency (in minutes).

The default value is 5 minutes.

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port. The default is 5432.

ServerName -> (string)

The host name of the endpoint database.

For an Amazon RDS PostgreSQL instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) , in the `` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

For an Aurora PostgreSQL instance, this is the output of [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) , in the `Endpoint` field.

Username -> (string)

Endpoint connection user name.

SlotName -> (string)

Sets the name of a previously created logical replication slot for a change data capture (CDC) load of the PostgreSQL source instance.

When used with the `CdcStartPosition` request parameter for the DMS API , this attribute also makes it possible to use native CDC start points. DMS verifies that the specified logical replication slot exists before starting the CDC load task. It also verifies that the task was created with a valid setting of `CdcStartPosition` . If the specified slot doesnât exist or the task doesnât have a valid `CdcStartPosition` setting, DMS raises an error.

For more information about setting the `CdcStartPosition` request parameter, see [Determining a CDC native start point](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native) in the *Database Migration Service User Guide* . For more information about using `CdcStartPosition` , see [CreateReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html) , [StartReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html) , and [ModifyReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html) .

PluginName -> (string)

Specifies the plugin to use to create a replication slot.

The default value is `pglogical` .

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the PostgreSQL endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the PostgreSQL endpoint connection details.

TrimSpaceInChar -> (boolean)

Use the `TrimSpaceInChar` source endpoint setting to trim data on CHAR and NCHAR data types during migration. The default value is `true` .

MapBooleanAsBoolean -> (boolean)

When true, lets PostgreSQL migrate the boolean type as boolean. By default, PostgreSQL migrates booleans as `varchar(5)` . You must set this setting on both the source and target endpoints for it to take effect.

The default value is `false` .

MapJsonbAsClob -> (boolean)

When true, DMS migrates JSONB values as CLOB.

The default value is `false` .

MapLongVarcharAs -> (string)

Sets what datatype to map LONG values as.

The default value is `wstring` .

DatabaseMode -> (string)

Specifies the default behavior of the replicationâs handling of PostgreSQL- compatible endpoints that require some additional configuration, such as Babelfish endpoints.

BabelfishDatabaseName -> (string)

The Babelfish for Aurora PostgreSQL database name for the endpoint.

DisableUnicodeSourceFilter -> (boolean)

Disables the Unicode source filter with PostgreSQL, for values passed into the Selection rule filter on Source Endpoint column values. By default DMS performs source filter comparisons using a Unicode string which can cause look ups to ignore the indexes in the text columns and slow down migrations.

Unicode support should only be disabled when using a selection rule filter is on a text column in the Source database that is indexed.

ServiceAccessRoleArn -> (string)

The IAM role arn you can use to authenticate the connection to your endpoint. Ensure to include `iam:PassRole` and `rds-db:connect` actions in permission policy.

AuthenticationMethod -> (string)

This attribute allows you to specify the authentication method as âiam authâ.

MySQLSettings -> (structure)

The settings for the MySQL source and target endpoint. For more information, see the `MySQLSettings` structure.

AfterConnectScript -> (string)

Specifies a script to run immediately after DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails.

For this parameter, provide the code of the script itself, not the name of a file containing the script.

CleanSourceMetadataOnMismatch -> (boolean)

Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.

DatabaseName -> (string)

Database name for the endpoint. For a MySQL source or target endpoint, donât explicitly specify the database using the `DatabaseName` request parameter on either the `CreateEndpoint` or `ModifyEndpoint` API call. Specifying `DatabaseName` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the DMS task.

EventsPollInterval -> (integer)

Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds.

Example: `eventsPollInterval=5;`

In the example, DMS checks for changes in the binary logs every five seconds.

TargetDbType -> (string)

Specifies where to migrate source tables on the target, either to a single database or multiple databases. If you specify `SPECIFIC_DATABASE` , specify the database name using the `DatabaseName` parameter of the `Endpoint` object.

Example: `targetDbType=MULTIPLE_DATABASES`

MaxFileSize -> (integer)

Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.

Example: `maxFileSize=512`

ParallelLoadThreads -> (integer)

Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.

Example: `parallelLoadThreads=1`

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port.

ServerName -> (string)

The host name of the endpoint database.

For an Amazon RDS MySQL instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) , in the `` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

For an Aurora MySQL instance, this is the output of [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) , in the `Endpoint` field.

ServerTimezone -> (string)

Specifies the time zone for the source MySQL database.

Example: `serverTimezone=US/Pacific;`

Note: Do not enclose time zones in single quotes.

Username -> (string)

Endpoint connection user name.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the MySQL endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the MySQL endpoint connection details.

ExecuteTimeout -> (integer)

Sets the client statement timeout (in seconds) for a MySQL source endpoint.

ServiceAccessRoleArn -> (string)

The IAM role you can use to authenticate when connecting to your endpoint. Ensure to include `iam:PassRole` and `rds-db:connect` actions in permission policy.

AuthenticationMethod -> (string)

This attribute allows you to specify the authentication method as âiam authâ.

OracleSettings -> (structure)

The settings for the Oracle source and target endpoint. For more information, see the `OracleSettings` structure.

AddSupplementalLogging -> (boolean)

Set this attribute to set up table-level supplemental logging for the Oracle database. This attribute enables PRIMARY KEY supplemental logging on all tables selected for a migration task.

If you use this option, you still need to enable database-level supplemental logging.

ArchivedLogDestId -> (integer)

Specifies the ID of the destination for the archived redo logs. This value should be the same as a number in the dest_id column of the v$archived_log view. If you work with an additional redo log destination, use the `AdditionalArchivedLogDestId` option to specify the additional destination ID. Doing this improves performance by ensuring that the correct logs are accessed from the outset.

AdditionalArchivedLogDestId -> (integer)

Set this attribute with `ArchivedLogDestId` in a primary/ standby setup. This attribute is useful in the case of a switchover. In this case, DMS needs to know which destination to get archive redo logs from to read changes. This need arises because the previous primary instance is now a standby instance after switchover.

Although DMS supports the use of the Oracle `RESETLOGS` option to open the database, never use `RESETLOGS` unless necessary. For additional information about `RESETLOGS` , see [RMAN Data Repair Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B) in the *Oracle Database Backup and Recovery Userâs Guide* .

ExtraArchivedLogDestIds -> (list)

Specifies the IDs of one more destinations for one or more archived redo logs. These IDs are the values of the `dest_id` column in the `v$archived_log` view. Use this setting with the `archivedLogDestId` extra connection attribute in a primary-to-single setup or a primary-to-multiple-standby setup.

This setting is useful in a switchover when you use an Oracle Data Guard database as a source. In this case, DMS needs information about what destination to get archive redo logs from to read changes. DMS needs this because after the switchover the previous primary is a standby instance. For example, in a primary-to-single standby setup you might apply the following settings.

`archivedLogDestId=1; ExtraArchivedLogDestIds=[2]`

In a primary-to-multiple-standby setup, you might apply the following settings.

`archivedLogDestId=1; ExtraArchivedLogDestIds=[2,3,4]`

Although DMS supports the use of the Oracle `RESETLOGS` option to open the database, never use `RESETLOGS` unless itâs necessary. For more information about `RESETLOGS` , see [RMAN Data Repair Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B) in the *Oracle Database Backup and Recovery Userâs Guide* .

(integer)

AllowSelectNestedTables -> (boolean)

Set this attribute to `true` to enable replication of Oracle tables containing columns that are nested tables or defined types.

ParallelAsmReadThreads -> (integer)

Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 2 (the default) and 8 (the maximum). Use this attribute together with the `readAheadBlocks` attribute.

ReadAheadBlocks -> (integer)

Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 1000 (the default) and 200,000 (the maximum).

AccessAlternateDirectly -> (boolean)

Set this attribute to `false` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to not access redo logs through any specified path prefix replacement using direct file access.

UseAlternateFolderForOnline -> (boolean)

Set this attribute to `true` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to use any specified prefix replacement to access all online redo logs.

OraclePathPrefix -> (string)

Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the default Oracle root used to access the redo logs.

UsePathPrefix -> (string)

Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the path prefix used to replace the default Oracle root to access the redo logs.

ReplacePathPrefix -> (boolean)

Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This setting tells DMS instance to replace the default Oracle root with the specified `usePathPrefix` setting to access the redo logs.

EnableHomogenousTablespace -> (boolean)

Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target.

DirectPathNoLog -> (boolean)

When set to `true` , this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs.

ArchivedLogsOnly -> (boolean)

When this field is set to `True` , DMS only accesses the archived redo logs. If the archived redo logs are stored on Automatic Storage Management (ASM) only, the DMS user account needs to be granted ASM privileges.

AsmPassword -> (string)

For an Oracle source endpoint, your Oracle Automatic Storage Management (ASM) password. You can set this value from the `` *asm_user_password* `` value. You set this value as part of the comma-separated value that you set to the `Password` request parameter when you create the endpoint to access transaction logs using Binary Reader. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration) .

AsmServer -> (string)

For an Oracle source endpoint, your ASM server address. You can set this value from the `asm_server` value. You set `asm_server` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration) .

AsmUser -> (string)

For an Oracle source endpoint, your ASM user name. You can set this value from the `asm_user` value. You set `asm_user` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration) .

CharLengthSemantics -> (string)

Specifies whether the length of a character column is in bytes or in characters. To indicate that the character column length is in characters, set this attribute to `CHAR` . Otherwise, the character column length is in bytes.

Example: `charLengthSemantics=CHAR;`

DatabaseName -> (string)

Database name for the endpoint.

DirectPathParallelLoad -> (boolean)

When set to `true` , this attribute specifies a parallel load when `useDirectPathFullLoad` is set to `Y` . This attribute also only applies when you use the DMS parallel load feature. Note that the target table cannot have any constraints or indexes.

FailTasksOnLobTruncation -> (boolean)

When set to `true` , this attribute causes a task to fail if the actual size of an LOB column is greater than the specified `LobMaxSize` .

If a task is set to limited LOB mode and this option is set to `true` , the task fails instead of truncating the LOB data.

NumberDatatypeScale -> (integer)

Specifies the number scale. You can select a scale up to 38, or you can select FLOAT. By default, the NUMBER data type is converted to precision 38, scale 10.

Example: `numberDataTypeScale=12`

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port.

ReadTableSpaceName -> (boolean)

When set to `true` , this attribute supports tablespace replication.

RetryInterval -> (integer)

Specifies the number of seconds that the system waits before resending a query.

Example: `retryInterval=6;`

SecurityDbEncryption -> (string)

For an Oracle source endpoint, the transparent data encryption (TDE) password required by AWM DMS to access Oracle redo logs encrypted by TDE using Binary Reader. It is also the `` *TDE_Password* `` part of the comma-separated value you set to the `Password` request parameter when you create the endpoint. The `SecurityDbEncryptian` setting is related to this `SecurityDbEncryptionName` setting. For more information, see [Supported encryption methods for using Oracle as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption) in the *Database Migration Service User Guide* .

SecurityDbEncryptionName -> (string)

For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE. The key value is the value of the `SecurityDbEncryption` setting. For more information on setting the key name value of `SecurityDbEncryptionName` , see the information and example for setting the `securityDbEncryptionName` extra connection attribute in [Supported encryption methods for using Oracle as a source for DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption) in the *Database Migration Service User Guide* .

ServerName -> (string)

Fully qualified domain name of the endpoint.

For an Amazon RDS Oracle instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) , in the `` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

SpatialDataOptionToGeoJsonFunctionName -> (string)

Use this attribute to convert `SDO_GEOMETRY` to `GEOJSON` format. By default, DMS calls the `SDO2GEOJSON` custom function if present and accessible. Or you can create your own custom function that mimics the operation of `SDOGEOJSON` and set `SpatialDataOptionToGeoJsonFunctionName` to call it instead.

StandbyDelayTime -> (integer)

Use this attribute to specify a time in minutes for the delay in standby sync. If the source is an Oracle Active Data Guard standby database, use this attribute to specify the time lag between primary and standby databases.

In DMS, you can create an Oracle CDC task that uses an Active Data Guard standby instance as a source for replicating ongoing changes. Doing this eliminates the need to connect to an active database that might be in production.

Username -> (string)

Endpoint connection user name.

UseBFile -> (boolean)

Set this attribute to True to capture change data using the Binary Reader utility. Set `UseLogminerReader` to False to set this attribute to True. To use Binary Reader with Amazon RDS for Oracle as the source, you set additional attributes. For more information about using this setting with Oracle Automatic Storage Management (ASM), see [Using Oracle LogMiner or DMS Binary Reader for CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC) .

UseDirectPathFullLoad -> (boolean)

Set this attribute to True to have DMS use a direct path full load. Specify this value to use the direct path protocol in the Oracle Call Interface (OCI). By using this OCI protocol, you can bulk-load Oracle target tables during a full load.

UseLogminerReader -> (boolean)

Set this attribute to True to capture change data using the Oracle LogMiner utility (the default). Set this attribute to False if you want to access the redo logs as a binary file. When you set `UseLogminerReader` to False, also set `UseBfile` to True. For more information on this setting and using Oracle ASM, see [Using Oracle LogMiner or DMS Binary Reader for CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC) in the *DMS User Guide* .

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the Oracle endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Oracle endpoint connection details.

SecretsManagerOracleAsmAccessRoleArn -> (string)

Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the `SecretsManagerOracleAsmSecret` . This `SecretsManagerOracleAsmSecret` has the secret value that allows access to the Oracle ASM of the endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerOracleAsmSecretId` . Or you can specify clear-text values for `AsmUser` , `AsmPassword` , and `AsmServerName` . You canât specify both. For more information on creating this `SecretsManagerOracleAsmSecret` and the `SecretsManagerOracleAsmAccessRoleArn` and `SecretsManagerOracleAsmSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerOracleAsmSecretId -> (string)

Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the `SecretsManagerOracleAsmSecret` that contains the Oracle ASM connection details for the Oracle endpoint.

TrimSpaceInChar -> (boolean)

Use the `TrimSpaceInChar` source endpoint setting to trim data on CHAR and NCHAR data types during migration. The default value is `true` .

ConvertTimestampWithZoneToUTC -> (boolean)

When true, converts timestamps with the `timezone` datatype to their UTC value.

OpenTransactionWindow -> (integer)

The timeframe in minutes to check for open transactions for a CDC-only task.

You can specify an integer value between 0 (the default) and 240 (the maximum).

### Note

This parameter is only valid in DMS version 3.5.0 and later.

AuthenticationMethod -> (string)

Specifies the authentication method to be used with Oracle.

SybaseSettings -> (structure)

The settings for the SAP ASE source and target endpoint. For more information, see the `SybaseSettings` structure.

DatabaseName -> (string)

Database name for the endpoint.

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port. The default is 5000.

ServerName -> (string)

Fully qualified domain name of the endpoint.

Username -> (string)

Endpoint connection user name.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the SAP ASE endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the SAP SAE endpoint connection details.

MicrosoftSQLServerSettings -> (structure)

The settings for the Microsoft SQL Server source and target endpoint. For more information, see the `MicrosoftSQLServerSettings` structure.

Port -> (integer)

Endpoint TCP port.

BcpPacketSize -> (integer)

The maximum size of the packets (in bytes) used to transfer data using BCP.

DatabaseName -> (string)

Database name for the endpoint.

ControlTablesFileGroup -> (string)

Specifies a file group for the DMS internal tables. When the replication task starts, all the internal DMS control tables ([awsdms_](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html#id7) apply_exception, awsdms_apply, awsdms_changes) are created for the specified file group.

Password -> (string)

Endpoint connection password.

QuerySingleAlwaysOnNode -> (boolean)

Cleans and recreates table metadata information on the replication instance when a mismatch occurs. An example is a situation where running an alter DDL statement on a table might result in different information about the table cached in the replication instance.

ReadBackupOnly -> (boolean)

When this attribute is set to `Y` , DMS only reads changes from transaction log backups and doesnât read from the active transaction log file during ongoing replication. Setting this parameter to `Y` enables you to control active transaction log file growth during full load and ongoing replication tasks. However, it can add some source latency to ongoing replication.

SafeguardPolicy -> (string)

Use this attribute to minimize the need to access the backup log and enable DMS to prevent truncation using one of the following two methods.

*Start transactions in the database:* This is the default method. When this method is used, DMS prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started arenât truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method.

*Exclusively use sp_repldone within a single task* : When this method is used, DMS reads the changes and then uses sp_repldone to mark the TLOG transactions as ready for truncation. Although this method doesnât involve any transactional activities, it can only be used when Microsoft Replication isnât running. Also, when using this method, only one DMS task can access the database at any given time. Therefore, if you need to run parallel DMS tasks against the same database, use the default method.

ServerName -> (string)

Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) , in the `` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

Username -> (string)

Endpoint connection user name.

UseBcpFullLoad -> (boolean)

Use this to attribute to transfer data for full-load operations using BCP. When the target table contains an identity column that does not exist in the source table, you must disable the use BCP for loading table option.

UseThirdPartyBackupDevice -> (boolean)

When this attribute is set to `Y` , DMS processes third-party transaction log backups if they are created in native format.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the SQL Server endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the SQL Server endpoint connection details.

TrimSpaceInChar -> (boolean)

Use the `TrimSpaceInChar` source endpoint setting to right-trim data on CHAR and NCHAR data types during migration. Setting `TrimSpaceInChar` does not left-trim data. The default value is `true` .

TlogAccessMode -> (string)

Indicates the mode used to fetch CDC data.

ForceLobLookup -> (boolean)

Forces LOB lookup on inline LOB.

AuthenticationMethod -> (string)

Specifies the authentication method to be used with Microsoft SQL Server.

IBMDb2Settings -> (structure)

The settings for the IBM Db2 LUW source endpoint. For more information, see the `IBMDb2Settings` structure.

DatabaseName -> (string)

Database name for the endpoint.

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port. The default value is 50000.

ServerName -> (string)

Fully qualified domain name of the endpoint.

SetDataCaptureChanges -> (boolean)

Enables ongoing replication (CDC) as a BOOLEAN value. The default is true.

CurrentLsn -> (string)

For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.

MaxKBytesPerRead -> (integer)

Maximum number of bytes per read, as a NUMBER value. The default is 64 KB.

Username -> (string)

Endpoint connection user name.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the Db2 LUW endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Db2 LUW endpoint connection details.

LoadTimeout -> (integer)

The amount of time (in milliseconds) before DMS times out operations performed by DMS on the Db2 target. The default value is 1200 (20 minutes).

WriteBufferSize -> (integer)

The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk on the DMS replication instance. The default value is 1024 (1 MB).

MaxFileSize -> (integer)

Specifies the maximum size (in KB) of .csv files used to transfer data to Db2 LUW.

KeepCsvFiles -> (boolean)

If true, DMS saves any .csv files to the Db2 LUW target that were used to replicate data. DMS uses these files for analysis and troubleshooting.

The default value is false.

DocDbSettings -> (structure)

Provides information that defines a DocumentDB endpoint.

Username -> (string)

The user name you use to access the DocumentDB source endpoint.

Password -> (string)

The password for the user account you use to access the DocumentDB source endpoint.

ServerName -> (string)

The name of the server on the DocumentDB source endpoint.

Port -> (integer)

The port value for the DocumentDB source endpoint.

DatabaseName -> (string)

The database name on the DocumentDB source endpoint.

NestingLevel -> (string)

Specifies either document or table mode.

Default value is `"none"` . Specify `"none"` to use document mode. Specify `"one"` to use table mode.

ExtractDocId -> (boolean)

Specifies the document ID. Use this setting when `NestingLevel` is set to `"none"` .

Default value is `"false"` .

DocsToInvestigate -> (integer)

Indicates the number of documents to preview to determine the document organization. Use this setting when `NestingLevel` is set to `"one"` .

Must be a positive value greater than `0` . Default value is `1000` .

KmsKeyId -> (string)

The KMS key identifier that is used to encrypt the content on the replication instance. If you donât specify a value for the `KmsKeyId` parameter, then DMS uses your default encryption key. KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret` . The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the DocumentDB endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *Database Migration Service User Guide* .

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the DocumentDB endpoint connection details.

UseUpdateLookUp -> (boolean)

If `true` , DMS retrieves the entire document from the DocumentDB source during migration. This may cause a migration failure if the server response exceeds bandwidth limits. To fetch only updates and deletes during migration, set this parameter to `false` .

ReplicateShardCollections -> (boolean)

If `true` , DMS replicates data to shard collections. DMS only uses this setting if the target endpoint is a DocumentDB elastic cluster.

When this setting is `true` , note the following:

- You must set `TargetTablePrepMode` to `nothing` .
- DMS automatically sets `useUpdateLookup` to `false` .

RedisSettings -> (structure)

The settings for the Redis target endpoint. For more information, see the `RedisSettings` structure.

ServerName -> (string)

Fully qualified domain name of the endpoint.

Port -> (integer)

Transmission Control Protocol (TCP) port for the endpoint.

SslSecurityProtocol -> (string)

The connection to a Redis target endpoint using Transport Layer Security (TLS). Valid values include `plaintext` and `ssl-encryption` . The default is `ssl-encryption` . The `ssl-encryption` option makes an encrypted connection. Optionally, you can identify an Amazon Resource Name (ARN) for an SSL certificate authority (CA) using the `SslCaCertificateArn` setting. If an ARN isnât given for a CA, DMS uses the Amazon root CA.

The `plaintext` option doesnât provide Transport Layer Security (TLS) encryption for traffic between endpoint and database.

AuthType -> (string)

The type of authentication to perform when connecting to a Redis target. Options include `none` , `auth-token` , and `auth-role` . The `auth-token` option requires an `AuthPassword` value to be provided. The `auth-role` option requires `AuthUserName` and `AuthPassword` values to be provided.

AuthUserName -> (string)

The user name provided with the `auth-role` option of the `AuthType` setting for a Redis target endpoint.

AuthPassword -> (string)

The password provided with the `auth-role` and `auth-token` options of the `AuthType` setting for a Redis target endpoint.

SslCaCertificateArn -> (string)

The Amazon Resource Name (ARN) for the certificate authority (CA) that DMS uses to connect to your Redis target endpoint.

GcpMySQLSettings -> (structure)

Settings in JSON format for the source GCP MySQL endpoint.

AfterConnectScript -> (string)

Specifies a script to run immediately after DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails.

For this parameter, provide the code of the script itself, not the name of a file containing the script.

CleanSourceMetadataOnMismatch -> (boolean)

Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.

DatabaseName -> (string)

Database name for the endpoint. For a MySQL source or target endpoint, donât explicitly specify the database using the `DatabaseName` request parameter on either the `CreateEndpoint` or `ModifyEndpoint` API call. Specifying `DatabaseName` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the DMS task.

EventsPollInterval -> (integer)

Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds.

Example: `eventsPollInterval=5;`

In the example, DMS checks for changes in the binary logs every five seconds.

TargetDbType -> (string)

Specifies where to migrate source tables on the target, either to a single database or multiple databases.

Example: `targetDbType=MULTIPLE_DATABASES`

MaxFileSize -> (integer)

Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.

Example: `maxFileSize=512`

ParallelLoadThreads -> (integer)

Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.

Example: `parallelLoadThreads=1`

Password -> (string)

Endpoint connection password.

Port -> (integer)

Endpoint TCP port.

ServerName -> (string)

The MySQL host name.

ServerTimezone -> (string)

Specifies the time zone for the source MySQL database.

Example: `serverTimezone=US/Pacific;`

Note: Do not enclose time zones in single quotes.

Username -> (string)

Endpoint connection user name.

SecretsManagerAccessRoleArn -> (string)

The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret.` The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the Amazon Web Services Secrets Manager secret that allows access to the MySQL endpoint.

### Note

You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId` . Or you can specify clear-text values for `UserName` , `Password` , `ServerName` , and `Port` . You canât specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the Database Migration Service User Guide.

SecretsManagerSecretId -> (string)

The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the MySQL endpoint connection details.

TimestreamSettings -> (structure)

The settings for the Amazon Timestream target endpoint. For more information, see the `TimestreamSettings` structure.

DatabaseName -> (string)

Database name for the endpoint.

MemoryDuration -> (integer)

Set this attribute to specify the length of time to store all of the tables in memory that are migrated into Amazon Timestream from the source database. Time is measured in units of hours. When Timestream data comes in, it first resides in memory for the specified duration, which allows quick access to it.

MagneticDuration -> (integer)

Set this attribute to specify the default magnetic duration applied to the Amazon Timestream tables in days. This is the number of days that records remain in magnetic store before being discarded. For more information, see [Storage](https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html) in the [Amazon Timestream Developer Guide](https://docs.aws.amazon.com/timestream/latest/developerguide/) .

CdcInsertsAndUpdates -> (boolean)

Set this attribute to `true` to specify that DMS only applies inserts and updates, and not deletes. Amazon Timestream does not allow deleting records, so if this value is `false` , DMS nulls out the corresponding record in the Timestream database rather than deleting it.

EnableMagneticStoreWrites -> (boolean)

Set this attribute to `true` to enable memory store writes. When this value is `false` , DMS does not write records that are older in days than the value specified in `MagneticDuration` , because Amazon Timestream does not allow memory writes by default. For more information, see [Storage](https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html) in the [Amazon Timestream Developer Guide](https://docs.aws.amazon.com/timestream/latest/developerguide/) .