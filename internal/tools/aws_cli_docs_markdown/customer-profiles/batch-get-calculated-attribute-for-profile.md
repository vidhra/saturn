# batch-get-calculated-attribute-for-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/batch-get-calculated-attribute-for-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/batch-get-calculated-attribute-for-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# batch-get-calculated-attribute-for-profile

## Description

Fetch the possible attribute values given the attribute name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)

## Synopsis

```
batch-get-calculated-attribute-for-profile
--calculated-attribute-name <value>
--domain-name <value>
--profile-ids <value>
[--condition-overrides <value>]
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

`--calculated-attribute-name` (string)

The unique name of the calculated attribute.

`--domain-name` (string)

The unique name of the domain.

`--profile-ids` (list)

List of unique identifiers for customer profiles to retrieve.

(string)

Syntax:

```
"string" "string" ...
```

`--condition-overrides` (structure)

Overrides the condition block within the original calculated attribute definition.

Range -> (structure)

The relative time period over which data is included in the aggregation for this override.

Start -> (integer)

The start time of when to include objects.

End -> (integer)

The end time of when to include objects.

Unit -> (string)

The unit for start and end.

Shorthand Syntax:

```
Range={Start=integer,End=integer,Unit=string}
```

JSON Syntax:

```
{
  "Range": {
    "Start": integer,
    "End": integer,
    "Unit": "DAYS"
  }
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

Errors -> (list)

List of errors for calculated attribute values that could not be retrieved.

(structure)

Error object describing why a specific profile and calculated attribute failed.

Code -> (string)

Status code for why a specific profile and calculated attribute failed.

Message -> (string)

Message describing why a specific profile and calculated attribute failed.

ProfileId -> (string)

The profile id that failed.

CalculatedAttributeValues -> (list)

List of calculated attribute values retrieved.

(structure)

The object containing the values of a single calculated attribute value.

CalculatedAttributeName -> (string)

The unique name of the calculated attribute.

DisplayName -> (string)

The display name of the calculated attribute.

IsDataPartial -> (string)

Indicates whether the calculated attributeâs value is based on partial data. If the data is partial, it is set to true.

ProfileId -> (string)

The profile id belonging to this calculated attribute value.

Value -> (string)

The value of the calculated attribute.

ConditionOverrides -> (structure)

Overrides the condition block within the original calculated attribute definition.

Range -> (structure)

The relative time period over which data is included in the aggregation for this override.

Start -> (integer)

The start time of when to include objects.

End -> (integer)

The end time of when to include objects.

Unit -> (string)

The unit for start and end.