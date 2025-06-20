# disableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/disable.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/disable.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# disable

## Description

Disables Amazon Inspector scans for one or more Amazon Web Services accounts. Disabling all scan types in an account disables the Amazon Inspector service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/Disable)

## Synopsis

```
disable
[--account-ids <value>]
[--resource-types <value>]
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

`--account-ids` (list)

An array of account IDs you want to disable Amazon Inspector scans for.

(string)

Syntax:

```
"string" "string" ...
```

`--resource-types` (list)

The resource scan types you want to disable.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  EC2
  ECR
  LAMBDA
  LAMBDA_CODE
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

accounts -> (list)

Information on the accounts that have had Amazon Inspector scans successfully disabled. Details are provided for each account.

(structure)

An Amazon Web Services account within your environment that Amazon Inspector has been enabled for.

accountId -> (string)

The ID of the Amazon Web Services account.

resourceStatus -> (structure)

Details of the status of Amazon Inspector scans by resource type.

ec2 -> (string)

The status of Amazon Inspector scanning for Amazon EC2 resources.

ecr -> (string)

The status of Amazon Inspector scanning for Amazon ECR resources.

lambda -> (string)

The status of Amazon Inspector scanning for Amazon Web Services Lambda function.

lambdaCode -> (string)

The status of Amazon Inspector scanning for custom application code for Amazon Web Services Lambda functions.

status -> (string)

The status of Amazon Inspector for the account.

failedAccounts -> (list)

Information on any accounts for which Amazon Inspector scans could not be disabled. Details are provided for each account.

(structure)

An object with details on why an account failed to enable Amazon Inspector.

accountId -> (string)

The Amazon Web Services account ID.

errorCode -> (string)

The error code explaining why the account failed to enable Amazon Inspector.

errorMessage -> (string)

The error message received when the account failed to enable Amazon Inspector.

resourceStatus -> (structure)

An object detailing which resources Amazon Inspector is enabled to scan for the account.

ec2 -> (string)

The status of Amazon Inspector scanning for Amazon EC2 resources.

ecr -> (string)

The status of Amazon Inspector scanning for Amazon ECR resources.

lambda -> (string)

The status of Amazon Inspector scanning for Amazon Web Services Lambda function.

lambdaCode -> (string)

The status of Amazon Inspector scanning for custom application code for Amazon Web Services Lambda functions.

status -> (string)

The status of Amazon Inspector for the account.