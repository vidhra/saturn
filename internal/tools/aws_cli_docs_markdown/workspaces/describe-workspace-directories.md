# describe-workspace-directoriesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-directories.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-directories.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# describe-workspace-directories

## Description

Describes the available directories that are registered with Amazon WorkSpaces.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceDirectories)

`describe-workspace-directories` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Directories`

## Synopsis

```
describe-workspace-directories
[--directory-ids <value>]
[--workspace-directory-names <value>]
[--limit <value>]
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--max-items <value>]
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

`--directory-ids` (list)

The identifiers of the directories. If the value is null, all directories are retrieved.

(string)

Syntax:

```
"string" "string" ...
```

`--workspace-directory-names` (list)

The names of the WorkSpace directories.

(string)

Syntax:

```
"string" "string" ...
```

`--limit` (integer)

The maximum number of directories to return.

`--filters` (list)

The filter condition for the WorkSpaces.

(structure)

Describes the filter conditions for the WorkSpaces to return.

Name -> (string)

The name of the WorkSpaces to filter.

Values -> (list)

The values for filtering WorkSpaces

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "USER_IDENTITY_TYPE"|"WORKSPACE_TYPE",
    "Values": ["string", ...]
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe a registered directory**

The following `describe-workspace-directories` example describes the specified registered directory.

```
aws workspaces describe-workspace-directories \
    --directory-ids d-926722edaf
```

Output:

```
{
    "Directories": [
        {
            "DirectoryId": "d-926722edaf",
            "Alias": "d-926722edaf",
            "DirectoryName": "example.com",
            "RegistrationCode": "WSpdx+9RJ8JT",
            "SubnetIds": [
                "subnet-9d19c4c6",
                "subnet-500d5819"
            ],
            "DnsIpAddresses": [
                "172.16.1.140",
                "172.16.0.30"
            ],
            "CustomerUserName": "Administrator",
            "IamRoleId": "arn:aws:iam::123456789012:role/workspaces_DefaultRole",
            "DirectoryType": "SIMPLE_AD",
            "WorkspaceSecurityGroupId": "sg-0d89e927e5645d7c5",
            "State": "REGISTERED",
            "WorkspaceCreationProperties": {
                "EnableWorkDocs": false,
                "EnableInternetAccess": false,
                "UserEnabledAsLocalAdministrator": true,
                "EnableMaintenanceMode": true
            },
            "WorkspaceAccessProperties": {
                "DeviceTypeWindows": "ALLOW",
                "DeviceTypeOsx": "ALLOW",
                "DeviceTypeWeb": "DENY",
                "DeviceTypeIos": "ALLOW",
                "DeviceTypeAndroid": "ALLOW",
                "DeviceTypeChromeOs": "ALLOW",
                "DeviceTypeZeroClient": "ALLOW",
                "DeviceTypeLinux": "DENY"
            },
            "Tenancy": "SHARED",
            "SelfservicePermissions": {
                "RestartWorkspace": "ENABLED",
                "IncreaseVolumeSize": "DISABLED",
                "ChangeComputeType": "DISABLED",
                "SwitchRunningMode": "DISABLED",
                "RebuildWorkspace": "DISABLED"
            }
        }
    ]
}
```

For more information, see [Manage directories for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html) in the *Amazon WorkSpaces Administration Guide*.

## Output

Directories -> (list)

Information about the directories.

(structure)

Describes a directory that is used with Amazon WorkSpaces.

DirectoryId -> (string)

The directory identifier.

Alias -> (string)

The directory alias.

DirectoryName -> (string)

The name of the directory.

RegistrationCode -> (string)

The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.

SubnetIds -> (list)

The identifiers of the subnets used with the directory.

(string)

DnsIpAddresses -> (list)

The IP addresses of the DNS servers for the directory.

(string)

CustomerUserName -> (string)

The user name for the service account.

IamRoleId -> (string)

The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.

DirectoryType -> (string)

The directory type.

WorkspaceSecurityGroupId -> (string)

The identifier of the security group that is assigned to new WorkSpaces.

State -> (string)

The state of the directoryâs registration with Amazon WorkSpaces. After a directory is deregistered, the `DEREGISTERED` state is returned very briefly before the directory metadata is cleaned up, so this state is rarely returned. To confirm that a directory is deregistered, check for the directory ID by using [DescribeWorkspaceDirectories](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html) . If the directory ID isnât returned, then the directory has been successfully deregistered.

WorkspaceCreationProperties -> (structure)

The default creation properties for all WorkSpaces in the directory.

EnableInternetAccess -> (boolean)

Specifies whether to automatically assign an Elastic public IP address to WorkSpaces in this directory by default. If enabled, the Elastic public IP address allows outbound internet access from your WorkSpaces when youâre using an internet gateway in the Amazon VPC in which your WorkSpaces are located. If youâre using a Network Address Translation (NAT) gateway for outbound internet access from your VPC, or if your WorkSpaces are in public subnets and you manually assign them Elastic IP addresses, you should disable this setting. This setting applies to new WorkSpaces that you launch or to existing WorkSpaces that you rebuild. For more information, see [Configure a VPC for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html) .

DefaultOu -> (string)

The organizational unit (OU) in the directory for the WorkSpace machine accounts.

CustomSecurityGroupId -> (string)

The identifier of the default security group to apply to WorkSpaces when they are created. For more information, see [Security Groups for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html) .

UserEnabledAsLocalAdministrator -> (boolean)

Specifies whether WorkSpace users are local administrators on their WorkSpaces.

EnableMaintenanceMode -> (boolean)

Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see [WorkSpace Maintenance](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html) .

InstanceIamRoleArn -> (string)

Indicates the IAM role ARN of the instance.

ipGroupIds -> (list)

The identifiers of the IP access control groups associated with the directory.

(string)

WorkspaceAccessProperties -> (structure)

The devices and operating systems that users can use to access WorkSpaces.

DeviceTypeWindows -> (string)

Indicates whether users can use Windows clients to access their WorkSpaces.

DeviceTypeOsx -> (string)

Indicates whether users can use macOS clients to access their WorkSpaces.

DeviceTypeWeb -> (string)

Indicates whether users can access their WorkSpaces through a web browser.

DeviceTypeIos -> (string)

Indicates whether users can use iOS devices to access their WorkSpaces.

DeviceTypeAndroid -> (string)

Indicates whether users can use Android and Android-compatible Chrome OS devices to access their WorkSpaces.

DeviceTypeChromeOs -> (string)

Indicates whether users can use Chromebooks to access their WorkSpaces.

DeviceTypeZeroClient -> (string)

Indicates whether users can use zero client devices to access their WorkSpaces.

DeviceTypeLinux -> (string)

Indicates whether users can use Linux clients to access their WorkSpaces.

DeviceTypeWorkSpacesThinClient -> (string)

Indicates whether users can access their WorkSpaces through a WorkSpaces Thin Client.

Tenancy -> (string)

Specifies whether the directory is dedicated or shared. To use Bring Your Own License (BYOL), this value must be set to `DEDICATED` . For more information, see [Bring Your Own Windows Desktop Images](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html) .

SelfservicePermissions -> (structure)

The default self-service permissions for WorkSpaces in the directory.

RestartWorkspace -> (string)

Specifies whether users can restart their WorkSpace.

IncreaseVolumeSize -> (string)

Specifies whether users can increase the volume size of the drives on their WorkSpace.

ChangeComputeType -> (string)

Specifies whether users can change the compute type (bundle) for their WorkSpace.

SwitchRunningMode -> (string)

Specifies whether users can switch the running mode of their WorkSpace.

RebuildWorkspace -> (string)

Specifies whether users can rebuild the operating system of a WorkSpace to its original state.

SamlProperties -> (structure)

Describes the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.

Status -> (string)

Indicates the status of SAML 2.0 authentication. These statuses include the following.

- If the setting is `DISABLED` , end users will be directed to login with their directory credentials.
- If the setting is `ENABLED` , end users will be directed to login via the user access URL. Users attempting to connect to WorkSpaces from a client application that does not support SAML 2.0 authentication will not be able to connect.
- If the setting is `ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK` , end users will be directed to login via the user access URL on supported client applications, but will not prevent clients that do not support SAML 2.0 authentication from connecting as if SAML 2.0 authentication was disabled.

UserAccessUrl -> (string)

The SAML 2.0 identity provider (IdP) user access URL is the URL a user would navigate to in their web browser in order to federate from the IdP and directly access the application, without any SAML 2.0 service provider (SP) bindings.

RelayStateParameterName -> (string)

The relay state parameter name supported by the SAML 2.0 identity provider (IdP). When the end user is redirected to the user access URL from the WorkSpaces client application, this relay state parameter name is appended as a query parameter to the URL along with the relay state endpoint to return the user to the client application session.

To use SAML 2.0 authentication with WorkSpaces, the IdP must support IdP-initiated deep linking for the relay state URL. Consult your IdP documentation for more information.

CertificateBasedAuthProperties -> (structure)

The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory for WorkSpaces login.

Status -> (string)

The status of the certificate-based authentication properties.

CertificateAuthorityArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Certificate Manager Private CA resource.

EndpointEncryptionMode -> (string)

Endpoint encryption mode that allows you to configure the specified directory between Standard TLS and FIPS 140-2 validated mode.

MicrosoftEntraConfig -> (structure)

Specifies details about Microsoft Entra configurations.

TenantId -> (string)

The identifier of the tenant.

ApplicationConfigSecretArn -> (string)

The Amazon Resource Name (ARN) of the application config.

WorkspaceDirectoryName -> (string)

The name fo the WorkSpace directory.

WorkspaceDirectoryDescription -> (string)

The description of the WorkSpace directory

UserIdentityType -> (string)

Indicates the identity type of the specifired user.

WorkspaceType -> (string)

Indicates whether the directoryâs WorkSpace type is personal or pools.

IDCConfig -> (structure)

Specifies details about identity center configurations.

InstanceArn -> (string)

The Amazon Resource Name (ARN) of the identity center instance.

ApplicationArn -> (string)

The Amazon Resource Name (ARN) of the application.

ActiveDirectoryConfig -> (structure)

Information about the Active Directory config.

DomainName -> (string)

The name of the domain.

ServiceAccountSecretArn -> (string)

Indicates the secret ARN on the service account.

StreamingProperties -> (structure)

The streaming properties to configure.

StreamingExperiencePreferredProtocol -> (string)

Indicates the type of preferred protocol for the streaming experience.

UserSettings -> (list)

Indicates the permission settings asscoiated with the user.

(structure)

Information about the userâs permission settings.

Action -> (string)

Indicates the type of action.

Permission -> (string)

Indicates if the setting is enabled or disabled.

MaximumLength -> (integer)

Indicates the maximum character length for the specified user setting.

StorageConnectors -> (list)

Indicates the storage connector used

(structure)

Describes the storage connector.

ConnectorType -> (string)

The type of connector used to save user files.

Status -> (string)

Indicates if the storage connetor is enabled or disabled.

GlobalAccelerator -> (structure)

Indicates the Global Accelerator properties.

Mode -> (string)

Indicates if Global Accelerator for directory is enabled or disabled.

PreferredProtocol -> (string)

Indicates the preferred protocol for Global Accelerator.

ErrorMessage -> (string)

The error message returned.

NextToken -> (string)

The token to use to retrieve the next page of results. This value is null when there are no more results to return.