# put-remediation-exceptionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-remediation-exceptions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-remediation-exceptions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# put-remediation-exceptions

## Description

A remediation exception is when a specified resource is no longer considered for auto-remediation. This API adds a new exception or updates an existing exception for a specified resource with a specified Config rule.

### Note

**Exceptions block auto remediation**

Config generates a remediation exception when a problem occurs running a remediation action for a specified resource. Remediation exceptions blocks auto-remediation until the exception is cleared.

### Note

**Manual remediation is recommended when placing an exception**

When placing an exception on an Amazon Web Services resource, it is recommended that remediation is set as manual remediation until the given Config rule for the specified resource evaluates the resource as `NON_COMPLIANT` . Once the resource has been evaluated as `NON_COMPLIANT` , you can add remediation exceptions and change the remediation type back from Manual to Auto if you want to use auto-remediation. Otherwise, using auto-remediation before a `NON_COMPLIANT` evaluation result can delete resources before the exception is applied.

### Note

**Exceptions can only be performed on non-compliant resources**

Placing an exception can only be performed on resources that are `NON_COMPLIANT` . If you use this API for `COMPLIANT` resources or resources that are `NOT_APPLICABLE` , a remediation exception will not be generated. For more information on the conditions that initiate the possible Config evaluation results, see [Concepts | Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#aws-config-rules) in the *Config Developer Guide* .

### Note

**Exceptions cannot be placed on service-linked remediation actions**

You cannot place an exception on service-linked remediation actions, such as remediation actions put by an organizational conformance pack.

### Note

**Auto remediation can be initiated even for compliant resources**

If you enable auto remediation for a specific Config rule using the [PutRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/emAPI_PutRemediationConfigurations.html) API or the Config console, it initiates the remediation process for all non-compliant resources for that specific rule. The auto remediation process relies on the compliance data snapshot which is captured on a periodic basis. Any non-compliant resource that is updated between the snapshot schedule will continue to be remediated based on the last known compliance data snapshot.

This means that in some cases auto remediation can be initiated even for compliant resources, since the bootstrap processor uses a database that can have stale evaluation results based on the last known compliance data snapshot.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutRemediationExceptions)

## Synopsis

```
put-remediation-exceptions
--config-rule-name <value>
--resource-keys <value>
[--message <value>]
[--expiration-time <value>]
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

`--config-rule-name` (string)

The name of the Config rule for which you want to create remediation exception.

`--resource-keys` (list)

An exception list of resource exception keys to be processed with the current request. Config adds exception for each resource key. For example, Config adds 3 exceptions for 3 resource keys.

(structure)

The details that identify a resource within Config, including the resource type and resource ID.

ResourceType -> (string)

The type of a resource.

ResourceId -> (string)

The ID of the resource (for example., sg-xxxxxx).

Shorthand Syntax:

```
ResourceType=string,ResourceId=string ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "string",
    "ResourceId": "string"
  }
  ...
]
```

`--message` (string)

The message contains an explanation of the exception.

`--expiration-time` (timestamp)

The exception is automatically deleted after the expiration date.

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

FailedBatches -> (list)

Returns a list of failed remediation exceptions batch objects. Each object in the batch consists of a list of failed items and failure messages.

(structure)

List of each of the failed remediation exceptions with specific reasons.

FailureMessage -> (string)

Returns a failure message. For example, the auto-remediation has failed.

FailedItems -> (list)

Returns remediation exception resource key object of the failed items.

(structure)

An object that represents the details about the remediation exception. The details include the rule name, an explanation of an exception, the time when the exception will be deleted, the resource ID, and resource type.

ConfigRuleName -> (string)

The name of the Config rule.

ResourceType -> (string)

The type of a resource.

ResourceId -> (string)

The ID of the resource (for example., sg-xxxxxx).

Message -> (string)

An explanation of an remediation exception.

ExpirationTime -> (timestamp)

The time when the remediation exception will be deleted.