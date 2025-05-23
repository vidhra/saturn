# create-protectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [shield](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/index.html#cli-aws-shield) ]

# create-protection

## Description

Enables Shield Advanced for a specific Amazon Web Services resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.

You can add protection to only a single resource with each `CreateProtection` request. You can add protection to multiple resources at once through the Shield Advanced console at [https://console.aws.amazon.com/wafv2/shieldv2#/](https://console.aws.amazon.com/wafv2/shieldv2#/) . For more information see [Getting Started with Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html) and [Adding Shield Advanced protection to Amazon Web Services resources](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/CreateProtection)

## Synopsis

```
create-protection
--name <value>
--resource-arn <value>
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

`--name` (string)

Friendly name for the `Protection` you are creating.

`--resource-arn` (string)

The ARN (Amazon Resource Name) of the resource to be protected.

The ARN should be in one of the following formats:

- For an Application Load Balancer: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html#id1)arn:aws:elasticloadbalancing:*region* :*account-id* :loadbalancer/app/*load-balancer-name* /*load-balancer-id* ``
- For an Elastic Load Balancer (Classic Load Balancer): [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html#id3)arn:aws:elasticloadbalancing:*region* :*account-id* :loadbalancer/*load-balancer-name* ``
- For an Amazon CloudFront distribution: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html#id5)arn:aws:cloudfront::*account-id* :distribution/*distribution-id* ``
- For an Global Accelerator standard accelerator: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html#id7)arn:aws:globalaccelerator::*account-id* :accelerator/*accelerator-id* ``
- For Amazon Route 53: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html#id9)arn:aws:route53:::hostedzone/*hosted-zone-id* ``
- For an Elastic IP address: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html#id11)arn:aws:ec2:*region* :*account-id* :eip-allocation/*allocation-id* ``

`--tags` (list)

One or more tag key-value pairs for the  Protection object that is created.

(structure)

A tag associated with an Amazon Web Services resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing or other management. Typically, the tag key represents a category, such as âenvironmentâ, and the tag value represents a specific value within that category, such as âtest,â âdevelopment,â or âproductionâ. Or you might set the tag key to âcustomerâ and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.

Key -> (string)

Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as âcustomer.â Tag keys are case-sensitive.

Value -> (string)

Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as âcompanyAâ or âcompanyB.â Tag values are case-sensitive.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

**To enable AWS Shield Advanced protection for a single AWS resource**

The following `create-protection` example enables Shield Advanced protection for the specified AWS CloudFront distribution.

```
aws shield create-protection \
    --name "Protection for CloudFront distribution" \
    --resource-arn arn:aws:cloudfront::123456789012:distribution/E198WC25FXOWY8
```

Output:

```
{
    "ProtectionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

For more information, see [Specify Your Resources to Protect](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-choose-resources.html) in the *AWS Shield Advanced Developer Guide*.

## Output

ProtectionId -> (string)

The unique identifier (ID) for the  Protection object that is created.