# get-account-limitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-account-limit.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-account-limit.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# get-account-limit

## Description

Gets the specified limit for the current account, for example, the maximum number of health checks that you can create using the account.

For the default limit, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide* . To request a higher limit, [open a case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53) .

### Note

You can also view account limits in Amazon Web Services Trusted Advisor. Sign in to the Amazon Web Services Management Console and open the Trusted Advisor console at [https://console.aws.amazon.com/trustedadvisor/](https://console.aws.amazon.com/trustedadvisor) . Then choose **Service limits** in the navigation pane.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetAccountLimit)

## Synopsis

```
get-account-limit
--type <value>
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

`--type` (string)

The limit that you want to get. Valid values include the following:

- **MAX_HEALTH_CHECKS_BY_OWNER** : The maximum number of health checks that you can create using the current account.
- **MAX_HOSTED_ZONES_BY_OWNER** : The maximum number of hosted zones that you can create using the current account.
- **MAX_REUSABLE_DELEGATION_SETS_BY_OWNER** : The maximum number of reusable delegation sets that you can create using the current account.
- **MAX_TRAFFIC_POLICIES_BY_OWNER** : The maximum number of traffic policies that you can create using the current account.
- **MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER** : The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)

Possible values:

- `MAX_HEALTH_CHECKS_BY_OWNER`
- `MAX_HOSTED_ZONES_BY_OWNER`
- `MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER`
- `MAX_REUSABLE_DELEGATION_SETS_BY_OWNER`
- `MAX_TRAFFIC_POLICIES_BY_OWNER`

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

Limit -> (structure)

The current setting for the specified limit. For example, if you specified `MAX_HEALTH_CHECKS_BY_OWNER` for the value of `Type` in the request, the value of `Limit` is the maximum number of health checks that you can create using the current account.

Type -> (string)

The limit that you requested. Valid values include the following:

- **MAX_HEALTH_CHECKS_BY_OWNER** : The maximum number of health checks that you can create using the current account.
- **MAX_HOSTED_ZONES_BY_OWNER** : The maximum number of hosted zones that you can create using the current account.
- **MAX_REUSABLE_DELEGATION_SETS_BY_OWNER** : The maximum number of reusable delegation sets that you can create using the current account.
- **MAX_TRAFFIC_POLICIES_BY_OWNER** : The maximum number of traffic policies that you can create using the current account.
- **MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER** : The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)

Value -> (long)

The current value for the limit that is specified by [Type](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AccountLimit.html#Route53-Type-AccountLimit-Type) .

Count -> (long)

The current number of entities that you have created of the specified type. For example, if you specified `MAX_HEALTH_CHECKS_BY_OWNER` for the value of `Type` in the request, the value of `Count` is the current number of health checks that you have created using the current account.