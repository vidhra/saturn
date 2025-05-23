# describe-dry-run-progressÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/describe-dry-run-progress.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/describe-dry-run-progress.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# describe-dry-run-progress

## Description

Describes the progress of a pre-update dry run analysis on an Amazon OpenSearch Service domain. For more information, see [Determining whether a change will cause a blue/green deployment](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#dryrun) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/DescribeDryRunProgress)

## Synopsis

```
describe-dry-run-progress
--domain-name <value>
[--dry-run-id <value>]
[--load-dry-run-config | --no-load-dry-run-config]
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

The name of the domain.

`--dry-run-id` (string)

The unique identifier of the dry run.

`--load-dry-run-config` | `--no-load-dry-run-config` (boolean)

Whether to include the configuration of the dry run in the response. The configuration specifies the updates that youâre planning to make on the domain.

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

DryRunProgressStatus -> (structure)

The current status of the dry run, including any validation errors.

DryRunId -> (string)

The unique identifier of the dry run.

DryRunStatus -> (string)

The current status of the dry run.

CreationDate -> (string)

The timestamp when the dry run was initiated.

UpdateDate -> (string)

The timestamp when the dry run was last updated.

ValidationFailures -> (list)

Any validation failures that occurred as a result of the dry run.

(structure)

A validation failure that occurred as the result of a pre-update validation check (verbose dry run) on a domain.

Code -> (string)

The error code of the failure.

Message -> (string)

A message corresponding to the failure.

DryRunConfig -> (structure)

Details about the changes youâre planning to make on the domain.

DomainId -> (string)

Unique identifier for the domain.

DomainName -> (string)

Name of the domain. Domain names are unique across all domains owned by the same account within an Amazon Web Services Region.

ARN -> (string)

The Amazon Resource Name (ARN) of the domain. For more information, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *AWS Identity and Access Management User Guide* .

Created -> (boolean)

Creation status of an OpenSearch Service domain. True if domain creation is complete. False if domain creation is still in progress.

Deleted -> (boolean)

Deletion status of an OpenSearch Service domain. True if domain deletion is complete. False if domain deletion is still in progress. Once deletion is complete, the status of the domain is no longer returned.

Endpoint -> (string)

Domain-specific endpoint used to submit index, search, and data upload requests to the domain.

EndpointV2 -> (string)

If `IPAddressType` to set to `dualstack` , a version 2 domain endpoint is provisioned. This endpoint functions like a normal endpoint, except that it works with both IPv4 and IPv6 IP addresses. Normal endpoints work only with IPv4 IP addresses.

Endpoints -> (map)

The key-value pair that exists if the OpenSearch Service domain uses VPC endpoints. For example:

- **IPv4 IP addresses** - `'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`
- **Dual stack IP addresses** - `'vpcv2':'vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.aos.us-east-1.on.aws'`

key -> (string)

value -> (string)

The domain endpoint to which index and search requests are submitted. For example, `search-imdb-movies-oopcnjfn6ugo.eu-west-1.es.amazonaws.com` or `doc-imdb-movies-oopcnjfn6u.eu-west-1.es.amazonaws.com` .

DomainEndpointV2HostedZoneId -> (string)

The dual stack hosted zone ID for the domain.

Processing -> (boolean)

The status of the domain configuration. True if OpenSearch Service is processing configuration changes. False if the configuration is active.

UpgradeProcessing -> (boolean)

The status of a domain version upgrade to a new version of OpenSearch or Elasticsearch. True if OpenSearch Service is in the process of a version upgrade. False if the configuration is active.

EngineVersion -> (string)

Version of OpenSearch or Elasticsearch that the domain is running, in the format `Elasticsearch_X.Y` or `OpenSearch_X.Y` .

ClusterConfig -> (structure)

Container for the cluster configuration of the domain.

InstanceType -> (string)

Instance type of data nodes in the cluster.

InstanceCount -> (integer)

Number of data nodes in the cluster. This number must be greater than 1, otherwise you receive a validation exception.

DedicatedMasterEnabled -> (boolean)

Indicates whether dedicated master nodes are enabled for the cluster.``True`` if the cluster will use a dedicated master node.``False`` if the cluster will not.

ZoneAwarenessEnabled -> (boolean)

Indicates whether multiple Availability Zones are enabled. For more information, see [Configuring a multi-AZ domain in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html) .

ZoneAwarenessConfig -> (structure)

Container for zone awareness configuration options. Only required if `ZoneAwarenessEnabled` is `true` .

AvailabilityZoneCount -> (integer)

If you enabled multiple Availability Zones, this value is the number of zones that you want the domain to use. Valid values are `2` and `3` . If your domain is provisioned within a VPC, this value be equal to number of subnets.

DedicatedMasterType -> (string)

OpenSearch Service instance type of the dedicated master nodes in the cluster.

DedicatedMasterCount -> (integer)

Number of dedicated master nodes in the cluster. This number must be greater than 2 and not 4, otherwise you receive a validation exception.

WarmEnabled -> (boolean)

Whether to enable warm storage for the cluster.

WarmType -> (string)

The instance type for the clusterâs warm nodes.

WarmCount -> (integer)

The number of warm nodes in the cluster.

ColdStorageOptions -> (structure)

Container for cold storage configuration options.

Enabled -> (boolean)

Whether to enable or disable cold storage on the domain. You must enable UltraWarm storage to enable cold storage.

MultiAZWithStandbyEnabled -> (boolean)

A boolean that indicates whether a multi-AZ domain is turned on with a standby AZ. For more information, see [Configuring a multi-AZ domain in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html) .

NodeOptions -> (list)

List of node options for the domain.

(structure)

Configuration settings for defining the node type within a cluster.

NodeType -> (string)

Defines the type of node, such as coordinating nodes.

NodeConfig -> (structure)

Configuration options for defining the setup of any node type.

Enabled -> (boolean)

A boolean value indicating whether a specific node type is active or inactive.

Type -> (string)

The instance type of a particular node within the cluster.

Count -> (integer)

The number of nodes of a specific type within the cluster.

EBSOptions -> (structure)

Container for EBS-based storage settings for the domain.

EBSEnabled -> (boolean)

Indicates whether EBS volumes are attached to data nodes in an OpenSearch Service domain.

VolumeType -> (string)

Specifies the type of EBS volumes attached to data nodes.

VolumeSize -> (integer)

Specifies the size (in GiB) of EBS volumes attached to data nodes.

Iops -> (integer)

Specifies the baseline input/output (I/O) performance of EBS volumes attached to data nodes. Applicable only for the `gp3` and provisioned IOPS EBS volume types.

Throughput -> (integer)

Specifies the throughput (in MiB/s) of the EBS volumes attached to data nodes. Applicable only for the `gp3` volume type.

AccessPolicies -> (string)

Identity and Access Management (IAM) policy document specifying the access policies for the domain.

IPAddressType -> (string)

The type of IP addresses supported by the endpoint for the domain.

SnapshotOptions -> (structure)

DEPRECATED. Container for parameters required to configure automated snapshots of domain indexes.

AutomatedSnapshotStartHour -> (integer)

The time, in UTC format, when OpenSearch Service takes a daily automated snapshot of the specified domain. Default is `0` hours.

VPCOptions -> (structure)

The VPC configuration for the domain.

VPCId -> (string)

The ID for your VPC. Amazon VPC generates this value when you create a VPC.

SubnetIds -> (list)

A list of subnet IDs associated with the VPC endpoints for the domain.

(string)

AvailabilityZones -> (list)

The list of Availability Zones associated with the VPC subnets.

(string)

SecurityGroupIds -> (list)

The list of security group IDs associated with the VPC endpoints for the domain.

(string)

CognitoOptions -> (structure)

Key-value pairs to configure Amazon Cognito authentication for OpenSearch Dashboards.

Enabled -> (boolean)

Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards.

UserPoolId -> (string)

The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

IdentityPoolId -> (string)

The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

RoleArn -> (string)

The `AmazonOpenSearchServiceCognitoAccess` role that allows OpenSearch Service to configure your user pool and identity pool.

EncryptionAtRestOptions -> (structure)

Encryption at rest settings for the domain.

Enabled -> (boolean)

True to enable encryption at rest.

KmsKeyId -> (string)

The KMS key ID. Takes the form `1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a` .

NodeToNodeEncryptionOptions -> (structure)

Whether node-to-node encryption is enabled or disabled.

Enabled -> (boolean)

True to enable node-to-node encryption.

AdvancedOptions -> (map)

Key-value pairs that specify advanced configuration options.

key -> (string)

value -> (string)

LogPublishingOptions -> (map)

Log publishing options for the domain.

key -> (string)

The type of log file. Can be one of the following:

- **INDEX_SLOW_LOGS** - Index slow logs contain insert requests that took more time than the configured index query log threshold to execute.
- **SEARCH_SLOW_LOGS** - Search slow logs contain search queries that took more time than the configured search query log threshold to execute.
- **ES_APPLICATION_LOGS** - OpenSearch application logs contain information about errors and warnings raised during the operation of the service and can be useful for troubleshooting.
- **AUDIT_LOGS** - Audit logs contain records of user requests for access to the domain.

value -> (structure)

Specifies whether the Amazon OpenSearch Service domain publishes the OpenSearch application and slow logs to Amazon CloudWatch. For more information, see [Monitoring OpenSearch logs with Amazon CloudWatch Logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html) .

### Note

After you enable log publishing, you still have to enable the collection of slow logs using the OpenSearch REST API.

CloudWatchLogsLogGroupArn -> (string)

The Amazon Resource Name (ARN) of the CloudWatch Logs group to publish logs to.

Enabled -> (boolean)

Whether the log should be published.

ServiceSoftwareOptions -> (structure)

The current status of the domainâs service software.

CurrentVersion -> (string)

The current service software version present on the domain.

NewVersion -> (string)

The new service software version, if one is available.

UpdateAvailable -> (boolean)

True if youâre able to update your service software version. False if you canât update your service software version.

Cancellable -> (boolean)

True if youâre able to cancel your service software version update. False if you canât cancel your service software update.

UpdateStatus -> (string)

The status of your service software update.

Description -> (string)

A description of the service software update status.

AutomatedUpdateDate -> (timestamp)

The timestamp, in Epoch time, until which you can manually request a service software update. After this date, we automatically update your service software.

OptionalDeployment -> (boolean)

True if a service software is never automatically updated. False if a service software is automatically updated after the automated update date.

DomainEndpointOptions -> (structure)

Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.

EnforceHTTPS -> (boolean)

True to require that all traffic to the domain arrive over HTTPS.

TLSSecurityPolicy -> (string)

Specify the TLS security policy to apply to the HTTPS endpoint of the domain. The policy can be one of the following values:

- **Policy-Min-TLS-1-0-2019-07:** TLS security policy that supports TLS version 1.0 to TLS version 1.2
- **Policy-Min-TLS-1-2-2019-07:** TLS security policy that supports only TLS version 1.2
- **Policy-Min-TLS-1-2-PFS-2023-10:** TLS security policy that supports TLS version 1.2 to TLS version 1.3 with perfect forward secrecy cipher suites

CustomEndpointEnabled -> (boolean)

Whether to enable a custom endpoint for the domain.

CustomEndpoint -> (string)

The fully qualified URL for the custom endpoint.

CustomEndpointCertificateArn -> (string)

The ARN for your security certificate, managed in Amazon Web Services Certificate Manager (ACM).

AdvancedSecurityOptions -> (structure)

Settings for fine-grained access control.

Enabled -> (boolean)

True if fine-grained access control is enabled.

InternalUserDatabaseEnabled -> (boolean)

True if the internal user database is enabled.

SAMLOptions -> (structure)

Container for information about the SAML configuration for OpenSearch Dashboards.

Enabled -> (boolean)

True if SAML is enabled.

Idp -> (structure)

Describes the SAML identity providerâs information.

MetadataContent -> (string)

The metadata of the SAML application, in XML format.

EntityId -> (string)

The unique entity ID of the application in the SAML identity provider.

SubjectKey -> (string)

The key used for matching the SAML subject attribute.

RolesKey -> (string)

The key used for matching the SAML roles attribute.

SessionTimeoutMinutes -> (integer)

The duration, in minutes, after which a user session becomes inactive.

JWTOptions -> (structure)

Container for information about the JWT configuration of the Amazon OpenSearch Service.

Enabled -> (boolean)

True if JWT use is enabled.

SubjectKey -> (string)

The key used for matching the JWT subject attribute.

RolesKey -> (string)

The key used for matching the JWT roles attribute.

PublicKey -> (string)

The key used to verify the signature of incoming JWT requests.

AnonymousAuthDisableDate -> (timestamp)

Date and time when the migration period will be disabled. Only necessary when [enabling fine-grained access control on an existing domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing) .

AnonymousAuthEnabled -> (boolean)

True if a 30-day migration period is enabled, during which administrators can create role mappings. Only necessary when [enabling fine-grained access control on an existing domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing) .

IdentityCenterOptions -> (structure)

Configuration options for controlling IAM Identity Center integration within a domain.

EnabledAPIAccess -> (boolean)

Indicates whether IAM Identity Center is enabled for the application.

IdentityCenterInstanceARN -> (string)

The Amazon Resource Name (ARN) of the IAM Identity Center instance.

SubjectKey -> (string)

Specifies the attribute that contains the subject identifier (such as username, user ID, or email) in IAM Identity Center.

RolesKey -> (string)

Specifies the attribute that contains the backend role identifier (such as group name or group ID) in IAM Identity Center.

IdentityCenterApplicationARN -> (string)

The ARN of the IAM Identity Center application that integrates with Amazon OpenSearch Service.

IdentityStoreId -> (string)

The identifier of the IAM Identity Store.

AutoTuneOptions -> (structure)

Auto-Tune settings for the domain.

State -> (string)

The current state of Auto-Tune on the domain.

ErrorMessage -> (string)

Any errors that occurred while enabling or disabling Auto-Tune.

UseOffPeakWindow -> (boolean)

Whether the domainâs off-peak window will be used to deploy Auto-Tune changes rather than a maintenance schedule.

ChangeProgressDetails -> (structure)

Information about a configuration change happening on the domain.

ChangeId -> (string)

The ID of the configuration change.

Message -> (string)

A message corresponding to the status of the configuration change.

ConfigChangeStatus -> (string)

The current status of the configuration change.

InitiatedBy -> (string)

The IAM principal who initiated the configuration change.

StartTime -> (timestamp)

The time that the configuration change was initiated, in Universal Coordinated Time (UTC).

LastUpdatedTime -> (timestamp)

The last time that the configuration change was updated.

OffPeakWindowOptions -> (structure)

Options that specify a custom 10-hour window during which OpenSearch Service can perform configuration changes on the domain.

Enabled -> (boolean)

Whether to enable an off-peak window.

This option is only available when modifying a domain created prior to February 16, 2023, not when creating a new domain. All domains created after this date have the off-peak window enabled by default. You canât disable the off-peak window after itâs enabled for a domain.

OffPeakWindow -> (structure)

Off-peak window settings for the domain.

WindowStartTime -> (structure)

A custom start time for the off-peak window, in Coordinated Universal Time (UTC). The window length will always be 10 hours, so you canât specify an end time. For example, if you specify 11:00 P.M. UTC as a start time, the end time will automatically be set to 9:00 A.M.

Hours -> (long)

The start hour of the window in Coordinated Universal Time (UTC), using 24-hour time. For example, `17` refers to 5:00 P.M. UTC.

Minutes -> (long)

The start minute of the window, in UTC.

SoftwareUpdateOptions -> (structure)

Service software update options for the domain.

AutoSoftwareUpdateEnabled -> (boolean)

Whether automatic service software updates are enabled for the domain.

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

- `PLAIN_TEXT` : Contain direct values such as â1â, âTrueâ, or âc5.large.searchâ.
- `STRINGIFIED_JSON` : Contain content in JSON format, such as {âEnabledâ:âTrueâ}â.

AIMLOptions -> (structure)

Container for parameters required to enable all machine learning features.

NaturalLanguageQueryGenerationOptions -> (structure)

Container for parameters required for natural language query generation on the specified domain.

DesiredState -> (string)

The desired state of the natural language query generation feature. Valid values are ENABLED and DISABLED.

CurrentState -> (string)

The current state of the natural language query generation feature, indicating completion, in progress, or failure.

DryRunResults -> (structure)

The results of the dry run.

DeploymentType -> (string)

Specifies the way in which OpenSearch Service will apply an update. Possible values are:

- **Blue/Green** - The update requires a blue/green deployment.
- **DynamicUpdate** - No blue/green deployment required
- **Undetermined** - The domain is in the middle of an update and canât predict the deployment type. Try again after the update is complete.
- **None** - The request doesnât include any configuration changes.

Message -> (string)

A message corresponding to the deployment type.