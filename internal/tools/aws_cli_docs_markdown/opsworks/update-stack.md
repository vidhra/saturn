# update-stackÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-stack.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-stack.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# update-stack

## Description

Updates a specified stack.

**Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateStack)

## Synopsis

```
update-stack
--stack-id <value>
[--name <value>]
[--attributes <value>]
[--service-role-arn <value>]
[--default-instance-profile-arn <value>]
[--default-os <value>]
[--hostname-theme <value>]
[--default-availability-zone <value>]
[--default-subnet-id <value>]
[--custom-json <value>]
[--configuration-manager <value>]
[--chef-configuration <value>]
[--use-custom-cookbooks | --no-use-custom-cookbooks]
[--custom-cookbooks-source <value>]
[--default-ssh-key-name <value>]
[--default-root-device-type <value>]
[--use-opsworks-security-groups | --no-use-opsworks-security-groups]
[--agent-version <value>]
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

`--name` (string)

The stackâs new name. Stack names can be a maximum of 64 characters.

`--attributes` (map)

One or more user-defined key-value pairs to be added to the stack attributes.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string

Where valid key names are:
  Color
```

JSON Syntax:

```
{"Color": "string"
  ...}
```

`--service-role-arn` (string)

Do not use this parameter. You cannot update a stackâs service role.

`--default-instance-profile-arn` (string)

The ARN of an IAM profile that is the default profile for all of the stackâs EC2 instances. For more information about IAM ARNs, see [Using Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) .

`--default-os` (string)

The stackâs operating system, which must be set to one of the following:

- A supported Linux operating system: An Amazon Linux version, such as `Amazon Linux 2` , `Amazon Linux 2018.03` , `Amazon Linux 2017.09` , `Amazon Linux 2017.03` , `Amazon Linux 2016.09` , `Amazon Linux 2016.03` , `Amazon Linux 2015.09` , or `Amazon Linux 2015.03` .
- A supported Ubuntu operating system, such as `Ubuntu 18.04 LTS` , `Ubuntu 16.04 LTS` , `Ubuntu 14.04 LTS` , or `Ubuntu 12.04 LTS` .
- `CentOS Linux 7`
- `Red Hat Enterprise Linux 7`
- A supported Windows operating system, such as `Microsoft Windows Server 2012 R2 Base` , `Microsoft Windows Server 2012 R2 with SQL Server Express` , `Microsoft Windows Server 2012 R2 with SQL Server Standard` , or `Microsoft Windows Server 2012 R2 with SQL Server Web` .
- A custom AMI: `Custom` . You specify the custom AMI you want to use when you create instances. For more information about how to use custom AMIs with OpsWorks, see [Using Custom AMIs](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html) .

The default option is the stackâs current operating system. Not all operating systems are supported with all versions of Chef. For more information about supported operating systems, see [OpsWorks Stacks Operating Systems](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html) .

`--hostname-theme` (string)

The stackâs new host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stackâs instances. By default, `HostnameTheme` is set to `Layer_Dependent` , which creates host names by appending integers to the layerâs short name. The other themes are:

- `Baked_Goods`
- `Clouds`
- `Europe_Cities`
- `Fruits`
- `Greek_Deities_and_Titans`
- `Legendary_creatures_from_Japan`
- `Planets_and_Moons`
- `Roman_Deities`
- `Scottish_Islands`
- `US_Cities`
- `Wild_Cats`

To obtain a generated host name, call `GetHostNameSuggestion` , which returns a host name based on the current theme.

`--default-availability-zone` (string)

The stackâs default Availability Zone, which must be in the stackâs region. For more information, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) . If you also specify a value for `DefaultSubnetId` , the subnet must be in the same zone. For more information, see  CreateStack .

`--default-subnet-id` (string)

The stackâs default VPC subnet ID. This parameter is required if you specify a value for the `VpcId` parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for `DefaultAvailabilityZone` , the subnet must be in that zone. For information on default values and when this parameter is required, see the `VpcId` parameter description.

`--custom-json` (string)

A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration JSON values or to pass data to recipes. The string should be in the following format:

`"{\"key1\": \"value1\", \"key2\": \"value2\",...}"`

For more information about custom JSON, see [Use Custom JSON to Modify the Stack Configuration Attributes](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html) .

`--configuration-manager` (structure)

The configuration manager. When you update a stack, we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.

Name -> (string)

The name. This parameter must be set to `Chef` .

Version -> (string)

The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 12.

Shorthand Syntax:

```
Name=string,Version=string
```

JSON Syntax:

```
{
  "Name": "string",
  "Version": "string"
}
```

`--chef-configuration` (structure)

A `ChefConfiguration` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see [Create a New Stack](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html) .

ManageBerkshelf -> (boolean)

Whether to enable Berkshelf.

BerkshelfVersion -> (string)

The Berkshelf version.

Shorthand Syntax:

```
ManageBerkshelf=boolean,BerkshelfVersion=string
```

JSON Syntax:

```
{
  "ManageBerkshelf": true|false,
  "BerkshelfVersion": "string"
}
```

`--use-custom-cookbooks` | `--no-use-custom-cookbooks` (boolean)

Whether the stack uses custom cookbooks.

`--custom-cookbooks-source` (structure)

Contains the information required to retrieve an app or cookbook from a repository. For more information, see [Adding Apps](https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html) or [Cookbooks and Recipes](https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html) .

Type -> (string)

The repository type.

Url -> (string)

The source URL. The following is an example of an Amazon S3 source URL: `https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz` .

Username -> (string)

This parameter depends on the repository type.

- For Amazon S3 bundles, set `Username` to the appropriate IAM access key ID.
- For HTTP bundles, Git repositories, and Subversion repositories, set `Username` to the user name.

Password -> (string)

When included in a request, the parameter depends on the repository type.

- For Amazon S3 bundles, set `Password` to the appropriate IAM secret access key.
- For HTTP bundles and Subversion repositories, set `Password` to the password.

For more information on how to safely handle IAM credentials, see [https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html) .

In responses, OpsWorks Stacks returns `*****FILTERED*****` instead of the actual value.

SshKey -> (string)

In requests, the repositoryâs SSH key.

In responses, OpsWorks Stacks returns `*****FILTERED*****` instead of the actual value.

Revision -> (string)

The applicationâs version. OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

Shorthand Syntax:

```
Type=string,Url=string,Username=string,Password=string,SshKey=string,Revision=string
```

JSON Syntax:

```
{
  "Type": "git"|"svn"|"archive"|"s3",
  "Url": "string",
  "Username": "string",
  "Password": "string",
  "SshKey": "string",
  "Revision": "string"
}
```

`--default-ssh-key-name` (string)

A default Amazon EC2 key-pair name. The default value is `none` . If you specify a key-pair name, OpsWorks Stacks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see [Using SSH to Communicate with an Instance](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html) and [Managing SSH Access](https://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html) . You can override this setting by specifying a different key pair, or no key pair, when you [create an instance](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html) .

`--default-root-device-type` (string)

The default root device type. This value is used by default for all instances in the stack, but you can override it when you create an instance. For more information, see [Storage for the Root Device](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device) .

Possible values:

- `ebs`
- `instance-store`

`--use-opsworks-security-groups` | `--no-use-opsworks-security-groups` (boolean)

Whether to associate the OpsWorks Stacks built-in security groups with the stackâs layers.

OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. `UseOpsworksSecurityGroups` allows you to provide your own custom security groups instead of using the built-in groups. `UseOpsworksSecurityGroups` has the following settings:

- True - OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group.
- False - OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on. Custom security groups are required only for those layers that need custom settings.

For more information, see [Create a New Stack](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html) .

`--agent-version` (string)

The default OpsWorks Stacks agent version. You have the following options:

- Auto-update - Set this parameter to `LATEST` . OpsWorks Stacks automatically installs new agent versions on the stackâs instances as soon as they are available.
- Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. OpsWorks Stacks installs that version on the stackâs instances.

The default setting is `LATEST` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.

### Note

You can also specify an agent version when you create or update an instance, which overrides the stackâs default setting.

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

None