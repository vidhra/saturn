# create-networkÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-network.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-network.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/index.html#cli-aws-managedblockchain) ]

# create-network

## Description

Creates a new blockchain network using Amazon Managed Blockchain.

Applies only to Hyperledger Fabric.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-2018-09-24/CreateNetwork)

## Synopsis

```
create-network
[--client-request-token <value>]
--name <value>
[--description <value>]
--framework <value>
--framework-version <value>
[--framework-configuration <value>]
--voting-policy <value>
--member-configuration <value>
[--tags <value>]
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

`--client-request-token` (string)

This is a unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the Amazon Web Services CLI.

`--name` (string)

The name of the network.

`--description` (string)

An optional description for the network.

`--framework` (string)

The blockchain framework that the network uses.

Possible values:

- `HYPERLEDGER_FABRIC`
- `ETHEREUM`

`--framework-version` (string)

The version of the blockchain framework that the network uses.

`--framework-configuration` (structure)

Configuration properties of the blockchain framework relevant to the network configuration.

Fabric -> (structure)

Hyperledger Fabric configuration properties for a Managed Blockchain network that uses Hyperledger Fabric.

Edition -> (string)

The edition of Amazon Managed Blockchain that the network uses. For more information, see [Amazon Managed Blockchain Pricing](http://aws.amazon.com/managed-blockchain/pricing/) .

Shorthand Syntax:

```
Fabric={Edition=string}
```

JSON Syntax:

```
{
  "Fabric": {
    "Edition": "STARTER"|"STANDARD"
  }
}
```

`--voting-policy` (structure)

The voting rules used by the network to determine if a proposal is approved.

ApprovalThresholdPolicy -> (structure)

Defines the rules for the network for voting on proposals, such as the percentage of `YES` votes required for the proposal to be approved and the duration of the proposal. The policy applies to all proposals and is specified when the network is created.

ThresholdPercentage -> (integer)

The percentage of votes among all members that must be `YES` for a proposal to be approved. For example, a `ThresholdPercentage` value of `50` indicates 50%. The `ThresholdComparator` determines the precise comparison. If a `ThresholdPercentage` value of `50` is specified on a network with 10 members, along with a `ThresholdComparator` value of `GREATER_THAN` , this indicates that 6 `YES` votes are required for the proposal to be approved.

ProposalDurationInHours -> (integer)

The duration from the time that a proposal is created until it expires. If members cast neither the required number of `YES` votes to approve the proposal nor the number of `NO` votes required to reject it before the duration expires, the proposal is `EXPIRED` and `ProposalActions` arenât carried out.

ThresholdComparator -> (string)

Determines whether the vote percentage must be greater than the `ThresholdPercentage` or must be greater than or equal to the `ThresholdPercentage` to be approved.

Shorthand Syntax:

```
ApprovalThresholdPolicy={ThresholdPercentage=integer,ProposalDurationInHours=integer,ThresholdComparator=string}
```

JSON Syntax:

```
{
  "ApprovalThresholdPolicy": {
    "ThresholdPercentage": integer,
    "ProposalDurationInHours": integer,
    "ThresholdComparator": "GREATER_THAN"|"GREATER_THAN_OR_EQUAL_TO"
  }
}
```

`--member-configuration` (structure)

Configuration properties for the first member within the network.

Name -> (string)

The name of the member.

Description -> (string)

An optional description of the member.

FrameworkConfiguration -> (structure)

Configuration properties of the blockchain framework relevant to the member.

Fabric -> (structure)

Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses Hyperledger Fabric.

AdminUsername -> (string)

The user name for the memberâs initial administrative user.

AdminPassword -> (string)

The password for the memberâs initial administrative user. The `AdminPassword` must be at least 8 characters long and no more than 32 characters. It must contain at least one uppercase letter, one lowercase letter, and one digit. It cannot have a single quotation mark (â), a double quotation marks (â), a forward slash(/), a backward slash(), @, or a space.

LogPublishingConfiguration -> (structure)

Configuration properties for logging events associated with a member of a Managed Blockchain network.

Fabric -> (structure)

Configuration properties for logging events associated with a member of a Managed Blockchain network using the Hyperledger Fabric framework.

CaLogs -> (structure)

Configuration properties for logging events associated with a memberâs Certificate Authority (CA). CA logs help you determine when a member in your account joins the network, or when new peers register with a member CA.

Cloudwatch -> (structure)

Parameters for publishing logs to Amazon CloudWatch Logs.

Enabled -> (boolean)

Indicates whether logging is enabled.

Tags -> (map)

Tags assigned to the member. Tags consist of a key and optional value.

When specifying tags during creation, you can specify multiple key-value pairs in a single request, with an overall maximum of 50 tags added to each resource.

For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide* , or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide* .

key -> (string)

value -> (string)

KmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the customer managed key in Key Management Service (KMS) to use for encryption at rest in the member. This parameter is inherited by any nodes that this member creates. For more information, see [Encryption at Rest](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide* .

Use one of the following options to specify this parameter:

- **Undefined or empty string** - By default, use an KMS key that is owned and managed by Amazon Web Services on your behalf.
- **A valid symmetric customer managed KMS key** - Use the specified KMS key in your account that you create, own, and manage. Amazon Managed Blockchain doesnât support asymmetric keys. For more information, see [Using symmetric and asymmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Key Management Service Developer Guide* . The following is an example of a KMS key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

JSON Syntax:

```
{
  "Name": "string",
  "Description": "string",
  "FrameworkConfiguration": {
    "Fabric": {
      "AdminUsername": "string",
      "AdminPassword": "string"
    }
  },
  "LogPublishingConfiguration": {
    "Fabric": {
      "CaLogs": {
        "Cloudwatch": {
          "Enabled": true|false
        }
      }
    }
  },
  "Tags": {"string": "string"
    ...},
  "KmsKeyArn": "string"
}
```

`--tags` (map)

Tags to assign to the network.

Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.

For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide* , or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide* .

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

NetworkId -> (string)

The unique identifier for the network.

MemberId -> (string)

The unique identifier for the first member within the network.