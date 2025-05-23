# update-datasetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-dataset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-dataset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [databrew](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/index.html#cli-aws-databrew) ]

# update-dataset

## Description

Modifies the definition of an existing DataBrew dataset.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/databrew-2017-07-25/UpdateDataset)

## Synopsis

```
update-dataset
--name <value>
[--format <value>]
[--format-options <value>]
--input <value>
[--path-options <value>]
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

`--name` (string)

The name of the dataset to be updated.

`--format` (string)

The file format of a dataset that is created from an Amazon S3 file or folder.

Possible values:

- `CSV`
- `JSON`
- `PARQUET`
- `EXCEL`
- `ORC`

`--format-options` (structure)

Represents a set of options that define the structure of either comma-separated value (CSV), Excel, or JSON input.

Json -> (structure)

Options that define how JSON input is to be interpreted by DataBrew.

MultiLine -> (boolean)

A value that specifies whether JSON input contains embedded new line characters.

Excel -> (structure)

Options that define how Excel input is to be interpreted by DataBrew.

SheetNames -> (list)

One or more named sheets in the Excel file that will be included in the dataset.

(string)

SheetIndexes -> (list)

One or more sheet numbers in the Excel file that will be included in the dataset.

(integer)

HeaderRow -> (boolean)

A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.

Csv -> (structure)

Options that define how CSV input is to be interpreted by DataBrew.

Delimiter -> (string)

A single character that specifies the delimiter being used in the CSV file.

HeaderRow -> (boolean)

A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.

Shorthand Syntax:

```
Json={MultiLine=boolean},Excel={SheetNames=[string,string],SheetIndexes=[integer,integer],HeaderRow=boolean},Csv={Delimiter=string,HeaderRow=boolean}
```

JSON Syntax:

```
{
  "Json": {
    "MultiLine": true|false
  },
  "Excel": {
    "SheetNames": ["string", ...],
    "SheetIndexes": [integer, ...],
    "HeaderRow": true|false
  },
  "Csv": {
    "Delimiter": "string",
    "HeaderRow": true|false
  }
}
```

`--input` (structure)

Represents information on how DataBrew can find data, in either the Glue Data Catalog or Amazon S3.

S3InputDefinition -> (structure)

The Amazon S3 location where the data is stored.

Bucket -> (string)

The Amazon S3 bucket name.

Key -> (string)

The unique name of the object in the bucket.

BucketOwner -> (string)

The Amazon Web Services account ID of the bucket owner.

DataCatalogInputDefinition -> (structure)

The Glue Data Catalog parameters for the data.

CatalogId -> (string)

The unique identifier of the Amazon Web Services account that holds the Data Catalog that stores the data.

DatabaseName -> (string)

The name of a database in the Data Catalog.

TableName -> (string)

The name of a database table in the Data Catalog. This table corresponds to a DataBrew dataset.

TempDirectory -> (structure)

Represents an Amazon location where DataBrew can store intermediate results.

Bucket -> (string)

The Amazon S3 bucket name.

Key -> (string)

The unique name of the object in the bucket.

BucketOwner -> (string)

The Amazon Web Services account ID of the bucket owner.

DatabaseInputDefinition -> (structure)

Connection information for dataset input files stored in a database.

GlueConnectionName -> (string)

The Glue Connection that stores the connection information for the target database.

DatabaseTableName -> (string)

The table within the target database.

TempDirectory -> (structure)

Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read input data, or write output from a job.

Bucket -> (string)

The Amazon S3 bucket name.

Key -> (string)

The unique name of the object in the bucket.

BucketOwner -> (string)

The Amazon Web Services account ID of the bucket owner.

QueryString -> (string)

Custom SQL to run against the provided Glue connection. This SQL will be used as the input for DataBrew projects and jobs.

Metadata -> (structure)

Contains additional resource information needed for specific datasets.

SourceArn -> (string)

The Amazon Resource Name (ARN) associated with the dataset. Currently, DataBrew only supports ARNs from Amazon AppFlow.

Shorthand Syntax:

```
S3InputDefinition={Bucket=string,Key=string,BucketOwner=string},DataCatalogInputDefinition={CatalogId=string,DatabaseName=string,TableName=string,TempDirectory={Bucket=string,Key=string,BucketOwner=string}},DatabaseInputDefinition={GlueConnectionName=string,DatabaseTableName=string,TempDirectory={Bucket=string,Key=string,BucketOwner=string},QueryString=string},Metadata={SourceArn=string}
```

JSON Syntax:

```
{
  "S3InputDefinition": {
    "Bucket": "string",
    "Key": "string",
    "BucketOwner": "string"
  },
  "DataCatalogInputDefinition": {
    "CatalogId": "string",
    "DatabaseName": "string",
    "TableName": "string",
    "TempDirectory": {
      "Bucket": "string",
      "Key": "string",
      "BucketOwner": "string"
    }
  },
  "DatabaseInputDefinition": {
    "GlueConnectionName": "string",
    "DatabaseTableName": "string",
    "TempDirectory": {
      "Bucket": "string",
      "Key": "string",
      "BucketOwner": "string"
    },
    "QueryString": "string"
  },
  "Metadata": {
    "SourceArn": "string"
  }
}
```

`--path-options` (structure)

A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.

LastModifiedDateCondition -> (structure)

If provided, this structure defines a date range for matching Amazon S3 objects based on their LastModifiedDate attribute in Amazon S3.

Expression -> (string)

The expression which includes condition names followed by substitution variables, possibly grouped and combined with other conditions. For example, â(starts_with :prefix1 or starts_with :prefix2) and (ends_with :suffix1 or ends_with :suffix2)â. Substitution variables should start with â:â symbol.

ValuesMap -> (map)

The map of substitution variable names to their values used in this filter expression.

key -> (string)

value -> (string)

FilesLimit -> (structure)

If provided, this structure imposes a limit on a number of files that should be selected.

MaxFiles -> (integer)

The number of Amazon S3 files to select.

OrderedBy -> (string)

A criteria to use for Amazon S3 files sorting before their selection. By default uses LAST_MODIFIED_DATE as a sorting criteria. Currently itâs the only allowed value.

Order -> (string)

A criteria to use for Amazon S3 files sorting before their selection. By default uses DESCENDING order, i.e. most recent files are selected first. Another possible value is ASCENDING.

Parameters -> (map)

A structure that maps names of parameters used in the Amazon S3 path of a dataset to their definitions.

key -> (string)

value -> (structure)

Represents a dataset parameter that defines type and conditions for a parameter in the Amazon S3 path of the dataset.

Name -> (string)

The name of the parameter that is used in the datasetâs Amazon S3 path.

Type -> (string)

The type of the dataset parameter, can be one of a âStringâ, âNumberâ or âDatetimeâ.

DatetimeOptions -> (structure)

Additional parameter options such as a format and a timezone. Required for datetime parameters.

Format -> (string)

Required option, that defines the datetime format used for a date parameter in the Amazon S3 path. Should use only supported datetime specifiers and separation characters, all literal a-z or A-Z characters should be escaped with single quotes. E.g. âMM.dd.yyyy-âatâ-HH:mmâ.

TimezoneOffset -> (string)

Optional value for a timezone offset of the datetime parameter value in the Amazon S3 path. Shouldnât be used if Format for this parameter includes timezone fields. If no offset specified, UTC is assumed.

LocaleCode -> (string)

Optional value for a non-US locale code, needed for correct interpretation of some date formats.

CreateColumn -> (boolean)

Optional boolean value that defines whether the captured value of this parameter should be used to create a new column in a dataset.

Filter -> (structure)

The optional filter expression structure to apply additional matching criteria to the parameter.

Expression -> (string)

The expression which includes condition names followed by substitution variables, possibly grouped and combined with other conditions. For example, â(starts_with :prefix1 or starts_with :prefix2) and (ends_with :suffix1 or ends_with :suffix2)â. Substitution variables should start with â:â symbol.

ValuesMap -> (map)

The map of substitution variable names to their values used in this filter expression.

key -> (string)

value -> (string)

Shorthand Syntax:

```
LastModifiedDateCondition={Expression=string,ValuesMap={KeyName1=string,KeyName2=string}},FilesLimit={MaxFiles=integer,OrderedBy=string,Order=string},Parameters={KeyName1={Name=string,Type=string,DatetimeOptions={Format=string,TimezoneOffset=string,LocaleCode=string},CreateColumn=boolean,Filter={Expression=string,ValuesMap={KeyName1=string,KeyName2=string}}},KeyName2={Name=string,Type=string,DatetimeOptions={Format=string,TimezoneOffset=string,LocaleCode=string},CreateColumn=boolean,Filter={Expression=string,ValuesMap={KeyName1=string,KeyName2=string}}}}
```

JSON Syntax:

```
{
  "LastModifiedDateCondition": {
    "Expression": "string",
    "ValuesMap": {"string": "string"
      ...}
  },
  "FilesLimit": {
    "MaxFiles": integer,
    "OrderedBy": "LAST_MODIFIED_DATE",
    "Order": "DESCENDING"|"ASCENDING"
  },
  "Parameters": {"string": {
        "Name": "string",
        "Type": "Datetime"|"Number"|"String",
        "DatetimeOptions": {
          "Format": "string",
          "TimezoneOffset": "string",
          "LocaleCode": "string"
        },
        "CreateColumn": true|false,
        "Filter": {
          "Expression": "string",
          "ValuesMap": {"string": "string"
            ...}
        }
      }
    ...}
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

## Output

Name -> (string)

The name of the dataset that you updated.