# create-sampling-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/create-sampling-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/create-sampling-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [xray](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/index.html#cli-aws-xray) ]

# create-sampling-rule

## Description

Creates a rule to control sampling behavior for instrumented applications. Services retrieve rules with [GetSamplingRules](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html) , and evaluate each rule in ascending order of *priority* for each request. If a rule matches, the service records a trace, borrowing it from the reservoir size. After 10 seconds, the service reports back to X-Ray with [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html) to get updated versions of each in-use rule. The updated rule contains a trace quota that the service can use instead of borrowing from the reservoir.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/CreateSamplingRule)

## Synopsis

```
create-sampling-rule
--sampling-rule <value>
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

`--sampling-rule` (structure)

The rule definition.

RuleName -> (string)

The name of the sampling rule. Specify a rule by either name or ARN, but not both.

RuleARN -> (string)

The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

ResourceARN -> (string)

Matches the ARN of the Amazon Web Services resource on which the service runs.

Priority -> (integer)

The priority of the sampling rule.

FixedRate -> (double)

The percentage of matching requests to instrument, after the reservoir is exhausted.

ReservoirSize -> (integer)

A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.

ServiceName -> (string)

Matches the `name` that the service uses to identify itself in segments.

ServiceType -> (string)

Matches the `origin` that the service uses to identify its type in segments.

Host -> (string)

Matches the hostname from a request URL.

HTTPMethod -> (string)

Matches the HTTP method of a request.

URLPath -> (string)

Matches the path from a request URL.

Version -> (integer)

The version of the sampling rule format (`1` ).

Attributes -> (map)

Matches attributes derived from the request.

key -> (string)

value -> (string)

Shorthand Syntax:

```
RuleName=string,RuleARN=string,ResourceARN=string,Priority=integer,FixedRate=double,ReservoirSize=integer,ServiceName=string,ServiceType=string,Host=string,HTTPMethod=string,URLPath=string,Version=integer,Attributes={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "RuleName": "string",
  "RuleARN": "string",
  "ResourceARN": "string",
  "Priority": integer,
  "FixedRate": double,
  "ReservoirSize": integer,
  "ServiceName": "string",
  "ServiceType": "string",
  "Host": "string",
  "HTTPMethod": "string",
  "URLPath": "string",
  "Version": integer,
  "Attributes": {"string": "string"
    ...}
}
```

`--tags` (list)

A map that contains one or more tag keys and tag values to attach to an X-Ray sampling rule. For more information about ways to use tags, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference* .

The following restrictions apply to tags:

- Maximum number of user-applied tags per resource: 50
- Maximum tag key length: 128 Unicode characters
- Maximum tag value length: 256 Unicode characters
- Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / = + - and @
- Tag keys and values are case sensitive.
- Donât use `aws:` as a prefix for keys; itâs reserved for Amazon Web Services use.

(structure)

A map that contains tag keys and tag values to attach to an Amazon Web Services X-Ray group or sampling rule. For more information about ways to use tags, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference* .

The following restrictions apply to tags:

- Maximum number of user-applied tags per resource: 50
- Tag keys and values are case sensitive.
- Donât use `aws:` as a prefix for keys; itâs reserved for Amazon Web Services use. You cannot edit or delete system tags.

Key -> (string)

A tag key, such as `Stage` or `Name` . A tag key cannot be empty. The key can be a maximum of 128 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`

Value -> (string)

An optional tag value, such as `Production` or `test-only` . The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a sampling rule**

The following `create-sampling-rule` example creates a rule to control sampling behavior for instrumented applications. The rules are provided by a JSON file. The majority of the sampling rule fields are required to create the rule.

```
aws xray create-sampling-rule \
    --cli-input-json file://9000-base-scorekeep.json
```

Contents of `9000-base-scorekeep.json`:

```
{
    "SamplingRule": {
        "RuleName": "base-scorekeep",
        "ResourceARN": "*",
        "Priority": 9000,
        "FixedRate": 0.1,
        "ReservoirSize": 5,
        "ServiceName": "Scorekeep",
        "ServiceType": "*",
        "Host": "*",
        "HTTPMethod": "*",
        "URLPath": "*",
        "Version": 1
    }
}
```

Output:

```
{
    "SamplingRuleRecord": {
        "SamplingRule": {
            "RuleName": "base-scorekeep",
            "RuleARN": "arn:aws:xray:us-west-2:123456789012:sampling-rule/base-scorekeep",
            "ResourceARN": "*",
            "Priority": 9000,
            "FixedRate": 0.1,
            "ReservoirSize": 5,
            "ServiceName": "Scorekeep",
            "ServiceType": "*",
            "Host": "*",
            "HTTPMethod": "*",
            "URLPath": "*",
            "Version": 1,
            "Attributes": {}
        },
        "CreatedAt": 1530574410.0,
        "ModifiedAt": 1530574410.0
    }
}
```

For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling) in the *AWS X-Ray Developer Guide*.

## Output

SamplingRuleRecord -> (structure)

The saved rule definition and metadata.

SamplingRule -> (structure)

The sampling rule.

RuleName -> (string)

The name of the sampling rule. Specify a rule by either name or ARN, but not both.

RuleARN -> (string)

The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

ResourceARN -> (string)

Matches the ARN of the Amazon Web Services resource on which the service runs.

Priority -> (integer)

The priority of the sampling rule.

FixedRate -> (double)

The percentage of matching requests to instrument, after the reservoir is exhausted.

ReservoirSize -> (integer)

A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.

ServiceName -> (string)

Matches the `name` that the service uses to identify itself in segments.

ServiceType -> (string)

Matches the `origin` that the service uses to identify its type in segments.

Host -> (string)

Matches the hostname from a request URL.

HTTPMethod -> (string)

Matches the HTTP method of a request.

URLPath -> (string)

Matches the path from a request URL.

Version -> (integer)

The version of the sampling rule format (`1` ).

Attributes -> (map)

Matches attributes derived from the request.

key -> (string)

value -> (string)

CreatedAt -> (timestamp)

When the rule was created.

ModifiedAt -> (timestamp)

When the rule was last modified.