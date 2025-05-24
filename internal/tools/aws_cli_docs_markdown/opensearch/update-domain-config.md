# update-domain-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/update-domain-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/update-domain-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# update-domain-config

## Description

Modifies the cluster configuration of the specified Amazon OpenSearch Service domain.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/UpdateDomainConfig)

## Synopsis

```
update-domain-config
--domain-name <value>
[--cluster-config <value>]
[--ebs-options <value>]
[--snapshot-options <value>]
[--vpc-options <value>]
[--cognito-options <value>]
[--advanced-options <value>]
[--access-policies <value>]
[--ip-address-type <value>]
[--log-publishing-options <value>]
[--encryption-at-rest-options <value>]
[--domain-endpoint-options <value>]
[--node-to-node-encryption-options <value>]
[--advanced-security-options <value>]
[--identity-center-options <value>]
[--auto-tune-options <value>]
[--dry-run | --no-dry-run]
[--dry-run-mode <value>]
[--off-peak-window-options <value>]
[--software-update-options <value>]
[--aiml-options <value>]
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

The name of the domain that youâre updating.

`--cluster-config` (structure)

Changes that you want to make to the cluster configuration, such as the instance type and number of EC2 instances.

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

JSON Syntax:

```
{
  "InstanceType": "m3.medium.search"|"m3.large.search"|"m3.xlarge.search"|"m3.2xlarge.search"|"m4.large.search"|"m4.xlarge.search"|"m4.2xlarge.search"|"m4.4xlarge.search"|"m4.10xlarge.search"|"m5.large.search"|"m5.xlarge.search"|"m5.2xlarge.search"|"m5.4xlarge.search"|"m5.12xlarge.search"|"m5.24xlarge.search"|"r5.large.search"|"r5.xlarge.search"|"r5.2xlarge.search"|"r5.4xlarge.search"|"r5.12xlarge.search"|"r5.24xlarge.search"|"c5.large.search"|"c5.xlarge.search"|"c5.2xlarge.search"|"c5.4xlarge.search"|"c5.9xlarge.search"|"c5.18xlarge.search"|"t3.nano.search"|"t3.micro.search"|"t3.small.search"|"t3.medium.search"|"t3.large.search"|"t3.xlarge.search"|"t3.2xlarge.search"|"or1.medium.search"|"or1.large.search"|"or1.xlarge.search"|"or1.2xlarge.search"|"or1.4xlarge.search"|"or1.8xlarge.search"|"or1.12xlarge.search"|"or1.16xlarge.search"|"ultrawarm1.medium.search"|"ultrawarm1.large.search"|"ultrawarm1.xlarge.search"|"t2.micro.search"|"t2.small.search"|"t2.medium.search"|"r3.large.search"|"r3.xlarge.search"|"r3.2xlarge.search"|"r3.4xlarge.search"|"r3.8xlarge.search"|"i2.xlarge.search"|"i2.2xlarge.search"|"d2.xlarge.search"|"d2.2xlarge.search"|"d2.4xlarge.search"|"d2.8xlarge.search"|"c4.large.search"|"c4.xlarge.search"|"c4.2xlarge.search"|"c4.4xlarge.search"|"c4.8xlarge.search"|"r4.large.search"|"r4.xlarge.search"|"r4.2xlarge.search"|"r4.4xlarge.search"|"r4.8xlarge.search"|"r4.16xlarge.search"|"i3.large.search"|"i3.xlarge.search"|"i3.2xlarge.search"|"i3.4xlarge.search"|"i3.8xlarge.search"|"i3.16xlarge.search"|"r6g.large.search"|"r6g.xlarge.search"|"r6g.2xlarge.search"|"r6g.4xlarge.search"|"r6g.8xlarge.search"|"r6g.12xlarge.search"|"m6g.large.search"|"m6g.xlarge.search"|"m6g.2xlarge.search"|"m6g.4xlarge.search"|"m6g.8xlarge.search"|"m6g.12xlarge.search"|"c6g.large.search"|"c6g.xlarge.search"|"c6g.2xlarge.search"|"c6g.4xlarge.search"|"c6g.8xlarge.search"|"c6g.12xlarge.search"|"r6gd.large.search"|"r6gd.xlarge.search"|"r6gd.2xlarge.search"|"r6gd.4xlarge.search"|"r6gd.8xlarge.search"|"r6gd.12xlarge.search"|"r6gd.16xlarge.search"|"t4g.small.search"|"t4g.medium.search",
  "InstanceCount": integer,
  "DedicatedMasterEnabled": true|false,
  "ZoneAwarenessEnabled": true|false,
  "ZoneAwarenessConfig": {
    "AvailabilityZoneCount": integer
  },
  "DedicatedMasterType": "m3.medium.search"|"m3.large.search"|"m3.xlarge.search"|"m3.2xlarge.search"|"m4.large.search"|"m4.xlarge.search"|"m4.2xlarge.search"|"m4.4xlarge.search"|"m4.10xlarge.search"|"m5.large.search"|"m5.xlarge.search"|"m5.2xlarge.search"|"m5.4xlarge.search"|"m5.12xlarge.search"|"m5.24xlarge.search"|"r5.large.search"|"r5.xlarge.search"|"r5.2xlarge.search"|"r5.4xlarge.search"|"r5.12xlarge.search"|"r5.24xlarge.search"|"c5.large.search"|"c5.xlarge.search"|"c5.2xlarge.search"|"c5.4xlarge.search"|"c5.9xlarge.search"|"c5.18xlarge.search"|"t3.nano.search"|"t3.micro.search"|"t3.small.search"|"t3.medium.search"|"t3.large.search"|"t3.xlarge.search"|"t3.2xlarge.search"|"or1.medium.search"|"or1.large.search"|"or1.xlarge.search"|"or1.2xlarge.search"|"or1.4xlarge.search"|"or1.8xlarge.search"|"or1.12xlarge.search"|"or1.16xlarge.search"|"ultrawarm1.medium.search"|"ultrawarm1.large.search"|"ultrawarm1.xlarge.search"|"t2.micro.search"|"t2.small.search"|"t2.medium.search"|"r3.large.search"|"r3.xlarge.search"|"r3.2xlarge.search"|"r3.4xlarge.search"|"r3.8xlarge.search"|"i2.xlarge.search"|"i2.2xlarge.search"|"d2.xlarge.search"|"d2.2xlarge.search"|"d2.4xlarge.search"|"d2.8xlarge.search"|"c4.large.search"|"c4.xlarge.search"|"c4.2xlarge.search"|"c4.4xlarge.search"|"c4.8xlarge.search"|"r4.large.search"|"r4.xlarge.search"|"r4.2xlarge.search"|"r4.4xlarge.search"|"r4.8xlarge.search"|"r4.16xlarge.search"|"i3.large.search"|"i3.xlarge.search"|"i3.2xlarge.search"|"i3.4xlarge.search"|"i3.8xlarge.search"|"i3.16xlarge.search"|"r6g.large.search"|"r6g.xlarge.search"|"r6g.2xlarge.search"|"r6g.4xlarge.search"|"r6g.8xlarge.search"|"r6g.12xlarge.search"|"m6g.large.search"|"m6g.xlarge.search"|"m6g.2xlarge.search"|"m6g.4xlarge.search"|"m6g.8xlarge.search"|"m6g.12xlarge.search"|"c6g.large.search"|"c6g.xlarge.search"|"c6g.2xlarge.search"|"c6g.4xlarge.search"|"c6g.8xlarge.search"|"c6g.12xlarge.search"|"r6gd.large.search"|"r6gd.xlarge.search"|"r6gd.2xlarge.search"|"r6gd.4xlarge.search"|"r6gd.8xlarge.search"|"r6gd.12xlarge.search"|"r6gd.16xlarge.search"|"t4g.small.search"|"t4g.medium.search",
  "DedicatedMasterCount": integer,
  "WarmEnabled": true|false,
  "WarmType": "ultrawarm1.medium.search"|"ultrawarm1.large.search"|"ultrawarm1.xlarge.search",
  "WarmCount": integer,
  "ColdStorageOptions": {
    "Enabled": true|false
  },
  "MultiAZWithStandbyEnabled": true|false,
  "NodeOptions": [
    {
      "NodeType": "coordinator",
      "NodeConfig": {
        "Enabled": true|false,
        "Type": "m3.medium.search"|"m3.large.search"|"m3.xlarge.search"|"m3.2xlarge.search"|"m4.large.search"|"m4.xlarge.search"|"m4.2xlarge.search"|"m4.4xlarge.search"|"m4.10xlarge.search"|"m5.large.search"|"m5.xlarge.search"|"m5.2xlarge.search"|"m5.4xlarge.search"|"m5.12xlarge.search"|"m5.24xlarge.search"|"r5.large.search"|"r5.xlarge.search"|"r5.2xlarge.search"|"r5.4xlarge.search"|"r5.12xlarge.search"|"r5.24xlarge.search"|"c5.large.search"|"c5.xlarge.search"|"c5.2xlarge.search"|"c5.4xlarge.search"|"c5.9xlarge.search"|"c5.18xlarge.search"|"t3.nano.search"|"t3.micro.search"|"t3.small.search"|"t3.medium.search"|"t3.large.search"|"t3.xlarge.search"|"t3.2xlarge.search"|"or1.medium.search"|"or1.large.search"|"or1.xlarge.search"|"or1.2xlarge.search"|"or1.4xlarge.search"|"or1.8xlarge.search"|"or1.12xlarge.search"|"or1.16xlarge.search"|"ultrawarm1.medium.search"|"ultrawarm1.large.search"|"ultrawarm1.xlarge.search"|"t2.micro.search"|"t2.small.search"|"t2.medium.search"|"r3.large.search"|"r3.xlarge.search"|"r3.2xlarge.search"|"r3.4xlarge.search"|"r3.8xlarge.search"|"i2.xlarge.search"|"i2.2xlarge.search"|"d2.xlarge.search"|"d2.2xlarge.search"|"d2.4xlarge.search"|"d2.8xlarge.search"|"c4.large.search"|"c4.xlarge.search"|"c4.2xlarge.search"|"c4.4xlarge.search"|"c4.8xlarge.search"|"r4.large.search"|"r4.xlarge.search"|"r4.2xlarge.search"|"r4.4xlarge.search"|"r4.8xlarge.search"|"r4.16xlarge.search"|"i3.large.search"|"i3.xlarge.search"|"i3.2xlarge.search"|"i3.4xlarge.search"|"i3.8xlarge.search"|"i3.16xlarge.search"|"r6g.large.search"|"r6g.xlarge.search"|"r6g.2xlarge.search"|"r6g.4xlarge.search"|"r6g.8xlarge.search"|"r6g.12xlarge.search"|"m6g.large.search"|"m6g.xlarge.search"|"m6g.2xlarge.search"|"m6g.4xlarge.search"|"m6g.8xlarge.search"|"m6g.12xlarge.search"|"c6g.large.search"|"c6g.xlarge.search"|"c6g.2xlarge.search"|"c6g.4xlarge.search"|"c6g.8xlarge.search"|"c6g.12xlarge.search"|"r6gd.large.search"|"r6gd.xlarge.search"|"r6gd.2xlarge.search"|"r6gd.4xlarge.search"|"r6gd.8xlarge.search"|"r6gd.12xlarge.search"|"r6gd.16xlarge.search"|"t4g.small.search"|"t4g.medium.search",
        "Count": integer
      }
    }
    ...
  ]
}
```

`--ebs-options` (structure)

The type and size of the EBS volume to attach to instances in the domain.

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

The time, in UTC format, when OpenSearch Service takes a daily automated snapshot of the specified domain. Default is `0` hours.

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

Options to specify the subnets and security groups for a VPC endpoint. For more information, see [Launching your Amazon OpenSearch Service domains using a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html) .

SubnetIds -> (list)

A list of subnet IDs associated with the VPC endpoints for the domain. If your domain uses multiple Availability Zones, you need to provide two subnet IDs, one per zone. Otherwise, provide only one.

(string)

SecurityGroupIds -> (list)

The list of security group IDs associated with the VPC endpoints for the domain. If you do not provide a security group ID, OpenSearch Service uses the default security group for the VPC.

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

Key-value pairs to configure Amazon Cognito authentication for OpenSearch Dashboards.

Enabled -> (boolean)

Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards.

UserPoolId -> (string)

The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

IdentityPoolId -> (string)

The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

RoleArn -> (string)

The `AmazonOpenSearchServiceCognitoAccess` role that allows OpenSearch Service to configure your user pool and identity pool.

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

Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:

- `"rest.action.multi.allow_explicit_index": "true" | "false"` - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.
- `"indices.fielddata.cache.size": "80"` - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.
- `"indices.query.bool.max_clause_count": "1024"` - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a `TooManyClauses` error.

For more information, see [Advanced cluster parameters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options) .

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

Identity and Access Management (IAM) access policy as a JSON-formatted string.

`--ip-address-type` (string)

Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If your IP address type is currently set to dual stack, you canât change it.

Possible values:

- `ipv4`
- `dualstack`

`--log-publishing-options` (map)

Options to publish OpenSearch logs to Amazon CloudWatch Logs.

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

`--encryption-at-rest-options` (structure)

Encryption at rest options for the domain.

Enabled -> (boolean)

True to enable encryption at rest.

KmsKeyId -> (string)

The KMS key ID. Takes the form `1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a` .

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

`--domain-endpoint-options` (structure)

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

`--node-to-node-encryption-options` (structure)

Node-to-node encryption options for the domain.

Enabled -> (boolean)

True to enable node-to-node encryption.

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

`--advanced-security-options` (structure)

Options for fine-grained access control.

Enabled -> (boolean)

True to enable fine-grained access control.

InternalUserDatabaseEnabled -> (boolean)

True to enable the internal user database.

MasterUserOptions -> (structure)

Container for information about the master user.

MasterUserARN -> (string)

Amazon Resource Name (ARN) for the master user. Only specify if `InternalUserDatabaseEnabled` is `false` .

MasterUserName -> (string)

User name for the master user. Only specify if `InternalUserDatabaseEnabled` is `true` .

MasterUserPassword -> (string)

Password for the master user. Only specify if `InternalUserDatabaseEnabled` is `true` .

SAMLOptions -> (structure)

Container for information about the SAML configuration for OpenSearch Dashboards.

Enabled -> (boolean)

True to enable SAML authentication for a domain.

Idp -> (structure)

The SAML Identity Providerâs information.

MetadataContent -> (string)

The metadata of the SAML application, in XML format.

EntityId -> (string)

The unique entity ID of the application in the SAML identity provider.

MasterUserName -> (string)

The SAML master user name, which is stored in the domainâs internal user database.

MasterBackendRole -> (string)

The backend role that the SAML master user is mapped to.

SubjectKey -> (string)

Element of the SAML assertion to use for the user name. Default is `NameID` .

RolesKey -> (string)

Element of the SAML assertion to use for backend roles. Default is `roles` .

SessionTimeoutMinutes -> (integer)

The duration, in minutes, after which a user session becomes inactive. Acceptable values are between 1 and 1440, and the default value is 60.

JWTOptions -> (structure)

Container for information about the JWT configuration of the Amazon OpenSearch Service.

Enabled -> (boolean)

True to enable JWT authentication and authorization for a domain.

SubjectKey -> (string)

Element of the JWT assertion to use for the user name.

RolesKey -> (string)

Element of the JWT assertion to use for roles.

PublicKey -> (string)

Element of the JWT assertion used by the cluster to verify JWT signatures.

AnonymousAuthEnabled -> (boolean)

True to enable a 30-day migration period during which administrators can create role mappings. Only necessary when [enabling fine-grained access control on an existing domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing) .

Shorthand Syntax:

```
Enabled=boolean,InternalUserDatabaseEnabled=boolean,MasterUserOptions={MasterUserARN=string,MasterUserName=string,MasterUserPassword=string},SAMLOptions={Enabled=boolean,Idp={MetadataContent=string,EntityId=string},MasterUserName=string,MasterBackendRole=string,SubjectKey=string,RolesKey=string,SessionTimeoutMinutes=integer},JWTOptions={Enabled=boolean,SubjectKey=string,RolesKey=string,PublicKey=string},AnonymousAuthEnabled=boolean
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
  "JWTOptions": {
    "Enabled": true|false,
    "SubjectKey": "string",
    "RolesKey": "string",
    "PublicKey": "string"
  },
  "AnonymousAuthEnabled": true|false
}
```

`--identity-center-options` (structure)

Configuration settings for enabling and managing IAM Identity Center.

EnabledAPIAccess -> (boolean)

Indicates whether IAM Identity Center is enabled for API access in Amazon OpenSearch Service.

IdentityCenterInstanceARN -> (string)

The ARN of the IAM Identity Center instance used to create an OpenSearch UI application that uses IAM Identity Center for authentication.

SubjectKey -> (string)

Specifies the attribute that contains the subject identifier (such as username, user ID, or email) in IAM Identity Center.

RolesKey -> (string)

Specifies the attribute that contains the backend role identifier (such as group name or group ID) in IAM Identity Center.

Shorthand Syntax:

```
EnabledAPIAccess=boolean,IdentityCenterInstanceARN=string,SubjectKey=string,RolesKey=string
```

JSON Syntax:

```
{
  "EnabledAPIAccess": true|false,
  "IdentityCenterInstanceARN": "string",
  "SubjectKey": "UserName"|"UserId"|"Email",
  "RolesKey": "GroupName"|"GroupId"
}
```

`--auto-tune-options` (structure)

Options for Auto-Tune.

DesiredState -> (string)

Whether Auto-Tune is enabled or disabled.

RollbackOnDisable -> (string)

When disabling Auto-Tune, specify `NO_ROLLBACK` to retain all prior Auto-Tune settings or `DEFAULT_ROLLBACK` to revert to the OpenSearch Service defaults. If you specify `DEFAULT_ROLLBACK` , you must include a `MaintenanceSchedule` in the request. Otherwise, OpenSearch Service is unable to perform the rollback.

MaintenanceSchedules -> (list)

DEPRECATED. Use [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html) instead.

A list of maintenance schedules during which Auto-Tune can deploy changes.

(structure)

### Note

This object is deprecated. Use the domainâs [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html) to schedule Auto-Tune optimizations. For migration instructions, see [Migrating from Auto-Tune maintenance windows](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html#off-peak-migrate) .

The Auto-Tune maintenance schedule. For more information, see [Auto-Tune for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html) .

StartAt -> (timestamp)

The Epoch timestamp at which the Auto-Tune maintenance schedule starts.

Duration -> (structure)

The duration of the maintenance schedule. For example, `"Duration": {"Value": 2, "Unit": "HOURS"}` .

Value -> (long)

Integer to specify the value of a maintenance schedule duration.

Unit -> (string)

The unit of measurement for the duration of a maintenance schedule.

CronExpressionForRecurrence -> (string)

A cron expression for a recurring maintenance schedule during which Auto-Tune can deploy changes.

UseOffPeakWindow -> (boolean)

Whether to use the domainâs [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindow.html) to deploy configuration changes on the domain rather than a maintenance schedule.

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
  ],
  "UseOffPeakWindow": true|false
}
```

`--dry-run` | `--no-dry-run` (boolean)

This flag, when set to True, specifies whether the `UpdateDomain` request should return the results of a dry run analysis without actually applying the change. A dry run determines what type of deployment the update will cause.

`--dry-run-mode` (string)

The type of dry run to perform.

- `Basic` only returns the type of deployment (blue/green or dynamic) that the update will cause.
- `Verbose` runs an additional check to validate the changes youâre making. For more information, see [Validating a domain update](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#validation-check) .

Possible values:

- `Basic`
- `Verbose`

`--off-peak-window-options` (structure)

Off-peak window options for the domain.

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

Shorthand Syntax:

```
Enabled=boolean,OffPeakWindow={WindowStartTime={Hours=long,Minutes=long}}
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "OffPeakWindow": {
    "WindowStartTime": {
      "Hours": long,
      "Minutes": long
    }
  }
}
```

`--software-update-options` (structure)

Service software update options for the domain.

AutoSoftwareUpdateEnabled -> (boolean)

Whether automatic service software updates are enabled for the domain.

Shorthand Syntax:

```
AutoSoftwareUpdateEnabled=boolean
```

JSON Syntax:

```
{
  "AutoSoftwareUpdateEnabled": true|false
}
```

`--aiml-options` (structure)

Options for all machine learning features for the specified domain.

NaturalLanguageQueryGenerationOptions -> (structure)

Container for parameters required for natural language query generation on the specified domain.

DesiredState -> (string)

The desired state of the natural language query generation feature. Valid values are ENABLED and DISABLED.

Shorthand Syntax:

```
NaturalLanguageQueryGenerationOptions={DesiredState=string}
```

JSON Syntax:

```
{
  "NaturalLanguageQueryGenerationOptions": {
    "DesiredState": "ENABLED"|"DISABLED"
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

## Output

DomainConfig -> (structure)

The status of the updated domain.

EngineVersion -> (structure)

The OpenSearch or Elasticsearch version that the domain is running.

Options -> (string)

The OpenSearch or Elasticsearch version for the specified domain.

Status -> (structure)

The status of the version options for the specified domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

ClusterConfig -> (structure)

Container for the cluster configuration of a the domain.

Options -> (structure)

Cluster configuration options for the specified domain.

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

Status -> (structure)

The status of cluster configuration options for the specified domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

EBSOptions -> (structure)

Container for EBS options configured for the domain.

Options -> (structure)

The configured EBS options for the specified domain.

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

Status -> (structure)

The status of the EBS options for the specified domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

AccessPolicies -> (structure)

Specifies the access policies for the domain.

Options -> (string)

The access policy configured for the domain. Access policies can be resource-based, IP-based, or IAM-based. For more information, see [Configuring access policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-access-policies) .

Status -> (structure)

The status of the access policy for the domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

IPAddressType -> (structure)

Choose either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you canât change your address type later.

Options -> (string)

The IP address options for the domain.

Status -> (structure)

Provides the current status of an entity.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

SnapshotOptions -> (structure)

DEPRECATED. Container for parameters required to configure automated snapshots of domain indexes.

Options -> (structure)

The daily snapshot options specified for the domain.

AutomatedSnapshotStartHour -> (integer)

The time, in UTC format, when OpenSearch Service takes a daily automated snapshot of the specified domain. Default is `0` hours.

Status -> (structure)

The status of a daily automated snapshot.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

VPCOptions -> (structure)

The current VPC options for the domain and the status of any updates to their configuration.

Options -> (structure)

The VPC options for the specified domain.

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

Status -> (structure)

The status of the VPC options for the specified domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

CognitoOptions -> (structure)

Container for Amazon Cognito options for the domain.

Options -> (structure)

Cognito options for the specified domain.

Enabled -> (boolean)

Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards.

UserPoolId -> (string)

The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

IdentityPoolId -> (string)

The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

RoleArn -> (string)

The `AmazonOpenSearchServiceCognitoAccess` role that allows OpenSearch Service to configure your user pool and identity pool.

Status -> (structure)

The status of the Cognito options for the specified domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

EncryptionAtRestOptions -> (structure)

Key-value pairs to enable encryption at rest.

Options -> (structure)

Encryption at rest options for the specified domain.

Enabled -> (boolean)

True to enable encryption at rest.

KmsKeyId -> (string)

The KMS key ID. Takes the form `1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a` .

Status -> (structure)

The status of the encryption at rest options for the specified domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

NodeToNodeEncryptionOptions -> (structure)

Whether node-to-node encryption is enabled or disabled.

Options -> (structure)

The node-to-node encryption options for the specified domain.

Enabled -> (boolean)

True to enable node-to-node encryption.

Status -> (structure)

The status of the node-to-node encryption options for the specified domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

AdvancedOptions -> (structure)

Key-value pairs to specify advanced configuration options. For more information, see [Advanced options](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options) .

Options -> (map)

The status of advanced options for the specified domain.

key -> (string)

value -> (string)

Status -> (structure)

The status of advanced options for the specified domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

LogPublishingOptions -> (structure)

Key-value pairs to configure log publishing.

Options -> (map)

The log publishing options configured for the domain.

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

Status -> (structure)

The status of the log publishing options for the domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

DomainEndpointOptions -> (structure)

Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.

Options -> (structure)

Options to configure the endpoint for a domain.

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

Status -> (structure)

The status of the endpoint options for a domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

AdvancedSecurityOptions -> (structure)

Container for fine-grained access control settings for the domain.

Options -> (structure)

Container for fine-grained access control settings.

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

Status -> (structure)

Status of the fine-grained access control settings for a domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

IdentityCenterOptions -> (structure)

Configuration options for enabling and managing IAM Identity Center integration within a domain.

Options -> (structure)

Configuration settings for IAM Identity Center integration.

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

Status -> (structure)

The status of IAM Identity Center configuration settings for a domain.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

AutoTuneOptions -> (structure)

Container for Auto-Tune settings for the domain.

Options -> (structure)

Auto-Tune settings for updating a domain.

DesiredState -> (string)

Whether Auto-Tune is enabled or disabled.

RollbackOnDisable -> (string)

When disabling Auto-Tune, specify `NO_ROLLBACK` to retain all prior Auto-Tune settings or `DEFAULT_ROLLBACK` to revert to the OpenSearch Service defaults. If you specify `DEFAULT_ROLLBACK` , you must include a `MaintenanceSchedule` in the request. Otherwise, OpenSearch Service is unable to perform the rollback.

MaintenanceSchedules -> (list)

DEPRECATED. Use [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html) instead.

A list of maintenance schedules during which Auto-Tune can deploy changes.

(structure)

### Note

This object is deprecated. Use the domainâs [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html) to schedule Auto-Tune optimizations. For migration instructions, see [Migrating from Auto-Tune maintenance windows](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html#off-peak-migrate) .

The Auto-Tune maintenance schedule. For more information, see [Auto-Tune for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html) .

StartAt -> (timestamp)

The Epoch timestamp at which the Auto-Tune maintenance schedule starts.

Duration -> (structure)

The duration of the maintenance schedule. For example, `"Duration": {"Value": 2, "Unit": "HOURS"}` .

Value -> (long)

Integer to specify the value of a maintenance schedule duration.

Unit -> (string)

The unit of measurement for the duration of a maintenance schedule.

CronExpressionForRecurrence -> (string)

A cron expression for a recurring maintenance schedule during which Auto-Tune can deploy changes.

UseOffPeakWindow -> (boolean)

Whether to use the domainâs [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindow.html) to deploy configuration changes on the domain rather than a maintenance schedule.

Status -> (structure)

The current status of Auto-Tune for a domain.

CreationDate -> (timestamp)

Date and time when Auto-Tune was enabled for the domain.

UpdateDate -> (timestamp)

Date and time when the Auto-Tune options were last updated for the domain.

UpdateVersion -> (integer)

The latest version of the Auto-Tune options.

State -> (string)

The current state of Auto-Tune on the domain.

ErrorMessage -> (string)

Any errors that occurred while enabling or disabling Auto-Tune.

PendingDeletion -> (boolean)

Indicates whether the domain is being deleted.

ChangeProgressDetails -> (structure)

Container for information about the progress of an existing configuration change.

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

Container for off-peak window options for the domain.

Options -> (structure)

The domainâs off-peak window configuration.

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

Status -> (structure)

The current status of off-peak window options.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

SoftwareUpdateOptions -> (structure)

Software update options for the domain.

Options -> (structure)

The service software update options for a domain.

AutoSoftwareUpdateEnabled -> (boolean)

Whether automatic service software updates are enabled for the domain.

Status -> (structure)

The status of service software update options, including creation date and last updated date.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

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

Options -> (structure)

Machine learning options on the specified domain.

NaturalLanguageQueryGenerationOptions -> (structure)

Container for parameters required for natural language query generation on the specified domain.

DesiredState -> (string)

The desired state of the natural language query generation feature. Valid values are ENABLED and DISABLED.

CurrentState -> (string)

The current state of the natural language query generation feature, indicating completion, in progress, or failure.

Status -> (structure)

Provides the current status of an entity.

CreationDate -> (timestamp)

The timestamp when the entity was created.

UpdateDate -> (timestamp)

The timestamp of the last time the entity was updated.

UpdateVersion -> (integer)

The latest version of the entity.

State -> (string)

The state of the entity.

PendingDeletion -> (boolean)

Indicates whether the entity is being deleted.

DryRunResults -> (structure)

Results of the dry run performed in the update domain request.

DeploymentType -> (string)

Specifies the way in which OpenSearch Service will apply an update. Possible values are:

- **Blue/Green** - The update requires a blue/green deployment.
- **DynamicUpdate** - No blue/green deployment required
- **Undetermined** - The domain is in the middle of an update and canât predict the deployment type. Try again after the update is complete.
- **None** - The request doesnât include any configuration changes.

Message -> (string)

A message corresponding to the deployment type.

DryRunProgressStatus -> (structure)

The status of the dry run being performed on the domain, if any.

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