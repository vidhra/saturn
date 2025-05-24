# list-core-devicesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-core-devices.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-core-devices.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [greengrassv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/index.html#cli-aws-greengrassv2) ]

# list-core-devices

## Description

Retrieves a paginated list of Greengrass core devices.

### Note

IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isnât running on the device, or if device isnât connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.

Core devices send status updates at the following times:

- When the IoT Greengrass Core software starts
- When the core device receives a deployment from the Amazon Web Services Cloud
- For Greengrass nucleus 2.12.2 and earlier, the core device sends status updates when the status of any component on the core device becomes `ERRORED` or `BROKEN` .
- For Greengrass nucleus 2.12.3 and later, the core device sends status updates when the status of any component on the core device becomes `ERRORED` , `BROKEN` , `RUNNING` , or `FINISHED` .
- At a [regular interval that you can configure](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss) , which defaults to 24 hours
- For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/greengrassv2-2020-11-30/ListCoreDevices)

`list-core-devices` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `coreDevices`

## Synopsis

```
list-core-devices
[--thing-group-arn <value>]
[--status <value>]
[--runtime <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--thing-group-arn` (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the IoT thing group by which to filter. If you specify this parameter, the list includes only core devices that have successfully deployed a deployment that targets the thing group. When you remove a core device from a thing group, the list continues to include that core device.

`--status` (string)

The core device status by which to filter. If you specify this parameter, the list includes only core devices that have this status. Choose one of the following options:

- `HEALTHY` â The IoT Greengrass Core software and all components run on the core device without issue.
- `UNHEALTHY` â The IoT Greengrass Core software or a component is in a failed state on the core device.

Possible values:

- `HEALTHY`
- `UNHEALTHY`

`--runtime` (string)

The runtime to be used by the core device. The runtime can be:

- `aws_nucleus_classic`
- `aws_nucleus_lite`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To list core devices**

The following `list-core-devices` example lists the AWS IoT Greengrass core devices in your AWS account in the current Region.

```
aws greengrassv2 list-core-devices
```

Output:

```
{
    "coreDevices": [
        {
            "coreDeviceThingName": "MyGreengrassCore",
            "status": "HEALTHY",
            "lastStatusUpdateTimestamp": "2021-01-08T04:57:58.838000-08:00"
        }
    ]
}
```

For more information, see [Check core device status](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-status.html) in the *AWS IoT Greengrass V2 Developer Guide*.

## Output

coreDevices -> (list)

A list that summarizes each core device.

(structure)

Contains information about a Greengrass core device, which is an IoT thing that runs the IoT Greengrass Core software.

coreDeviceThingName -> (string)

The name of the core device. This is also the name of the IoT thing.

status -> (string)

The status of the core device. Core devices can have the following statuses:

- `HEALTHY` â The IoT Greengrass Core software and all components run on the core device without issue.
- `UNHEALTHY` â The IoT Greengrass Core software or a component is in a failed state on the core device.

lastStatusUpdateTimestamp -> (timestamp)

The time at which the core deviceâs status last updated, expressed in ISO 8601 format.

platform -> (string)

The operating system platform that the core device runs.

architecture -> (string)

The computer architecture of the core device.

runtime -> (string)

The runtime for the core device. The runtime can be:

- `aws_nucleus_classic`
- `aws_nucleus_lite`

nextToken -> (string)

The token for the next set of results, or null if there are no additional results.