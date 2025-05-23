# describe-serversÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/describe-servers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/describe-servers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworkscm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/index.html#cli-aws-opsworkscm) ]

# describe-servers

## Description

Lists all configuration management servers that are identified with your account. Only the stored results from Amazon DynamoDB are returned. AWS OpsWorks CM does not query other services.

This operation is synchronous.

A `ResourceNotFoundException` is thrown when the server does not exist. A `ValidationException` is raised when parameters of the request are not valid.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeServers)

`describe-servers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Servers`

## Synopsis

```
describe-servers
[--server-name <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--server-name` (string)

Describes the server with the specified ServerName.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

**To describe servers**

The following `describe-servers` command returns information about all servers
that are associated with your account, and in your default region.:

```
aws opsworks-cm describe-servers
```

The output for each server entry returned by the command resembles the following.
*Output*:

```
{
 "Servers": [
    {
       "BackupRetentionCount": 8,
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
       "InstanceProfileArn": "arn:aws:iam::1019881987024:instance-profile/automate-06-1010V4UU2WRM2",
       "InstanceType": "m4.large",
       "KeyPair": "",
       "MaintenanceStatus": "SUCCESS",
       "PreferredBackupWindow": "03:00",
       "PreferredMaintenanceWindow": "Mon:09:00",
       "SecurityGroupIds": [ "sg-1a24c270" ],
       "ServerArn": "arn:aws:iam::1019881987024:instance/automate-06-1010V4UU2WRM2",
       "ServerName": "automate-06",
       "ServiceRoleArn": "arn:aws:iam::1019881987024:role/aws-opsworks-cm-service-role.1114810729735",
       "Status": "HEALTHY",
       "StatusReason": "",
       "SubnetIds": [ "subnet-49436a18" ]
    }
 ]
}
```

**More Information**

For more information, see [DescribeServers](http://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DescribeServers.html) in the *AWS OpsWorks for Chef Automate API Guide*.

## Output

Servers -> (list)

Contains the response to a `DescribeServers` request.

*For Chef Automate servers:* If `DescribeServersResponse$Servers$EngineAttributes` includes CHEF_MAJOR_UPGRADE_AVAILABLE, you can upgrade the Chef Automate server to Chef Automate 2. To be eligible for upgrade, a server running Chef Automate 1 must have had at least one successful maintenance run after November 1, 2019.

*For Puppet servers:* `DescribeServersResponse$Servers$EngineAttributes` contains the following two responses:

- `PUPPET_API_CA_CERT` , the PEM-encoded CA certificate that is used by the Puppet API over TCP port number 8140. The CA certificate is also used to sign node certificates.
- `PUPPET_API_CRL` , a certificate revocation list. The certificate revocation list is for internal maintenance purposes only. For more information about the Puppet certificate revocation list, see [Man Page: puppet certificate_revocation_list](https://puppet.com/docs/puppet/5.5/man/certificate_revocation_list.html) in the Puppet documentation.

(structure)

Describes a configuration management server.

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

NextToken -> (string)

This is not currently implemented for `DescribeServers` requests.