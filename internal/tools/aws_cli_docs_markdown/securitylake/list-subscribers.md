# list-subscribersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-subscribers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-subscribers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securitylake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/index.html#cli-aws-securitylake) ]

# list-subscribers

## Description

Lists all subscribers for the specific Amazon Security Lake account ID. You can retrieve a list of subscriptions associated with a specific organization or Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securitylake-2018-05-10/ListSubscribers)

`list-subscribers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `subscribers`

## Synopsis

```
list-subscribers
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

**To retrieve the Amazon Security Lake subscribers**

The following `list-subscribers` example lists all the Amazon Security Lake subscribers in a specific account.

```
aws securitylake list-subscribers
```

Output:

```
{
    "subscribers": [
        {
            "accessTypes": [
                "S3"
            ],
            "createdAt": "2024-06-04T15:02:28.921000+00:00",
            "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-E1WG1ZNPRXT0D4",
            "s3BucketArn": "amzn-s3-demo-bucket--usw2-az1--x-s3",
            "sources": [
                {
                    "awsLogSource": {
                        "sourceName": "CLOUD_TRAIL_MGMT",
                        "sourceVersion": "2.0"
                    }
                },
                {
                    "awsLogSource": {
                        "sourceName": "LAMBDA_EXECUTION",
                        "sourceVersion": "1.0"
                    }
                },
                {
                    "customLogSource": {
                        "attributes": {
                            "crawlerArn": "arn:aws:glue:eu-west-2:123456789012:crawler/E1WG1ZNPRXT0D4",
                            "databaseArn": "arn:aws:glue:eu-west-2:123456789012:database/E1WG1ZNPRXT0D4",
                            "tableArn": "arn:aws:glue:eu-west-2:123456789012:table/E1WG1ZNPRXT0D4"
                        },
                        "provider": {
                            "location": "amzn-s3-demo-bucket--usw2-az1--x-s3",
                            "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-E1WG1ZNPRXT0D4"
                        },
                        "sourceName": "testCustom2"
                    }
                }
            ],
            "subscriberArn": "arn:aws:securitylake:eu-west-2:123456789012:subscriber/E1WG1ZNPRXT0D4",
            "subscriberEndpoint": "arn:aws:sqs:eu-west-2:123456789012:AmazonSecurityLake-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111-Main-Queue",
            "subscriberId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "subscriberIdentity": {
                "externalId": "ext123456789012",
                "principal": "123456789012"
            },
            "subscriberName": "Test",
            "subscriberStatus": "ACTIVE",
            "updatedAt": "2024-06-04T15:02:35.617000+00:00"
        }
    ]
}
```

For more information, see [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html) in the *Amazon Security Lake User Guide*.

## Output

nextToken -> (string)

If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.

subscribers -> (list)

The subscribers available for the specified Security Lake account ID.

(structure)

Provides details about the Amazon Security Lake account subscription. Subscribers are notified of new objects for a source as the data is written to your Amazon S3 bucket for Security Lake.

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