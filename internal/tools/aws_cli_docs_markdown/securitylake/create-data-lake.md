# create-data-lakeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securitylake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/index.html#cli-aws-securitylake) ]

# create-data-lake

## Description

Initializes an Amazon Security Lake instance with the provided (or default) configuration. You can enable Security Lake in Amazon Web Services Regions with customized settings before enabling log collection in Regions. To specify particular Regions, configure these Regions using the `configurations` parameter. If you have already enabled Security Lake in a Region when you call this command, the command will update the Region if you provide new configuration parameters. If you have not already enabled Security Lake in the Region when you call this API, it will set up the data lake in the Region with the specified configurations.

When you enable Security Lake, it starts ingesting security data after the `CreateAwsLogSource` call and after you create subscribers using the `CreateSubscriber` API. This includes ingesting security data from sources, storing data, and making data accessible to subscribers. Security Lake also enables all the existing settings and resources that it stores or maintains for your Amazon Web Services account in the current Region, including security log and event data. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securitylake-2018-05-10/CreateDataLake)

## Synopsis

```
create-data-lake
--configurations <value>
--meta-store-manager-role-arn <value>
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

`--configurations` (list)

Specify the Region or Regions that will contribute data to the rollup region.

(structure)

Provides details of Amazon Security Lake object.

encryptionConfiguration -> (structure)

Provides encryption details of Amazon Security Lake object.

kmsKeyId -> (string)

The identifier of KMS encryption key used by Amazon Security Lake to encrypt the Security Lake object.

lifecycleConfiguration -> (structure)

Provides lifecycle details of Amazon Security Lake object.

expiration -> (structure)

Provides data expiration details of Amazon Security Lake object.

days -> (integer)

Number of days before data expires in the Amazon Security Lake object.

transitions -> (list)

Provides data storage transition details of Amazon Security Lake object.

(structure)

Provide transition lifecycle details of Amazon Security Lake object.

days -> (integer)

Number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.

storageClass -> (string)

The range of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads.

region -> (string)

The Amazon Web Services Regions where Security Lake is automatically enabled.

replicationConfiguration -> (structure)

Provides replication details of Amazon Security Lake object.

regions -> (list)

Specifies one or more centralized rollup Regions. The Amazon Web Services Region specified in the `region` parameter of the ` `CreateDataLake` [https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake).html`__ or ` `UpdateDataLake` [https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake).html`__ operations contributes data to the rollup Region or Regions specified in this parameter.

Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. S3 buckets that are configured for object replication can be owned by the same Amazon Web Services account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different Regions or within the same Region as the source bucket.

(string)

roleArn -> (string)

Replication settings for the Amazon S3 buckets. This parameter uses the Identity and Access Management (IAM) role you created that is managed by Security Lake, to ensure the replication setting is correct.

JSON Syntax:

```
[
  {
    "encryptionConfiguration": {
      "kmsKeyId": "string"
    },
    "lifecycleConfiguration": {
      "expiration": {
        "days": integer
      },
      "transitions": [
        {
          "days": integer,
          "storageClass": "string"
        }
        ...
      ]
    },
    "region": "string",
    "replicationConfiguration": {
      "regions": ["string", ...],
      "roleArn": "string"
    }
  }
  ...
]
```

`--meta-store-manager-role-arn` (string)

The Amazon Resource Name (ARN) used to create and update the Glue table. This table contains partitions generated by the ingestion and normalization of Amazon Web Services log sources and custom sources.

`--tags` (list)

An array of objects, one for each tag to associate with the data lake configuration. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.

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

**Example 1: To configure your data lake in multiple Regions**

The following `create-data-lake` example enables Amazon Security Lake in multiple AWS Regions and configures your data lake.

```
aws securitylake create-data-lake \
    --configurations '[{"encryptionConfiguration": {"kmsKeyId":"S3_MANAGED_KEY"},"region":"us-east-1","lifecycleConfiguration": {"expiration":{"days":365},"transitions":[{"days":60,"storageClass":"ONEZONE_IA"}]}}, {"encryptionConfiguration": {"kmsKeyId":"S3_MANAGED_KEY"},"region":"us-east-2","lifecycleConfiguration": {"expiration":{"days":365},"transitions":[{"days":60,"storageClass":"ONEZONE_IA"}]}}]' \
    --meta-store-manager-role-arn "arn:aws:iam:us-east-1:123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager"
```

Output:

```
{
    "dataLakes": [
        {
            "createStatus": "COMPLETED",
            "dataLakeArn": "arn:aws:securitylake:us-east-1:522481757177:data-lake/default",
            "encryptionConfiguration": {
                "kmsKeyId": "S3_MANAGED_KEY"
            },
            "lifecycleConfiguration": {
                "expiration": {
                    "days": 365
                },
                "transitions": [
                    {
                        "days": 60,
                        "storageClass": "ONEZONE_IA"
                    }
                ]
            },
            "region": "us-east-1",
            "replicationConfiguration": {
                "regions": [
                    "ap-northeast-3"
                ],
                "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default"
            },
            "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-1-gnevt6s8z7bzby8oi3uiaysbr8v2ml",
            "updateStatus": {
                "exception": {},
                "requestId": "f20a6450-d24a-4f87-a6be-1d4c075a59c2",
                "status": "INITIALIZED"
            }
        },
        {
            "createStatus": "COMPLETED",
            "dataLakeArn": "arn:aws:securitylake:us-east-2:522481757177:data-lake/default",
            "encryptionConfiguration": {
                "kmsKeyId": "S3_MANAGED_KEY"
            },
            "lifecycleConfiguration": {
                "expiration": {
                    "days": 365
                },
                "transitions": [
                    {
                        "days": 60,
                        "storageClass": "ONEZONE_IA"
                    }
                ]
            },
            "region": "us-east-2",
            "replicationConfiguration": {
                "regions": [
                    "ap-northeast-3"
                ],
                "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default"
            },
            "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-2-cehuifzl5rwmhm6m62h7zhvtseogr9",
            "updateStatus": {
                "exception": {},
                "requestId": "f20a6450-d24a-4f87-a6be-1d4c075a59c2",
                "status": "INITIALIZED"
            }
        }
    ]
}
```

For more information, see [Getting started with Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html) in the *Amazon Security Lake User Guide*.

**Example 2: To configure your data lake in a single Region**

The following `create-data-lake` example enables Amazon Security Lake in a single AWS Region and configures your data lake.

```
aws securitylake create-data-lake \
    --configurations '[{"encryptionConfiguration": {"kmsKeyId":"1234abcd-12ab-34cd-56ef-1234567890ab"},"region":"us-east-2","lifecycleConfiguration": {"expiration":{"days":500},"transitions":[{"days":30,"storageClass":"GLACIER"}]}}]' \
    --meta-store-manager-role-arn "arn:aws:iam:us-east-1:123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager"
```

Output:

```
{
    "dataLakes": [
        {
            "createStatus": "COMPLETED",
            "dataLakeArn": "arn:aws:securitylake:us-east-2:522481757177:data-lake/default",
            "encryptionConfiguration": {
                "kmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
            },
            "lifecycleConfiguration": {
                "expiration": {
                    "days": 500
                },
                "transitions": [
                    {
                        "days": 30,
                        "storageClass": "GLACIER"
                    }
                ]
            },
            "region": "us-east-2",
            "replicationConfiguration": {
                "regions": [
                    "ap-northeast-3"
                ],
                "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default"
            },
            "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-2-cehuifzl5rwmhm6m62h7zhvtseogr9",
            "updateStatus": {
                "exception": {},
                "requestId": "77702a53-dcbf-493e-b8ef-518e362f3003",
                "status": "INITIALIZED"
            }
        }
    ]
}
```

For more information, see [Getting started with Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html) in the *Amazon Security Lake User Guide*.

## Output

dataLakes -> (list)

The created Security Lake configuration object.

(structure)

Provides details of Amazon Security Lake object.

createStatus -> (string)

Retrieves the status of the `CreateDatalake` API call for an account in Amazon Security Lake.

dataLakeArn -> (string)

The Amazon Resource Name (ARN) created by you to provide to the subscriber. For more information about ARNs and how to use them in policies, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html) .

encryptionConfiguration -> (structure)

Provides encryption details of Amazon Security Lake object.

kmsKeyId -> (string)

The identifier of KMS encryption key used by Amazon Security Lake to encrypt the Security Lake object.

lifecycleConfiguration -> (structure)

Provides lifecycle details of Amazon Security Lake object.

expiration -> (structure)

Provides data expiration details of Amazon Security Lake object.

days -> (integer)

Number of days before data expires in the Amazon Security Lake object.

transitions -> (list)

Provides data storage transition details of Amazon Security Lake object.

(structure)

Provide transition lifecycle details of Amazon Security Lake object.

days -> (integer)

Number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.

storageClass -> (string)

The range of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads.

region -> (string)

The Amazon Web Services Regions where Security Lake is enabled.

replicationConfiguration -> (structure)

Provides replication details of Amazon Security Lake object.

regions -> (list)

Specifies one or more centralized rollup Regions. The Amazon Web Services Region specified in the `region` parameter of the ` `CreateDataLake` [https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake).html`__ or ` `UpdateDataLake` [https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake).html`__ operations contributes data to the rollup Region or Regions specified in this parameter.

Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. S3 buckets that are configured for object replication can be owned by the same Amazon Web Services account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different Regions or within the same Region as the source bucket.

(string)

roleArn -> (string)

Replication settings for the Amazon S3 buckets. This parameter uses the Identity and Access Management (IAM) role you created that is managed by Security Lake, to ensure the replication setting is correct.

s3BucketArn -> (string)

The ARN for the Amazon Security Lake Amazon S3 bucket.

updateStatus -> (structure)

The status of the last `UpdateDataLake` or `DeleteDataLake` API request.

exception -> (structure)

The details of the last `UpdateDataLake` or `DeleteDataLake` API request which failed.

code -> (string)

The reason code for the exception of the last `UpdateDataLake` or `DeleteDataLake` API request.

reason -> (string)

The reason for the exception of the last `UpdateDataLake` or `DeleteDataLake` API request.

requestId -> (string)

The unique ID for the last `UpdateDataLake` or `DeleteDataLake` API request.

status -> (string)

The status of the last `UpdateDataLake` or `DeleteDataLake` API request that was requested.