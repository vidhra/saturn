# create-access-previewÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-access-preview.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-access-preview.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [accessanalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html#cli-aws-accessanalyzer) ]

# create-access-preview

## Description

Creates an access preview that allows you to preview IAM Access Analyzer findings for your resource before deploying resource permissions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/accessanalyzer-2019-11-01/CreateAccessPreview)

## Synopsis

```
create-access-preview
--analyzer-arn <value>
--configurations <value>
[--client-token <value>]
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

`--analyzer-arn` (string)

The [ARN of the account analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the access preview. You can only create an access preview for analyzers with an `Account` type and `Active` status.

`--configurations` (map)

Access control configuration for your resource that is used to generate the access preview. The access preview includes findings for external access allowed to the resource with the proposed access control configuration. The configuration must contain exactly one element.

key -> (string)

value -> (tagged union structure)

Access control configuration structures for your resource. You specify the configuration as a type-value pair. You can specify only one type of access control configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ebsSnapshot`, `ecrRepository`, `iamRole`, `efsFileSystem`, `kmsKey`, `rdsDbClusterSnapshot`, `rdsDbSnapshot`, `secretsManagerSecret`, `s3Bucket`, `snsTopic`, `sqsQueue`, `s3ExpressDirectoryBucket`, `dynamodbStream`, `dynamodbTable`.

ebsSnapshot -> (structure)

The access control configuration is for an Amazon EBS volume snapshot.

userIds -> (list)

The IDs of the Amazon Web Services accounts that have access to the Amazon EBS volume snapshot.

- If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the `userIds` , then the access preview uses the existing shared `userIds` for the snapshot.
- If the access preview is for a new resource and you do not specify the `userIds` , then the access preview considers the snapshot without any `userIds` .
- To propose deletion of existing shared `accountIds` , you can specify an empty list for `userIds` .

(string)

groups -> (list)

The groups that have access to the Amazon EBS volume snapshot. If the value `all` is specified, then the Amazon EBS volume snapshot is public.

- If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the `groups` , then the access preview uses the existing shared `groups` for the snapshot.
- If the access preview is for a new resource and you do not specify the `groups` , then the access preview considers the snapshot without any `groups` .
- To propose deletion of existing shared `groups` , you can specify an empty list for `groups` .

(string)

kmsKeyId -> (string)

The KMS key identifier for an encrypted Amazon EBS volume snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

- If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the `kmsKeyId` , or you specify an empty string, then the access preview uses the existing `kmsKeyId` of the snapshot.
- If the access preview is for a new resource and you do not specify the `kmsKeyId` , the access preview considers the snapshot as unencrypted.

ecrRepository -> (structure)

The access control configuration is for an Amazon ECR repository.

repositoryPolicy -> (string)

The JSON repository policy text to apply to the Amazon ECR repository. For more information, see [Private repository policy examples](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html) in the *Amazon ECR User Guide* .

iamRole -> (structure)

The access control configuration is for an IAM role.

trustPolicy -> (string)

The proposed trust policy for the IAM role.

efsFileSystem -> (structure)

The access control configuration is for an Amazon EFS file system.

fileSystemPolicy -> (string)

The JSON policy definition to apply to the Amazon EFS file system. For more information on the elements that make up a file system policy, see [Amazon EFS Resource-based policies](https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-policies) .

kmsKey -> (structure)

The access control configuration is for a KMS key.

keyPolicies -> (map)

Resource policy configuration for the KMS key. The only valid value for the name of the key policy is `default` . For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default) .

key -> (string)

value -> (string)

grants -> (list)

A list of proposed grant configurations for the KMS key. If the proposed grant configuration is for an existing key, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the key.

(structure)

A proposed grant configuration for a KMS key. For more information, see [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) .

operations -> (list)

A list of operations that the grant permits.

(string)

granteePrincipal -> (string)

The principal that is given permission to perform the operations that the grant permits.

retiringPrincipal -> (string)

The principal that is given permission to retire the grant by using [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) operation.

constraints -> (structure)

Use this structure to propose allowing [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) in the grant only when the operation request includes the specified [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) .

encryptionContextEquals -> (map)

A list of key-value pairs that must match the encryption context in the [cryptographic operation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.

key -> (string)

value -> (string)

encryptionContextSubset -> (map)

A list of key-value pairs that must be included in the encryption context of the [cryptographic operation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.

key -> (string)

value -> (string)

issuingAccount -> (string)

The Amazon Web Services account under which the grant was issued. The account is used to propose KMS grants issued by accounts other than the owner of the key.

rdsDbClusterSnapshot -> (structure)

The access control configuration is for an Amazon RDS DB cluster snapshot.

attributes -> (map)

The names and values of manual DB cluster snapshot attributes. Manual DB cluster snapshot attributes are used to authorize other Amazon Web Services accounts to restore a manual DB cluster snapshot. The only valid value for `AttributeName` for the attribute map is `restore`

key -> (string)

value -> (tagged union structure)

The values for a manual Amazon RDS DB cluster snapshot attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `accountIds`.

accountIds -> (list)

The Amazon Web Services account IDs that have access to the manual Amazon RDS DB cluster snapshot. If the value `all` is specified, then the Amazon RDS DB cluster snapshot is public and can be copied or restored by all Amazon Web Services accounts.

- If the configuration is for an existing Amazon RDS DB cluster snapshot and you do not specify the `accountIds` in `RdsDbClusterSnapshotAttributeValue` , then the access preview uses the existing shared `accountIds` for the snapshot.
- If the access preview is for a new resource and you do not specify the specify the `accountIds` in `RdsDbClusterSnapshotAttributeValue` , then the access preview considers the snapshot without any attributes.
- To propose deletion of existing shared `accountIds` , you can specify an empty list for `accountIds` in the `RdsDbClusterSnapshotAttributeValue` .

(string)

kmsKeyId -> (string)

The KMS key identifier for an encrypted Amazon RDS DB cluster snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

- If the configuration is for an existing Amazon RDS DB cluster snapshot and you do not specify the `kmsKeyId` , or you specify an empty string, then the access preview uses the existing `kmsKeyId` of the snapshot.
- If the access preview is for a new resource and you do not specify the specify the `kmsKeyId` , then the access preview considers the snapshot as unencrypted.

rdsDbSnapshot -> (structure)

The access control configuration is for an Amazon RDS DB snapshot.

attributes -> (map)

The names and values of manual DB snapshot attributes. Manual DB snapshot attributes are used to authorize other Amazon Web Services accounts to restore a manual DB snapshot. The only valid value for `attributeName` for the attribute map is restore.

key -> (string)

value -> (tagged union structure)

The name and values of a manual Amazon RDS DB snapshot attribute. Manual DB snapshot attributes are used to authorize other Amazon Web Services accounts to restore a manual DB snapshot.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `accountIds`.

accountIds -> (list)

The Amazon Web Services account IDs that have access to the manual Amazon RDS DB snapshot. If the value `all` is specified, then the Amazon RDS DB snapshot is public and can be copied or restored by all Amazon Web Services accounts.

- If the configuration is for an existing Amazon RDS DB snapshot and you do not specify the `accountIds` in `RdsDbSnapshotAttributeValue` , then the access preview uses the existing shared `accountIds` for the snapshot.
- If the access preview is for a new resource and you do not specify the specify the `accountIds` in `RdsDbSnapshotAttributeValue` , then the access preview considers the snapshot without any attributes.
- To propose deletion of an existing shared `accountIds` , you can specify an empty list for `accountIds` in the `RdsDbSnapshotAttributeValue` .

(string)

kmsKeyId -> (string)

The KMS key identifier for an encrypted Amazon RDS DB snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

- If the configuration is for an existing Amazon RDS DB snapshot and you do not specify the `kmsKeyId` , or you specify an empty string, then the access preview uses the existing `kmsKeyId` of the snapshot.
- If the access preview is for a new resource and you do not specify the specify the `kmsKeyId` , then the access preview considers the snapshot as unencrypted.

secretsManagerSecret -> (structure)

The access control configuration is for a Secrets Manager secret.

kmsKeyId -> (string)

The proposed ARN, key ID, or alias of the KMS key.

secretPolicy -> (string)

The proposed resource policy defining who can access or manage the secret.

s3Bucket -> (structure)

The access control configuration is for an Amazon S3 bucket.

bucketPolicy -> (string)

The proposed bucket policy for the Amazon S3 bucket.

bucketAclGrants -> (list)

The proposed list of ACL grants for the Amazon S3 bucket. You can propose up to 100 ACL grants per bucket. If the proposed grant configuration is for an existing bucket, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the bucket.

(structure)

A proposed access control list grant configuration for an Amazon S3 bucket. For more information, see [How to Specify an ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#setting-acls) .

permission -> (string)

The permissions being granted.

grantee -> (tagged union structure)

The grantee to whom youâre assigning access rights.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `id`, `uri`.

id -> (string)

The value specified is the canonical user ID of an Amazon Web Services account.

uri -> (string)

Used for granting permissions to a predefined group.

bucketPublicAccessBlock -> (structure)

The proposed block public access configuration for the Amazon S3 bucket.

ignorePublicAcls -> (boolean)

Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket.

restrictPublicBuckets -> (boolean)

Specifies whether Amazon S3 should restrict public bucket policies for this bucket.

accessPoints -> (map)

The configuration of Amazon S3 access points or multi-region access points for the bucket. You can propose up to 10 new access points per bucket.

key -> (string)

value -> (structure)

The configuration for an Amazon S3 access point or multi-region access point for the bucket. You can propose up to 10 access points or multi-region access points per bucket. If the proposed Amazon S3 access point configuration is for an existing bucket, the access preview uses the proposed access point configuration in place of the existing access points. To propose an access point without a policy, you can provide an empty string as the access point policy. For more information, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html) . For more information about access point policy limits, see [Access points restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points-restrictions-limitations.html) .

accessPointPolicy -> (string)

The access point or multi-region access point policy.

publicAccessBlock -> (structure)

The proposed `S3PublicAccessBlock` configuration to apply to this Amazon S3 access point or multi-region access point.

ignorePublicAcls -> (boolean)

Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket.

restrictPublicBuckets -> (boolean)

Specifies whether Amazon S3 should restrict public bucket policies for this bucket.

networkOrigin -> (tagged union structure)

The proposed `Internet` and `VpcConfiguration` to apply to this Amazon S3 access point. `VpcConfiguration` does not apply to multi-region access points. If the access preview is for a new resource and neither is specified, the access preview uses `Internet` for the network origin. If the access preview is for an existing resource and neither is specified, the access preview uses the existing network origin.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `vpcConfiguration`, `internetConfiguration`.

vpcConfiguration -> (structure)

The proposed virtual private cloud (VPC) configuration for the Amazon S3 access point. VPC configuration does not apply to multi-region access points. For more information, see [VpcConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VpcConfiguration.html) .

vpcId -> (string)

If this field is specified, this access point will only allow connections from the specified VPC ID.

internetConfiguration -> (structure)

The configuration for the Amazon S3 access point or multi-region access point with an `Internet` origin.

snsTopic -> (structure)

The access control configuration is for an Amazon SNS topic

topicPolicy -> (string)

The JSON policy text that defines who can access an Amazon SNS topic. For more information, see [Example cases for Amazon SNS access control](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html) in the *Amazon SNS Developer Guide* .

sqsQueue -> (structure)

The access control configuration is for an Amazon SQS queue.

queuePolicy -> (string)

The proposed resource policy for the Amazon SQS queue.

s3ExpressDirectoryBucket -> (structure)

The access control configuration is for an Amazon S3 directory bucket.

bucketPolicy -> (string)

The proposed bucket policy for the Amazon S3 directory bucket.

accessPoints -> (map)

The proposed access points for the Amazon S3 directory bucket.

key -> (string)

value -> (structure)

Proposed configuration for an access point attached to an Amazon S3 directory bucket. You can propose up to 10 access points per bucket. If the proposed access point configuration is for an existing Amazon S3 directory bucket, the access preview uses the proposed access point configuration in place of the existing access points. To propose an access point without a policy, you can provide an empty string as the access point policy. For more information about access points for Amazon S3 directory buckets, see [Managing access to directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the Amazon Simple Storage Service User Guide.

accessPointPolicy -> (string)

The proposed access point policy for an Amazon S3 directory bucket access point.

networkOrigin -> (tagged union structure)

The proposed `InternetConfiguration` or `VpcConfiguration` to apply to the Amazon S3 access point. You can make the access point accessible from the internet, or you can specify that all requests made through that access point must originate from a specific virtual private cloud (VPC). You can specify only one type of network configuration. For more information, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `vpcConfiguration`, `internetConfiguration`.

vpcConfiguration -> (structure)

The proposed virtual private cloud (VPC) configuration for the Amazon S3 access point. VPC configuration does not apply to multi-region access points. For more information, see [VpcConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VpcConfiguration.html) .

vpcId -> (string)

If this field is specified, this access point will only allow connections from the specified VPC ID.

internetConfiguration -> (structure)

The configuration for the Amazon S3 access point or multi-region access point with an `Internet` origin.

dynamodbStream -> (structure)

The access control configuration is for a DynamoDB stream.

streamPolicy -> (string)

The proposed resource policy defining who can access or manage the DynamoDB stream.

dynamodbTable -> (structure)

The access control configuration is for a DynamoDB table or index.

tablePolicy -> (string)

The proposed resource policy defining who can access or manage the DynamoDB table.

JSON Syntax:

```
{"string": {
      "ebsSnapshot": {
        "userIds": ["string", ...],
        "groups": ["string", ...],
        "kmsKeyId": "string"
      },
      "ecrRepository": {
        "repositoryPolicy": "string"
      },
      "iamRole": {
        "trustPolicy": "string"
      },
      "efsFileSystem": {
        "fileSystemPolicy": "string"
      },
      "kmsKey": {
        "keyPolicies": {"string": "string"
          ...},
        "grants": [
          {
            "operations": ["CreateGrant"|"Decrypt"|"DescribeKey"|"Encrypt"|"GenerateDataKey"|"GenerateDataKeyPair"|"GenerateDataKeyPairWithoutPlaintext"|"GenerateDataKeyWithoutPlaintext"|"GetPublicKey"|"ReEncryptFrom"|"ReEncryptTo"|"RetireGrant"|"Sign"|"Verify", ...],
            "granteePrincipal": "string",
            "retiringPrincipal": "string",
            "constraints": {
              "encryptionContextEquals": {"string": "string"
                ...},
              "encryptionContextSubset": {"string": "string"
                ...}
            },
            "issuingAccount": "string"
          }
          ...
        ]
      },
      "rdsDbClusterSnapshot": {
        "attributes": {"string": {
              "accountIds": ["string", ...]
            }
          ...},
        "kmsKeyId": "string"
      },
      "rdsDbSnapshot": {
        "attributes": {"string": {
              "accountIds": ["string", ...]
            }
          ...},
        "kmsKeyId": "string"
      },
      "secretsManagerSecret": {
        "kmsKeyId": "string",
        "secretPolicy": "string"
      },
      "s3Bucket": {
        "bucketPolicy": "string",
        "bucketAclGrants": [
          {
            "permission": "READ"|"WRITE"|"READ_ACP"|"WRITE_ACP"|"FULL_CONTROL",
            "grantee": {
              "id": "string",
              "uri": "string"
            }
          }
          ...
        ],
        "bucketPublicAccessBlock": {
          "ignorePublicAcls": true|false,
          "restrictPublicBuckets": true|false
        },
        "accessPoints": {"string": {
              "accessPointPolicy": "string",
              "publicAccessBlock": {
                "ignorePublicAcls": true|false,
                "restrictPublicBuckets": true|false
              },
              "networkOrigin": {
                "vpcConfiguration": {
                  "vpcId": "string"
                },
                "internetConfiguration": {

                }
              }
            }
          ...}
      },
      "snsTopic": {
        "topicPolicy": "string"
      },
      "sqsQueue": {
        "queuePolicy": "string"
      },
      "s3ExpressDirectoryBucket": {
        "bucketPolicy": "string",
        "accessPoints": {"string": {
              "accessPointPolicy": "string",
              "networkOrigin": {
                "vpcConfiguration": {
                  "vpcId": "string"
                },
                "internetConfiguration": {

                }
              }
            }
          ...}
      },
      "dynamodbStream": {
        "streamPolicy": "string"
      },
      "dynamodbTable": {
        "tablePolicy": "string"
      }
    }
  ...}
```

`--client-token` (string)

A client token.

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

**To create an access preview that allows you to preview IAM Access Analyzer findings for your resource before deploying resource permissions**

The following `create-access-preview` example creates an access preview that allows you to preview IAM Access Analyzer findings for your resource before deploying resource permissions in your AWS account.

```
aws accessanalyzer create-access-preview \
    --analyzer-arn arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account \
    --configurations file://myfile.json
```

Contents of `myfile.json`:

```
{
    "arn:aws:s3:::amzn-s3-demo-bucket": {
        "s3Bucket": {
            "bucketPolicy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":[\"arn:aws:iam::111122223333:root\"]},\"Action\":[\"s3:PutObject\",\"s3:PutObjectAcl\"],\"Resource\":\"arn:aws:s3:::amzn-s3-demo-bucket/*\"}]}",
            "bucketPublicAccessBlock": {
                "ignorePublicAcls": true,
                "restrictPublicBuckets": true
            },
            "bucketAclGrants": [
                {
                    "grantee": {
                        "id": "79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be"
                    },
                    "permission": "READ"
                }
            ]
        }
    }
}
```

Output:

```
{
    "id": "3c65eb13-6ef9-4629-8919-a32043619e6b"
}
```

For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html) in the *AWS IAM User Guide*.

## Output

id -> (string)

The unique ID for the access preview.