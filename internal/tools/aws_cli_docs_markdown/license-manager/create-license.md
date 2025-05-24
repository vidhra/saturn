# create-licenseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/index.html#cli-aws-license-manager) ]

# create-license

## Description

Creates a license.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/CreateLicense)

## Synopsis

```
create-license
--license-name <value>
--product-name <value>
--product-sku <value>
--issuer <value>
--home-region <value>
--validity <value>
--entitlements <value>
--beneficiary <value>
--consumption-configuration <value>
[--license-metadata <value>]
--client-token <value>
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

`--license-name` (string)

License name.

`--product-name` (string)

Product name.

`--product-sku` (string)

Product SKU.

`--issuer` (structure)

License issuer.

Name -> (string)

Issuer name.

SignKey -> (string)

Asymmetric KMS key from Key Management Service. The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.

Shorthand Syntax:

```
Name=string,SignKey=string
```

JSON Syntax:

```
{
  "Name": "string",
  "SignKey": "string"
}
```

`--home-region` (string)

Home Region for the license.

`--validity` (structure)

Date and time range during which the license is valid, in ISO8601-UTC format.

Begin -> (string)

Start of the time range.

End -> (string)

End of the time range.

Shorthand Syntax:

```
Begin=string,End=string
```

JSON Syntax:

```
{
  "Begin": "string",
  "End": "string"
}
```

`--entitlements` (list)

License entitlements.

(structure)

Describes a resource entitled for use with a license.

Name -> (string)

Entitlement name.

Value -> (string)

Entitlement resource. Use only if the unit is None.

MaxCount -> (long)

Maximum entitlement count. Use if the unit is not None.

Overage -> (boolean)

Indicates whether overages are allowed.

Unit -> (string)

Entitlement unit.

AllowCheckIn -> (boolean)

Indicates whether check-ins are allowed.

Shorthand Syntax:

```
Name=string,Value=string,MaxCount=long,Overage=boolean,Unit=string,AllowCheckIn=boolean ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string",
    "MaxCount": long,
    "Overage": true|false,
    "Unit": "Count"|"None"|"Seconds"|"Microseconds"|"Milliseconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second",
    "AllowCheckIn": true|false
  }
  ...
]
```

`--beneficiary` (string)

License beneficiary.

`--consumption-configuration` (structure)

Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.

RenewType -> (string)

Renewal frequency.

ProvisionalConfiguration -> (structure)

Details about a provisional configuration.

MaxTimeToLiveInMinutes -> (integer)

Maximum time for the provisional configuration, in minutes.

BorrowConfiguration -> (structure)

Details about a borrow configuration.

AllowEarlyCheckIn -> (boolean)

Indicates whether early check-ins are allowed.

MaxTimeToLiveInMinutes -> (integer)

Maximum time for the borrow configuration, in minutes.

Shorthand Syntax:

```
RenewType=string,ProvisionalConfiguration={MaxTimeToLiveInMinutes=integer},BorrowConfiguration={AllowEarlyCheckIn=boolean,MaxTimeToLiveInMinutes=integer}
```

JSON Syntax:

```
{
  "RenewType": "None"|"Weekly"|"Monthly",
  "ProvisionalConfiguration": {
    "MaxTimeToLiveInMinutes": integer
  },
  "BorrowConfiguration": {
    "AllowEarlyCheckIn": true|false,
    "MaxTimeToLiveInMinutes": integer
  }
}
```

`--license-metadata` (list)

Information about the license.

(structure)

Describes key/value pairs.

Name -> (string)

The key name.

Value -> (string)

The value.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--tags` (list)

Tags to add to the license. For more information about tagging support in License Manager, see the [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html) operation.

(structure)

Details about the tags for a resource. For more information about tagging support in License Manager, see the [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html) operation.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

LicenseArn -> (string)

Amazon Resource Name (ARN) of the license.

Status -> (string)

License status.

Version -> (string)

License version.