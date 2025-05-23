# describe-remediation-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-remediation-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-remediation-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# describe-remediation-configurations

## Description

Returns the details of one or more remediation configurations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeRemediationConfigurations)

## Synopsis

```
describe-remediation-configurations
--config-rule-names <value>
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

`--config-rule-names` (list)

A list of Config rule names of remediation configurations for which you want details.

(string)

Syntax:

```
"string" "string" ...
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

RemediationConfigurations -> (list)

Returns a remediation configuration object.

(structure)

An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.

ConfigRuleName -> (string)

The name of the Config rule.

TargetType -> (string)

The type of the target. Target executes remediation. For example, SSM document.

TargetId -> (string)

Target ID is the name of the SSM document.

TargetVersion -> (string)

Version of the target. For example, version of the SSM document.

### Note

If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.

Parameters -> (map)

An object of the RemediationParameterValue.

key -> (string)

value -> (structure)

The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.

ResourceValue -> (structure)

The value is dynamic and changes at run-time.

Value -> (string)

The value is a resource ID.

StaticValue -> (structure)

The value is static and does not change at run-time.

Values -> (list)

A list of values. For example, the ARN of the assumed role.

(string)

ResourceType -> (string)

The type of a resource.

Automatic -> (boolean)

The remediation is triggered automatically.

ExecutionControls -> (structure)

An ExecutionControls object.

SsmControls -> (structure)

A SsmControls object.

ConcurrentExecutionRatePercentage -> (integer)

The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.

ErrorPercentage -> (integer)

The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.

MaximumAutomaticAttempts -> (integer)

The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.

For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.

RetryAttemptSeconds -> (long)

Time window to determine whether or not to add a remediation exception to prevent infinite remediation attempts. If `MaximumAutomaticAttempts` remediation attempts have been made under `RetryAttemptSeconds` , a remediation exception will be added to the resource. If you do not select a number, the default is 60 seconds.

For example, if you specify `RetryAttemptSeconds` as 50 seconds and `MaximumAutomaticAttempts` as 5, Config will run auto-remediations 5 times within 50 seconds before adding a remediation exception to the resource.

Arn -> (string)

Amazon Resource Name (ARN) of remediation configuration.

CreatedByService -> (string)

Name of the service that owns the service-linked rule, if applicable.