# describe-brokerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-broker.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-broker.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mq](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/index.html#cli-aws-mq) ]

# describe-broker

## Description

Returns information about the specified broker.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/DescribeBroker)

## Synopsis

```
describe-broker
--broker-id <value>
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

`--broker-id` (string)

The unique ID that Amazon MQ generates for the broker.

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

ActionsRequired -> (list)

Actions required for a broker.

(structure)

Action required for a broker.

ActionRequiredCode -> (string)

The code you can use to find instructions on the action required to resolve your broker issue.

ActionRequiredInfo -> (string)

Information about the action required to resolve your broker issue.

AuthenticationStrategy -> (string)

The authentication strategy used to secure the broker. The default is SIMPLE.

AutoMinorVersionUpgrade -> (boolean)

Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot.

BrokerArn -> (string)

The brokerâs Amazon Resource Name (ARN).

BrokerId -> (string)

The unique ID that Amazon MQ generates for the broker.

BrokerInstances -> (list)

A list of information about allocated brokers.

(structure)

Returns information about all brokers.

ConsoleURL -> (string)

The brokers web console URL.

Endpoints -> (list)

The brokerâs wire-level protocol endpoints.

(string)

IpAddress -> (string)

The IP address of the Elastic Network Interface (ENI) attached to the broker. Does not apply to RabbitMQ brokers.

BrokerName -> (string)

The brokerâs name. This value must be unique in your Amazon Web Services account account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.

BrokerState -> (string)

The brokerâs status.

Configurations -> (structure)

The list of all revisions for the specified configuration.

Current -> (structure)

The brokerâs current configuration.

Id -> (string)

Required. The unique ID that Amazon MQ generates for the configuration.

Revision -> (integer)

The revision number of the configuration.

History -> (list)

The history of configurations applied to the broker.

(structure)

A list of information about the configuration.

Id -> (string)

Required. The unique ID that Amazon MQ generates for the configuration.

Revision -> (integer)

The revision number of the configuration.

Pending -> (structure)

The brokerâs pending configuration.

Id -> (string)

Required. The unique ID that Amazon MQ generates for the configuration.

Revision -> (integer)

The revision number of the configuration.

Created -> (timestamp)

The time when the broker was created.

DeploymentMode -> (string)

The brokerâs deployment mode.

EncryptionOptions -> (structure)

Encryption options for the broker.

KmsKeyId -> (string)

The customer master key (CMK) to use for the A KMS (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will use a default CMK to encrypt your data.

UseAwsOwnedKey -> (boolean)

Enables the use of an Amazon Web Services owned CMK using KMS (KMS). Set to true by default, if no value is provided, for example, for RabbitMQ brokers.

EngineType -> (string)

The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.

EngineVersion -> (string)

The broker engine version. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide.

HostInstanceType -> (string)

The brokerâs instance type.

LdapServerMetadata -> (structure)

The metadata of the LDAP server used to authenticate and authorize connections to the broker.

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

Logs -> (structure)

The list of information about logs currently enabled and pending to be deployed for the specified broker.

Audit -> (boolean)

Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged.

AuditLogGroup -> (string)

The location of the CloudWatch Logs log group where audit logs are sent.

General -> (boolean)

Enables general logging.

GeneralLogGroup -> (string)

The location of the CloudWatch Logs log group where general logs are sent.

Pending -> (structure)

The list of information about logs pending to be deployed for the specified broker.

Audit -> (boolean)

Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged.

General -> (boolean)

Enables general logging.

MaintenanceWindowStartTime -> (structure)

The parameters that determine the WeeklyStartTime.

DayOfWeek -> (string)

Required. The day of the week.

TimeOfDay -> (string)

Required. The time, in 24-hour format.

TimeZone -> (string)

The time zone, UTC by default, in either the Country/City format, or the UTC offset format.

PendingAuthenticationStrategy -> (string)

The authentication strategy that will be applied when the broker is rebooted. The default is SIMPLE.

PendingEngineVersion -> (string)

The broker engine version to upgrade to. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide.

PendingHostInstanceType -> (string)

The brokerâs host instance type to upgrade to. For a list of supported instance types, see [Broker instance types](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker.html#broker-instance-types) .

PendingLdapServerMetadata -> (structure)

The metadata of the LDAP server that will be used to authenticate and authorize connections to the broker after it is rebooted.

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

PendingSecurityGroups -> (list)

The list of pending security groups to authorize connections to brokers.

(string)

PubliclyAccessible -> (boolean)

Enables connections from applications outside of the VPC that hosts the brokerâs subnets.

SecurityGroups -> (list)

The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.

(string)

StorageType -> (string)

The brokerâs storage type.

SubnetIds -> (list)

The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones.

(string)

Tags -> (map)

The list of all tags associated with this broker.

key -> (string)

value -> (string)

Users -> (list)

The list of all broker usernames for the specified broker.

(structure)

Returns a list of all broker users. Does not apply to RabbitMQ brokers.

PendingChange -> (string)

The type of change pending for the broker user.

Username -> (string)

Required. The username of the broker user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

DataReplicationMetadata -> (structure)

The replication details of the data replication-enabled broker. Only returned if dataReplicationMode is set to CRDR.

DataReplicationCounterpart -> (structure)

Describes the replica/primary broker. Only returned if this broker is currently set as a primary or replica in the brokerâs dataReplicationRole property.

BrokerId -> (string)

Required. The unique broker id generated by Amazon MQ.

Region -> (string)

Required. The region of the broker.

DataReplicationRole -> (string)

Defines the role of this broker in a data replication pair. When a replica broker is promoted to primary, this role is interchanged.

DataReplicationMode -> (string)

Describes whether this broker is a part of a data replication pair.

PendingDataReplicationMetadata -> (structure)

The pending replication details of the data replication-enabled broker. Only returned if pendingDataReplicationMode is set to CRDR.

DataReplicationCounterpart -> (structure)

Describes the replica/primary broker. Only returned if this broker is currently set as a primary or replica in the brokerâs dataReplicationRole property.

BrokerId -> (string)

Required. The unique broker id generated by Amazon MQ.

Region -> (string)

Required. The region of the broker.

DataReplicationRole -> (string)

Defines the role of this broker in a data replication pair. When a replica broker is promoted to primary, this role is interchanged.

PendingDataReplicationMode -> (string)

Describes whether this broker will be a part of a data replication pair after reboot.