# batch-get-configuration-policy-associationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-configuration-policy-associations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-configuration-policy-associations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# batch-get-configuration-policy-associations

## Description

Returns associations between an Security Hub configuration and a batch of target accounts, organizational units, or the root. Only the Security Hub delegated administrator can invoke this operation from the home Region. A configuration can refer to a configuration policy or to a self-managed configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)

## Synopsis

```
batch-get-configuration-policy-associations
--configuration-policy-association-identifiers <value>
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

`--configuration-policy-association-identifiers` (list)

Specifies one or more target account IDs, organizational unit (OU) IDs, or the root ID to retrieve associations for.

(structure)

Provides details about the association between an Security Hub configuration and a target account, organizational unit, or the root. An association can exist between a target and a configuration policy, or between a target and self-managed behavior.

Target -> (tagged union structure)

The target account, organizational unit, or the root.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AccountId`, `OrganizationalUnitId`, `RootId`.

AccountId -> (string)

The Amazon Web Services account ID of the target account.

OrganizationalUnitId -> (string)

The organizational unit ID of the target organizational unit.

RootId -> (string)

The ID of the organization root.

Shorthand Syntax:

```
Target={AccountId=string,OrganizationalUnitId=string,RootId=string} ...
```

JSON Syntax:

```
[
  {
    "Target": {
      "AccountId": "string",
      "OrganizationalUnitId": "string",
      "RootId": "string"
    }
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

**To get configuration association details for a batch of targets**

The following `batch-get-configuration-policy-associations` example retrieves association details for the specified targets. You can provide account IDs, organizational unit IDs, or the root ID for the target.

```
aws securityhub batch-get-configuration-policy-associations \
    --target '{"OrganizationalUnitId": "ou-6hi7-8j91kl2m"}'
```

Output:

```
{
    "ConfigurationPolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "TargetId": "ou-6hi7-8j91kl2m",
    "TargetType": "ORGANIZATIONAL_UNIT",
    "AssociationType": "APPLIED",
    "UpdatedAt": "2023-09-26T21:13:01.816000+00:00",
    "AssociationStatus": "SUCCESS",
    "AssociationStatusMessage": "Association applied successfully on this target."
}
```

For more information, see [Viewing Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/view-policy.html) in the *AWS Security Hub User Guide*.

## Output

ConfigurationPolicyAssociations -> (list)

Describes associations for the target accounts, OUs, or the root.

(structure)

An object that contains the details of a configuration policy association thatâs returned in a `ListConfigurationPolicyAssociations` request.

ConfigurationPolicyId -> (string)

The universally unique identifier (UUID) of the configuration policy.

TargetId -> (string)

The identifier of the target account, organizational unit, or the root.

TargetType -> (string)

Specifies whether the target is an Amazon Web Services account, organizational unit, or the root.

AssociationType -> (string)

Indicates whether the association between the specified target and the configuration was directly applied by the Security Hub delegated administrator or inherited from a parent.

UpdatedAt -> (timestamp)

The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated.

AssociationStatus -> (string)

The current status of the association between the specified target and the configuration.

AssociationStatusMessage -> (string)

The explanation for a `FAILED` value for `AssociationStatus` .

UnprocessedConfigurationPolicyAssociations -> (list)

An array of configuration policy associations, one for each configuration policy association identifier, that was specified in the request but couldnât be processed due to an error.

(structure)

An array of configuration policy associations, one for each configuration policy association identifier, that was specified in a `BatchGetConfigurationPolicyAssociations` request but couldnât be processed due to an error.

ConfigurationPolicyAssociationIdentifiers -> (structure)

Configuration policy association identifiers that were specified in a `BatchGetConfigurationPolicyAssociations` request but couldnât be processed due to an error.

Target -> (tagged union structure)

The target account, organizational unit, or the root.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AccountId`, `OrganizationalUnitId`, `RootId`.

AccountId -> (string)

The Amazon Web Services account ID of the target account.

OrganizationalUnitId -> (string)

The organizational unit ID of the target organizational unit.

RootId -> (string)

The ID of the organization root.

ErrorCode -> (string)

An HTTP status code that identifies why the configuration policy association failed.

ErrorReason -> (string)

A string that identifies why the configuration policy association failed.