# update-account-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/update-account-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/update-account-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/index.html#cli-aws-timestream-query) ]

# update-account-settings

## Description

Transitions your account to use TCUs for query pricing and modifies the maximum query compute units that youâve configured. If you reduce the value of `MaxQueryTCU` to a desired configuration, the new value can take up to 24 hours to be effective.

### Note

After youâve transitioned your account to use TCUs for query pricing, you canât transition to using bytes scanned for query pricing.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-query-2018-11-01/UpdateAccountSettings)

## Synopsis

```
update-account-settings
[--max-query-tcu <value>]
[--query-pricing-model <value>]
[--query-compute <value>]
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

`--max-query-tcu` (integer)

The maximum number of compute units the service will use at any point in time to serve your queries. To run queries, you must set a minimum capacity of 4 TCU. You can set the maximum number of TCU in multiples of 4, for example, 4, 8, 16, 32, and so on. The maximum value supported for `MaxQueryTCU` is 1000. To request an increase to this soft limit, contact Amazon Web Services Support. For information about the default quota for maxQueryTCU, see Default quotas. This configuration is applicable only for on-demand usage of Timestream Compute Units (TCUs).

The maximum value supported for `MaxQueryTCU` is 1000. To request an increase to this soft limit, contact Amazon Web Services Support. For information about the default quota for `maxQueryTCU` , see [Default quotas](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.default) .

`--query-pricing-model` (string)

The pricing model for queries in an account.

### Note

The `QueryPricingModel` parameter is used by several Timestream operations; however, the `UpdateAccountSettings` API operation doesnât recognize any values other than `COMPUTE_UNITS` .

Possible values:

- `BYTES_SCANNED`
- `COMPUTE_UNITS`

`--query-compute` (structure)

Modifies the query compute settings configured in your account, including the query pricing model and provisioned Timestream Compute Units (TCUs) in your account.

### Note

This API is idempotent, meaning that making the same request multiple times will have the same effect as making the request once.

ComputeMode -> (string)

The mode in which Timestream Compute Units (TCUs) are allocated and utilized within an account. Note that in the Asia Pacific (Mumbai) region, the API operation only recognizes the value `PROVISIONED` .

ProvisionedCapacity -> (structure)

Configuration object that contains settings for provisioned Timestream Compute Units (TCUs) in your account.

TargetQueryTCU -> (integer)

The target compute capacity for querying data, specified in Timestream Compute Units (TCUs).

NotificationConfiguration -> (structure)

Configuration settings for notifications related to the provisioned capacity update.

SnsConfiguration -> (structure)

Details on SNS that are required to send the notification.

TopicArn -> (string)

SNS topic ARN that the scheduled query status notifications will be sent to.

RoleArn -> (string)

An Amazon Resource Name (ARN) that grants Timestream permission to publish notifications. This field is only visible if SNS Topic is provided when updating the account settings.

JSON Syntax:

```
{
  "ComputeMode": "ON_DEMAND"|"PROVISIONED",
  "ProvisionedCapacity": {
    "TargetQueryTCU": integer,
    "NotificationConfiguration": {
      "SnsConfiguration": {
        "TopicArn": "string"
      },
      "RoleArn": "string"
    }
  }
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

MaxQueryTCU -> (integer)

The configured maximum number of compute units the service will use at any point in time to serve your queries.

QueryPricingModel -> (string)

The pricing model for an account.

QueryCompute -> (structure)

Confirms the updated account settings for querying data in your account.

ComputeMode -> (string)

The mode in which Timestream Compute Units (TCUs) are allocated and utilized within an account. Note that in the Asia Pacific (Mumbai) region, the API operation only recognizes the value `PROVISIONED` .

ProvisionedCapacity -> (structure)

Configuration object that contains settings for provisioned Timestream Compute Units (TCUs) in your account.

ActiveQueryTCU -> (integer)

The number of Timestream Compute Units (TCUs) provisioned in the account. This field is only visible when the compute mode is `PROVISIONED` .

NotificationConfiguration -> (structure)

An object that contains settings for notifications that are sent whenever the provisioned capacity settings are modified. This field is only visible when the compute mode is `PROVISIONED` .

SnsConfiguration -> (structure)

Details on SNS that are required to send the notification.

TopicArn -> (string)

SNS topic ARN that the scheduled query status notifications will be sent to.

RoleArn -> (string)

An Amazon Resource Name (ARN) that grants Timestream permission to publish notifications. This field is only visible if SNS Topic is provided when updating the account settings.

LastUpdate -> (structure)

Information about the last update to the provisioned capacity settings.

TargetQueryTCU -> (integer)

The number of TimeStream Compute Units (TCUs) requested in the last account settings update.

Status -> (string)

The status of the last update. Can be either `PENDING` , `FAILED` , or `SUCCEEDED` .

StatusMessage -> (string)

Error message describing the last account settings update status, visible only if an error occurred.