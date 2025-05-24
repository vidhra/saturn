# create-brokerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mq](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/index.html#cli-aws-mq) ]

# create-broker

## Description

Creates a broker. Note: This API is asynchronous.

To create a broker, you must either use the AmazonMQFullAccess IAM policy or include the following EC2 permissions in your IAM policy.

- ec2:CreateNetworkInterface This permission is required to allow Amazon MQ to create an elastic network interface (ENI) on behalf of your account.
- ec2:CreateNetworkInterfacePermission This permission is required to attach the ENI to the broker instance.
- ec2:DeleteNetworkInterface
- ec2:DeleteNetworkInterfacePermission
- ec2:DetachNetworkInterface
- ec2:DescribeInternetGateways
- ec2:DescribeNetworkInterfaces
- ec2:DescribeNetworkInterfacePermissions
- ec2:DescribeRouteTables
- ec2:DescribeSecurityGroups
- ec2:DescribeSubnets
- ec2:DescribeVpcs

For more information, see [Create an IAM User and Get Your Amazon Web Services Credentials](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/amazon-mq-setting-up.html#create-iam-user) and [Never Modify or Delete the Amazon MQ Elastic Network Interface](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/connecting-to-amazon-mq.html#never-modify-delete-elastic-network-interface) in the *Amazon MQ Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/CreateBroker)

## Synopsis

```
create-broker
[--authentication-strategy <value>]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
--broker-name <value>
[--configuration <value>]
[--creator-request-id <value>]
--deployment-mode <value>
[--encryption-options <value>]
--engine-type <value>
[--engine-version <value>]
--host-instance-type <value>
[--ldap-server-metadata <value>]
[--logs <value>]
[--maintenance-window-start-time <value>]
--publicly-accessible | --no-publicly-accessible
[--security-groups <value>]
[--storage-type <value>]
[--subnet-ids <value>]
[--tags <value>]
--users <value>
[--data-replication-mode <value>]
[--data-replication-primary-broker-arn <value>]
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

`--authentication-strategy` (string)

Optional. The authentication strategy used to secure the broker. The default is SIMPLE.

Possible values:

- `SIMPLE`
- `LDAP`

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot. Set to true by default, if no value is specified.

### Note

Must be set to true for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above.

`--broker-name` (string)

Required. The brokerâs name. This value must be unique in your Amazon Web Services account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.

### Warning

Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker names are not intended to be used for private or sensitive data.

`--configuration` (structure)

A list of information about the configuration.

Id -> (string)

Required. The unique ID that Amazon MQ generates for the configuration.

Revision -> (integer)

The revision number of the configuration.

Shorthand Syntax:

```
Id=string,Revision=integer
```

JSON Syntax:

```
{
  "Id": "string",
  "Revision": integer
}
```

`--creator-request-id` (string)

The unique ID that the requester receives for the created broker. Amazon MQ passes your ID with the API action.

### Note

We recommend using a Universally Unique Identifier (UUID) for the creatorRequestId. You may omit the creatorRequestId if your application doesnât require idempotency.

`--deployment-mode` (string)

Required. The brokerâs deployment mode.

Possible values:

- `SINGLE_INSTANCE`
- `ACTIVE_STANDBY_MULTI_AZ`
- `CLUSTER_MULTI_AZ`

`--encryption-options` (structure)

Encryption options for the broker.

KmsKeyId -> (string)

The customer master key (CMK) to use for the A KMS (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will use a default CMK to encrypt your data.

UseAwsOwnedKey -> (boolean)

Enables the use of an Amazon Web Services owned CMK using KMS (KMS). Set to true by default, if no value is provided, for example, for RabbitMQ brokers.

Shorthand Syntax:

```
KmsKeyId=string,UseAwsOwnedKey=boolean
```

JSON Syntax:

```
{
  "KmsKeyId": "string",
  "UseAwsOwnedKey": true|false
}
```

`--engine-type` (string)

Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.

Possible values:

- `ACTIVEMQ`
- `RABBITMQ`

`--engine-version` (string)

The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide.

`--host-instance-type` (string)

Required. The brokerâs instance type.

`--ldap-server-metadata` (structure)

Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.

Hosts -> (list)

Specifies the location of the LDAP server such as Directory Service for Microsoft Active Directory. Optional failover server.

(string)

RoleBase -> (string)

The distinguished name of the node in the directory information tree (DIT) to search for roles or groups. For example, ou=group, ou=corp, dc=corp, dc=example, dc=com.

RoleName -> (string)

Specifies the LDAP attribute that identifies the group name attribute in the object returned from the group membership query.

RoleSearchMatching -> (string)

The LDAP search filter used to find roles within the roleBase. The distinguished name of the user matched by userSearchMatching is substituted into the {0} placeholder in the search filter. The clientâs username is substituted into the {1} placeholder. For example, if you set this option to (member=uid={1})for the user janedoe, the search filter becomes (member=uid=janedoe) after string substitution. It matches all role entries that have a member attribute equal to uid=janedoe under the subtree selected by the roleBase.

RoleSearchSubtree -> (boolean)

The directory search scope for the role. If set to true, scope is to search the entire subtree.

ServiceAccountPassword -> (string)

Service account password. A service account is an account in your LDAP server that has access to initiate a connection. For example, cn=admin,dc=corp, dc=example, dc=com.

ServiceAccountUsername -> (string)

Service account username. A service account is an account in your LDAP server that has access to initiate a connection. For example, cn=admin,dc=corp, dc=example, dc=com.

UserBase -> (string)

Select a particular subtree of the directory information tree (DIT) to search for user entries. The subtree is specified by a DN, which specifies the base node of the subtree. For example, by setting this option to ou=Users,ou=corp, dc=corp, dc=example, dc=com, the search for user entries is restricted to the subtree beneath ou=Users, ou=corp, dc=corp, dc=example, dc=com.

UserRoleName -> (string)

Specifies the name of the LDAP attribute for the user group membership.

UserSearchMatching -> (string)

The LDAP search filter used to find users within the userBase. The clientâs username is substituted into the {0} placeholder in the search filter. For example, if this option is set to (uid={0}) and the received username is janedoe, the search filter becomes (uid=janedoe) after string substitution. It will result in matching an entry like uid=janedoe, ou=Users,ou=corp, dc=corp, dc=example, dc=com.

UserSearchSubtree -> (boolean)

The directory search scope for the user. If set to true, scope is to search the entire subtree.

Shorthand Syntax:

```
Hosts=string,string,RoleBase=string,RoleName=string,RoleSearchMatching=string,RoleSearchSubtree=boolean,ServiceAccountPassword=string,ServiceAccountUsername=string,UserBase=string,UserRoleName=string,UserSearchMatching=string,UserSearchSubtree=boolean
```

JSON Syntax:

```
{
  "Hosts": ["string", ...],
  "RoleBase": "string",
  "RoleName": "string",
  "RoleSearchMatching": "string",
  "RoleSearchSubtree": true|false,
  "ServiceAccountPassword": "string",
  "ServiceAccountUsername": "string",
  "UserBase": "string",
  "UserRoleName": "string",
  "UserSearchMatching": "string",
  "UserSearchSubtree": true|false
}
```

`--logs` (structure)

Enables Amazon CloudWatch logging for brokers.

Audit -> (boolean)

Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Does not apply to RabbitMQ brokers.

General -> (boolean)

Enables general logging.

Shorthand Syntax:

```
Audit=boolean,General=boolean
```

JSON Syntax:

```
{
  "Audit": true|false,
  "General": true|false
}
```

`--maintenance-window-start-time` (structure)

The parameters that determine the WeeklyStartTime.

DayOfWeek -> (string)

Required. The day of the week.

TimeOfDay -> (string)

Required. The time, in 24-hour format.

TimeZone -> (string)

The time zone, UTC by default, in either the Country/City format, or the UTC offset format.

Shorthand Syntax:

```
DayOfWeek=string,TimeOfDay=string,TimeZone=string
```

JSON Syntax:

```
{
  "DayOfWeek": "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY",
  "TimeOfDay": "string",
  "TimeZone": "string"
}
```

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Enables connections from applications outside of the VPC that hosts the brokerâs subnets. Set to false by default, if no value is provided.

`--security-groups` (list)

The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.

(string)

Syntax:

```
"string" "string" ...
```

`--storage-type` (string)

The brokerâs storage type.

Possible values:

- `EBS`
- `EFS`

`--subnet-ids` (list)

The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ Amazon MQ for ActiveMQ deployment requires two subnets. A CLUSTER_MULTI_AZ Amazon MQ for RabbitMQ deployment has no subnet requirements when deployed with public accessibility. Deployment without public accessibility requires at least one subnet.

### Warning

If you specify subnets in a [shared VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your Amazon Web Services account. Amazon MQ will not be able to create VPC endpoints in VPCs that are not owned by your Amazon Web Services account.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (map)

Create tags when creating the broker.

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

`--users` (list)

The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.

(structure)

A user associated with the broker. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.

ConsoleAccess -> (boolean)

Enables access to the ActiveMQ Web Console for the ActiveMQ user. Does not apply to RabbitMQ brokers.

Groups -> (list)

The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. Does not apply to RabbitMQ brokers.

(string)

Password -> (string)

Required. The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=).

Username -> (string)

The username of the broker user. The following restrictions apply to broker usernames:

- For Amazon MQ for ActiveMQ brokers, this value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
- para>For Amazon MQ for RabbitMQ brokers, this value can contain only alphanumeric characters, dashes, periods, underscores (- . _). This value must not contain a tilde (~) character. Amazon MQ prohibts using guest as a valid usename. This value must be 2-100 characters long.

### Warning

Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker usernames are not intended to be used for private or sensitive data.

ReplicationUser -> (boolean)

Defines if this user is intended for CRDR replication purposes.

Shorthand Syntax:

```
ConsoleAccess=boolean,Groups=string,string,Password=string,Username=string,ReplicationUser=boolean ...
```

JSON Syntax:

```
[
  {
    "ConsoleAccess": true|false,
    "Groups": ["string", ...],
    "Password": "string",
    "Username": "string",
    "ReplicationUser": true|false
  }
  ...
]
```

`--data-replication-mode` (string)

Defines whether this broker is a part of a data replication pair.

Possible values:

- `NONE`
- `CRDR`

`--data-replication-primary-broker-arn` (string)

The Amazon Resource Name (ARN) of the primary broker that is used to replicate data from in a data replication pair, and is applied to the replica broker. Must be set when dataReplicationMode is set to CRDR.

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

BrokerArn -> (string)

The brokerâs Amazon Resource Name (ARN).

BrokerId -> (string)

The unique ID that Amazon MQ generates for the broker.