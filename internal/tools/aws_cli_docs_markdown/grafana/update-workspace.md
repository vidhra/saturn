# update-workspaceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/update-workspace.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/update-workspace.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [grafana](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/index.html#cli-aws-grafana) ]

# update-workspace

## Description

Modifies an existing Amazon Managed Grafana workspace. If you use this operation and omit any optional parameters, the existing values of those parameters are not changed.

To modify the user authentication methods that the workspace uses, such as SAML or IAM Identity Center, use [UpdateWorkspaceAuthentication](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceAuthentication.html) .

To modify which users in the workspace have the `Admin` and `Editor` Grafana roles, use [UpdatePermissions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/grafana-2020-08-18/UpdateWorkspace)

## Synopsis

```
update-workspace
[--account-access-type <value>]
[--network-access-control <value>]
[--organization-role-name <value>]
[--permission-type <value>]
[--remove-network-access-configuration | --no-remove-network-access-configuration]
[--remove-vpc-configuration | --no-remove-vpc-configuration]
[--stack-set-name <value>]
[--vpc-configuration <value>]
[--workspace-data-sources <value>]
[--workspace-description <value>]
--workspace-id <value>
[--workspace-name <value>]
[--workspace-notification-destinations <value>]
[--workspace-organizational-units <value>]
[--workspace-role-arn <value>]
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

`--account-access-type` (string)

Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify `ORGANIZATION` , you must specify which organizational units the workspace can access in the `workspaceOrganizationalUnits` parameter.

Possible values:

- `CURRENT_ACCOUNT`
- `ORGANIZATION`

`--network-access-control` (structure)

The configuration settings for network access to your workspace.

When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.

If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.

prefixListIds -> (list)

An array of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration (passed an empty array) then no IP addresses are allowed to access the workspace. You create a prefix list using the Amazon VPC console.

Prefix list IDs have the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/update-workspace.html#id1)pl-*1a2b3c4d* `` .

For more information about prefix lists, see [Group CIDR blocks using managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) in the *Amazon Virtual Private Cloud User Guide* .

(string)

vpceIds -> (list)

An array of Amazon VPC endpoint IDs for the workspace. You can create VPC endpoints to your Amazon Managed Grafana workspace for access from within a VPC. If a `NetworkAccessConfiguration` is specified then only VPC endpoints specified here are allowed to access the workspace. If you pass in an empty array of strings, then no VPCs are allowed to access the workspace.

VPC endpoint IDs have the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/update-workspace.html#id3)vpce-*1a2b3c4d* `` .

For more information about creating an interface VPC endpoint, see [Interface VPC endpoints](https://docs.aws.amazon.com/grafana/latest/userguide/VPC-endpoints) in the *Amazon Managed Grafana User Guide* .

### Note

The only VPC endpoints that can be specified here are interface VPC endpoints for Grafana workspaces (using the `com.amazonaws.[region].grafana-workspace` service endpoint). Other VPC endpoints are ignored.

(string)

Shorthand Syntax:

```
prefixListIds=string,string,vpceIds=string,string
```

JSON Syntax:

```
{
  "prefixListIds": ["string", ...],
  "vpceIds": ["string", ...]
}
```

`--organization-role-name` (string)

The name of an IAM role that already exists to use to access resources through Organizations. This can only be used with a workspace that has the `permissionType` set to `CUSTOMER_MANAGED` .

`--permission-type` (string)

Use this parameter if you want to change a workspace from `SERVICE_MANAGED` to `CUSTOMER_MANAGED` . This allows you to manage the permissions that the workspace uses to access datasources and notification channels. If the workspace is in a member Amazon Web Services account of an organization, and that account is not a delegated administrator account, and you want the workspace to access data sources in other Amazon Web Services accounts in the organization, you must choose `CUSTOMER_MANAGED` .

If you specify this as `CUSTOMER_MANAGED` , you must also specify a `workspaceRoleArn` that the workspace will use for accessing Amazon Web Services resources.

For more information on the role and permissions needed, see [Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html)

### Note

Do not use this to convert a `CUSTOMER_MANAGED` workspace to `SERVICE_MANAGED` . Do not include this parameter if you want to leave the workspace as `SERVICE_MANAGED` .

You can convert a `CUSTOMER_MANAGED` workspace to `SERVICE_MANAGED` using the Amazon Managed Grafana console. For more information, see [Managing permissions for data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html) .

Possible values:

- `CUSTOMER_MANAGED`
- `SERVICE_MANAGED`

`--remove-network-access-configuration` | `--no-remove-network-access-configuration` (boolean)

Whether to remove the network access configuration from the workspace.

Setting this to `true` and providing a `networkAccessControl` to set will return an error.

If you remove this configuration by setting this to `true` , then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.

`--remove-vpc-configuration` | `--no-remove-vpc-configuration` (boolean)

Whether to remove the VPC configuration from the workspace.

Setting this to `true` and providing a `vpcConfiguration` to set will return an error.

`--stack-set-name` (string)

The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.

`--vpc-configuration` (structure)

The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.

securityGroupIds -> (list)

The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.

(string)

subnetIds -> (list)

The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.

(string)

Shorthand Syntax:

```
securityGroupIds=string,string,subnetIds=string,string
```

JSON Syntax:

```
{
  "securityGroupIds": ["string", ...],
  "subnetIds": ["string", ...]
}
```

`--workspace-data-sources` (list)

This parameter is for internal use only, and should not be used.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  AMAZON_OPENSEARCH_SERVICE
  CLOUDWATCH
  PROMETHEUS
  XRAY
  TIMESTREAM
  SITEWISE
  ATHENA
  REDSHIFT
  TWINMAKER
```

`--workspace-description` (string)

A description for the workspace. This is used only to help you identify this workspace.

`--workspace-id` (string)

The ID of the workspace to update.

`--workspace-name` (string)

A new name for the workspace to update.

`--workspace-notification-destinations` (list)

Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  SNS
```

`--workspace-organizational-units` (list)

Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.

(string)

Syntax:

```
"string" "string" ...
```

`--workspace-role-arn` (string)

Specifies an IAM role that grants permissions to Amazon Web Services resources that the workspace accesses, such as data sources and notification channels. If this workspace has `permissionType` `CUSTOMER_MANAGED` , then this role is required.

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

workspace -> (structure)

A structure containing data about the workspace that was created.

accountAccessType -> (string)

Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If this is `ORGANIZATION` , the `workspaceOrganizationalUnits` parameter specifies which organizational units the workspace can access.

authentication -> (structure)

A structure that describes whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication.

providers -> (list)

Specifies whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication.

(string)

samlConfigurationStatus -> (string)

Specifies whether the workplaceâs user authentication method is fully configured.

created -> (timestamp)

The date that the workspace was created.

dataSources -> (list)

Specifies the Amazon Web Services data sources that have been configured to have IAM roles and permissions created to allow Amazon Managed Grafana to read data from these sources.

This list is only used when the workspace was created through the Amazon Web Services console, and the `permissionType` is `SERVICE_MANAGED` .

(string)

description -> (string)

The user-defined description of the workspace.

endpoint -> (string)

The URL that users can use to access the Grafana console in the workspace.

freeTrialConsumed -> (boolean)

Specifies whether this workspace has already fully used its free trial for Grafana Enterprise.

### Note

Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.

freeTrialExpiration -> (timestamp)

If this workspace is currently in the free trial period for Grafana Enterprise, this value specifies when that free trial ends.

### Note

Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.

grafanaToken -> (string)

The token that ties this workspace to a Grafana Labs account. For more information, see [Link your account with Grafana Labs](https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise) .

grafanaVersion -> (string)

The version of Grafana supported in this workspace.

id -> (string)

The unique ID of this workspace.

licenseExpiration -> (timestamp)

If this workspace has a full Grafana Enterprise license purchased through Amazon Web Services Marketplace, this specifies when the license ends and will need to be renewed. Purchasing the Enterprise plugins option through Amazon Managed Grafana does not have an expiration. It is valid until the license is removed.

licenseType -> (string)

Specifies whether this workspace has a full Grafana Enterprise license.

### Note

Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.

modified -> (timestamp)

The most recent date that the workspace was modified.

name -> (string)

The name of the workspace.

networkAccessControl -> (structure)

The configuration settings for network access to your workspace.

prefixListIds -> (list)

An array of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration (passed an empty array) then no IP addresses are allowed to access the workspace. You create a prefix list using the Amazon VPC console.

Prefix list IDs have the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/update-workspace.html#id5)pl-*1a2b3c4d* `` .

For more information about prefix lists, see [Group CIDR blocks using managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) in the *Amazon Virtual Private Cloud User Guide* .

(string)

vpceIds -> (list)

An array of Amazon VPC endpoint IDs for the workspace. You can create VPC endpoints to your Amazon Managed Grafana workspace for access from within a VPC. If a `NetworkAccessConfiguration` is specified then only VPC endpoints specified here are allowed to access the workspace. If you pass in an empty array of strings, then no VPCs are allowed to access the workspace.

VPC endpoint IDs have the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/update-workspace.html#id7)vpce-*1a2b3c4d* `` .

For more information about creating an interface VPC endpoint, see [Interface VPC endpoints](https://docs.aws.amazon.com/grafana/latest/userguide/VPC-endpoints) in the *Amazon Managed Grafana User Guide* .

### Note

The only VPC endpoints that can be specified here are interface VPC endpoints for Grafana workspaces (using the `com.amazonaws.[region].grafana-workspace` service endpoint). Other VPC endpoints are ignored.

(string)

notificationDestinations -> (list)

The Amazon Web Services notification channels that Amazon Managed Grafana can automatically create IAM roles and permissions for, to allow Amazon Managed Grafana to use these channels.

(string)

organizationRoleName -> (string)

The name of the IAM role that is used to access resources through Organizations.

organizationalUnits -> (list)

Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.

(string)

permissionType -> (string)

If this is `SERVICE_MANAGED` , and the workplace was created through the Amazon Managed Grafana console, then Amazon Managed Grafana automatically creates the IAM roles and provisions the permissions that the workspace needs to use Amazon Web Services data sources and notification channels.

If this is `CUSTOMER_MANAGED` , you must manage those roles and permissions yourself.

If you are working with a workspace in a member account of an organization and that account is not a delegated administrator account, and you want the workspace to access data sources in other Amazon Web Services accounts in the organization, this parameter must be set to `CUSTOMER_MANAGED` .

For more information about converting between customer and service managed, see [Managing permissions for data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html) . For more information about the roles and permissions that must be managed for customer managed workspaces, see [Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html)

stackSetName -> (string)

The name of the CloudFormation stack set that is used to generate IAM roles to be used for this workspace.

status -> (string)

The current status of the workspace.

tags -> (map)

The list of tags associated with the workspace.

key -> (string)

value -> (string)

vpcConfiguration -> (structure)

The configuration for connecting to data sources in a private VPC (Amazon Virtual Private Cloud).

securityGroupIds -> (list)

The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.

(string)

subnetIds -> (list)

The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.

(string)

workspaceRoleArn -> (string)

The IAM role that grants permissions to the Amazon Web Services resources that the workspace will view data from. This role must already exist.