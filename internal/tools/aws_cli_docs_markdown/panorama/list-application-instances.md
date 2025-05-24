# list-application-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/panorama/list-application-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/panorama/list-application-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [panorama](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/panorama/index.html#cli-aws-panorama) ]

# list-application-instances

## Description

Returns a list of application instances.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/panorama-2019-07-24/ListApplicationInstances)

## Synopsis

```
list-application-instances
[--device-id <value>]
[--max-results <value>]
[--next-token <value>]
[--status-filter <value>]
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

`--device-id` (string)

The application instancesâ device ID.

`--max-results` (integer)

The maximum number of application instances to return in one page of results.

`--next-token` (string)

Specify the pagination token from a previous request to retrieve the next page of results.

`--status-filter` (string)

Only include instances with a specific status.

Possible values:

- `DEPLOYMENT_SUCCEEDED`
- `DEPLOYMENT_ERROR`
- `REMOVAL_SUCCEEDED`
- `REMOVAL_FAILED`
- `PROCESSING_DEPLOYMENT`
- `PROCESSING_REMOVAL`
- `DEPLOYMENT_FAILED`

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

ApplicationInstances -> (list)

A list of application instances.

(structure)

An application instance on a device.

ApplicationInstanceId -> (string)

The application instanceâs ID.

Arn -> (string)

The application instanceâs ARN.

CreatedTime -> (timestamp)

When the application instance was created.

DefaultRuntimeContextDevice -> (string)

The deviceâs ID.

DefaultRuntimeContextDeviceName -> (string)

The deviceâs name.

Description -> (string)

The application instanceâs description.

HealthStatus -> (string)

The application instanceâs health status.

Name -> (string)

The application instanceâs name.

RuntimeContextStates -> (list)

The applicationâs state.

(structure)

An application instanceâs state.

DesiredState -> (string)

The applicationâs desired state.

DeviceReportedStatus -> (string)

The applicationâs reported status.

DeviceReportedTime -> (timestamp)

When the device reported the applicationâs state.

RuntimeContextName -> (string)

The deviceâs name.

Status -> (string)

The application instanceâs status.

StatusDescription -> (string)

The application instanceâs status description.

Tags -> (map)

The application instanceâs tags.

key -> (string)

value -> (string)

NextToken -> (string)

A pagination token thatâs included if more results are available.