# describe-account-policiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-account-policies.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-account-policies.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# describe-account-policies

## Description

Returns a list of all CloudWatch Logs account policies in the account.

To use this operation, you must be signed on with the correct permissions depending on the type of policy that you are retrieving information for.

- To see data protection policies, you must have the `logs:GetDataProtectionPolicy` and `logs:DescribeAccountPolicies` permissions.
- To see subscription filter policies, you must have the `logs:DescribeSubscriptionFilters` and `logs:DescribeAccountPolicies` permissions.
- To see transformer policies, you must have the `logs:GetTransformer` and `logs:DescribeAccountPolicies` permissions.
- To see field index policies, you must have the `logs:DescribeIndexPolicies` and `logs:DescribeAccountPolicies` permissions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeAccountPolicies)

## Synopsis

```
describe-account-policies
--policy-type <value>
[--policy-name <value>]
[--account-identifiers <value>]
[--next-token <value>]
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

`--policy-type` (string)

Use this parameter to limit the returned policies to only the policies that match the policy type that you specify.

Possible values:

- `DATA_PROTECTION_POLICY`
- `SUBSCRIPTION_FILTER_POLICY`
- `FIELD_INDEX_POLICY`
- `TRANSFORMER_POLICY`

`--policy-name` (string)

Use this parameter to limit the returned policies to only the policy with the name that you specify.

`--account-identifiers` (list)

If you are using an account that is set up as a monitoring account for CloudWatch unified cross-account observability, you can use this to specify the account ID of a source account. If you do, the operation returns the account policy for the specified account. Currently, you can specify only one account ID in this parameter.

If you omit this parameter, only the policy in the current account is returned.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token for the next set of items to return. (You received this token from a previous call.)

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

accountPolicies -> (list)

An array of structures that contain information about the CloudWatch Logs account policies that match the specified filters.

(structure)

A structure that contains information about one CloudWatch Logs account policy.

policyName -> (string)

The name of the account policy.

policyDocument -> (string)

The policy document for this account policy.

The JSON specified in `policyDocument` can be up to 30,720 characters.

lastUpdatedTime -> (long)

The date and time that this policy was most recently updated.

policyType -> (string)

The type of policy for this account policy.

scope -> (string)

The scope of the account policy.

selectionCriteria -> (string)

The log group selection criteria that is used for this policy.

accountId -> (string)

The Amazon Web Services account ID that the policy applies to.

nextToken -> (string)

The token to use when requesting the next set of items. The token expires after 24 hours.