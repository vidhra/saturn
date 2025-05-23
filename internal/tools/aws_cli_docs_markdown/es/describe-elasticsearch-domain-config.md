# describe-elasticsearch-domain-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domain-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domain-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [es](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/index.html#cli-aws-es) ]

# describe-elasticsearch-domain-config

## Description

Provides cluster configuration information about the specified Elasticsearch domain, such as the state, creation date, update version, and update date for cluster options.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeElasticsearchDomainConfig)

## Synopsis

```
describe-elasticsearch-domain-config
--domain-name <value>
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

The Elasticsearch domain that you want to get information about.

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

**To get domain configuration details**

The following `describe-elasticsearch-domain-config` example provides configuration details for a given domain, along with status information for each individual domain component.

```
aws es describe-elasticsearch-domain-config \
    --domain-name cli-example
```

Output:

```
{
    "DomainConfig": {
        "ElasticsearchVersion": {
            "Options": "7.4",
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "ElasticsearchClusterConfig": {
            "Options": {
                "InstanceType": "c5.large.elasticsearch",
                "InstanceCount": 1,
                "DedicatedMasterEnabled": true,
                "ZoneAwarenessEnabled": false,
                "DedicatedMasterType": "c5.large.elasticsearch",
                "DedicatedMasterCount": 3,
                "WarmEnabled": true,
                "WarmType": "ultrawarm1.medium.elasticsearch",
                "WarmCount": 2
            },
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "EBSOptions": {
            "Options": {
                "EBSEnabled": true,
                "VolumeType": "gp2",
                "VolumeSize": 10
            },
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "AccessPolicies": {
            "Options": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":\"es:*\",\"Resource\":\"arn:aws:es:us-east-1:123456789012:domain/cli-example/*\"}]}",
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "SnapshotOptions": {
            "Options": {
                "AutomatedSnapshotStartHour": 0
            },
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "VPCOptions": {
            "Options": {},
            "Status": {
                "CreationDate": 1591210426.162,
                "UpdateDate": 1591210426.162,
                "UpdateVersion": 18,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "CognitoOptions": {
            "Options": {
                "Enabled": false
            },
            "Status": {
                "CreationDate": 1591210426.163,
                "UpdateDate": 1591210426.163,
                "UpdateVersion": 18,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "EncryptionAtRestOptions": {
            "Options": {
                "Enabled": true,
                "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/1a2a3a4a-1a2a-1a2a-1a2a-1a2a3a4a5a6a"
            },
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "NodeToNodeEncryptionOptions": {
            "Options": {
                "Enabled": true
            },
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "AdvancedOptions": {
            "Options": {
                "rest.action.multi.allow_explicit_index": "true"
            },
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "LogPublishingOptions": {
            "Options": {},
            "Status": {
                "CreationDate": 1591210426.164,
                "UpdateDate": 1591210426.164,
                "UpdateVersion": 18,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "DomainEndpointOptions": {
            "Options": {
                "EnforceHTTPS": true,
                "TLSSecurityPolicy": "Policy-Min-TLS-1-0-2019-07"
            },
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589395827.325,
                "UpdateVersion": 8,
                "State": "Active",
                "PendingDeletion": false
            }
        },
        "AdvancedSecurityOptions": {
            "Options": {
                "Enabled": true,
                "InternalUserDatabaseEnabled": true
            },
            "Status": {
                "CreationDate": 1589395034.946,
                "UpdateDate": 1589827485.577,
                "UpdateVersion": 14,
                "State": "Active",
                "PendingDeletion": false
            }
        }
    }
}
```

For more information, see [Creating and Managing Amazon Elasticsearch Service Domains](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html) in the *Amazon Elasticsearch Service Developer Guide*.

## Output

DomainConfig -> (structure)

The configuration information of the domain requested in the `DescribeElasticsearchDomainConfig` request.

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