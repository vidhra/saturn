# create-pricing-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/create-pricing-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/create-pricing-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [billingconductor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/index.html#cli-aws-billingconductor) ]

# create-pricing-rule

## Description

Creates a pricing rule can be associated to a pricing plan, or a set of pricing plans.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/billingconductor-2021-07-30/CreatePricingRule)

## Synopsis

```
create-pricing-rule
[--client-token <value>]
--name <value>
[--description <value>]
--scope <value>
--type <value>
[--modifier-percentage <value>]
[--service <value>]
[--tags <value>]
[--billing-entity <value>]
[--tiering <value>]
[--usage-type <value>]
[--operation <value>]
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

`--client-token` (string)

The token thatâs needed to support idempotency. Idempotency isnât currently supported, but will be implemented in a future update.

`--name` (string)

The pricing rule name. The names must be unique to each pricing rule.

`--description` (string)

The pricing rule description.

`--scope` (string)

The scope of pricing rule that indicates if itâs globally applicable, or itâs service-specific.

Possible values:

- `GLOBAL`
- `SERVICE`
- `BILLING_ENTITY`
- `SKU`

`--type` (string)

The type of pricing rule.

Possible values:

- `MARKUP`
- `DISCOUNT`
- `TIERING`

`--modifier-percentage` (double)

A percentage modifier thatâs applied on the public pricing rates.

`--service` (string)

If the `Scope` attribute is set to `SERVICE` or `SKU` , the attribute indicates which service the `PricingRule` is applicable for.

`--tags` (map)

A map that contains tag keys and tag values that are attached to a pricing rule.

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

`--billing-entity` (string)

The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace.

`--tiering` (structure)

The set of tiering configurations for the pricing rule.

FreeTier -> (structure)

The possible Amazon Web Services Free Tier configurations.

Activated -> (boolean)

Activate or deactivate Amazon Web Services Free Tier.

Shorthand Syntax:

```
FreeTier={Activated=boolean}
```

JSON Syntax:

```
{
  "FreeTier": {
    "Activated": true|false
  }
}
```

`--usage-type` (string)

Usage type is the unit that each service uses to measure the usage of a specific type of resource.

If the `Scope` attribute is set to `SKU` , this attribute indicates which usage type the `PricingRule` is modifying. For example, `USW2-BoxUsage:m2.2xlarge` describes an``M2 High Memory Double Extra Large`` instance in the US West (Oregon) Region. `</p>`

`--operation` (string)

Operation is the specific Amazon Web Services action covered by this line item. This describes the specific usage of the line item.

If the `Scope` attribute is set to `SKU` , this attribute indicates which operation the `PricingRule` is modifying. For example, a value of `RunInstances:0202` indicates the operation of running an Amazon EC2 instance.

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

Arn -> (string)

The Amazon Resource Name (ARN) of the created pricing rule.