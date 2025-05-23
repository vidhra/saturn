# get-apps-listÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-apps-list.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-apps-list.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/index.html#cli-aws-fms) ]

# get-apps-list

## Description

Returns information about the specified Firewall Manager applications list.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetAppsList)

## Synopsis

```
get-apps-list
--list-id <value>
[--default-list | --no-default-list]
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

`--list-id` (string)

The ID of the Firewall Manager applications list that you want the details for.

`--default-list` | `--no-default-list` (boolean)

Specifies whether the list to retrieve is a default list owned by Firewall Manager.

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

AppsList -> (structure)

Information about the specified Firewall Manager applications list.

ListId -> (string)

The ID of the Firewall Manager applications list.

ListName -> (string)

The name of the Firewall Manager applications list.

ListUpdateToken -> (string)

A unique identifier for each update to the list. When you update the list, the update token must match the token of the current version of the application list. You can retrieve the update token by getting the list.

CreateTime -> (timestamp)

The time that the Firewall Manager applications list was created.

LastUpdateTime -> (timestamp)

The time that the Firewall Manager applications list was last updated.

AppsList -> (list)

An array of applications in the Firewall Manager applications list.

(structure)

An individual Firewall Manager application.

AppName -> (string)

The applicationâs name.

Protocol -> (string)

The IP protocol name or number. The name can be one of `tcp` , `udp` , or `icmp` . For information on possible numbers, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) .

Port -> (long)

The applicationâs port number, for example `80` .

PreviousAppsList -> (map)

A map of previous version numbers to their corresponding `App` object arrays.

key -> (string)

value -> (list)

(structure)

An individual Firewall Manager application.

AppName -> (string)

The applicationâs name.

Protocol -> (string)

The IP protocol name or number. The name can be one of `tcp` , `udp` , or `icmp` . For information on possible numbers, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) .

Port -> (long)

The applicationâs port number, for example `80` .

AppsListArn -> (string)

The Amazon Resource Name (ARN) of the applications list.