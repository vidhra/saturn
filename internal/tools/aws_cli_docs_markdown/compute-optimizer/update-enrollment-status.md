# update-enrollment-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/update-enrollment-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/update-enrollment-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# update-enrollment-status

## Description

Updates the enrollment (opt in and opt out) status of an account to the Compute Optimizer service.

If the account is a management account of an organization, this action can also be used to enroll member accounts of the organization.

You must have the appropriate permissions to opt in to Compute Optimizer, to view its recommendations, and to opt out. For more information, see [Controlling access with Amazon Web Services Identity and Access Management](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html) in the *Compute Optimizer User Guide* .

When you opt in, Compute Optimizer automatically creates a service-linked role in your account to access its data. For more information, see [Using Service-Linked Roles for Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/using-service-linked-roles.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)

## Synopsis

```
update-enrollment-status
--status <value>
[--include-member-accounts | --no-include-member-accounts]
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

`--status` (string)

The new enrollment status of the account.

The following status options are available:

- `Active` - Opts in your account to the Compute Optimizer service. Compute Optimizer begins analyzing the configuration and utilization metrics of your Amazon Web Services resources after you opt in. For more information, see [Metrics analyzed by Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html) in the *Compute Optimizer User Guide* .
- `Inactive` - Opts out your account from the Compute Optimizer service. Your accountâs recommendations and related metrics data will be deleted from Compute Optimizer after you opt out.

### Note

The `Pending` and `Failed` options cannot be used to update the enrollment status of an account. They are returned in the response of a request to update the enrollment status of an account.

Possible values:

- `Active`
- `Inactive`
- `Pending`
- `Failed`

`--include-member-accounts` | `--no-include-member-accounts` (boolean)

Indicates whether to enroll member accounts of the organization if the account is the management account of an organization.

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

status -> (string)

The enrollment status of the account.

statusReason -> (string)

The reason for the enrollment status of the account. For example, an account might show a status of `Pending` because member accounts of an organization require more time to be enrolled in the service.