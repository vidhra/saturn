# modify-replication-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# modify-replication-config

## Description

Modifies an existing DMS Serverless replication configuration that you can use to start a replication. This command includes input validation and logic to check the state of any replication that uses this configuration. You can only modify a replication configuration before any replication that uses it has started. As soon as you have initially started a replication with a given configuiration, you canât modify that configuration, even if you stop it.

Other run statuses that allow you to run this command include FAILED and CREATED. A provisioning state that allows you to run this command is FAILED_PROVISION.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyReplicationConfig)

## Synopsis

```
modify-replication-config
--replication-config-arn <value>
[--replication-config-identifier <value>]
[--replication-type <value>]
[--table-mappings <value>]
[--replication-settings <value>]
[--supplemental-settings <value>]
[--compute-config <value>]
[--source-endpoint-arn <value>]
[--target-endpoint-arn <value>]
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

`--replication-config-arn` (string)

The Amazon Resource Name of the replication to modify.

`--replication-config-identifier` (string)

The new replication config to apply to the replication.

`--replication-type` (string)

The type of replication.

Possible values:

- `full-load`
- `cdc`
- `full-load-and-cdc`

`--table-mappings` (string)

Table mappings specified in the replication.

`--replication-settings` (string)

The settings for the replication.

`--supplemental-settings` (string)

Additional settings for the replication.

`--compute-config` (structure)

Configuration parameters for provisioning an DMS Serverless replication.

AvailabilityZone -> (string)

The Availability Zone where the DMS Serverless replication using this configuration will run. The default value is a random, system-chosen Availability Zone in the configurationâs Amazon Web Services Region, for example, `"us-west-2"` . You canât set this parameter if the `MultiAZ` parameter is set to `true` .

DnsNameServers -> (string)

A list of custom DNS name servers supported for the DMS Serverless replication to access your source or target database. This list overrides the default name servers supported by the DMS Serverless replication. You can specify a comma-separated list of internet addresses for up to four DNS name servers. For example: `"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"`

KmsKeyId -> (string)

An Key Management Service (KMS) key Amazon Resource Name (ARN) that is used to encrypt the data during DMS Serverless replication.

If you donât specify a value for the `KmsKeyId` parameter, DMS uses your default encryption key.

KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

MaxCapacityUnits -> (integer)

Specifies the maximum value of the DMS capacity units (DCUs) for which a given DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the maximum value that you can specify for DMS Serverless is 384. The `MaxCapacityUnits` parameter is the only DCU parameter you are required to specify.

MinCapacityUnits -> (integer)

Specifies the minimum value of the DMS capacity units (DCUs) for which a given DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the minimum DCU value that you can specify for DMS Serverless is 1. If you donât set this value, DMS sets this parameter to the minimum DCU value allowed, 1. If there is no current source activity, DMS scales down your replication until it reaches the value specified in `MinCapacityUnits` .

MultiAZ -> (boolean)

Specifies whether the DMS Serverless replication is a Multi-AZ deployment. You canât set the `AvailabilityZone` parameter if the `MultiAZ` parameter is set to `true` .

PreferredMaintenanceWindow -> (string)

The weekly time range during which system maintenance can occur for the DMS Serverless replication, in Universal Coordinated Time (UTC). The format is `ddd:hh24:mi-ddd:hh24:mi` .

The default is a 30-minute window selected at random from an 8-hour block of time per Amazon Web Services Region. This maintenance occurs on a random day of the week. Valid values for days of the week include `Mon` , `Tue` , `Wed` , `Thu` , `Fri` , `Sat` , and `Sun` .

Constraints include a minimum 30-minute window.

ReplicationSubnetGroupId -> (string)

Specifies a subnet group identifier to associate with the DMS Serverless replication.

VpcSecurityGroupIds -> (list)

Specifies the virtual private cloud (VPC) security group to use with the DMS Serverless replication. The VPC security group must work with the VPC containing the replication.

(string)

Shorthand Syntax:

```
AvailabilityZone=string,DnsNameServers=string,KmsKeyId=string,MaxCapacityUnits=integer,MinCapacityUnits=integer,MultiAZ=boolean,PreferredMaintenanceWindow=string,ReplicationSubnetGroupId=string,VpcSecurityGroupIds=string,string
```

JSON Syntax:

```
{
  "AvailabilityZone": "string",
  "DnsNameServers": "string",
  "KmsKeyId": "string",
  "MaxCapacityUnits": integer,
  "MinCapacityUnits": integer,
  "MultiAZ": true|false,
  "PreferredMaintenanceWindow": "string",
  "ReplicationSubnetGroupId": "string",
  "VpcSecurityGroupIds": ["string", ...]
}
```

`--source-endpoint-arn` (string)

The Amazon Resource Name (ARN) of the source endpoint for this DMS serverless replication configuration.

`--target-endpoint-arn` (string)

The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration.

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

ReplicationConfig -> (structure)

Information about the serverless replication config that was modified.

ReplicationConfigIdentifier -> (string)

The identifier for the `ReplicationConfig` associated with the replication.

ReplicationConfigArn -> (string)

The Amazon Resource Name (ARN) of this DMS Serverless replication configuration.

SourceEndpointArn -> (string)

The Amazon Resource Name (ARN) of the source endpoint for this DMS serverless replication configuration.

TargetEndpointArn -> (string)

The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration.

ReplicationType -> (string)

The type of the replication.

ComputeConfig -> (structure)

Configuration parameters for provisioning an DMS serverless replication.

AvailabilityZone -> (string)

The Availability Zone where the DMS Serverless replication using this configuration will run. The default value is a random, system-chosen Availability Zone in the configurationâs Amazon Web Services Region, for example, `"us-west-2"` . You canât set this parameter if the `MultiAZ` parameter is set to `true` .

DnsNameServers -> (string)

A list of custom DNS name servers supported for the DMS Serverless replication to access your source or target database. This list overrides the default name servers supported by the DMS Serverless replication. You can specify a comma-separated list of internet addresses for up to four DNS name servers. For example: `"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"`

KmsKeyId -> (string)

An Key Management Service (KMS) key Amazon Resource Name (ARN) that is used to encrypt the data during DMS Serverless replication.

If you donât specify a value for the `KmsKeyId` parameter, DMS uses your default encryption key.

KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

MaxCapacityUnits -> (integer)

Specifies the maximum value of the DMS capacity units (DCUs) for which a given DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the maximum value that you can specify for DMS Serverless is 384. The `MaxCapacityUnits` parameter is the only DCU parameter you are required to specify.

MinCapacityUnits -> (integer)

Specifies the minimum value of the DMS capacity units (DCUs) for which a given DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the minimum DCU value that you can specify for DMS Serverless is 1. If you donât set this value, DMS sets this parameter to the minimum DCU value allowed, 1. If there is no current source activity, DMS scales down your replication until it reaches the value specified in `MinCapacityUnits` .

MultiAZ -> (boolean)

Specifies whether the DMS Serverless replication is a Multi-AZ deployment. You canât set the `AvailabilityZone` parameter if the `MultiAZ` parameter is set to `true` .

PreferredMaintenanceWindow -> (string)

The weekly time range during which system maintenance can occur for the DMS Serverless replication, in Universal Coordinated Time (UTC). The format is `ddd:hh24:mi-ddd:hh24:mi` .

The default is a 30-minute window selected at random from an 8-hour block of time per Amazon Web Services Region. This maintenance occurs on a random day of the week. Valid values for days of the week include `Mon` , `Tue` , `Wed` , `Thu` , `Fri` , `Sat` , and `Sun` .

Constraints include a minimum 30-minute window.

ReplicationSubnetGroupId -> (string)

Specifies a subnet group identifier to associate with the DMS Serverless replication.

VpcSecurityGroupIds -> (list)

Specifies the virtual private cloud (VPC) security group to use with the DMS Serverless replication. The VPC security group must work with the VPC containing the replication.

(string)

ReplicationSettings -> (string)

Configuration parameters for an DMS serverless replication.

SupplementalSettings -> (string)

Additional parameters for an DMS serverless replication.

TableMappings -> (string)

Table mappings specified in the replication.

ReplicationConfigCreateTime -> (timestamp)

The time the serverless replication config was created.

ReplicationConfigUpdateTime -> (timestamp)

The time the serverless replication config was updated.