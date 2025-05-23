# describe-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [discovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/index.html#cli-aws-discovery) ]

# describe-configurations

## Description

Retrieves attributes for a list of configuration item IDs.

### Note

All of the supplied IDs must be for the same asset type from one of the following:

- server
- application
- process
- connection

Output fields are specific to the asset type specified. For example, the output for a *server* configuration item includes a list of attributes about the server, such as host name, operating system, number of network cards, etc.

For a complete list of outputs for each asset type, see [Using the DescribeConfigurations Action](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#DescribeConfigurations) in the *Amazon Web Services Application Discovery Service User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeConfigurations)

## Synopsis

```
describe-configurations
--configuration-ids <value>
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

`--configuration-ids` (list)

One or more configuration IDs.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Describe selected asset configurations**

This example command describes the configurations of two specified servers. The action detects the type of asset from the configuration ID. Only one type of asset is allowed per command.

Command:

```
aws discovery describe-configurations --configuration-ids "d-server-099385097ef9fbcfb" "d-server-0c4f2dd1fee22c6c1"
```

Output:

```
{
    "configurations": [
        {
                 "server.performance.maxCpuUsagePct": "0.0",
                 "server.performance.maxDiskReadIOPS": "0.0",
                 "server.performance.avgCpuUsagePct": "0.0",
                 "server.type": "EC2",
                 "server.performance.maxNetworkReadsPerSecondInKB": "0.19140625",
                 "server.hostName": "ip-172-31-35-152",
                 "server.configurationId": "d-server-0c4f2dd1fee22c6c1",
                 "server.tags.hasMoreValues": "false",
                 "server.performance.minFreeRAMInKB": "1543496.0",
                 "server.osVersion": "3.14.48-33.39.amzn1.x86_64",
                 "server.performance.maxDiskReadsPerSecondInKB": "0.0",
                 "server.applications": "[]",
                 "server.performance.numDisks": "1",
                 "server.performance.numCpus": "1",
                 "server.performance.numCores": "1",
                 "server.performance.maxDiskWriteIOPS": "0.0",
                 "server.performance.maxNetworkWritesPerSecondInKB": "0.82421875",
                 "server.performance.avgDiskWritesPerSecondInKB": "0.0",
                 "server.networkInterfaceInfo": "[{\"name\":\"eth0\",\"macAddress\":\"06:A7:7D:3F:54:57\",\"ipAddress\":\"172.31.35.152\",\"netMask\":\"255.255.240.0\"},{\"name\":\"lo\",\"macAddress\":\"00:00:00:00:00:00\",\"ipAddress\":\"127.0.0.1\",\"netMask\":\"255.0.0.0\"},{\"name\":\"eth0\",\"macAddress\":\"06:A7:7D:3F:54:57\",\"ipAddress\":\"fe80::4a7:7dff:fe3f:5457\"},{\"name\":\"lo\",\"macAddress\":\"00:00:00:00:00:00\",\"ipAddress\":\"::1\"}]",
                 "server.performance.avgNetworkReadsPerSecondInKB": "0.04915364583333333",
                 "server.tags": "[]",
                 "server.applications.hasMoreValues": "false",
                 "server.timeOfCreation": "2016-10-28 23:44:00.0",
                 "server.agentId": "i-4447bc1b",
                 "server.performance.maxDiskWritesPerSecondInKB": "0.0",
                 "server.performance.avgDiskReadIOPS": "0.0",
                 "server.performance.avgFreeRAMInKB": "1547210.1333333333",
                 "server.performance.avgDiskReadsPerSecondInKB": "0.0",
                 "server.performance.avgDiskWriteIOPS": "0.0",
                 "server.performance.numNetworkCards": "2",
                 "server.hypervisor": "xen",
                 "server.networkInterfaceInfo.hasMoreValues": "false",
                 "server.performance.avgNetworkWritesPerSecondInKB": "0.1380859375",
                 "server.osName": "Linux - Amazon Linux AMI release 2015.03",
                 "server.performance.totalRAMInKB": "1694732.0",
                 "server.cpuType": "x64"
        },
        {
                 "server.performance.maxCpuUsagePct": "100.0",
                 "server.performance.maxDiskReadIOPS": "0.0",
                 "server.performance.avgCpuUsagePct": "14.733333333333338",
                 "server.type": "EC2",
                 "server.performance.maxNetworkReadsPerSecondInKB": "13.400390625",
                 "server.hostName": "ip-172-31-42-208",
                 "server.configurationId": "d-server-099385097ef9fbcfb",
                 "server.tags.hasMoreValues": "false",
                 "server.performance.minFreeRAMInKB": "1531104.0",
                 "server.osVersion": "3.14.48-33.39.amzn1.x86_64",
                 "server.performance.maxDiskReadsPerSecondInKB": "0.0",
                 "server.applications": "[]",
                 "server.performance.numDisks": "1",
                 "server.performance.numCpus": "1",
                 "server.performance.numCores": "1",
                 "server.performance.maxDiskWriteIOPS": "1.0",
                 "server.performance.maxNetworkWritesPerSecondInKB": "12.271484375",
                 "server.performance.avgDiskWritesPerSecondInKB": "0.5333333333333334",
                 "server.networkInterfaceInfo": "[{\"name\":\"eth0\",\"macAddress\":\"06:4A:79:60:75:61\",\"ipAddress\":\"172.31.42.208\",\"netMask\":\"255.255.240.0\"},{\"name\":\"eth0\",\"macAddress\":\"06:4A:79:60:75:61\",\"ipAddress\":\"fe80::44a:79ff:fe60:7561\"},{\"name\":\"lo\",\"macAddress\":\"00:00:00:00:00:00\",\"ipAddress\":\"::1\"},{\"name\":\"lo\",\"macAddress\":\"00:00:00:00:00:00\",\"ipAddress\":\"127.0.0.1\",\"netMask\":\"255.0.0.0\"}]",
                 "server.performance.avgNetworkReadsPerSecondInKB": "2.8720052083333334",
                 "server.tags": "[]",
                 "server.applications.hasMoreValues": "false",
                 "server.timeOfCreation": "2016-10-28 23:44:30.0",
                 "server.agentId": "i-c142b99e",
                 "server.performance.maxDiskWritesPerSecondInKB": "4.0",
                 "server.performance.avgDiskReadIOPS": "0.0",
                 "server.performance.avgFreeRAMInKB": "1534946.4",
                 "server.performance.avgDiskReadsPerSecondInKB": "0.0",
                 "server.performance.avgDiskWriteIOPS": "0.13333333333333336",
                 "server.performance.numNetworkCards": "2",
                 "server.hypervisor": "xen",
                 "server.networkInterfaceInfo.hasMoreValues": "false",
                 "server.performance.avgNetworkWritesPerSecondInKB": "1.7977864583333332",
                 "server.osName": "Linux - Amazon Linux AMI release 2015.03",
                 "server.performance.totalRAMInKB": "1694732.0",
                 "server.cpuType": "x64"
        }
    ]
}
```

**Describe selected asset configurations**

This example command describes the configurations of two specified applications. The action detects the type of asset from the configuration ID. Only one type of asset is allowed per command.

Command:

```
aws discovery describe-configurations --configuration-ids "d-application-0ac39bc0e4fad0e42" "d-application-02444a45288013764q"
```

Output:

```
{
    "configurations": [
        {
                 "application.serverCount": "0",
                 "application.name": "Application-12345",
                 "application.lastModifiedTime": "2016-12-13 23:53:27.0",
                 "application.description": "",
                 "application.timeOfCreation": "2016-12-13 23:53:27.0",
                 "application.configurationId": "d-application-0ac39bc0e4fad0e42"
        },
        {
                 "application.serverCount": "0",
                 "application.name": "Application-67890",
                 "application.lastModifiedTime": "2016-12-13 23:53:33.0",
                 "application.description": "",
                 "application.timeOfCreation": "2016-12-13 23:53:33.0",
                 "application.configurationId": "d-application-02444a45288013764"
         }
    ]
}
```

## Output

configurations -> (list)

A key in the response map. The value is an array of data.

(map)

key -> (string)

value -> (string)