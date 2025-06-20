# update-findings-filterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-findings-filter.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-findings-filter.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# update-findings-filter

## Description

Updates the criteria and other settings for a findings filter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/UpdateFindingsFilter)

## Synopsis

```
update-findings-filter
[--action <value>]
[--client-token <value>]
[--description <value>]
[--finding-criteria <value>]
--id <value>
[--name <value>]
[--position <value>]
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

`--action` (string)

The action to perform on findings that match the filter criteria (findingCriteria). Valid values are: ARCHIVE, suppress (automatically archive) the findings; and, NOOP, donât perform any action on the findings.

Possible values:

- `ARCHIVE`
- `NOOP`

`--client-token` (string)

A unique, case-sensitive token that you provide to ensure the idempotency of the request.

`--description` (string)

A custom description of the filter. The description can contain as many as 512 characters.

We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users of your account might be able to see this description, depending on the actions that theyâre allowed to perform in Amazon Macie.

`--finding-criteria` (structure)

The criteria to use to filter findings.

criterion -> (map)

A condition that specifies the property, operator, and one or more values to use to filter the results.

key -> (string)

value -> (structure)

Specifies the operator to use in a property-based condition that filters the results of a query for findings. For detailed information and examples of each operator, see [Fundamentals of filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-basics.html) in the *Amazon Macie User Guide* .

eq -> (list)

The value for the property matches (equals) the specified value. If you specify multiple values, Macie uses OR logic to join the values.

(string)

eqExactMatch -> (list)

The value for the property exclusively matches (equals an exact match for) all the specified values. If you specify multiple values, Amazon Macie uses AND logic to join the values.

You can use this operator with the following properties: customDataIdentifiers.detections.arn, customDataIdentifiers.detections.name, resourcesAffected.s3Bucket.tags.key, resourcesAffected.s3Bucket.tags.value, resourcesAffected.s3Object.tags.key, resourcesAffected.s3Object.tags.value, sensitiveData.category, and sensitiveData.detections.type.

(string)

gt -> (long)

The value for the property is greater than the specified value.

gte -> (long)

The value for the property is greater than or equal to the specified value.

lt -> (long)

The value for the property is less than the specified value.

lte -> (long)

The value for the property is less than or equal to the specified value.

neq -> (list)

The value for the property doesnât match (doesnât equal) the specified value. If you specify multiple values, Macie uses OR logic to join the values.

(string)

Shorthand Syntax:

```
criterion={KeyName1={eq=[string,string],eqExactMatch=[string,string],gt=long,gte=long,lt=long,lte=long,neq=[string,string]},KeyName2={eq=[string,string],eqExactMatch=[string,string],gt=long,gte=long,lt=long,lte=long,neq=[string,string]}}
```

JSON Syntax:

```
{
  "criterion": {"string": {
        "eq": ["string", ...],
        "eqExactMatch": ["string", ...],
        "gt": long,
        "gte": long,
        "lt": long,
        "lte": long,
        "neq": ["string", ...]
      }
    ...}
}
```

`--id` (string)

The unique identifier for the Amazon Macie resource that the request applies to.

`--name` (string)

A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.

We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see this name, depending on the actions that theyâre allowed to perform in Amazon Macie.

`--position` (integer)

The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.

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

arn -> (string)

The Amazon Resource Name (ARN) of the filter that was updated.

id -> (string)

The unique identifier for the filter that was updated.