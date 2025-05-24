# register-usageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/register-usage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/register-usage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [meteringmarketplace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/index.html#cli-aws-meteringmarketplace) ]

# register-usage

## Description

Paid container software products sold through Amazon Web Services Marketplace must integrate with the Amazon Web Services Marketplace Metering Service and call the `RegisterUsage` operation for software entitlement and metering. Free and BYOL products for Amazon ECS or Amazon EKS arenât required to call `RegisterUsage` , but you may choose to do so if you would like to receive usage data in your seller reports. The sections below explain the behavior of `RegisterUsage` . `RegisterUsage` performs two primary functions: metering and entitlement.

- *Entitlement* : `RegisterUsage` allows you to verify that the customer running your paid software is subscribed to your product on Amazon Web Services Marketplace, enabling you to guard against unauthorized use. Your container image that integrates with `RegisterUsage` is only required to guard against unauthorized use at container startup, as such a `CustomerNotSubscribedException` or `PlatformNotSupportedException` will only be thrown on the initial call to `RegisterUsage` . Subsequent calls from the same Amazon ECS task instance (e.g. task-id) or Amazon EKS pod will not throw a `CustomerNotSubscribedException` , even if the customer unsubscribes while the Amazon ECS task or Amazon EKS pod is still running.
- *Metering* : `RegisterUsage` meters software use per ECS task, per hour, or per pod for Amazon EKS with usage prorated to the second. A minimum of 1 minute of usage applies to tasks that are short lived. For example, if a customer has a 10 node Amazon ECS or Amazon EKS cluster and a service configured as a Daemon Set, then Amazon ECS or Amazon EKS will launch a task on all 10 cluster nodes and the customer will be charged for 10 tasks. Software metering is handled by the Amazon Web Services Marketplace metering control planeâyour software is not required to perform metering-specific actions other than to call `RegisterUsage` to commence metering. The Amazon Web Services Marketplace metering control plane will also bill customers for running ECS tasks and Amazon EKS pods, regardless of the customerâs subscription state, which removes the need for your software to run entitlement checks at runtime. For containers, `RegisterUsage` should be called immediately at launch. If you donât register the container within the first 6 hours of the launch, Amazon Web Services Marketplace Metering Service doesnât provide any metering guarantees for previous months. Metering will continue, however, for the current month forward until the container ends. `RegisterUsage` is for metering paid hourly container products. For Amazon Web Services Regions that support `RegisterUsage` , see [RegisterUsage Region support](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#registerusage-region-support) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/meteringmarketplace-2016-01-14/RegisterUsage)

## Synopsis

```
register-usage
--product-code <value>
--public-key-version <value>
[--nonce <value>]
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

`--product-code` (string)

Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.

`--public-key-version` (integer)

Public Key Version provided by Amazon Web Services Marketplace

`--nonce` (string)

(Optional) To scope down the registration to a specific running software instance and guard against replay attacks.

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

PublicKeyRotationTimestamp -> (timestamp)

(Optional) Only included when public key version has expired

Signature -> (string)

JWT Token