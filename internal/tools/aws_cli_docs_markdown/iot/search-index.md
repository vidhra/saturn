# search-indexÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/search-index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/search-index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# search-index

## Description

The query search index.

Requires permission to access the [SearchIndex](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SearchIndex)

## Synopsis

```
search-index
[--index-name <value>]
--query-string <value>
[--next-token <value>]
[--max-results <value>]
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

`--index-name` (string)

The search index name.

`--query-string` (string)

The search query string. For more information about the search query syntax, see [Query syntax](https://docs.aws.amazon.com/iot/latest/developerguide/query-syntax.html) .

`--next-token` (string)

The token used to get the next set of results, or `null` if there are no additional results.

`--max-results` (integer)

The maximum number of results to return per page at one time. This maximum number cannot exceed 100. The response might contain fewer results but will never contain more. You can use ` `nextToken` [https://docs.aws.amazon.com/iot/latest/apireference/API_SearchIndex.html#iot-SearchIndex-request](https://docs.aws.amazon.com/iot/latest/apireference/API_SearchIndex.html#iot-SearchIndex-request)-nextToken`__ to retrieve the next set of results until `nextToken` returns `NULL` .

`--query-version` (string)

The query version.

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

**To query the thing index**

The following `search-index` example queries the `AWS_Things` index for things that have a type of `LightBulb`.

```
aws iot search-index \
    --index-name "AWS_Things" \
    --query-string "thingTypeName:LightBulb"
```

Output:

```
{
    "things": [
        {
            "thingName": "MyLightBulb",
            "thingId": "40da2e73-c6af-406e-b415-15acae538797",
            "thingTypeName": "LightBulb",
            "thingGroupNames": [
                "LightBulbs",
                "DeadBulbs"
            ],
            "attributes": {
                "model": "123",
                "wattage": "75"
            },
            "connectivity": {
                "connected": false
            }
        },
        {
            "thingName": "ThirdBulb",
            "thingId": "615c8455-33d5-40e8-95fd-3ee8b24490af",
            "thingTypeName": "LightBulb",
            "attributes": {
                "model": "123",
                "wattage": "75"
            },
            "connectivity": {
                "connected": false
            }
        },
        {
            "thingName": "MyOtherLightBulb",
            "thingId": "6dae0d3f-40c1-476a-80c4-1ed24ba6aa11",
            "thingTypeName": "LightBulb",
            "attributes": {
                "model": "123",
                "wattage": "75"
            },
            "connectivity": {
                "connected": false
            }
        }
    ]
}
```

For more information, see [Managing Thing Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html) in the *AWS IoT Developer Guide*.

## Output

nextToken -> (string)

The token used to get the next set of results, or `null` if there are no additional results.

things -> (list)

The things that match the search query.

(structure)

The thing search index document.

thingName -> (string)

The thing name.

thingId -> (string)

The thing ID.

thingTypeName -> (string)

The thing type name.

thingGroupNames -> (list)

Thing group and billing group names.

(string)

attributes -> (map)

The attributes.

key -> (string)

value -> (string)

shadow -> (string)

The unnamed shadow and named shadow.

For more information about shadows, see [IoT Device Shadow service.](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)

deviceDefender -> (string)

Contains Device Defender data.

For more information about Device Defender, see [Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html) .

connectivity -> (structure)

Indicates whether the thing is connected to the Amazon Web Services IoT Core service.

connected -> (boolean)

True if the thing is connected to the Amazon Web Services IoT Core service; false if it is not connected.

timestamp -> (long)

The epoch time (in milliseconds) when the thing last connected or disconnected. If the thing has been disconnected for approximately an hour, the time value might be missing.

disconnectReason -> (string)

The reason why the client is disconnected. If the thing has been disconnected for approximately an hour, the `disconnectReason` value might be missing.

thingGroups -> (list)

The thing groups that match the search query.

(structure)

The thing group search index document.

thingGroupName -> (string)

The thing group name.

thingGroupId -> (string)

The thing group ID.

thingGroupDescription -> (string)

The thing group description.

attributes -> (map)

The thing group attributes.

key -> (string)

value -> (string)

parentGroupNames -> (list)

Parent group names.

(string)