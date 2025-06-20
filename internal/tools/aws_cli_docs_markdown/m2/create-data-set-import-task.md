# create-data-set-import-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/create-data-set-import-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/create-data-set-import-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [m2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/index.html#cli-aws-m2) ]

# create-data-set-import-task

## Description

Starts a data set import task for a specific application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/m2-2021-04-28/CreateDataSetImportTask)

## Synopsis

```
create-data-set-import-task
--application-id <value>
[--client-token <value>]
--import-config <value>
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

`--application-id` (string)

The unique identifier of the application for which you want to import data sets.

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set import. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.

`--import-config` (tagged union structure)

The data set import task configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dataSets`, `s3Location`.

dataSets -> (list)

The data sets.

(structure)

Identifies a specific data set to import from an external location.

dataSet -> (structure)

The data set.

datasetName -> (string)

The logical identifier for a specific data set (in mainframe format).

datasetOrg -> (tagged union structure)

The type of dataset. The only supported value is VSAM.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `gdg`, `po`, `ps`, `vsam`.

gdg -> (structure)

The generation data group of the data set.

limit -> (integer)

The maximum number of generation data sets, up to 255, in a GDG.

rollDisposition -> (string)

The disposition of the data set in the catalog.

po -> (structure)

The details of a PO type data set.

encoding -> (string)

The character set encoding of the data set.

format -> (string)

The format of the data set records.

memberFileExtensions -> (list)

An array containing one or more filename extensions, allowing you to specify which files to be included as PDS member.

(string)

ps -> (structure)

The details of a PS type data set.

encoding -> (string)

The character set encoding of the data set.

format -> (string)

The format of the data set records.

vsam -> (structure)

The details of a VSAM data set.

alternateKeys -> (list)

The alternate key definitions, if any. A legacy dataset might not have any alternate key defined, but if those alternate keys definitions exist, provide them as some applications will make use of them.

(structure)

Defines an alternate key. This value is optional. A legacy data set might not have any alternate key defined but if those alternate keys definitions exist, provide them, as some applications will make use of them.

allowDuplicates -> (boolean)

Indicates whether the alternate key values are supposed to be unique for the given data set.

length -> (integer)

A strictly positive integer value representing the length of the alternate key.

name -> (string)

The name of the alternate key.

offset -> (integer)

A positive integer value representing the offset to mark the start of the alternate key part in the record byte array.

compressed -> (boolean)

Indicates whether indexes for this dataset are stored as compressed values. If you have a large data set (typically > 100 Mb), consider setting this flag to True.

encoding -> (string)

The character set used by the data set. Can be ASCII, EBCDIC, or unknown.

format -> (string)

The record format of the data set.

primaryKey -> (structure)

The primary key of the data set.

length -> (integer)

A strictly positive integer value representing the length of the primary key.

name -> (string)

A name for the Primary Key.

offset -> (integer)

A positive integer value representing the offset to mark the start of the primary key in the record byte array.

recordLength -> (structure)

The length of a record.

max -> (integer)

The maximum record length. In case of fixed, both minimum and maximum are the same.

min -> (integer)

The minimum record length of a record.

relativePath -> (string)

The relative location of the data set in the database or file system.

storageType -> (string)

The storage type of the data set: database or file system. For Micro Focus, database corresponds to datastore and file system corresponds to EFS/FSX. For Blu Age, there is no support of file system and database corresponds to Blusam.

externalLocation -> (tagged union structure)

The location of the data set.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3Location`.

s3Location -> (string)

The URI of the Amazon S3 bucket.

s3Location -> (string)

The Amazon S3 location of the data sets.

JSON Syntax:

```
{
  "dataSets": [
    {
      "dataSet": {
        "datasetName": "string",
        "datasetOrg": {
          "gdg": {
            "limit": integer,
            "rollDisposition": "string"
          },
          "po": {
            "encoding": "string",
            "format": "string",
            "memberFileExtensions": ["string", ...]
          },
          "ps": {
            "encoding": "string",
            "format": "string"
          },
          "vsam": {
            "alternateKeys": [
              {
                "allowDuplicates": true|false,
                "length": integer,
                "name": "string",
                "offset": integer
              }
              ...
            ],
            "compressed": true|false,
            "encoding": "string",
            "format": "string",
            "primaryKey": {
              "length": integer,
              "name": "string",
              "offset": integer
            }
          }
        },
        "recordLength": {
          "max": integer,
          "min": integer
        },
        "relativePath": "string",
        "storageType": "string"
      },
      "externalLocation": {
        "s3Location": "string"
      }
    }
    ...
  ],
  "s3Location": "string"
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

taskId -> (string)

The task identifier. This operation is asynchronous. Use this identifier with the  GetDataSetImportTask operation to obtain the status of this task.