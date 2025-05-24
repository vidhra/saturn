# list-installed-componentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-installed-components.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-installed-components.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [greengrassv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/index.html#cli-aws-greengrassv2) ]

# list-installed-components

## Description

Retrieves a paginated list of the components that a Greengrass core device runs. By default, this list doesnât include components that are deployed as dependencies of other components. To include dependencies in the response, set the `topologyFilter` parameter to `ALL` .

### Note

IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isnât running on the device, or if device isnât connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.

Core devices send status updates at the following times:

- When the IoT Greengrass Core software starts
- When the core device receives a deployment from the Amazon Web Services Cloud
- When the status of any component on the core device becomes `BROKEN`
- At a [regular interval that you can configure](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss) , which defaults to 24 hours
- For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/greengrassv2-2020-11-30/ListInstalledComponents)

`list-installed-components` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `installedComponents`

## Synopsis

```
list-installed-components
--core-device-thing-name <value>
[--topology-filter <value>]
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

`--core-device-thing-name` (string)

The name of the core device. This is also the name of the IoT thing.

`--topology-filter` (string)

The filter for the list of components. Choose from the following options:

- `ALL` â The list includes all components installed on the core device.
- `ROOT` â The list includes only *root* components, which are components that you specify in a deployment. When you choose this option, the list doesnât include components that the core device installs as dependencies of other components.

Default: `ROOT`

Possible values:

- `ALL`
- `ROOT`

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

**To list components installed on a core device**

The following `list-installed-components` example lists the components that are installed on an AWS IoT Greengrass core device.

```
aws greengrassv2 list-installed-components \
    --core-device-thing-name MyGreengrassCore
```

Output:

```
{
    "installedComponents": [
        {
            "componentName": "aws.greengrass.Cli",
            "componentVersion": "2.0.3",
            "lifecycleState": "RUNNING",
            "isRoot": true
        },
        {
            "componentName": "aws.greengrass.Nucleus",
            "componentVersion": "2.0.3",
            "lifecycleState": "FINISHED",
            "isRoot": true
        }
    ]
}
```

For more information, see [Check core device status](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-status.html) in the *AWS IoT Greengrass V2 Developer Guide*.

## Output

installedComponents -> (list)

A list that summarizes each component on the core device.

### Note

Greengrass nucleus v2.7.0 or later is required to get an accurate `lastStatusChangeTimestamp` response. This response can be inaccurate in earlier Greengrass nucleus versions.

### Note

Greengrass nucleus v2.8.0 or later is required to get an accurate `lastInstallationSource` and `lastReportedTimestamp` response. This response can be inaccurate or null in earlier Greengrass nucleus versions.

(structure)

Contains information about a component on a Greengrass core device.

componentName -> (string)

The name of the component.

componentVersion -> (string)

The version of the component.

lifecycleState -> (string)

The lifecycle state of the component.

lifecycleStateDetails -> (string)

A detailed response about the lifecycle state of the component that explains the reason why a component has an error or is broken.

isRoot -> (boolean)

Whether or not the component is a root component.

lastStatusChangeTimestamp -> (timestamp)

The status of how current the data is.

This response is based off of component state changes. The status reflects component disruptions and deployments. If a component only sees a configuration update during a deployment, it might not undergo a state change and this status would not be updated.

lastReportedTimestamp -> (timestamp)

The last time the Greengrass core device sent a message containing a componentâs state to the Amazon Web Services Cloud.

A component does not need to see a state change for this field to update.

lastInstallationSource -> (string)

The most recent deployment source that brought the component to the Greengrass core device. For a thing group deployment or thing deployment, the source will be the ID of the last deployment that contained the component. For local deployments it will be `LOCAL` .

### Note

Any deployment will attempt to reinstall currently broken components on the device, which will update the last installation source.

lifecycleStatusCodes -> (list)

The status codes that indicate the reason for failure whenever the `lifecycleState` has an error or is in a broken state.

### Note

Greengrass nucleus v2.8.0 or later is required to get an accurate `lifecycleStatusCodes` response. This response can be inaccurate in earlier Greengrass nucleus versions.

(string)

nextToken -> (string)

The token for the next set of results, or null if there are no additional results.