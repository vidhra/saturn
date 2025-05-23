# update-sampling-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/update-sampling-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/update-sampling-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [xray](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/index.html#cli-aws-xray) ]

# update-sampling-rule

## Description

Modifies a sampling ruleâs configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/UpdateSamplingRule)

## Synopsis

```
update-sampling-rule
--sampling-rule-update <value>
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

`--sampling-rule-update` (structure)

The rule and fields to change.

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

Host -> (string)

Matches the hostname from a request URL.

ServiceName -> (string)

Matches the `name` that the service uses to identify itself in segments.

ServiceType -> (string)

Matches the `origin` that the service uses to identify its type in segments.

HTTPMethod -> (string)

Matches the HTTP method of a request.

URLPath -> (string)

Matches the path from a request URL.

Attributes -> (map)

Matches attributes derived from the request.

key -> (string)

value -> (string)

Shorthand Syntax:

```
RuleName=string,RuleARN=string,ResourceARN=string,Priority=integer,FixedRate=double,ReservoirSize=integer,Host=string,ServiceName=string,ServiceType=string,HTTPMethod=string,URLPath=string,Attributes={KeyName1=string,KeyName2=string}
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
  "Host": "string",
  "ServiceName": "string",
  "ServiceType": "string",
  "HTTPMethod": "string",
  "URLPath": "string",
  "Attributes": {"string": "string"
    ...}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update a sampling rule**

The following `update-sampling-rule` example modifies a sampling ruleâs configuration. The rules are consumed from a JSON file. Only the fields being updated are required.

```
aws xray update-sampling-rule \
   --cli-input-json file://1000-default.json
```

Contents of `1000-default.json`:

```
{
    "SamplingRuleUpdate": {
        "RuleName": "Default",
        "FixedRate": 0.01,
        "ReservoirSize": 0
    }
}
```

Output:

```
{
    "SamplingRuleRecords": [
        {
            "SamplingRule": {
                "RuleName": "Default",
                "RuleARN": "arn:aws:xray:us-west-2:123456789012:sampling-rule/Default",
                "ResourceARN": "*",
                "Priority": 10000,
                "FixedRate": 0.01,
                "ReservoirSize": 0,
                "ServiceName": "*",
                "ServiceType": "*",
                "Host": "*",
                "HTTPMethod": "*",
                "URLPath": "*",
                "Version": 1,
                "Attributes": {}
            },
            "CreatedAt": 0.0,
            "ModifiedAt": 1529959993.0
        }
   ]
}
```

For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling) in the *AWS X-Ray Developer Guide*.

## Output

SamplingRuleRecord -> (structure)

The updated rule definition and metadata.

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