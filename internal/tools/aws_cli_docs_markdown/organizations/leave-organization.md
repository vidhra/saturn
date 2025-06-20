# leave-organizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/leave-organization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/leave-organization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [organizations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/index.html#cli-aws-organizations) ]

# leave-organization

## Description

Removes a member account from its parent organization. This version of the operation is performed by the account that wants to leave. To remove a member account as a user in the management account, use  RemoveAccountFromOrganization instead.

This operation can be called only from a member account in the organization.

### Warning

- The management account in an organization with all features enabled can set service control policies (SCPs) that can restrict what administrators of member accounts can do. This includes preventing them from successfully calling `LeaveOrganization` and leaving the organization.
- You can leave an organization as a member account only if the account is configured with the information required to operate as a standalone account. When you create an account in an organization using the Organizations console, API, or CLI commands, the information required of standalone accounts is *not* automatically collected. For each account that you want to make standalone, you must perform the following steps. If any of the steps are already completed for this account, that step doesnât appear.
- Choose a support plan
- Provide and verify the required contact information
- Provide a current payment method

Amazon Web Services uses the payment method to charge for any billable (not free tier) Amazon Web Services activity that occurs while the account isnât attached to an organization. For more information, see [Considerations before removing an account from an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_account-before-remove.html) in the *Organizations User Guide* .

- The account that you want to leave must not be a delegated administrator account for any Amazon Web Services service enabled for your organization. If the account is a delegated administrator, you must first change the delegated administrator account to another account that is remaining in the organization.
- You can leave an organization only after you enable IAM user access to billing in your account. For more information, see [About IAM access to the Billing and Cost Management console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html#ControllingAccessWebsite-Activate) in the *Amazon Web Services Billing and Cost Management User Guide* .
- After the account leaves the organization, all tags that were attached to the account object in the organization are deleted. Amazon Web Services accounts outside of an organization do not support tags.
- A newly created account has a waiting period before it can be removed from its organization. You must wait until at least seven days after the account was created. Invited accounts arenât subject to this waiting period.
- If you are using an organization principal to call `LeaveOrganization` across multiple accounts, you can only do this up to 5 accounts per second in a single organization.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/LeaveOrganization)

## Synopsis

```
leave-organization
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

**To leave an organization as a member account**

The following example shows the administrator of a member account requesting to leave the organization it is currently a member of:

```
aws organizations leave-organization
```

## Output

None