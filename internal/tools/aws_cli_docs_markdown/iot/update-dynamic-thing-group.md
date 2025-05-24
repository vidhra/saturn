# update-dynamic-thing-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dynamic-thing-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dynamic-thing-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# update-dynamic-thing-group

## Description

Updates a dynamic thing group.

Requires permission to access the [UpdateDynamicThingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateDynamicThingGroup)

## Synopsis

```
update-dynamic-thing-group
--thing-group-name <value>
--thing-group-properties <value>
[--expected-version <value>]
[--index-name <value>]
[--query-string <value>]
[--query-version <value>]
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

`--thing-group-name` (string)

The name of the dynamic thing group to update.

`--thing-group-properties` (structure)

The dynamic thing group properties to update.

thingGroupDescription -> (string)

The thing group description.

attributePayload -> (structure)

The thing group attributes in JSON format.

attributes -> (map)

A JSON string containing up to three key-value pair in JSON format. For example:

`{\"attributes\":{\"string1\":\"string2\"}}`

key -> (string)

value -> (string)

merge -> (boolean)

Specifies whether the list of attributes provided in the `AttributePayload` is merged with the attributes stored in the registry, instead of overwriting them.

To remove an attribute, call `UpdateThing` with an empty attribute value.

### Note

The `merge` attribute is only valid when calling `UpdateThing` or `UpdateThingGroup` .

Shorthand Syntax:

```
thingGroupDescription=string,attributePayload={attributes={KeyName1=string,KeyName2=string},merge=boolean}
```

JSON Syntax:

```
{
  "thingGroupDescription": "string",
  "attributePayload": {
    "attributes": {"string": "string"
      ...},
    "merge": true|false
  }
}
```

`--expected-version` (long)

The expected version of the dynamic thing group to update.

`--index-name` (string)

The dynamic thing group index to update.

### Note

Currently one index is supported: `AWS_Things` .

`--query-string` (string)

The dynamic thing group search query string to update.

`--query-version` (string)

The dynamic thing group query version to update.

### Note

Currently one query version is supported: â2017-09-30â. If not specified, the query version defaults to this value.

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

**To update a dynamic thing group**

The following `update-dynamic-thing-group` example updates the specified dynamic thing group. It provides a description and updates the query string to change the group membership criteria.

```
aws iot update-dynamic-thing-group \
    --thing-group-name "RoomTooWarm"
    --thing-group-properties "thingGroupDescription=\"This thing group contains rooms warmer than 65F.\"" \
    --query-string "attributes.temperature>65"
```

Output:

```
{
    "version": 2
}
```

For more information, see [Dynamic Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/dynamic-thing-groups.html) in the *AWS IoT Developers Guide*.

## Output

version -> (long)

The dynamic thing group version.