# grant-flow-entitlementsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/grant-flow-entitlements.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/grant-flow-entitlements.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/index.html#cli-aws-mediaconnect) ]

# grant-flow-entitlements

## Description

Grants entitlements to an existing flow.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/GrantFlowEntitlements)

## Synopsis

```
grant-flow-entitlements
--entitlements <value>
--flow-arn <value>
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

`--entitlements` (list)

The list of entitlements that you want to grant.

(structure)

The entitlements that you want to grant on a flow.

DataTransferSubscriberFeePercent -> (integer)

Percentage from 0-100 of the data transfer cost to be billed to the subscriber.

Description -> (string)

A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user.

Encryption -> (structure)

The type of encryption that will be used on the output that is associated with this entitlement. Allowable encryption types: static-key, speke.

Algorithm -> (string)

The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).

ConstantInitializationVector -> (string)

A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.

DeviceId -> (string)

The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.

KeyType -> (string)

The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).

Region -> (string)

The Amazon Web Services Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.

ResourceId -> (string)

An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

RoleArn -> (string)

The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).

SecretArn -> (string)

The ARN of the secret that you created in Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.

Url -> (string)

The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

EntitlementStatus -> (string)

An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you donât specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.

Name -> (string)

The name of the entitlement. This value must be unique within the current flow.

Subscribers -> (list)

The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.

(string)

Shorthand Syntax:

```
DataTransferSubscriberFeePercent=integer,Description=string,Encryption={Algorithm=string,ConstantInitializationVector=string,DeviceId=string,KeyType=string,Region=string,ResourceId=string,RoleArn=string,SecretArn=string,Url=string},EntitlementStatus=string,Name=string,Subscribers=string,string ...
```

JSON Syntax:

```
[
  {
    "DataTransferSubscriberFeePercent": integer,
    "Description": "string",
    "Encryption": {
      "Algorithm": "aes128"|"aes192"|"aes256",
      "ConstantInitializationVector": "string",
      "DeviceId": "string",
      "KeyType": "speke"|"static-key"|"srt-password",
      "Region": "string",
      "ResourceId": "string",
      "RoleArn": "string",
      "SecretArn": "string",
      "Url": "string"
    },
    "EntitlementStatus": "ENABLED"|"DISABLED",
    "Name": "string",
    "Subscribers": ["string", ...]
  }
  ...
]
```

`--flow-arn` (string)

The Amazon Resource Name (ARN) of the flow that you want to grant entitlements on.

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

**To grant an entitlement on a flow**

The following `grant-flow-entitlements` example grants an entitlement to the specified existing flow to share your content with another AWS account.

```
aws mediaconnect grant-flow-entitlements \
    --flow-arn arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame \
    --entitlements Description='For AnyCompany',Encryption={"Algorithm=aes128,KeyType=static-key,RoleArn=arn:aws:iam::111122223333:role/MediaConnect-ASM,SecretArn=arn:aws:secretsmanager:us-west-2:111122223333:secret:mySecret1"},Name=AnyCompany_Entitlement,Subscribers=444455556666 Description='For Example Corp',Name=ExampleCorp,Subscribers=777788889999
```

Output:

```
{
    "Entitlements": [
        {
            "Name": "AnyCompany_Entitlement",
            "EntitlementArn": "arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-11aa22bb11aa22bb-3333cccc4444:AnyCompany_Entitlement",
            "Subscribers": [
                "444455556666"
            ],
            "Description": "For AnyCompany",
            "Encryption": {
                "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:mySecret1",
                "Algorithm": "aes128",
                "RoleArn": "arn:aws:iam::111122223333:role/MediaConnect-ASM",
                "KeyType": "static-key"
            }
        },
        {
            "Name": "ExampleCorp",
            "EntitlementArn": "arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-3333cccc4444dddd-1111aaaa2222:ExampleCorp",
            "Subscribers": [
                "777788889999"
            ],
            "Description": "For Example Corp"
        }
    ],
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame"
}
```

For more information, see [Granting an Entitlement on a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-grant.html) in the *AWS Elemental MediaConnect User Guide*.

## Output

Entitlements -> (list)

The entitlements that were just granted.

(structure)

The settings for a flow entitlement.

DataTransferSubscriberFeePercent -> (integer)

Percentage from 0-100 of the data transfer cost to be billed to the subscriber.

Description -> (string)

A description of the entitlement.

Encryption -> (structure)

The type of encryption that will be used on the output that is associated with this entitlement.

Algorithm -> (string)

The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).

ConstantInitializationVector -> (string)

A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.

DeviceId -> (string)

The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.

KeyType -> (string)

The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).

Region -> (string)

The Amazon Web Services Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.

ResourceId -> (string)

An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

RoleArn -> (string)

The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).

SecretArn -> (string)

The ARN of the secret that you created in Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.

Url -> (string)

The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

EntitlementArn -> (string)

The ARN of the entitlement.

EntitlementStatus -> (string)

An indication of whether the entitlement is enabled.

Name -> (string)

The name of the entitlement.

Subscribers -> (list)

The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.

(string)

FlowArn -> (string)

The ARN of the flow that these entitlements were granted to.