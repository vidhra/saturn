# delete-recordÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/delete-record.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/delete-record.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-featurestore-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/index.html#cli-aws-sagemaker-featurestore-runtime) ]

# delete-record

## Description

Deletes a `Record` from a `FeatureGroup` in the `OnlineStore` . Feature Store supports both `SoftDelete` and `HardDelete` . For `SoftDelete` (default), feature columns are set to `null` and the record is no longer retrievable by `GetRecord` or `BatchGetRecord` . For `HardDelete` , the complete `Record` is removed from the `OnlineStore` . In both cases, Feature Store appends the deleted record marker to the `OfflineStore` . The deleted record marker is a record with the same `RecordIdentifer` as the original, but with `is_deleted` value set to `True` , `EventTime` set to the delete input `EventTime` , and other feature values set to `null` .

Note that the `EventTime` specified in `DeleteRecord` should be set later than the `EventTime` of the existing record in the `OnlineStore` for that `RecordIdentifer` . If it is not, the deletion does not occur:

- For `SoftDelete` , the existing (not deleted) record remains in the `OnlineStore` , though the delete record marker is still written to the `OfflineStore` .
- `HardDelete` returns `EventTime` : `400 ValidationException` to indicate that the delete operation failed. No delete record marker is written to the `OfflineStore` .

When a record is deleted from the `OnlineStore` , the deleted record marker is appended to the `OfflineStore` . If you have the Iceberg table format enabled for your `OfflineStore` , you can remove all history of a record from the `OfflineStore` using Amazon Athena or Apache Spark. For information on how to hard delete a record from the `OfflineStore` with the Iceberg table format enabled, see [Delete records from the offline store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-delete-records-offline-store.html#feature-store-delete-records-offline-store) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)

## Synopsis

```
delete-record
--feature-group-name <value>
--record-identifier-value-as-string <value>
--event-time <value>
[--target-stores <value>]
[--deletion-mode <value>]
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

`--feature-group-name` (string)

The name or Amazon Resource Name (ARN) of the feature group to delete the record from.

`--record-identifier-value-as-string` (string)

The value for the `RecordIdentifier` that uniquely identifies the record, in string format.

`--event-time` (string)

Timestamp indicating when the deletion event occurred. `EventTime` can be used to query data at a certain point in time.

`--target-stores` (list)

A list of stores from which youâre deleting the record. By default, Feature Store deletes the record from all of the stores that youâre using for the `FeatureGroup` .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  OnlineStore
  OfflineStore
```

`--deletion-mode` (string)

The name of the deletion mode for deleting the record. By default, the deletion mode is set to `SoftDelete` .

Possible values:

- `SoftDelete`
- `HardDelete`

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

None