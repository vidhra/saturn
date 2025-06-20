# create-organizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [organizations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/index.html#cli-aws-organizations) ]

# create-organization

## Description

Creates an Amazon Web Services organization. The account whose user is calling the `CreateOrganization` operation automatically becomes the [management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) of the new organization.

This operation must be called using credentials from the account that is to become the new organizationâs management account. The principal must also have the relevant IAM permissions.

By default (or if you set the `FeatureSet` parameter to `ALL` ), the new organization is created with all features enabled and service control policies automatically enabled in the root. If you instead choose to create the organization supporting only the consolidated billing features by setting the `FeatureSet` parameter to `CONSOLIDATED_BILLING` , no policy types are enabled by default and you canât use organization policies.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/CreateOrganization)

## Synopsis

```
create-organization
[--feature-set <value>]
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

`--feature-set` (string)

Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.

- `CONSOLIDATED_BILLING` : All member accounts have their bills consolidated to and paid by the management account. For more information, see [Consolidated billing](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-cb-only) in the *Organizations User Guide* . The consolidated billing feature subset isnât available for organizations in the Amazon Web Services GovCloud (US) Region.
- `ALL` : In addition to all the features supported by the consolidated billing feature set, the management account can also apply any policy type to any member account in the organization. For more information, see [All features](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all) in the *Organizations User Guide* .

Possible values:

- `ALL`
- `CONSOLIDATED_BILLING`

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

**Example 1: To create a new organization**

Bill wants to create an organization using credentials from account 111111111111. The following example shows that the account becomes the master account in the new organization. Because he does not specify a features set, the new organization defaults to all features enabled and service control policies are enabled on the root.

```
aws organizations create-organization
```

The output includes an organization object with details about the new organization:

```
{
        "Organization": {
                "AvailablePolicyTypes": [
                        {
                                "Status": "ENABLED",
                                "Type": "SERVICE_CONTROL_POLICY"
                        }
                ],
                "MasterAccountId": "111111111111",
                "MasterAccountArn": "arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111",
                "MasterAccountEmail": "bill@example.com",
                "FeatureSet": "ALL",
                "Id": "o-exampleorgid",
                "Arn": "arn:aws:organizations::111111111111:organization/o-exampleorgid"
        }
}
```

**Example 2: To create a new organization with only consolidated billing features enabled**

The following example creates an organization that supports only the consolidated billing features:

```
aws organizations create-organization --feature-set CONSOLIDATED_BILLING
```

The output includes an organization object with details about the new organization:

```
{
        "Organization": {
                "Arn": "arn:aws:organizations::111111111111:organization/o-exampleorgid",
                "AvailablePolicyTypes": [],
                "Id": "o-exampleorgid",
                "MasterAccountArn": "arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111",
                "MasterAccountEmail": "bill@example.com",
                "MasterAccountId": "111111111111",
                "FeatureSet": "CONSOLIDATED_BILLING"
        }
}
```

For more information, see [Creating an Organization](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_create.html) in the *AWS Organizations Users Guide*.

## Output

Organization -> (structure)

A structure that contains details about the newly created organization.

Id -> (string)

The unique identifier (ID) of an organization.

The [regex pattern](http://wikipedia.org/wiki/regex) for an organization ID string requires âo-â followed by from 10 to 32 lowercase letters or digits.

Arn -> (string)

The Amazon Resource Name (ARN) of an organization.

For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the *Amazon Web Services Service Authorization Reference* .

FeatureSet -> (string)

Specifies the functionality that currently is available to the organization. If set to âALLâ, then all features are enabled and policies can be applied to accounts in the organization. If set to âCONSOLIDATED_BILLINGâ, then only consolidated billing functionality is available. For more information, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *Organizations User Guide* .

MasterAccountArn -> (string)

The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.

For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the *Amazon Web Services Service Authorization Reference* .

MasterAccountId -> (string)

The unique identifier (ID) of the management account of an organization.

The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID string requires exactly 12 digits.

MasterAccountEmail -> (string)

The email address that is associated with the Amazon Web Services account that is designated as the management account for the organization.

AvailablePolicyTypes -> (list)

### Warning

Do not use. This field is deprecated and doesnât provide complete information about the policies in your organization.

To determine the policies that are enabled and available for use in your organization, use the  ListRoots operation instead.

(structure)

Contains information about a policy type and its status in the associated root.

Type -> (string)

The name of the policy type.

Status -> (string)

The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.