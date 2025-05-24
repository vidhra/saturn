# associate-kms-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/associate-kms-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/associate-kms-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# associate-kms-key

## Description

Associates the specified KMS key with either one log group in the account, or with all stored CloudWatch Logs query insights results in the account.

When you use `AssociateKmsKey` , you specify either the `logGroupName` parameter or the `resourceIdentifier` parameter. You canât specify both of those parameters in the same operation.

- Specify the `logGroupName` parameter to cause log events ingested into that log group to be encrypted with that key. Only the log events ingested after the key is associated are encrypted with that key. Associating a KMS key with a log group overrides any existing associations between the log group and a KMS key. After a KMS key is associated with a log group, all newly ingested data for the log group is encrypted using the KMS key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs. This enables CloudWatch Logs to decrypt this data whenever it is requested. Associating a key with a log group does not cause the results of queries of that log group to be encrypted with that key. To have query results encrypted with a KMS key, you must use an `AssociateKmsKey` operation with the `resourceIdentifier` parameter that specifies a `query-result` resource.
- Specify the `resourceIdentifier` parameter with a `query-result` resource, to use that key to encrypt the stored results of all future [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html) operations in the account. The response from a [GetQueryResults](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html) operation will still return the query results in plain text. Even if you have not associated a key with your query results, the query results are encrypted when stored, using the default CloudWatch Logs method. If you run a query from a monitoring account that queries logs in a source account, the query results key from the monitoring account, if any, is used.

### Warning

If you delete the key that is used to encrypt log events or log group query results, then all the associated stored log events or query results that were encrypted with that key will be unencryptable and unusable.

### Note

CloudWatch Logs supports only symmetric KMS keys. Do not associate an asymmetric KMS key with your log group or query results. For more information, see [Using Symmetric and Asymmetric Keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) .

It can take up to 5 minutes for this operation to take effect.

If you attempt to associate a KMS key with a log group but the KMS key does not exist or the KMS key is disabled, you receive an `InvalidParameterException` error.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/AssociateKmsKey)

## Synopsis

```
associate-kms-key
[--log-group-name <value>]
--kms-key-id <value>
[--resource-identifier <value>]
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

`--log-group-name` (string)

The name of the log group.

In your `AssociateKmsKey` operation, you must specify either the `resourceIdentifier` parameter or the `logGroup` parameter, but you canât specify both.

`--kms-key-id` (string)

The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data. This must be a symmetric KMS key. For more information, see [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms) and [Using Symmetric and Asymmetric Keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) .

`--resource-identifier` (string)

Specifies the target for this operation. You must specify one of the following:

- Specify the following ARN to have future [GetQueryResults](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html) operations in this account encrypt the results with the specified KMS key. Replace *REGION* and *ACCOUNT_ID* with your Region and account ID.  `arn:aws:logs:*REGION* :*ACCOUNT_ID* :query-result:*`
- Specify the ARN of a log group to have CloudWatch Logs use the KMS key to encrypt log events that are ingested and stored by that log group. The log group ARN must be in the following format. Replace *REGION* and *ACCOUNT_ID* with your Region and account ID.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/associate-kms-key.html#id1)arn:aws:logs:*REGION* :*ACCOUNT_ID* :log-group:*LOG_GROUP_NAME* ``

In your `AssociateKmsKey` operation, you must specify either the `resourceIdentifier` parameter or the `logGroup` parameter, but you canât specify both.

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

None