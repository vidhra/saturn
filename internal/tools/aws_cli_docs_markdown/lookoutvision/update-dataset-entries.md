# update-dataset-entriesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/update-dataset-entries.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/update-dataset-entries.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutvision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/index.html#cli-aws-lookoutvision) ]

# update-dataset-entries

## Description

Adds or updates one or more JSON Line entries in a dataset. A JSON Line includes information about an image used for training or testing an Amazon Lookout for Vision model.

To update an existing JSON Line, use the `source-ref` field to identify the JSON Line. The JSON line that you supply replaces the existing JSON line. Any existing annotations that are not in the new JSON line are removed from the dataset.

For more information, see *Defining JSON lines for anomaly classification* in the Amazon Lookout for Vision Developer Guide.

### Note

The images you reference in the `source-ref` field of a JSON line, must be in the same S3 bucket as the existing images in the dataset.

Updating a dataset might take a while to complete. To check the current status, call  DescribeDataset and check the `Status` field in the response.

This operation requires permissions to perform the `lookoutvision:UpdateDatasetEntries` operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutvision-2020-11-20/UpdateDatasetEntries)

## Synopsis

```
update-dataset-entries
--project-name <value>
--dataset-type <value>
--changes <value>
[--client-token <value>]
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

`--project-name` (string)

The name of the project that contains the dataset that you want to update.

`--dataset-type` (string)

The type of the dataset that you want to update. Specify `train` to update the training dataset. Specify `test` to update the test dataset. If you have a single dataset project, specify `train` .

`--changes` (blob)

The entries to add to the dataset.

`--client-token` (string)

ClientToken is an idempotency token that ensures a call to `UpdateDatasetEntries` completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from `UpdateDatasetEntries` . In this case, safely retry your call to `UpdateDatasetEntries` by using the same `ClientToken` parameter value.

If you donât supply a value for `ClientToken` , the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple updates with the same dataset entries. Youâll need to provide your own value for other use cases.

An error occurs if the other input parameters are not the same as in the first request. Using a different value for `ClientToken` is considered a new call to `UpdateDatasetEntries` . An idempotency token is active for 8 hours.

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

Status -> (string)

The status of the dataset update.