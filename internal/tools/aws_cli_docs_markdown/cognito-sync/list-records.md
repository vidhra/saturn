# list-recordsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/list-records.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/list-records.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-sync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/index.html#cli-aws-cognito-sync) ]

# list-records

## Description

Gets paginated records, optionally changed after a particular sync count for a dataset and identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.

ListRecords can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/ListRecords)

## Synopsis

```
list-records
--identity-pool-id <value>
--identity-id <value>
--dataset-name <value>
[--last-sync-count <value>]
[--next-token <value>]
[--max-results <value>]
[--sync-session-token <value>]
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

`--identity-pool-id` (string)
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

`--identity-id` (string)
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

`--dataset-name` (string)
A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, â_â (underscore), â-â (dash), and â.â (dot).

`--last-sync-count` (long)
The last server sync count for this record.

`--next-token` (string)
A pagination token for obtaining the next page of results.

`--max-results` (integer)
The maximum number of results to be returned.

`--sync-session-token` (string)
A token containing a session ID, identity ID, and expiration.

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

Records -> (list)

A list of all records.

(structure)

The basic data structure of a dataset.

Key -> (string)

The key for the record.

Value -> (string)

The value for the record.

SyncCount -> (long)

The server sync count for this record.

LastModifiedDate -> (timestamp)

The date on which the record was last modified.

LastModifiedBy -> (string)

The user/device that made the last change to this record.

DeviceLastModifiedDate -> (timestamp)

The last modified date of the client device.

NextToken -> (string)

A pagination token for obtaining the next page of results.

Count -> (integer)

Total number of records.

DatasetSyncCount -> (long)

Server sync count for this dataset.

LastModifiedBy -> (string)

The user/device that made the last change to this record.

MergedDatasetNames -> (list)

Names of merged datasets.

(string)

DatasetExists -> (boolean)

Indicates whether the dataset exists.

DatasetDeletedAfterRequestedSyncCount -> (boolean)

A boolean value specifying whether to delete the dataset locally.

SyncSessionToken -> (string)

A token containing a session ID, identity ID, and expiration.