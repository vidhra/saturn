# delete-elasticsearch-domainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-elasticsearch-domain.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-elasticsearch-domain.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [es](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/index.html#cli-aws-es) ]

# delete-elasticsearch-domain

## Description

Permanently deletes the specified Elasticsearch domain and all of its data. Once a domain is deleted, it cannot be recovered.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DeleteElasticsearchDomain)

## Synopsis

```
delete-elasticsearch-domain
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

The name of the Elasticsearch domain that you want to permanently delete.

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

DomainStatus -> (structure)

The status of the Elasticsearch domain being deleted.

DomainId -> (string)

The unique identifier for the specified Elasticsearch domain.

DomainName -> (string)

The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

ARN -> (string)

The Amazon resource name (ARN) of an Elasticsearch domain. See [Identifiers for IAM Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html) in *Using AWS Identity and Access Management* for more information.

Created -> (boolean)

The domain creation status. `True` if the creation of an Elasticsearch domain is complete. `False` if domain creation is still in progress.

Deleted -> (boolean)

The domain deletion status. `True` if a delete request has been received for the domain but resource cleanup is still in progress. `False` if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.

Endpoint -> (string)

The Elasticsearch domain endpoint that you use to submit index and search requests.

Endpoints -> (map)

Map containing the Elasticsearch domain endpoints used to submit index and search requests. Example `key, value` : `'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'` .

key -> (string)

value -> (string)

The endpoint to which service requests are submitted. For example, `search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com` or `doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com` .

Processing -> (boolean)

The status of the Elasticsearch domain configuration. `True` if Amazon Elasticsearch Service is processing configuration changes. `False` if the configuration is active.

UpgradeProcessing -> (boolean)

The status of an Elasticsearch domain version upgrade. `True` if Amazon Elasticsearch Service is undergoing a version upgrade. `False` if the configuration is active.

ElasticsearchVersion -> (string)

ElasticsearchClusterConfig -> (structure)

The type and number of instances in the domain cluster.

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

EBSOptions -> (structure)

The `EBSOptions` for the specified domain. See [Configuring EBS-based Storage](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs) for more information.

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

AccessPolicies -> (string)

IAM access policy as a JSON-formatted string.

SnapshotOptions -> (structure)

Specifies the status of the `SnapshotOptions`

AutomatedSnapshotStartHour -> (integer)

Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is `0` hours.

VPCOptions -> (structure)

The `VPCOptions` for the specified domain. For more information, see [VPC Endpoints for Amazon Elasticsearch Service Domains](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html) .

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

CognitoOptions -> (structure)

The `CognitoOptions` for the specified domain. For more information, see [Amazon Cognito Authentication for Kibana](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html) .

Enabled -> (boolean)

Specifies the option to enable Cognito for Kibana authentication.

UserPoolId -> (string)

Specifies the Cognito user pool ID for Kibana authentication.

IdentityPoolId -> (string)

Specifies the Cognito identity pool ID for Kibana authentication.

RoleArn -> (string)

Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito resources.

EncryptionAtRestOptions -> (structure)

Specifies the status of the `EncryptionAtRestOptions` .

Enabled -> (boolean)

Specifies the option to enable Encryption At Rest.

KmsKeyId -> (string)

Specifies the KMS Key ID for Encryption At Rest options.

NodeToNodeEncryptionOptions -> (structure)

Specifies the status of the `NodeToNodeEncryptionOptions` .

Enabled -> (boolean)

Specify true to enable node-to-node encryption.

AdvancedOptions -> (map)

Specifies the status of the `AdvancedOptions`

key -> (string)

value -> (string)

LogPublishingOptions -> (map)

Log publishing options for the given domain.

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

ServiceSoftwareOptions -> (structure)

The current status of the Elasticsearch domainâs service software.

CurrentVersion -> (string)

The current service software version that is present on the domain.

NewVersion -> (string)

The new service software version if one is available.

UpdateAvailable -> (boolean)

`True` if you are able to update you service software version. `False` if you are not able to update your service software version.

Cancellable -> (boolean)

`True` if you are able to cancel your service software version update. `False` if you are not able to cancel your service software version.

UpdateStatus -> (string)

The status of your service software update. This field can take the following values: `ELIGIBLE` , `PENDING_UPDATE` , `IN_PROGRESS` , `COMPLETED` , and `NOT_ELIGIBLE` .

Description -> (string)

The description of the `UpdateStatus` .

AutomatedUpdateDate -> (timestamp)

Timestamp, in Epoch time, until which you can manually request a service software update. After this date, we automatically update your service software.

OptionalDeployment -> (boolean)

`True` if a service software is never automatically updated. `False` if a service software is automatically updated after `AutomatedUpdateDate` .

DomainEndpointOptions -> (structure)

The current status of the Elasticsearch domainâs endpoint options.

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

AdvancedSecurityOptions -> (structure)

The current status of the Elasticsearch domainâs advanced security options.

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

AutoTuneOptions -> (structure)

The current status of the Elasticsearch domainâs Auto-Tune options.

State -> (string)

Specifies the `AutoTuneState` for the Elasticsearch domain.

ErrorMessage -> (string)

Specifies the error message while enabling or disabling the Auto-Tune.

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

DomainProcessingStatus -> (string)

The status of any changes that are currently in progress for the domain.

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