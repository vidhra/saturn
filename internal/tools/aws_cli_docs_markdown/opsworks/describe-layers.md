# describe-layersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-layers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-layers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# describe-layers

## Description

Requests a description of one or more layers in a specified stack.

### Note

This call accepts only one resource-identifying parameter.

**Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information about user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeLayers)

## Synopsis

```
describe-layers
[--stack-id <value>]
[--layer-ids <value>]
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

`--stack-id` (string)

The stack ID.

`--layer-ids` (list)

An array of layer IDs that specify the layers to be described. If you omit this parameter, `DescribeLayers` returns a description of every layer in the specified stack.

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

**To describe a stackâs layers**

The following `describe-layers` command describes the layers in a specified stack:

```
aws opsworks --region us-east-1 describe-layers --stack-id 38ee91e2-abdc-4208-a107-0b7168b3cc7a
```

*Output*:

```
{
  "Layers": [
      {
          "StackId": "38ee91e2-abdc-4208-a107-0b7168b3cc7a",
          "Type": "db-master",
          "DefaultSecurityGroupNames": [
              "AWS-OpsWorks-DB-Master-Server"
          ],
          "Name": "MySQL",
          "Packages": [],
          "DefaultRecipes": {
              "Undeploy": [],
              "Setup": [
                  "opsworks_initial_setup",
                  "ssh_host_keys",
                  "ssh_users",
                  "mysql::client",
                  "dependencies",
                  "ebs",
                  "opsworks_ganglia::client",
                  "mysql::server",
                  "dependencies",
                  "deploy::mysql"
              ],
              "Configure": [
                  "opsworks_ganglia::configure-client",
                  "ssh_users",
                  "agent_version",
                  "deploy::mysql"
              ],
              "Shutdown": [
                  "opsworks_shutdown::default",
                  "mysql::stop"
              ],
              "Deploy": [
                  "deploy::default",
                  "deploy::mysql"
              ]
          },
          "CustomRecipes": {
              "Undeploy": [],
              "Setup": [],
              "Configure": [],
              "Shutdown": [],
              "Deploy": []
          },
          "EnableAutoHealing": false,
          "LayerId": "41a20847-d594-4325-8447-171821916b73",
          "Attributes": {
              "MysqlRootPasswordUbiquitous": "true",
              "RubygemsVersion": null,
              "RailsStack": null,
              "HaproxyHealthCheckMethod": null,
              "RubyVersion": null,
              "BundlerVersion": null,
              "HaproxyStatsPassword": null,
              "PassengerVersion": null,
              "MemcachedMemory": null,
              "EnableHaproxyStats": null,
              "ManageBundler": null,
              "NodejsVersion": null,
              "HaproxyHealthCheckUrl": null,
              "MysqlRootPassword": "*****FILTERED*****",
              "GangliaPassword": null,
              "GangliaUser": null,
              "HaproxyStatsUrl": null,
              "GangliaUrl": null,
              "HaproxyStatsUser": null
          },
          "Shortname": "db-master",
          "AutoAssignElasticIps": false,
          "CustomSecurityGroupIds": [],
          "CreatedAt": "2013-07-25T18:11:19+00:00",
          "VolumeConfigurations": [
              {
                  "MountPoint": "/vol/mysql",
                  "Size": 10,
                  "NumberOfDisks": 1
              }
          ]
      },
      {
          "StackId": "38ee91e2-abdc-4208-a107-0b7168b3cc7a",
          "Type": "custom",
          "DefaultSecurityGroupNames": [
              "AWS-OpsWorks-Custom-Server"
          ],
          "Name": "TomCustom",
          "Packages": [],
          "DefaultRecipes": {
              "Undeploy": [],
              "Setup": [
                  "opsworks_initial_setup",
                  "ssh_host_keys",
                  "ssh_users",
                  "mysql::client",
                  "dependencies",
                  "ebs",
                  "opsworks_ganglia::client"
              ],
              "Configure": [
                  "opsworks_ganglia::configure-client",
                  "ssh_users",
                  "agent_version"
              ],
              "Shutdown": [
                  "opsworks_shutdown::default"
              ],
              "Deploy": [
                  "deploy::default"
              ]
          },
          "CustomRecipes": {
              "Undeploy": [],
              "Setup": [
                  "tomcat::setup"
              ],
              "Configure": [
                  "tomcat::configure"
              ],
              "Shutdown": [],
              "Deploy": [
                  "tomcat::deploy"
              ]
          },
          "EnableAutoHealing": true,
          "LayerId": "e6cbcd29-d223-40fc-8243-2eb213377440",
          "Attributes": {
              "MysqlRootPasswordUbiquitous": null,
              "RubygemsVersion": null,
              "RailsStack": null,
              "HaproxyHealthCheckMethod": null,
              "RubyVersion": null,
              "BundlerVersion": null,
              "HaproxyStatsPassword": null,
              "PassengerVersion": null,
              "MemcachedMemory": null,
              "EnableHaproxyStats": null,
              "ManageBundler": null,
              "NodejsVersion": null,
              "HaproxyHealthCheckUrl": null,
              "MysqlRootPassword": null,
              "GangliaPassword": null,
              "GangliaUser": null,
              "HaproxyStatsUrl": null,
              "GangliaUrl": null,
              "HaproxyStatsUser": null
          },
          "Shortname": "tomcustom",
          "AutoAssignElasticIps": false,
          "CustomSecurityGroupIds": [],
          "CreatedAt": "2013-07-25T18:12:53+00:00",
          "VolumeConfigurations": []
      }
  ]
}
```

**More Information**

For more information, see [Layers](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers.html) in the *AWS OpsWorks User Guide*.

## Output

Layers -> (list)

An array of `Layer` objects that describe the layers.

(structure)

Describes a layer.

Arn -> (string)

The Amazon Resource Number (ARN) of a layer.

StackId -> (string)

The layer stack ID.

LayerId -> (string)

The layer ID.

Type -> (string)

The layer type.

Name -> (string)

The layer name. Layer names can be a maximum of 32 characters.

Shortname -> (string)

The layer short name.

Attributes -> (map)

The layer attributes.

For the `HaproxyStatsPassword` , `MysqlRootPassword` , and `GangliaPassword` attributes, OpsWorks Stacks returns `*****FILTERED*****` instead of the actual value

For an ECS Cluster layer, OpsWorks Stacks the `EcsClusterArn` attribute is set to the clusterâs ARN.

key -> (string)

value -> (string)

CloudWatchLogsConfiguration -> (structure)

The Amazon CloudWatch Logs configuration settings for the layer.

Enabled -> (boolean)

Whether CloudWatch Logs is enabled for a layer.

LogStreams -> (list)

A list of configuration options for CloudWatch Logs.

(structure)

Describes the CloudWatch Logs configuration for a layer. For detailed information about members of this data type, see the [CloudWatch Logs Agent Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html) .

LogGroupName -> (string)

Specifies the destination log group. A log group is created automatically if it doesnât already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, â_â (underscore), â-â (hyphen), â/â (forward slash), and â.â (period).

DatetimeFormat -> (string)

Specifies how the time stamp is extracted from logs. For more information, see the [CloudWatch Logs Agent Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html) .

TimeZone -> (string)

Specifies the time zone of log event time stamps.

File -> (string)

Specifies log files that you want to push to CloudWatch Logs.

`File` can point to a specific file or multiple files (by using wild card characters such as `/var/log/system.log*` ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as `access_log.2014-06-01-01` , `access_log.2014-06-01-02` , and so on by using a pattern like `access_log.*` . Donât use a wildcard to match multiple file types, such as `access_log_80` and `access_log_443` . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.

Zipped files are not supported.

FileFingerprintLines -> (string)

Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as â1â, â2-5â. The default value is â1â, meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.

MultiLineStartPattern -> (string)

Specifies the pattern for identifying the start of a log message.

InitialPosition -> (string)

Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.

Encoding -> (string)

Specifies the encoding of the log file so that the file can be read correctly. The default is `utf_8` . Encodings supported by Python `codecs.decode()` can be used here.

BufferDuration -> (integer)

Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.

BatchCount -> (integer)

Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

BatchSize -> (integer)

Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.

CustomInstanceProfileArn -> (string)

The ARN of the default IAM profile to be used for the layerâs EC2 instances. For more information about IAM ARNs, see [Using Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) .

CustomJson -> (string)

A JSON formatted string containing the layerâs custom stack configuration and deployment attributes.

CustomSecurityGroupIds -> (list)

An array containing the layerâs custom security group IDs.

(string)

DefaultSecurityGroupNames -> (list)

An array containing the layerâs security group names.

(string)

Packages -> (list)

An array of `Package` objects that describe the layerâs packages.

(string)

VolumeConfigurations -> (list)

A `VolumeConfigurations` object that describes the layerâs Amazon EBS volumes.

(structure)

Describes an Amazon EBS volume configuration.

MountPoint -> (string)

The volume mount point. For example â/dev/sdhâ.

RaidLevel -> (integer)

The volume [RAID level](http://en.wikipedia.org/wiki/Standard_RAID_levels) .

NumberOfDisks -> (integer)

The number of disks in the volume.

Size -> (integer)

The volume size.

VolumeType -> (string)

The volume type. For more information, see [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) .

- `standard` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.
- `io1` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.
- `gp2` - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.
- `st1` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 125 GiB and a maximum size of 16384 GiB.
- `sc1` - Cold HDD. Cold HDD volumes must have a minimum size of 125 GiB and a maximum size of 16384 GiB.

Iops -> (integer)

For PIOPS volumes, the IOPS per disk.

Encrypted -> (boolean)

Specifies whether an Amazon EBS volume is encrypted. For more information, see [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) .

EnableAutoHealing -> (boolean)

Whether auto healing is disabled for the layer.

AutoAssignElasticIps -> (boolean)

Whether to automatically assign an [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) to the layerâs instances. For more information, see [How to Edit a Layer](https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html) .

AutoAssignPublicIps -> (boolean)

For stacks that are running in a VPC, whether to automatically assign a public IP address to the layerâs instances. For more information, see [How to Edit a Layer](https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html) .

DefaultRecipes -> (structure)

OpsWorks Stacks supports five lifecycle events: **setup** , **configuration** , **deploy** , **undeploy** , and **shutdown** . For each layer, OpsWorks Stacks runs a set of standard recipes for each event. You can also provide custom recipes for any or all layers and events. OpsWorks Stacks runs custom event recipes after the standard recipes. `LayerCustomRecipes` specifies the custom recipes for a particular layer to be run in response to each of the five events.

To specify a recipe, use the cookbookâs directory name in the repository followed by two colons and the recipe name, which is the recipeâs file name without the `.rb` extension. For example: `phpapp2::dbsetup` specifies the `dbsetup.rb` recipe in the repositoryâs `phpapp2` folder.

Setup -> (list)

An array of custom recipe names to be run following a `setup` event.

(string)

Configure -> (list)

An array of custom recipe names to be run following a `configure` event.

(string)

Deploy -> (list)

An array of custom recipe names to be run following a `deploy` event.

(string)

Undeploy -> (list)

An array of custom recipe names to be run following a `undeploy` event.

(string)

Shutdown -> (list)

An array of custom recipe names to be run following a `shutdown` event.

(string)

CustomRecipes -> (structure)

A `LayerCustomRecipes` object that specifies the layerâs custom recipes.

Setup -> (list)

An array of custom recipe names to be run following a `setup` event.

(string)

Configure -> (list)

An array of custom recipe names to be run following a `configure` event.

(string)

Deploy -> (list)

An array of custom recipe names to be run following a `deploy` event.

(string)

Undeploy -> (list)

An array of custom recipe names to be run following a `undeploy` event.

(string)

Shutdown -> (list)

An array of custom recipe names to be run following a `shutdown` event.

(string)

CreatedAt -> (string)

Date when the layer was created.

InstallUpdatesOnBoot -> (boolean)

Whether to install operating system and package updates when the instance boots. The default value is `true` . If this value is set to `false` , you must then update your instances manually by using  CreateDeployment to run the `update_dependencies` stack command or manually running `yum` (Amazon Linux) or `apt-get` (Ubuntu) on the instances.

### Note

We strongly recommend using the default value of `true` , to ensure that your instances have the latest security updates.

UseEbsOptimizedInstances -> (boolean)

Whether the layer uses Amazon EBS-optimized instances.

LifecycleEventConfiguration -> (structure)

A `LifeCycleEventConfiguration` object that specifies the Shutdown event configuration.

Shutdown -> (structure)

A `ShutdownEventConfiguration` object that specifies the Shutdown event configuration.

ExecutionTimeout -> (integer)

The time, in seconds, that OpsWorks Stacks waits after triggering a Shutdown event before shutting down an instance.

DelayUntilElbConnectionsDrained -> (boolean)

Whether to enable Elastic Load Balancing connection draining. For more information, see [Connection Draining](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain)