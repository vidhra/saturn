# update-service-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-linux-subscriptions/update-service-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-linux-subscriptions/update-service-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager-linux-subscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-linux-subscriptions/index.html#cli-aws-license-manager-linux-subscriptions) ]

# update-service-settings

## Description

Updates the service settings for Linux subscriptions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)

## Synopsis

```
update-service-settings
[--allow-update | --no-allow-update]
--linux-subscriptions-discovery <value>
--linux-subscriptions-discovery-settings <value>
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

`--allow-update` | `--no-allow-update` (boolean)

Describes if updates are allowed to the service settings for Linux subscriptions. If you allow updates, you can aggregate Linux subscription data in more than one home Region.

`--linux-subscriptions-discovery` (string)

Describes if the discovery of Linux subscriptions is enabled.

Possible values:

- `Enabled`
- `Disabled`

`--linux-subscriptions-discovery-settings` (structure)

The settings defined for Linux subscriptions discovery. The settings include if Organizations integration has been enabled, and which Regions data will be aggregated from.

OrganizationIntegration -> (string)

Details if you have enabled resource discovery across your accounts in Organizations.

SourceRegions -> (list)

The Regions in which to discover data for Linux subscriptions.

(string)

Shorthand Syntax:

```
OrganizationIntegration=string,SourceRegions=string,string
```

JSON Syntax:

```
{
  "OrganizationIntegration": "Enabled"|"Disabled",
  "SourceRegions": ["string", ...]
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

HomeRegions -> (list)

The Region in which License Manager displays the aggregated data for Linux subscriptions.

(string)

LinuxSubscriptionsDiscovery -> (string)

Lists if discovery has been enabled for Linux subscriptions.

LinuxSubscriptionsDiscoverySettings -> (structure)

The settings defined for Linux subscriptions discovery. The settings include if Organizations integration has been enabled, and which Regions data will be aggregated from.

OrganizationIntegration -> (string)

Details if you have enabled resource discovery across your accounts in Organizations.

SourceRegions -> (list)

The Regions in which to discover data for Linux subscriptions.

(string)

Status -> (string)

Indicates the status of Linux subscriptions settings being applied.

StatusMessage -> (map)

A message which details the Linux subscriptions service settings current status.

key -> (string)

value -> (string)