# create-layerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-layer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-layer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# create-layer

## Description

Creates a layer. For more information, see [How to Create a Layer](https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-create.html) .

### Note

You should use **CreateLayer** for noncustom layer types such as PHP App Server only if the stack does not have an existing layer of that type. A stack can have at most one instance of each noncustom layer; if you attempt to create a second instance, **CreateLayer** fails. A stack can have an arbitrary number of custom layers, so you can call **CreateLayer** as many times as you like for that layer type.

**Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateLayer)

## Synopsis

```
create-layer
--stack-id <value>
--type <value>
--name <value>
--shortname <value>
[--attributes <value>]
[--cloud-watch-logs-configuration <value>]
[--custom-instance-profile-arn <value>]
[--custom-json <value>]
[--custom-security-group-ids <value>]
[--packages <value>]
[--volume-configurations <value>]
[--enable-auto-healing | --no-enable-auto-healing]
[--auto-assign-elastic-ips | --no-auto-assign-elastic-ips]
[--auto-assign-public-ips | --no-auto-assign-public-ips]
[--custom-recipes <value>]
[--install-updates-on-boot | --no-install-updates-on-boot]
[--use-ebs-optimized-instances | --no-use-ebs-optimized-instances]
[--lifecycle-event-configuration <value>]
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

The layer stack ID.

`--type` (string)

The layer type. A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.

Possible values:

- `aws-flow-ruby`
- `ecs-cluster`
- `java-app`
- `lb`
- `web`
- `php-app`
- `rails-app`
- `nodejs-app`
- `memcached`
- `db-master`
- `monitoring-master`
- `custom`

`--name` (string)

The layer name, which is used by the console. Layer names can be a maximum of 32 characters.

`--shortname` (string)

For custom layers only, use this parameter to specify the layerâs short name, which is used internally by OpsWorks Stacks and by Chef recipes. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 32 characters, which are limited to the alphanumeric characters, â-â, â_â, and â.â.

Built-in layer short names are defined by OpsWorks Stacks. For more information, see the [Layer Reference](https://docs.aws.amazon.com/opsworks/latest/userguide/layers.html) .

`--attributes` (map)

One or more user-defined key-value pairs to be added to the stack attributes.

To create a cluster layer, set the `EcsClusterArn` attribute to the clusterâs ARN.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string

Where valid key names are:
  EcsClusterArn
  EnableHaproxyStats
  HaproxyStatsUrl
  HaproxyStatsUser
  HaproxyStatsPassword
  HaproxyHealthCheckUrl
  HaproxyHealthCheckMethod
  MysqlRootPassword
  MysqlRootPasswordUbiquitous
  GangliaUrl
  GangliaUser
  GangliaPassword
  MemcachedMemory
  NodejsVersion
  RubyVersion
  RubygemsVersion
  ManageBundler
  BundlerVersion
  RailsStack
  PassengerVersion
  Jvm
  JvmVersion
  JvmOptions
  JavaAppServer
  JavaAppServerVersion
```

JSON Syntax:

```
{"EcsClusterArn"|"EnableHaproxyStats"|"HaproxyStatsUrl"|"HaproxyStatsUser"|"HaproxyStatsPassword"|"HaproxyHealthCheckUrl"|"HaproxyHealthCheckMethod"|"MysqlRootPassword"|"MysqlRootPasswordUbiquitous"|"GangliaUrl"|"GangliaUser"|"GangliaPassword"|"MemcachedMemory"|"NodejsVersion"|"RubyVersion"|"RubygemsVersion"|"ManageBundler"|"BundlerVersion"|"RailsStack"|"PassengerVersion"|"Jvm"|"JvmVersion"|"JvmOptions"|"JavaAppServer"|"JavaAppServerVersion": "string"
  ...}
```

`--cloud-watch-logs-configuration` (structure)

Specifies CloudWatch Logs configuration options for the layer. For more information, see  CloudWatchLogsLogStream .

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

Shorthand Syntax:

```
Enabled=boolean,LogStreams=[{LogGroupName=string,DatetimeFormat=string,TimeZone=string,File=string,FileFingerprintLines=string,MultiLineStartPattern=string,InitialPosition=string,Encoding=string,BufferDuration=integer,BatchCount=integer,BatchSize=integer},{LogGroupName=string,DatetimeFormat=string,TimeZone=string,File=string,FileFingerprintLines=string,MultiLineStartPattern=string,InitialPosition=string,Encoding=string,BufferDuration=integer,BatchCount=integer,BatchSize=integer}]
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "LogStreams": [
    {
      "LogGroupName": "string",
      "DatetimeFormat": "string",
      "TimeZone": "LOCAL"|"UTC",
      "File": "string",
      "FileFingerprintLines": "string",
      "MultiLineStartPattern": "string",
      "InitialPosition": "start_of_file"|"end_of_file",
      "Encoding": "ascii"|"big5"|"big5hkscs"|"cp037"|"cp424"|"cp437"|"cp500"|"cp720"|"cp737"|"cp775"|"cp850"|"cp852"|"cp855"|"cp856"|"cp857"|"cp858"|"cp860"|"cp861"|"cp862"|"cp863"|"cp864"|"cp865"|"cp866"|"cp869"|"cp874"|"cp875"|"cp932"|"cp949"|"cp950"|"cp1006"|"cp1026"|"cp1140"|"cp1250"|"cp1251"|"cp1252"|"cp1253"|"cp1254"|"cp1255"|"cp1256"|"cp1257"|"cp1258"|"euc_jp"|"euc_jis_2004"|"euc_jisx0213"|"euc_kr"|"gb2312"|"gbk"|"gb18030"|"hz"|"iso2022_jp"|"iso2022_jp_1"|"iso2022_jp_2"|"iso2022_jp_2004"|"iso2022_jp_3"|"iso2022_jp_ext"|"iso2022_kr"|"latin_1"|"iso8859_2"|"iso8859_3"|"iso8859_4"|"iso8859_5"|"iso8859_6"|"iso8859_7"|"iso8859_8"|"iso8859_9"|"iso8859_10"|"iso8859_13"|"iso8859_14"|"iso8859_15"|"iso8859_16"|"johab"|"koi8_r"|"koi8_u"|"mac_cyrillic"|"mac_greek"|"mac_iceland"|"mac_latin2"|"mac_roman"|"mac_turkish"|"ptcp154"|"shift_jis"|"shift_jis_2004"|"shift_jisx0213"|"utf_32"|"utf_32_be"|"utf_32_le"|"utf_16"|"utf_16_be"|"utf_16_le"|"utf_7"|"utf_8"|"utf_8_sig",
      "BufferDuration": integer,
      "BatchCount": integer,
      "BatchSize": integer
    }
    ...
  ]
}
```

`--custom-instance-profile-arn` (string)

The ARN of an IAM profile to be used for the layerâs EC2 instances. For more information about IAM ARNs, see [Using Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) .

`--custom-json` (string)

A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layerâs instances. For more information, see [Using Custom JSON](https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html) . This feature is supported as of version 1.7.42 of the CLI.

`--custom-security-group-ids` (list)

An array containing the layer custom security group IDs.

(string)

Syntax:

```
"string" "string" ...
```

`--packages` (list)

An array of `Package` objects that describes the layer packages.

(string)

Syntax:

```
"string" "string" ...
```

`--volume-configurations` (list)

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

Shorthand Syntax:

```
MountPoint=string,RaidLevel=integer,NumberOfDisks=integer,Size=integer,VolumeType=string,Iops=integer,Encrypted=boolean ...
```

JSON Syntax:

```
[
  {
    "MountPoint": "string",
    "RaidLevel": integer,
    "NumberOfDisks": integer,
    "Size": integer,
    "VolumeType": "string",
    "Iops": integer,
    "Encrypted": true|false
  }
  ...
]
```

`--enable-auto-healing` | `--no-enable-auto-healing` (boolean)

Whether to disable auto healing for the layer.

`--auto-assign-elastic-ips` | `--no-auto-assign-elastic-ips` (boolean)

Whether to automatically assign an [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) to the layerâs instances. For more information, see [How to Edit a Layer](https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html) .

`--auto-assign-public-ips` | `--no-auto-assign-public-ips` (boolean)

For stacks that are running in a VPC, whether to automatically assign a public IP address to the layerâs instances. For more information, see [How to Edit a Layer](https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html) .

`--custom-recipes` (structure)

A `LayerCustomRecipes` object that specifies the layer custom recipes.

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

Shorthand Syntax:

```
Setup=string,string,Configure=string,string,Deploy=string,string,Undeploy=string,string,Shutdown=string,string
```

JSON Syntax:

```
{
  "Setup": ["string", ...],
  "Configure": ["string", ...],
  "Deploy": ["string", ...],
  "Undeploy": ["string", ...],
  "Shutdown": ["string", ...]
}
```

`--install-updates-on-boot` | `--no-install-updates-on-boot` (boolean)

Whether to install operating system and package updates when the instance boots. The default value is `true` . To control when updates are installed, set this value to `false` . You must then update your instances manually by using  CreateDeployment to run the `update_dependencies` stack command or by manually running `yum` (Amazon Linux) or `apt-get` (Ubuntu) on the instances.

### Note

To ensure that your instances have the latest security updates, we strongly recommend using the default value of `true` .

`--use-ebs-optimized-instances` | `--no-use-ebs-optimized-instances` (boolean)

Whether to use Amazon EBS-optimized instances.

`--lifecycle-event-configuration` (structure)

A `LifeCycleEventConfiguration` object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.

Shutdown -> (structure)

A `ShutdownEventConfiguration` object that specifies the Shutdown event configuration.

ExecutionTimeout -> (integer)

The time, in seconds, that OpsWorks Stacks waits after triggering a Shutdown event before shutting down an instance.

DelayUntilElbConnectionsDrained -> (boolean)

Whether to enable Elastic Load Balancing connection draining. For more information, see [Connection Draining](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain)

Shorthand Syntax:

```
Shutdown={ExecutionTimeout=integer,DelayUntilElbConnectionsDrained=boolean}
```

JSON Syntax:

```
{
  "Shutdown": {
    "ExecutionTimeout": integer,
    "DelayUntilElbConnectionsDrained": true|false
  }
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a layer**

The following `create-layer` command creates a PHP App Server layer named MyPHPLayer in a specified stack.

```
aws opsworks create-layer --region us-east-1 --stack-id f6673d70-32e6-4425-8999-265dd002fec7 --type php-app --name MyPHPLayer --shortname myphplayer
```

*Output*:

```
{
  "LayerId": "0b212672-6b4b-40e4-8a34-5a943cf2e07a"
}
```

**More Information**

For more information, see [How to Create a Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-create.html) in the *AWS OpsWorks User Guide*.

## Output

LayerId -> (string)

The layer ID.