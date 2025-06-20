# create-replication-configuration-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/create-replication-configuration-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/create-replication-configuration-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mgn](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/index.html#cli-aws-mgn) ]

# create-replication-configuration-template

## Description

Creates a new ReplicationConfigurationTemplate.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mgn-2020-02-26/CreateReplicationConfigurationTemplate)

## Synopsis

```
create-replication-configuration-template
--associate-default-security-group | --no-associate-default-security-group
--bandwidth-throttling <value>
--create-public-ip | --no-create-public-ip
--data-plane-routing <value>
--default-large-staging-disk-type <value>
--ebs-encryption <value>
[--ebs-encryption-key-arn <value>]
--replication-server-instance-type <value>
--replication-servers-security-groups-ids <value>
--staging-area-subnet-id <value>
--staging-area-tags <value>
[--tags <value>]
--use-dedicated-replication-server | --no-use-dedicated-replication-server
[--use-fips-endpoint | --no-use-fips-endpoint]
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

`--associate-default-security-group` | `--no-associate-default-security-group` (boolean)

Request to associate the default Application Migration Service Security group with the Replication Settings template.

`--bandwidth-throttling` (long)

Request to configure bandwidth throttling during Replication Settings template creation.

`--create-public-ip` | `--no-create-public-ip` (boolean)

Request to create Public IP during Replication Settings template creation.

`--data-plane-routing` (string)

Request to configure data plane routing during Replication Settings template creation.

Possible values:

- `PRIVATE_IP`
- `PUBLIC_IP`

`--default-large-staging-disk-type` (string)

Request to configure the default large staging disk EBS volume type during Replication Settings template creation.

Possible values:

- `GP2`
- `ST1`
- `GP3`

`--ebs-encryption` (string)

Request to configure EBS encryption during Replication Settings template creation.

Possible values:

- `DEFAULT`
- `CUSTOM`

`--ebs-encryption-key-arn` (string)

Request to configure an EBS encryption key during Replication Settings template creation.

`--replication-server-instance-type` (string)

Request to configure the Replication Server instance type during Replication Settings template creation.

`--replication-servers-security-groups-ids` (list)

Request to configure the Replication Server Security group ID during Replication Settings template creation.

(string)

Syntax:

```
"string" "string" ...
```

`--staging-area-subnet-id` (string)

Request to configure the Staging Area subnet ID during Replication Settings template creation.

`--staging-area-tags` (map)

Request to configure Staging Area tags during Replication Settings template creation.

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

`--tags` (map)

Request to configure tags during Replication Settings template creation.

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

`--use-dedicated-replication-server` | `--no-use-dedicated-replication-server` (boolean)

Request to use Dedicated Replication Servers during Replication Settings template creation.

`--use-fips-endpoint` | `--no-use-fips-endpoint` (boolean)

Request to use Fips Endpoint during Replication Settings template creation.

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

arn -> (string)

Replication Configuration template ARN.

associateDefaultSecurityGroup -> (boolean)

Replication Configuration template associate default Application Migration Service Security group.

bandwidthThrottling -> (long)

Replication Configuration template bandwidth throttling.

createPublicIP -> (boolean)

Replication Configuration template create Public IP.

dataPlaneRouting -> (string)

Replication Configuration template data plane routing.

defaultLargeStagingDiskType -> (string)

Replication Configuration template use default large Staging Disk type.

ebsEncryption -> (string)

Replication Configuration template EBS encryption.

ebsEncryptionKeyArn -> (string)

Replication Configuration template EBS encryption key ARN.

replicationConfigurationTemplateID -> (string)

Replication Configuration template ID.

replicationServerInstanceType -> (string)

Replication Configuration template server instance type.

replicationServersSecurityGroupsIDs -> (list)

Replication Configuration template server Security Groups IDs.

(string)

stagingAreaSubnetId -> (string)

Replication Configuration template Staging Area subnet ID.

stagingAreaTags -> (map)

Replication Configuration template Staging Area Tags.

key -> (string)

value -> (string)

tags -> (map)

Replication Configuration template Tags.

key -> (string)

value -> (string)

useDedicatedReplicationServer -> (boolean)

Replication Configuration template use Dedicated Replication Server.

useFipsEndpoint -> (boolean)

Replication Configuration template use Fips Endpoint.