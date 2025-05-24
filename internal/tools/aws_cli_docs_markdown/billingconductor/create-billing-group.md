# create-billing-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/create-billing-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/create-billing-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [billingconductor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/index.html#cli-aws-billingconductor) ]

# create-billing-group

## Description

Creates a billing group that resembles a consolidated billing family that Amazon Web Services charges, based off of the predefined pricing plan computation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/billingconductor-2021-07-30/CreateBillingGroup)

## Synopsis

```
create-billing-group
[--client-token <value>]
--name <value>
--account-grouping <value>
--computation-preference <value>
[--primary-account-id <value>]
[--description <value>]
[--tags <value>]
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

`--client-token` (string)

The token that is needed to support idempotency. Idempotency isnât currently supported, but will be implemented in a future update.

`--name` (string)

The billing group name. The names must be unique.

`--account-grouping` (structure)

The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family.

LinkedAccountIds -> (list)

The account IDs that make up the billing group. Account IDs must be a part of the consolidated billing family, and not associated with another billing group.

(string)

AutoAssociate -> (boolean)

Specifies if this billing group will automatically associate newly added Amazon Web Services accounts that join your consolidated billing family.

Shorthand Syntax:

```
LinkedAccountIds=string,string,AutoAssociate=boolean
```

JSON Syntax:

```
{
  "LinkedAccountIds": ["string", ...],
  "AutoAssociate": true|false
}
```

`--computation-preference` (structure)

The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group.

PricingPlanArn -> (string)

The Amazon Resource Name (ARN) of the pricing plan thatâs used to compute the Amazon Web Services charges for a billing group.

Shorthand Syntax:

```
PricingPlanArn=string
```

JSON Syntax:

```
{
  "PricingPlanArn": "string"
}
```

`--primary-account-id` (string)

The account ID that serves as the main account in a billing group.

`--description` (string)

The description of the billing group.

`--tags` (map)

A map that contains tag keys and tag values that are attached to a billing group. This feature isnât available during the beta.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

Arn -> (string)

The Amazon Resource Name (ARN) of the created billing group.