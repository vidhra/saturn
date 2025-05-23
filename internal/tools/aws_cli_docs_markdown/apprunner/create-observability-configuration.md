# create-observability-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-observability-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-observability-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apprunner](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/index.html#cli-aws-apprunner) ]

# create-observability-configuration

## Description

Create an App Runner observability configuration resource. App Runner requires this resource when you create or update App Runner services and you want to enable non-default observability features. You can share an observability configuration across multiple services.

Create multiple revisions of a configuration by calling this action multiple times using the same `ObservabilityConfigurationName` . The call returns incremental `ObservabilityConfigurationRevision` values. When you create a service and configure an observability configuration resource, the service uses the latest active revision of the observability configuration by default. You can optionally configure the service to use a specific revision.

The observability configuration resource is designed to configure multiple features (currently one feature, tracing). This action takes optional parameters that describe the configuration of these features (currently one parameter, `TraceConfiguration` ). If you donât specify a feature parameter, App Runner doesnât enable the feature.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apprunner-2020-05-15/CreateObservabilityConfiguration)

## Synopsis

```
create-observability-configuration
--observability-configuration-name <value>
[--trace-configuration <value>]
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

`--observability-configuration-name` (string)

A name for the observability configuration. When you use it for the first time in an Amazon Web Services Region, App Runner creates revision number `1` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.

### Note

The name `DefaultConfiguration` is reserved. You canât use it to create a new observability configuration, and you canât create a revision of it.

When you want to use your own observability configuration for your App Runner service, *create a configuration with a different name* , and then provide it when you create or update your service.

`--trace-configuration` (structure)

The configuration of the tracing feature within this observability configuration. If you donât specify it, App Runner doesnât enable tracing.

Vendor -> (string)

The implementation provider chosen for tracing App Runner services.

Shorthand Syntax:

```
Vendor=string
```

JSON Syntax:

```
{
  "Vendor": "AWSXRAY"
}
```

`--tags` (list)

A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.

(structure)

Describes a tag that is applied to an App Runner resource. A tag is a metadata item consisting of a key-value pair.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

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

ObservabilityConfiguration -> (structure)

A description of the App Runner observability configuration thatâs created by this request.

ObservabilityConfigurationArn -> (string)

The Amazon Resource Name (ARN) of this observability configuration.

ObservabilityConfigurationName -> (string)

The customer-provided observability configuration name. It can be used in multiple revisions of a configuration.

TraceConfiguration -> (structure)

The configuration of the tracing feature within this observability configuration. If not specified, tracing isnât enabled.

Vendor -> (string)

The implementation provider chosen for tracing App Runner services.

ObservabilityConfigurationRevision -> (integer)

The revision of this observability configuration. Itâs unique among all the active configurations (`"Status": "ACTIVE"` ) that share the same `ObservabilityConfigurationName` .

Latest -> (boolean)

Itâs set to `true` for the configuration with the highest `Revision` among all configurations that share the same `ObservabilityConfigurationName` . Itâs set to `false` otherwise.

Status -> (string)

The current state of the observability configuration. If the status of a configuration revision is `INACTIVE` , it was deleted and canât be used. Inactive configuration revisions are permanently removed some time after they are deleted.

CreatedAt -> (timestamp)

The time when the observability configuration was created. Itâs in Unix time stamp format.

DeletedAt -> (timestamp)

The time when the observability configuration was deleted. Itâs in Unix time stamp format.