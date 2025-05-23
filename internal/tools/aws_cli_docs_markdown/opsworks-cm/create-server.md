# create-serverÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/create-server.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/create-server.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworkscm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/index.html#cli-aws-opsworkscm) ]

# create-server

## Description

Creates and immedately starts a new server. The server is ready to use when it is in the `HEALTHY` state. By default, you can create a maximum of 10 servers.

This operation is asynchronous.

A `LimitExceededException` is thrown when you have created the maximum number of servers (10). A `ResourceAlreadyExistsException` is thrown when a server with the same name already exists in the account. A `ResourceNotFoundException` is thrown when you specify a backup ID that is not valid or is for a backup that does not exist. A `ValidationException` is thrown when parameters of the request are not valid.

If you do not specify a security group by adding the `SecurityGroupIds` parameter, AWS OpsWorks creates a new security group.

*Chef Automate:* The default security group opens the Chef server to the world on TCP port 443. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22.

*Puppet Enterprise:* The default security group opens TCP ports 22, 443, 4433, 8140, 8142, 8143, and 8170. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22.

By default, your server is accessible from any IP address. We recommend that you update your security group rules to allow access from known IP addresses and address ranges only. To edit security group rules, open Security Groups in the navigation pane of the EC2 management console.

To specify your own domain for a server, and provide your own self-signed or CA-signed certificate and private key, specify values for `CustomDomain` , `CustomCertificate` , and `CustomPrivateKey` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/CreateServer)

## Synopsis

```
create-server
[--associate-public-ip-address | --no-associate-public-ip-address]
[--custom-domain <value>]
[--custom-certificate <value>]
[--custom-private-key <value>]
[--disable-automated-backup | --no-disable-automated-backup]
--engine <value>
[--engine-model <value>]
[--engine-version <value>]
[--engine-attributes <value>]
[--backup-retention-count <value>]
--server-name <value>
--instance-profile-arn <value>
--instance-type <value>
[--key-pair <value>]
[--preferred-maintenance-window <value>]
[--preferred-backup-window <value>]
[--security-group-ids <value>]
--service-role-arn <value>
[--subnet-ids <value>]
[--tags <value>]
[--backup-id <value>]
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

`--associate-public-ip-address` | `--no-associate-public-ip-address` (boolean)

Associate a public IP address with a server that you are launching. Valid values are `true` or `false` . The default value is `true` .

`--custom-domain` (string)

An optional public endpoint of a server, such as `https://aws.my-company.com` . To access the server, create a CNAME DNS record in your preferred DNS service that points the custom domain to the endpoint that is generated when the server is created (the value of the CreateServer Endpoint attribute). You cannot access the server by using the generated `Endpoint` value if the server is using a custom domain. If you specify a custom domain, you must also specify values for `CustomCertificate` and `CustomPrivateKey` .

`--custom-certificate` (string)

A PEM-formatted HTTPS certificate. The value can be be a single, self-signed certificate, or a certificate chain. If you specify a custom certificate, you must also specify values for `CustomDomain` and `CustomPrivateKey` . The following are requirements for the `CustomCertificate` value:

- You can provide either a self-signed, custom certificate, or the full certificate chain.
- The certificate must be a valid X509 certificate, or a certificate chain in PEM format.
- The certificate must be valid at the time of upload. A certificate canât be used before its validity period begins (the certificateâs `NotBefore` date), or after it expires (the certificateâs `NotAfter` date).
- The certificateâs common name or subject alternative names (SANs), if present, must match the value of `CustomDomain` .
- The certificate must match the value of `CustomPrivateKey` .

`--custom-private-key` (string)

A private key in PEM format for connecting to the server by using HTTPS. The private key must not be encrypted; it cannot be protected by a password or passphrase. If you specify a custom private key, you must also specify values for `CustomDomain` and `CustomCertificate` .

`--disable-automated-backup` | `--no-disable-automated-backup` (boolean)

Enable or disable scheduled backups. Valid values are `true` or `false` . The default value is `true` .

`--engine` (string)

The configuration management engine to use. Valid values include `ChefAutomate` and `Puppet` .

`--engine-model` (string)

The engine model of the server. Valid values in this release include `Monolithic` for Puppet and `Single` for Chef.

`--engine-version` (string)

The major release version of the engine that you want to use. For a Chef server, the valid value for EngineVersion is currently `2` . For a Puppet server, valid values are `2019` or `2017` .

`--engine-attributes` (list)

Optional engine attributes on a specified server.

**Attributes accepted in a Chef createServer request:**

- `CHEF_AUTOMATE_PIVOTAL_KEY` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. When no CHEF_AUTOMATE_PIVOTAL_KEY is set, a private key is generated and returned in the response.
- `CHEF_AUTOMATE_ADMIN_PASSWORD` : The password for the administrative user in the Chef Automate web-based dashboard. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters ([!/@#$%^&+=_](mailto:!/%40#$%^&+=_)). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_AUTOMATE_ADMIN_PASSWORD is set, one is generated and returned in the response.

**Attributes accepted in a Puppet createServer request:**

- `PUPPET_ADMIN_PASSWORD` : To work with the Puppet Enterprise console, a password must use ASCII characters.
- `PUPPET_R10K_REMOTE` : The r10k remote is the URL of your control repository (for example, [ssh://git@your.git-repo.com:user/control-repo.git](ssh://git@your.git-repo.com:user/control-repo.git)). Specifying an r10k remote opens TCP port 8170.
- `PUPPET_R10K_PRIVATE_KEY` : If you are using a private Git repository, add PUPPET_R10K_PRIVATE_KEY to specify a PEM-encoded private SSH key.

(structure)

A name and value pair that is specific to the engine of the server.

Name -> (string)

The name of the engine attribute.

Value -> (string)

The value of the engine attribute.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--backup-retention-count` (integer)

The number of automated backups that you want to keep. Whenever a new backup is created, AWS OpsWorks CM deletes the oldest backups if this number is exceeded. The default value is `1` .

`--server-name` (string)

The name of the server. The server name must be unique within your AWS account, within each region. Server names must start with a letter; then letters, numbers, or hyphens (-) are allowed, up to a maximum of 40 characters.

`--instance-profile-arn` (string)

The ARN of the instance profile that your Amazon EC2 instances use. Although the AWS OpsWorks console typically creates the instance profile for you, if you are using API commands instead, run the service-role-creation.yaml AWS CloudFormation template, located at [https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml](https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml). This template creates a CloudFormation stack that includes the instance profile you need.

`--instance-type` (string)

The Amazon EC2 instance type to use. For example, `m5.large` .

`--key-pair` (string)

The Amazon EC2 key pair to set for the instance. This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH.

`--preferred-maintenance-window` (string)

The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance. Valid values must be specified in the following format: `DDD:HH:MM` . `MM` must be specified as `00` . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See `TimeWindowDefinition` for more information.

**Example:** `Mon:08:00` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)

`--preferred-backup-window` (string)

The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled. Valid values must be specified in one of the following formats:

- `HH:MM` for daily backups
- `DDD:HH:MM` for weekly backups

`MM` must be specified as `00` . The specified time is in coordinated universal time (UTC). The default value is a random, daily start time.

**Example:** `08:00` , which represents a daily start time of 08:00 UTC.

**Example:** `Mon:08:00` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)

`--security-group-ids` (list)

A list of security group IDs to attach to the Amazon EC2 instance. If you add this parameter, the specified security groups must be within the VPC that is specified by `SubnetIds` .

If you do not specify this parameter, AWS OpsWorks CM creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone).

(string)

Syntax:

```
"string" "string" ...
```

`--service-role-arn` (string)

The service role that the AWS OpsWorks CM service backend uses to work with your account. Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at [https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml](https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml). This template creates a CloudFormation stack that includes the service role and instance profile that you need.

`--subnet-ids` (list)

The IDs of subnets in which to launch the server EC2 instance.

Amazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have âAuto Assign Public IPâ enabled.

EC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have âAuto Assign Public IPâ enabled.

For more information about supported Amazon EC2 platforms, see [Supported Platforms](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server.

- The key cannot be empty.
- The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : / @`
- The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : / @`
- Leading and trailing white spaces are trimmed from both the key and value.
- A maximum of 50 user-applied tags is allowed for any AWS OpsWorks-CM server.

(structure)

A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server. Leading and trailing white spaces are trimmed from both the key and value. A maximum of 50 user-applied tags is allowed for tag-supported AWS OpsWorks-CM resources.

Key -> (string)

A tag key, such as `Stage` or `Name` . A tag key cannot be empty. The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`

Value -> (string)

An optional tag value, such as `Production` or `test-owcm-server` . The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--backup-id` (string)

If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId.

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

**To create a server**

The following `create-server` example creates a new Chef Automate server named `automate-06` in your default region. Note that defaults are used for most other settings, such as number of backups to retain, and maintenance and backup start times. Before you run a `create-server` command, complete prerequisites in [Getting Started with AWS OpsWorks for Chef Automate](https://docs.aws.amazon.com/opsworks/latest/userguide/gettingstarted-opscm.html) in the *AWS Opsworks for Chef Automate User Guide*.

```
aws opsworks-cm create-server \
    --engine "Chef" \
    --engine-model "Single" \
    --engine-version "12" \
    --server-name "automate-06" \
    --instance-profile-arn "arn:aws:iam::1019881987024:instance-profile/aws-opsworks-cm-ec2-role" \
    --instance-type "t2.medium" \
    --key-pair "amazon-test" \
    --service-role-arn "arn:aws:iam::044726508045:role/aws-opsworks-cm-service-role"
```

The output shows you information similar to the following about the new server:

```
{
    "Server": {
        "BackupRetentionCount": 10,
        "CreatedAt": 2016-07-29T13:38:47.520Z,
        "DisableAutomatedBackup": FALSE,
        "Endpoint": "https://opsworks-cm.us-east-1.amazonaws.com",
        "Engine": "Chef",
        "EngineAttributes": [
            {
                "Name": "CHEF_DELIVERY_ADMIN_PASSWORD",
                "Value": "1Password1"
            }
        ],
        "EngineModel": "Single",
        "EngineVersion": "12",
        "InstanceProfileArn": "arn:aws:iam::1019881987024:instance-profile/aws-opsworks-cm-ec2-role",
        "InstanceType": "t2.medium",
        "KeyPair": "amazon-test",
        "MaintenanceStatus": "",
        "PreferredBackupWindow": "Sun:02:00",
        "PreferredMaintenanceWindow": "00:00",
        "SecurityGroupIds": [ "sg-1a24c270" ],
        "ServerArn": "arn:aws:iam::1019881987024:instance/automate-06-1010V4UU2WRM2",
        "ServerName": "automate-06",
        "ServiceRoleArn": "arn:aws:iam::1019881987024:role/aws-opsworks-cm-service-role",
        "Status": "CREATING",
        "StatusReason": "",
        "SubnetIds": [ "subnet-49436a18" ]
    }
}
```

For more information, see [UpdateServer](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_UpdateServer.html) in the *AWS OpsWorks for Chef Automate API Reference*.

## Output

Server -> (structure)

The server that is created by the request.

AssociatePublicIpAddress -> (boolean)

Associate a public IP address with a server that you are launching.

BackupRetentionCount -> (integer)

The number of automated backups to keep.

ServerName -> (string)

The name of the server.

CreatedAt -> (timestamp)

Time stamp of server creation. Example `2016-07-29T13:38:47.520Z`

CloudFormationStackArn -> (string)

The ARN of the CloudFormation stack that was used to create the server.

CustomDomain -> (string)

An optional public endpoint of a server, such as `https://aws.my-company.com` . You cannot access the server by using the `Endpoint` value if the server has a `CustomDomain` specified.

DisableAutomatedBackup -> (boolean)

Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount.

Endpoint -> (string)

A DNS name that can be used to access the engine. Example: `myserver-asdfghjkl.us-east-1.opsworks.io` . You cannot access the server by using the `Endpoint` value if the server has a `CustomDomain` specified.

Engine -> (string)

The engine type of the server. Valid values in this release include `ChefAutomate` and `Puppet` .

EngineModel -> (string)

The engine model of the server. Valid values in this release include `Monolithic` for Puppet and `Single` for Chef.

EngineAttributes -> (list)

The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer().

**Attributes returned in a createServer response for Chef**

- `CHEF_AUTOMATE_PIVOTAL_KEY` : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
- `CHEF_STARTER_KIT` : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where youâve unzipped the file contents. From this directory, you can run Knife commands.

**Attributes returned in a createServer response for Puppet**

- `PUPPET_STARTER_KIT` : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where youâve unzipped the file contents.
- `PUPPET_ADMIN_PASSWORD` : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online.

(structure)

A name and value pair that is specific to the engine of the server.

Name -> (string)

The name of the engine attribute.

Value -> (string)

The value of the engine attribute.

EngineVersion -> (string)

The engine version of the server. For a Chef server, the valid value for EngineVersion is currently `2` . For a Puppet server, specify either `2019` or `2017` .

InstanceProfileArn -> (string)

The instance profile ARN of the server.

InstanceType -> (string)

The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console.

KeyPair -> (string)

The key pair associated with the server.

MaintenanceStatus -> (string)

The status of the most recent server maintenance run. Shows `SUCCESS` or `FAILED` .

PreferredMaintenanceWindow -> (string)

The preferred maintenance period specified for the server.

PreferredBackupWindow -> (string)

The preferred backup period specified for the server.

SecurityGroupIds -> (list)

The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console.

(string)

ServiceRoleArn -> (string)

The service role ARN used to create the server.

Status -> (string)

The serverâs status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the serverâs health state.

StatusReason -> (string)

Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results).

SubnetIds -> (list)

The subnet IDs specified in a CreateServer request.

(string)

ServerArn -> (string)

The ARN of the server.