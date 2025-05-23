# create-subscriberÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securitylake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/index.html#cli-aws-securitylake) ]

# create-subscriber

## Description

Creates a subscriber for accounts that are already enabled in Amazon Security Lake. You can create a subscriber with access to data in the current Amazon Web Services Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securitylake-2018-05-10/CreateSubscriber)

## Synopsis

```
create-subscriber
[--access-types <value>]
--sources <value>
[--subscriber-description <value>]
--subscriber-identity <value>
--subscriber-name <value>
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

`--access-types` (list)

The Amazon S3 or Lake Formation access type.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  LAKEFORMATION
  S3
```

`--sources` (list)

The supported Amazon Web Services services from which logs and events are collected. Security Lake supports log and event collection for natively supported Amazon Web Services services.

(tagged union structure)

The supported source types from which logs and events are collected in Amazon Security Lake. For a list of supported Amazon Web Services services, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `awsLogSource`, `customLogSource`.

awsLogSource -> (structure)

Amazon Security Lake supports log and event collection for natively supported Amazon Web Services services. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) .

sourceName -> (string)

The name for a Amazon Web Services source. This must be a Regionally unique value.

sourceVersion -> (string)

The version for a Amazon Web Services source. This must be a Regionally unique value.

customLogSource -> (structure)

Amazon Security Lake supports custom source types. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html) .

attributes -> (structure)

The attributes of a third-party custom source.

crawlerArn -> (string)

The ARN of the Glue crawler.

databaseArn -> (string)

The ARN of the Glue database where results are written, such as: `arn:aws:daylight:us-east-1::database/sometable/*` .

tableArn -> (string)

The ARN of the Glue table.

provider -> (structure)

The details of the log provider for a third-party custom source.

location -> (string)

The location of the partition in the Amazon S3 bucket for Security Lake.

roleArn -> (string)

The ARN of the IAM role to be used by the entity putting logs into your custom source partition. Security Lake will apply the correct access policies to this role, but you must first manually create the trust policy for this role. The IAM role name must start with the text âSecurity Lakeâ. The IAM role must trust the `logProviderAccountId` to assume the role.

sourceName -> (string)

The name for a third-party custom source. This must be a Regionally unique value.

sourceVersion -> (string)

The version for a third-party custom source. This must be a Regionally unique value.

Shorthand Syntax:

```
awsLogSource={sourceName=string,sourceVersion=string},customLogSource={attributes={crawlerArn=string,databaseArn=string,tableArn=string},provider={location=string,roleArn=string},sourceName=string,sourceVersion=string} ...
```

JSON Syntax:

```
[
  {
    "awsLogSource": {
      "sourceName": "ROUTE53"|"VPC_FLOW"|"SH_FINDINGS"|"CLOUD_TRAIL_MGMT"|"LAMBDA_EXECUTION"|"S3_DATA"|"EKS_AUDIT"|"WAF",
      "sourceVersion": "string"
    },
    "customLogSource": {
      "attributes": {
        "crawlerArn": "string",
        "databaseArn": "string",
        "tableArn": "string"
      },
      "provider": {
        "location": "string",
        "roleArn": "string"
      },
      "sourceName": "string",
      "sourceVersion": "string"
    }
  }
  ...
]
```

`--subscriber-description` (string)

The description for your subscriber account in Security Lake.

`--subscriber-identity` (structure)

The Amazon Web Services identity used to access your data.

externalId -> (string)

The external ID used to establish trust relationship with the Amazon Web Services identity.

principal -> (string)

The Amazon Web Services identity principal.

Shorthand Syntax:

```
externalId=string,principal=string
```

JSON Syntax:

```
{
  "externalId": "string",
  "principal": "string"
}
```

`--subscriber-name` (string)

The name of your Security Lake subscriber account.

`--tags` (list)

An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.

(structure)

A *tag* is a label that you can define and associate with Amazon Web Services resources, including certain types of Amazon Security Lake resources. Tags can help you identify, categorize, and manage resources in different ways, such as by owner, environment, or other criteria. You can associate tags with the following types of Security Lake resources: subscribers, and the data lake configuration for your Amazon Web Services account in individual Amazon Web Services Regions.

A resource can have up to 50 tags. Each tag consists of a required *tag key* and an associated *tag value* . A *tag key* is a general label that acts as a category for a more specific tag value. Each tag key must be unique and it can have only one tag value. A *tag value* acts as a descriptor for a tag key. Tag keys and values are case sensitive. They can contain letters, numbers, spaces, or the following symbols: _ . : / = + @ -

For more information, see [Tagging Amazon Security Lake resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tagging-resources.html) in the *Amazon Security Lake User Guide* .

key -> (string)

The name of the tag. This is a general label that acts as a category for a more specific tag value (`value` ).

value -> (string)

The value thatâs associated with the specified tag key (`key` ). This value acts as a descriptor for the tag key. A tag value cannot be null, but it can be an empty string.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To create a subscriber with data access**

The following `create-subscriber` example creates a subscriber in Security Lake with access to data in the current AWS Region for the specified subscriber identity for an AWS source.

```
aws securitylake create-subscriber \
    --access-types "S3" \
    --sources '[{"awsLogSource": {"sourceName": "VPC_FLOW","sourceVersion": "2.0"}}]' \
    --subscriber-name 'opensearch-s3' \
    --subscriber-identity '{"principal": "029189416600","externalId": "123456789012"}'
```

Output:

```
{
    "subscriber": {
        "accessTypes": [
            "S3"
        ],
        "createdAt": "2024-07-17T19:08:26.787000+00:00",
        "roleArn": "arn:aws:iam::773172568199:role/AmazonSecurityLake-896f218b-cfba-40be-a255-8b49a65d0407",
        "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-1-um632ufwpvxkyz0bc5hkb64atycnf3",
        "sources": [
            {
                "awsLogSource": {
                    "sourceName": "VPC_FLOW",
                    "sourceVersion": "2.0"
                }
            }
        ],
        "subscriberArn": "arn:aws:securitylake:us-east-1:773172568199:subscriber/896f218b-cfba-40be-a255-8b49a65d0407",
        "subscriberId": "896f218b-cfba-40be-a255-8b49a65d0407",
        "subscriberIdentity": {
            "externalId": "123456789012",
            "principal": "029189416600"
        },
        "subscriberName": "opensearch-s3",
        "subscriberStatus": "ACTIVE",
        "updatedAt": "2024-07-17T19:08:27.133000+00:00"
    }
}
```

For more information, see [Creating a subscriber with data access](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-data-access.html#create-subscriber-data-access) in the *Amazon Security Lake User Guide*.

**Example 2: To create a subscriber with query access**

The following `create-subscriber` example creates a subscriber in Security Lake with query access in the current AWS Region for the specified subscriber identity.

```
aws securitylake create-subscriber \
    --access-types "LAKEFORMATION" \
    --sources '[{"awsLogSource": {"sourceName": "VPC_FLOW","sourceVersion": "2.0"}}]' \
    --subscriber-name 'opensearch-s3' \
    --subscriber-identity '{"principal": "029189416600","externalId": "123456789012"}'
```

Output:

```
{
    "subscriber": {
        "accessTypes": [
            "LAKEFORMATION"
        ],
        "createdAt": "2024-07-18T01:05:55.853000+00:00",
        "resourceShareArn": "arn:aws:ram:us-east-1:123456789012:resource-share/8c31da49-c224-4f1e-bb12-37ab756d6d8a",
        "resourceShareName": "LakeFormation-V2-NAMENAMENA-123456789012",
        "sources": [
            {
                "awsLogSource": {
                    "sourceName": "VPC_FLOW",
                    "sourceVersion": "2.0"
                }
            }
        ],
        "subscriberArn": "arn:aws:securitylake:us-east-1:123456789012:subscriber/e762aabb-ce3d-4585-beab-63474597845d",
        "subscriberId": "e762aabb-ce3d-4585-beab-63474597845d",
        "subscriberIdentity": {
            "externalId": "123456789012",
            "principal": "029189416600"
        },
        "subscriberName": "opensearch-s3",
        "subscriberStatus": "ACTIVE",
        "updatedAt": "2024-07-18T01:05:58.393000+00:00"
    }
}
```

For more information, see [Creating a subscriber with query access](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-access.html#create-query-subscriber-procedures) in the *Amazon Security Lake User Guide*.

## Output

subscriber -> (structure)

Retrieve information about the subscriber created using the `CreateSubscriber` API.

accessTypes -> (list)

You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.

Subscribers can consume data by directly querying Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as `LAKEFORMATION` .

(string)

createdAt -> (timestamp)

The date and time when the subscriber was created.

resourceShareArn -> (string)

The Amazon Resource Name (ARN) which uniquely defines the Amazon Web Services RAM resource share. Before accepting the RAM resource share invitation, you can view details related to the RAM resource share.

This field is available only for Lake Formation subscribers created after March 8, 2023.

resourceShareName -> (string)

The name of the resource share.

roleArn -> (string)

The Amazon Resource Name (ARN) specifying the role of the subscriber.

s3BucketArn -> (string)

The ARN for the Amazon S3 bucket.

sources -> (list)

Amazon Security Lake supports log and event collection for natively supported Amazon Web Services services. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/source-management.html) .

(tagged union structure)

The supported source types from which logs and events are collected in Amazon Security Lake. For a list of supported Amazon Web Services services, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `awsLogSource`, `customLogSource`.

awsLogSource -> (structure)

Amazon Security Lake supports log and event collection for natively supported Amazon Web Services services. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) .

sourceName -> (string)

The name for a Amazon Web Services source. This must be a Regionally unique value.

sourceVersion -> (string)

The version for a Amazon Web Services source. This must be a Regionally unique value.

customLogSource -> (structure)

Amazon Security Lake supports custom source types. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html) .

attributes -> (structure)

The attributes of a third-party custom source.

crawlerArn -> (string)

The ARN of the Glue crawler.

databaseArn -> (string)

The ARN of the Glue database where results are written, such as: `arn:aws:daylight:us-east-1::database/sometable/*` .

tableArn -> (string)

The ARN of the Glue table.

provider -> (structure)

The details of the log provider for a third-party custom source.

location -> (string)

The location of the partition in the Amazon S3 bucket for Security Lake.

roleArn -> (string)

The ARN of the IAM role to be used by the entity putting logs into your custom source partition. Security Lake will apply the correct access policies to this role, but you must first manually create the trust policy for this role. The IAM role name must start with the text âSecurity Lakeâ. The IAM role must trust the `logProviderAccountId` to assume the role.

sourceName -> (string)

The name for a third-party custom source. This must be a Regionally unique value.

sourceVersion -> (string)

The version for a third-party custom source. This must be a Regionally unique value.

subscriberArn -> (string)

The subscriber ARN of the Amazon Security Lake subscriber account.

subscriberDescription -> (string)

The subscriber descriptions for a subscriber account. The description for a subscriber includes `subscriberName` , `accountID` , `externalID` , and `subscriberId` .

subscriberEndpoint -> (string)

The subscriber endpoint to which exception messages are posted.

subscriberId -> (string)

The subscriber ID of the Amazon Security Lake subscriber account.

subscriberIdentity -> (structure)

The Amazon Web Services identity used to access your data.

externalId -> (string)

The external ID used to establish trust relationship with the Amazon Web Services identity.

principal -> (string)

The Amazon Web Services identity principal.

subscriberName -> (string)

The name of your Amazon Security Lake subscriber account.

subscriberStatus -> (string)

The subscriber status of the Amazon Security Lake subscriber account.

updatedAt -> (timestamp)

The date and time when the subscriber was last updated.