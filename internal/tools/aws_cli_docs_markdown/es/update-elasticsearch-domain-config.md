# update-elasticsearch-domain-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-elasticsearch-domain-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-elasticsearch-domain-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [es](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/index.html#cli-aws-es) ]

# update-elasticsearch-domain-config

## Description

Modifies the cluster configuration of the specified Elasticsearch domain, setting as setting the instance type and the number of instances.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/UpdateElasticsearchDomainConfig)

## Synopsis

```
update-elasticsearch-domain-config
--domain-name <value>
[--elasticsearch-cluster-config <value>]
[--ebs-options <value>]
[--snapshot-options <value>]
[--vpc-options <value>]
[--cognito-options <value>]
[--advanced-options <value>]
[--access-policies <value>]
[--log-publishing-options <value>]
[--domain-endpoint-options <value>]
[--advanced-security-options <value>]
[--node-to-node-encryption-options <value>]
[--encryption-at-rest-options <value>]
[--auto-tune-options <value>]
[--dry-run | --no-dry-run]
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

`--domain-name` (string)

The name of the Elasticsearch domain that you are updating.

`--elasticsearch-cluster-config` (structure)

The type and number of instances to instantiate for the domain cluster.

InstanceType -> (string)

The instance type for an Elasticsearch cluster. UltraWarm instance types are not supported for data instances.

InstanceCount -> (integer)

The number of instances in the specified domain cluster.

DedicatedMasterEnabled -> (boolean)

A boolean value to indicate whether a dedicated master node is enabled. See [About Dedicated Master Nodes](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes) for more information.

ZoneAwarenessEnabled -> (boolean)

A boolean value to indicate whether zone awareness is enabled. See [About Zone Awareness](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness) for more information.

ZoneAwarenessConfig -> (structure)

Specifies the zone awareness configuration for a domain when zone awareness is enabled.

AvailabilityZoneCount -> (integer)

An integer value to indicate the number of availability zones for a domain when zone awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled

DedicatedMasterType -> (string)

The instance type for a dedicated master node.

DedicatedMasterCount -> (integer)

Total number of dedicated master nodes, active and on standby, for the cluster.

WarmEnabled -> (boolean)

True to enable warm storage.

WarmType -> (string)

The instance type for the Elasticsearch clusterâs warm nodes.

WarmCount -> (integer)

The number of warm nodes in the cluster.

ColdStorageOptions -> (structure)

Specifies the `ColdStorageOptions` config for Elasticsearch Domain

Enabled -> (boolean)

Enable cold storage option. Accepted values true or false

Shorthand Syntax:

```
InstanceType=string,InstanceCount=integer,DedicatedMasterEnabled=boolean,ZoneAwarenessEnabled=boolean,ZoneAwarenessConfig={AvailabilityZoneCount=integer},DedicatedMasterType=string,DedicatedMasterCount=integer,WarmEnabled=boolean,WarmType=string,WarmCount=integer,ColdStorageOptions={Enabled=boolean}
```

JSON Syntax:

```
{
  "InstanceType": "m3.medium.elasticsearch"|"m3.large.elasticsearch"|"m3.xlarge.elasticsearch"|"m3.2xlarge.elasticsearch"|"m4.large.elasticsearch"|"m4.xlarge.elasticsearch"|"m4.2xlarge.elasticsearch"|"m4.4xlarge.elasticsearch"|"m4.10xlarge.elasticsearch"|"m5.large.elasticsearch"|"m5.xlarge.elasticsearch"|"m5.2xlarge.elasticsearch"|"m5.4xlarge.elasticsearch"|"m5.12xlarge.elasticsearch"|"r5.large.elasticsearch"|"r5.xlarge.elasticsearch"|"r5.2xlarge.elasticsearch"|"r5.4xlarge.elasticsearch"|"r5.12xlarge.elasticsearch"|"c5.large.elasticsearch"|"c5.xlarge.elasticsearch"|"c5.2xlarge.elasticsearch"|"c5.4xlarge.elasticsearch"|"c5.9xlarge.elasticsearch"|"c5.18xlarge.elasticsearch"|"ultrawarm1.medium.elasticsearch"|"ultrawarm1.large.elasticsearch"|"t2.micro.elasticsearch"|"t2.small.elasticsearch"|"t2.medium.elasticsearch"|"r3.large.elasticsearch"|"r3.xlarge.elasticsearch"|"r3.2xlarge.elasticsearch"|"r3.4xlarge.elasticsearch"|"r3.8xlarge.elasticsearch"|"i2.xlarge.elasticsearch"|"i2.2xlarge.elasticsearch"|"d2.xlarge.elasticsearch"|"d2.2xlarge.elasticsearch"|"d2.4xlarge.elasticsearch"|"d2.8xlarge.elasticsearch"|"c4.large.elasticsearch"|"c4.xlarge.elasticsearch"|"c4.2xlarge.elasticsearch"|"c4.4xlarge.elasticsearch"|"c4.8xlarge.elasticsearch"|"r4.large.elasticsearch"|"r4.xlarge.elasticsearch"|"r4.2xlarge.elasticsearch"|"r4.4xlarge.elasticsearch"|"r4.8xlarge.elasticsearch"|"r4.16xlarge.elasticsearch"|"i3.large.elasticsearch"|"i3.xlarge.elasticsearch"|"i3.2xlarge.elasticsearch"|"i3.4xlarge.elasticsearch"|"i3.8xlarge.elasticsearch"|"i3.16xlarge.elasticsearch",
  "InstanceCount": integer,
  "DedicatedMasterEnabled": true|false,
  "ZoneAwarenessEnabled": true|false,
  "ZoneAwarenessConfig": {
    "AvailabilityZoneCount": integer
  },
  "DedicatedMasterType": "m3.medium.elasticsearch"|"m3.large.elasticsearch"|"m3.xlarge.elasticsearch"|"m3.2xlarge.elasticsearch"|"m4.large.elasticsearch"|"m4.xlarge.elasticsearch"|"m4.2xlarge.elasticsearch"|"m4.4xlarge.elasticsearch"|"m4.10xlarge.elasticsearch"|"m5.large.elasticsearch"|"m5.xlarge.elasticsearch"|"m5.2xlarge.elasticsearch"|"m5.4xlarge.elasticsearch"|"m5.12xlarge.elasticsearch"|"r5.large.elasticsearch"|"r5.xlarge.elasticsearch"|"r5.2xlarge.elasticsearch"|"r5.4xlarge.elasticsearch"|"r5.12xlarge.elasticsearch"|"c5.large.elasticsearch"|"c5.xlarge.elasticsearch"|"c5.2xlarge.elasticsearch"|"c5.4xlarge.elasticsearch"|"c5.9xlarge.elasticsearch"|"c5.18xlarge.elasticsearch"|"ultrawarm1.medium.elasticsearch"|"ultrawarm1.large.elasticsearch"|"t2.micro.elasticsearch"|"t2.small.elasticsearch"|"t2.medium.elasticsearch"|"r3.large.elasticsearch"|"r3.xlarge.elasticsearch"|"r3.2xlarge.elasticsearch"|"r3.4xlarge.elasticsearch"|"r3.8xlarge.elasticsearch"|"i2.xlarge.elasticsearch"|"i2.2xlarge.elasticsearch"|"d2.xlarge.elasticsearch"|"d2.2xlarge.elasticsearch"|"d2.4xlarge.elasticsearch"|"d2.8xlarge.elasticsearch"|"c4.large.elasticsearch"|"c4.xlarge.elasticsearch"|"c4.2xlarge.elasticsearch"|"c4.4xlarge.elasticsearch"|"c4.8xlarge.elasticsearch"|"r4.large.elasticsearch"|"r4.xlarge.elasticsearch"|"r4.2xlarge.elasticsearch"|"r4.4xlarge.elasticsearch"|"r4.8xlarge.elasticsearch"|"r4.16xlarge.elasticsearch"|"i3.large.elasticsearch"|"i3.xlarge.elasticsearch"|"i3.2xlarge.elasticsearch"|"i3.4xlarge.elasticsearch"|"i3.8xlarge.elasticsearch"|"i3.16xlarge.elasticsearch",
  "DedicatedMasterCount": integer,
  "WarmEnabled": true|false,
  "WarmType": "ultrawarm1.medium.elasticsearch"|"ultrawarm1.large.elasticsearch",
  "WarmCount": integer,
  "ColdStorageOptions": {
    "Enabled": true|false
  }
}
```

`--ebs-options` (structure)

Specify the type and size of the EBS volume that you want to use.

EBSEnabled -> (boolean)

Specifies whether EBS-based storage is enabled.

VolumeType -> (string)

Specifies the volume type for EBS-based storage.

VolumeSize -> (integer)

Integer to specify the size of an EBS volume.

Iops -> (integer)

Specifies the IOPS for Provisioned IOPS And GP3 EBS volume (SSD).

Throughput -> (integer)

Specifies the Throughput for GP3 EBS volume (SSD).

Shorthand Syntax:

```
EBSEnabled=boolean,VolumeType=string,VolumeSize=integer,Iops=integer,Throughput=integer
```

JSON Syntax:

```
{
  "EBSEnabled": true|false,
  "VolumeType": "standard"|"gp2"|"io1"|"gp3",
  "VolumeSize": integer,
  "Iops": integer,
  "Throughput": integer
}
```

`--snapshot-options` (structure)

Option to set the time, in UTC format, for the daily automated snapshot. Default value is `0` hours.

AutomatedSnapshotStartHour -> (integer)

Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is `0` hours.

Shorthand Syntax:

```
AutomatedSnapshotStartHour=integer
```

JSON Syntax:

```
{
  "AutomatedSnapshotStartHour": integer
}
```

`--vpc-options` (structure)

Options to specify the subnets and security groups for VPC endpoint. For more information, see [Creating a VPC](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc) in *VPC Endpoints for Amazon Elasticsearch Service Domains*

SubnetIds -> (list)

Specifies the subnets for VPC endpoint.

(string)

SecurityGroupIds -> (list)

Specifies the security groups for VPC endpoint.

(string)

Shorthand Syntax:

```
SubnetIds=string,string,SecurityGroupIds=string,string
```

JSON Syntax:

```
{
  "SubnetIds": ["string", ...],
  "SecurityGroupIds": ["string", ...]
}
```

`--cognito-options` (structure)

Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see [Amazon Cognito Authentication for Kibana](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html) .

Enabled -> (boolean)

Specifies the option to enable Cognito for Kibana authentication.

UserPoolId -> (string)

Specifies the Cognito user pool ID for Kibana authentication.

IdentityPoolId -> (string)

Specifies the Cognito identity pool ID for Kibana authentication.

RoleArn -> (string)

Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito resources.

Shorthand Syntax:

```
Enabled=boolean,UserPoolId=string,IdentityPoolId=string,RoleArn=string
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "UserPoolId": "string",
  "IdentityPoolId": "string",
  "RoleArn": "string"
}
```

`--advanced-options` (map)

Modifies the advanced option to allow references to indices in an HTTP request body. Must be `false` when configuring access to individual sub-resources. By default, the value is `true` . See [Configuration Advanced Options](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options) for more information.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--access-policies` (string)

IAM access policy as a JSON-formatted string.

`--log-publishing-options` (map)

Map of `LogType` and `LogPublishingOption` , each containing options to publish a given type of Elasticsearch log.

key -> (string)

Type of Log File, it can be one of the following:

- INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than configured index query log threshold to execute.
- SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than configured search query log threshold to execute.
- ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors and warnings raised during the operation of the service and can be useful for troubleshooting.
- AUDIT_LOGS: Audit logs contain records of user requests for access from the domain.

value -> (structure)

Log Publishing option that is set for given domain. Attributes and their details:

- CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
- Enabled: Whether the log publishing for given log type is enabled or not

CloudWatchLogsLogGroupArn -> (string)

ARN of the Cloudwatch log group to which log needs to be published.

Enabled -> (boolean)

Specifies whether given log publishing option is enabled or not.

Shorthand Syntax:

```
KeyName1=CloudWatchLogsLogGroupArn=string,Enabled=boolean,KeyName2=CloudWatchLogsLogGroupArn=string,Enabled=boolean

Where valid key names are:
  INDEX_SLOW_LOGS
  SEARCH_SLOW_LOGS
  ES_APPLICATION_LOGS
  AUDIT_LOGS
```

JSON Syntax:

```
{"INDEX_SLOW_LOGS"|"SEARCH_SLOW_LOGS"|"ES_APPLICATION_LOGS"|"AUDIT_LOGS": {
      "CloudWatchLogsLogGroupArn": "string",
      "Enabled": true|false
    }
  ...}
```

`--domain-endpoint-options` (structure)

Options to specify configuration that will be applied to the domain endpoint.

EnforceHTTPS -> (boolean)

Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

TLSSecurityPolicy -> (string)

Specify the TLS security policy that needs to be applied to the HTTPS endpoint of Elasticsearch domain. It can be one of the following values:

- **Policy-Min-TLS-1-0-2019-07:** TLS security policy that supports TLS version 1.0 to TLS version 1.2
- **Policy-Min-TLS-1-2-2019-07:** TLS security policy that supports only TLS version 1.2
- **Policy-Min-TLS-1-2-PFS-2023-10:** TLS security policy that supports TLS version 1.2 to TLS version 1.3 with perfect forward secrecy cipher suites

CustomEndpointEnabled -> (boolean)

Specify if custom endpoint should be enabled for the Elasticsearch domain.

CustomEndpoint -> (string)

Specify the fully qualified domain for your custom endpoint.

CustomEndpointCertificateArn -> (string)

Specify ACM certificate ARN for your custom endpoint.

Shorthand Syntax:

```
EnforceHTTPS=boolean,TLSSecurityPolicy=string,CustomEndpointEnabled=boolean,CustomEndpoint=string,CustomEndpointCertificateArn=string
```

JSON Syntax:

```
{
  "EnforceHTTPS": true|false,
  "TLSSecurityPolicy": "Policy-Min-TLS-1-0-2019-07"|"Policy-Min-TLS-1-2-2019-07"|"Policy-Min-TLS-1-2-PFS-2023-10",
  "CustomEndpointEnabled": true|false,
  "CustomEndpoint": "string",
  "CustomEndpointCertificateArn": "string"
}
```

`--advanced-security-options` (structure)

Specifies advanced security options.

Enabled -> (boolean)

True if advanced security is enabled.

InternalUserDatabaseEnabled -> (boolean)

True if the internal user database is enabled.

MasterUserOptions -> (structure)

Credentials for the master user: username and password, ARN, or both.

MasterUserARN -> (string)

ARN for the master user (if IAM is enabled).

MasterUserName -> (string)

The master userâs username, which is stored in the Amazon Elasticsearch Service domainâs internal database.

MasterUserPassword -> (string)

The master userâs password, which is stored in the Amazon Elasticsearch Service domainâs internal database.

SAMLOptions -> (structure)

Specifies the SAML application configuration for the domain.

Enabled -> (boolean)

True if SAML is enabled.

Idp -> (structure)

Specifies the SAML Identity Providerâs information.

MetadataContent -> (string)

The Metadata of the SAML application in xml format.

EntityId -> (string)

The unique Entity ID of the application in SAML Identity Provider.

MasterUserName -> (string)

The SAML master username, which is stored in the Amazon Elasticsearch Service domainâs internal database.

MasterBackendRole -> (string)

The backend role to which the SAML master user is mapped to.

SubjectKey -> (string)

The key to use for matching the SAML Subject attribute.

RolesKey -> (string)

The key to use for matching the SAML Roles attribute.

SessionTimeoutMinutes -> (integer)

The duration, in minutes, after which a user session becomes inactive. Acceptable values are between 1 and 1440, and the default value is 60.

AnonymousAuthEnabled -> (boolean)

True if Anonymous auth is enabled. Anonymous auth can be enabled only when AdvancedSecurity is enabled on existing domains.

Shorthand Syntax:

```
Enabled=boolean,InternalUserDatabaseEnabled=boolean,MasterUserOptions={MasterUserARN=string,MasterUserName=string,MasterUserPassword=string},SAMLOptions={Enabled=boolean,Idp={MetadataContent=string,EntityId=string},MasterUserName=string,MasterBackendRole=string,SubjectKey=string,RolesKey=string,SessionTimeoutMinutes=integer},AnonymousAuthEnabled=boolean
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "InternalUserDatabaseEnabled": true|false,
  "MasterUserOptions": {
    "MasterUserARN": "string",
    "MasterUserName": "string",
    "MasterUserPassword": "string"
  },
  "SAMLOptions": {
    "Enabled": true|false,
    "Idp": {
      "MetadataContent": "string",
      "EntityId": "string"
    },
    "MasterUserName": "string",
    "MasterBackendRole": "string",
    "SubjectKey": "string",
    "RolesKey": "string",
    "SessionTimeoutMinutes": integer
  },
  "AnonymousAuthEnabled": true|false
}
```

`--node-to-node-encryption-options` (structure)

Specifies the NodeToNodeEncryptionOptions.

Enabled -> (boolean)

Specify true to enable node-to-node encryption.

Shorthand Syntax:

```
Enabled=boolean
```

JSON Syntax:

```
{
  "Enabled": true|false
}
```

`--encryption-at-rest-options` (structure)

Specifies the Encryption At Rest Options.

Enabled -> (boolean)

Specifies the option to enable Encryption At Rest.

KmsKeyId -> (string)

Specifies the KMS Key ID for Encryption At Rest options.

Shorthand Syntax:

```
Enabled=boolean,KmsKeyId=string
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "KmsKeyId": "string"
}
```

`--auto-tune-options` (structure)

Specifies Auto-Tune options.

DesiredState -> (string)

Specifies the Auto-Tune desired state. Valid values are ENABLED, DISABLED.

RollbackOnDisable -> (string)

Specifies the rollback state while disabling Auto-Tune for the domain. Valid values are NO_ROLLBACK, DEFAULT_ROLLBACK.

MaintenanceSchedules -> (list)

Specifies list of maitenance schedules. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

(structure)

Specifies Auto-Tune maitenance schedule. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

StartAt -> (timestamp)

Specifies timestamp at which Auto-Tune maintenance schedule start.

Duration -> (structure)

Specifies maintenance schedule duration: duration value and duration unit. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

Value -> (long)

Integer to specify the value of a maintenance schedule duration. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

Unit -> (string)

Specifies the unit of a maintenance schedule duration. Valid value is HOURS. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

CronExpressionForRecurrence -> (string)

Specifies cron expression for a recurring maintenance schedule. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

JSON Syntax:

```
{
  "DesiredState": "ENABLED"|"DISABLED",
  "RollbackOnDisable": "NO_ROLLBACK"|"DEFAULT_ROLLBACK",
  "MaintenanceSchedules": [
    {
      "StartAt": timestamp,
      "Duration": {
        "Value": long,
        "Unit": "HOURS"
      },
      "CronExpressionForRecurrence": "string"
    }
    ...
  ]
}
```

`--dry-run` | `--no-dry-run` (boolean)

This flag, when set to True, specifies whether the `UpdateElasticsearchDomain` request should return the results of validation checks without actually applying the change. This flag, when set to True, specifies the deployment mechanism through which the update shall be applied on the domain. This will not actually perform the Update.

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

DomainConfig -> (structure)

The status of the updated Elasticsearch domain.

ElasticsearchVersion -> (structure)

String of format X.Y to specify version for the Elasticsearch domain.

Options -> (string)

Specifies the Elasticsearch version for the specified Elasticsearch domain.

Status -> (structure)

Specifies the status of the Elasticsearch version options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

ElasticsearchClusterConfig -> (structure)

Specifies the `ElasticsearchClusterConfig` for the Elasticsearch domain.

Options -> (structure)

Specifies the cluster configuration for the specified Elasticsearch domain.

InstanceType -> (string)

The instance type for an Elasticsearch cluster. UltraWarm instance types are not supported for data instances.

InstanceCount -> (integer)

The number of instances in the specified domain cluster.

DedicatedMasterEnabled -> (boolean)

A boolean value to indicate whether a dedicated master node is enabled. See [About Dedicated Master Nodes](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes) for more information.

ZoneAwarenessEnabled -> (boolean)

A boolean value to indicate whether zone awareness is enabled. See [About Zone Awareness](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness) for more information.

ZoneAwarenessConfig -> (structure)

Specifies the zone awareness configuration for a domain when zone awareness is enabled.

AvailabilityZoneCount -> (integer)

An integer value to indicate the number of availability zones for a domain when zone awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled

DedicatedMasterType -> (string)

The instance type for a dedicated master node.

DedicatedMasterCount -> (integer)

Total number of dedicated master nodes, active and on standby, for the cluster.

WarmEnabled -> (boolean)

True to enable warm storage.

WarmType -> (string)

The instance type for the Elasticsearch clusterâs warm nodes.

WarmCount -> (integer)

The number of warm nodes in the cluster.

ColdStorageOptions -> (structure)

Specifies the `ColdStorageOptions` config for Elasticsearch Domain

Enabled -> (boolean)

Enable cold storage option. Accepted values true or false

Status -> (structure)

Specifies the status of the configuration for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

EBSOptions -> (structure)

Specifies the `EBSOptions` for the Elasticsearch domain.

Options -> (structure)

Specifies the EBS options for the specified Elasticsearch domain.

EBSEnabled -> (boolean)

Specifies whether EBS-based storage is enabled.

VolumeType -> (string)

Specifies the volume type for EBS-based storage.

VolumeSize -> (integer)

Integer to specify the size of an EBS volume.

Iops -> (integer)

Specifies the IOPS for Provisioned IOPS And GP3 EBS volume (SSD).

Throughput -> (integer)

Specifies the Throughput for GP3 EBS volume (SSD).

Status -> (structure)

Specifies the status of the EBS options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

AccessPolicies -> (structure)

IAM access policy as a JSON-formatted string.

Options -> (string)

The access policy configured for the Elasticsearch domain. Access policies may be resource-based, IP-based, or IAM-based. See [Configuring Access Policies](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies) for more information.

Status -> (structure)

The status of the access policy for the Elasticsearch domain. See `OptionStatus` for the status information thatâs included.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

SnapshotOptions -> (structure)

Specifies the `SnapshotOptions` for the Elasticsearch domain.

Options -> (structure)

Specifies the daily snapshot options specified for the Elasticsearch domain.

AutomatedSnapshotStartHour -> (integer)

Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is `0` hours.

Status -> (structure)

Specifies the status of a daily automated snapshot.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

VPCOptions -> (structure)

The `VPCOptions` for the specified domain. For more information, see [VPC Endpoints for Amazon Elasticsearch Service Domains](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html) .

Options -> (structure)

Specifies the VPC options for the specified Elasticsearch domain.

VPCId -> (string)

The VPC Id for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

SubnetIds -> (list)

Specifies the subnets for VPC endpoint.

(string)

AvailabilityZones -> (list)

The availability zones for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

(string)

SecurityGroupIds -> (list)

Specifies the security groups for VPC endpoint.

(string)

Status -> (structure)

Specifies the status of the VPC options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

CognitoOptions -> (structure)

The `CognitoOptions` for the specified domain. For more information, see [Amazon Cognito Authentication for Kibana](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html) .

Options -> (structure)

Specifies the Cognito options for the specified Elasticsearch domain.

Enabled -> (boolean)

Specifies the option to enable Cognito for Kibana authentication.

UserPoolId -> (string)

Specifies the Cognito user pool ID for Kibana authentication.

IdentityPoolId -> (string)

Specifies the Cognito identity pool ID for Kibana authentication.

RoleArn -> (string)

Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito resources.

Status -> (structure)

Specifies the status of the Cognito options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

EncryptionAtRestOptions -> (structure)

Specifies the `EncryptionAtRestOptions` for the Elasticsearch domain.

Options -> (structure)

Specifies the Encryption At Rest options for the specified Elasticsearch domain.

Enabled -> (boolean)

Specifies the option to enable Encryption At Rest.

KmsKeyId -> (string)

Specifies the KMS Key ID for Encryption At Rest options.

Status -> (structure)

Specifies the status of the Encryption At Rest options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

NodeToNodeEncryptionOptions -> (structure)

Specifies the `NodeToNodeEncryptionOptions` for the Elasticsearch domain.

Options -> (structure)

Specifies the node-to-node encryption options for the specified Elasticsearch domain.

Enabled -> (boolean)

Specify true to enable node-to-node encryption.

Status -> (structure)

Specifies the status of the node-to-node encryption options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

AdvancedOptions -> (structure)

Specifies the `AdvancedOptions` for the domain. See [Configuring Advanced Options](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options) for more information.

Options -> (map)

Specifies the status of advanced options for the specified Elasticsearch domain.

key -> (string)

value -> (string)

Status -> (structure)

Specifies the status of `OptionStatus` for advanced options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

LogPublishingOptions -> (structure)

Log publishing options for the given domain.

Options -> (map)

The log publishing options configured for the Elasticsearch domain.

key -> (string)

Type of Log File, it can be one of the following:

- INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than configured index query log threshold to execute.
- SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than configured search query log threshold to execute.
- ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors and warnings raised during the operation of the service and can be useful for troubleshooting.
- AUDIT_LOGS: Audit logs contain records of user requests for access from the domain.

value -> (structure)

Log Publishing option that is set for given domain. Attributes and their details:

- CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
- Enabled: Whether the log publishing for given log type is enabled or not

CloudWatchLogsLogGroupArn -> (string)

ARN of the Cloudwatch log group to which log needs to be published.

Enabled -> (boolean)

Specifies whether given log publishing option is enabled or not.

Status -> (structure)

The status of the log publishing options for the Elasticsearch domain. See `OptionStatus` for the status information thatâs included.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

DomainEndpointOptions -> (structure)

Specifies the `DomainEndpointOptions` for the Elasticsearch domain.

Options -> (structure)

Options to configure endpoint for the Elasticsearch domain.

EnforceHTTPS -> (boolean)

Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.

TLSSecurityPolicy -> (string)

Specify the TLS security policy that needs to be applied to the HTTPS endpoint of Elasticsearch domain. It can be one of the following values:

- **Policy-Min-TLS-1-0-2019-07:** TLS security policy that supports TLS version 1.0 to TLS version 1.2
- **Policy-Min-TLS-1-2-2019-07:** TLS security policy that supports only TLS version 1.2
- **Policy-Min-TLS-1-2-PFS-2023-10:** TLS security policy that supports TLS version 1.2 to TLS version 1.3 with perfect forward secrecy cipher suites

CustomEndpointEnabled -> (boolean)

Specify if custom endpoint should be enabled for the Elasticsearch domain.

CustomEndpoint -> (string)

Specify the fully qualified domain for your custom endpoint.

CustomEndpointCertificateArn -> (string)

Specify ACM certificate ARN for your custom endpoint.

Status -> (structure)

The status of the endpoint options for the Elasticsearch domain. See `OptionStatus` for the status information thatâs included.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

AdvancedSecurityOptions -> (structure)

Specifies `AdvancedSecurityOptions` for the domain.

Options -> (structure)

Specifies advanced security options for the specified Elasticsearch domain.

Enabled -> (boolean)

True if advanced security is enabled.

InternalUserDatabaseEnabled -> (boolean)

True if the internal user database is enabled.

SAMLOptions -> (structure)

Describes the SAML application configured for a domain.

Enabled -> (boolean)

True if SAML is enabled.

Idp -> (structure)

Describes the SAML Identity Providerâs information.

MetadataContent -> (string)

The Metadata of the SAML application in xml format.

EntityId -> (string)

The unique Entity ID of the application in SAML Identity Provider.

SubjectKey -> (string)

The key used for matching the SAML Subject attribute.

RolesKey -> (string)

The key used for matching the SAML Roles attribute.

SessionTimeoutMinutes -> (integer)

The duration, in minutes, after which a user session becomes inactive.

AnonymousAuthDisableDate -> (timestamp)

Specifies the Anonymous Auth Disable Date when Anonymous Auth is enabled.

AnonymousAuthEnabled -> (boolean)

True if Anonymous auth is enabled. Anonymous auth can be enabled only when AdvancedSecurity is enabled on existing domains.

Status -> (structure)

Status of the advanced security options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells the creation date for the entity.

UpdateDate -> (timestamp)

Timestamp which tells the last updated time for the entity.

UpdateVersion -> (integer)

Specifies the latest version for the entity.

State -> (string)

Provides the `OptionState` for the Elasticsearch domain.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

AutoTuneOptions -> (structure)

Specifies `AutoTuneOptions` for the domain.

Options -> (structure)

Specifies Auto-Tune options for the specified Elasticsearch domain.

DesiredState -> (string)

Specifies the Auto-Tune desired state. Valid values are ENABLED, DISABLED.

RollbackOnDisable -> (string)

Specifies the rollback state while disabling Auto-Tune for the domain. Valid values are NO_ROLLBACK, DEFAULT_ROLLBACK.

MaintenanceSchedules -> (list)

Specifies list of maitenance schedules. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

(structure)

Specifies Auto-Tune maitenance schedule. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

StartAt -> (timestamp)

Specifies timestamp at which Auto-Tune maintenance schedule start.

Duration -> (structure)

Specifies maintenance schedule duration: duration value and duration unit. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

Value -> (long)

Integer to specify the value of a maintenance schedule duration. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

Unit -> (string)

Specifies the unit of a maintenance schedule duration. Valid value is HOURS. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

CronExpressionForRecurrence -> (string)

Specifies cron expression for a recurring maintenance schedule. See the [Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html) for more information.

Status -> (structure)

Specifies Status of the Auto-Tune options for the specified Elasticsearch domain.

CreationDate -> (timestamp)

Timestamp which tells Auto-Tune options creation date .

UpdateDate -> (timestamp)

Timestamp which tells Auto-Tune options last updated time.

UpdateVersion -> (integer)

Specifies the Auto-Tune options latest version.

State -> (string)

Specifies the `AutoTuneState` for the Elasticsearch domain.

ErrorMessage -> (string)

Specifies the error message while enabling or disabling the Auto-Tune options.

PendingDeletion -> (boolean)

Indicates whether the Elasticsearch domain is being deleted.

ChangeProgressDetails -> (structure)

Specifies change details of the domain configuration change.

ChangeId -> (string)

The unique change identifier associated with a specific domain configuration change.

Message -> (string)

Contains an optional message associated with the domain configuration change.

ConfigChangeStatus -> (string)

The current status of the configuration change.

StartTime -> (timestamp)

The time that the configuration change was initiated, in Universal Coordinated Time (UTC).

LastUpdatedTime -> (timestamp)

The last time that the configuration change was updated.

InitiatedBy -> (string)

The IAM principal who initiated the configuration change.

ModifyingProperties -> (list)

Information about the domain properties that are currently being modified.

(structure)

Information about the domain properties that are currently being modified.

Name -> (string)

The name of the property that is currently being modified.

ActiveValue -> (string)

The current value of the domain property that is being modified.

PendingValue -> (string)

The value that the property that is currently being modified will eventually have.

ValueType -> (string)

The type of value that is currently being modified. Properties can have two types:

- **PLAIN_TEXT** : Contain direct values such as â1â, âTrueâ, or âc5.large.searchâ.
- **STRINGIFIED_JSON** : Contain content in JSON format, such as {âEnabledâ:âTrueâ}â.

DryRunResults -> (structure)

Contains result of DryRun.

DeploymentType -> (string)

Specifies the deployment mechanism through which the update shall be applied on the domain. Possible responses are `Blue/Green` (The update will require a blue/green deployment.) `DynamicUpdate` (The update can be applied in-place without a Blue/Green deployment required.) `Undetermined` (The domain is undergoing an update which needs to complete before the deployment type can be predicted.) `None` (The configuration change matches the current configuration and will not result in any update.)

Message -> (string)

Contains an optional message associated with the DryRunResults.