# start-delivery-stream-encryptionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/start-delivery-stream-encryption.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/start-delivery-stream-encryption.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [firehose](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/index.html#cli-aws-firehose) ]

# start-delivery-stream-encryption

## Description

Enables server-side encryption (SSE) for the Firehose stream.

This operation is asynchronous. It returns immediately. When you invoke it, Firehose first sets the encryption status of the stream to `ENABLING` , and then to `ENABLED` . The encryption status of a Firehose stream is the `Status` property in  DeliveryStreamEncryptionConfiguration . If the operation fails, the encryption status changes to `ENABLING_FAILED` . You can continue to read and write data to your Firehose stream while the encryption status is `ENABLING` , but the data is not encrypted. It can take up to 5 seconds after the encryption status changes to `ENABLED` before all records written to the Firehose stream are encrypted. To find out whether a record or a batch of records was encrypted, check the response elements  PutRecordOutput$Encrypted and  PutRecordBatchOutput$Encrypted , respectively.

To check the encryption status of a Firehose stream, use  DescribeDeliveryStream .

Even if encryption is currently enabled for a Firehose stream, you can still invoke this operation on it to change the ARN of the CMK or both its type and ARN. If you invoke this method to change the CMK, and the old CMK is of type `CUSTOMER_MANAGED_CMK` , Firehose schedules the grant it had on the old CMK for retirement. If the new CMK is of type `CUSTOMER_MANAGED_CMK` , Firehose creates a grant that enables it to use the new CMK to encrypt and decrypt data and to manage the grant.

For the KMS grant creation to be successful, the Firehose API operations `StartDeliveryStreamEncryption` and `CreateDeliveryStream` should not be called with session credentials that are more than 6 hours old.

If a Firehose stream already has encryption enabled and then you invoke this operation to change the ARN of the CMK or both its type and ARN and you get `ENABLING_FAILED` , this only means that the attempt to change the CMK failed. In this case, encryption remains enabled with the old CMK.

If the encryption status of your Firehose stream is `ENABLING_FAILED` , you can invoke this operation again with a valid CMK. The CMK must be enabled and the key policy mustnât explicitly deny the permission for Firehose to invoke KMS encrypt and decrypt operations.

You can enable SSE for a Firehose stream only if itâs a Firehose stream that uses `DirectPut` as its source.

The `StartDeliveryStreamEncryption` and `StopDeliveryStreamEncryption` operations have a combined limit of 25 calls per Firehose stream per 24 hours. For example, you reach the limit if you call `StartDeliveryStreamEncryption` 13 times and `StopDeliveryStreamEncryption` 12 times for the same Firehose stream in a 24-hour period.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/StartDeliveryStreamEncryption)

## Synopsis

```
start-delivery-stream-encryption
--delivery-stream-name <value>
[--delivery-stream-encryption-configuration-input <value>]
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

`--delivery-stream-name` (string)

The name of the Firehose stream for which you want to enable server-side encryption (SSE).

`--delivery-stream-encryption-configuration-input` (structure)

Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).

KeyARN -> (string)

If you set `KeyType` to `CUSTOMER_MANAGED_CMK` , you must specify the Amazon Resource Name (ARN) of the CMK. If you set `KeyType` to `Amazon Web Services_OWNED_CMK` , Firehose uses a service-account CMK.

KeyType -> (string)

Indicates the type of customer master key (CMK) to use for encryption. The default setting is `Amazon Web Services_OWNED_CMK` . For more information about CMKs, see [Customer Master Keys (CMKs)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) . When you invoke  CreateDeliveryStream or  StartDeliveryStreamEncryption with `KeyType` set to CUSTOMER_MANAGED_CMK, Firehose invokes the Amazon KMS operation [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) to create a grant that allows the Firehose service to use the customer managed CMK to perform encryption and decryption. Firehose manages that grant.

When you invoke  StartDeliveryStreamEncryption to change the CMK for a Firehose stream that is encrypted with a customer managed CMK, Firehose schedules the grant it had on the old CMK for retirement.

You can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 Firehose streams. If a  CreateDeliveryStream or  StartDeliveryStreamEncryption operation exceeds this limit, Firehose throws a `LimitExceededException` .

### Warning

To encrypt your Firehose stream, use symmetric CMKs. Firehose doesnât support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see [About Symmetric and Asymmetric CMKs](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html) in the Amazon Web Services Key Management Service developer guide.

Shorthand Syntax:

```
KeyARN=string,KeyType=string
```

JSON Syntax:

```
{
  "KeyARN": "string",
  "KeyType": "AWS_OWNED_CMK"|"CUSTOMER_MANAGED_CMK"
}
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

None