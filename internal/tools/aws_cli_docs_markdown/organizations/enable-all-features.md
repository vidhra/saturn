# enable-all-featuresÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-all-features.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-all-features.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [organizations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/index.html#cli-aws-organizations) ]

# enable-all-features

## Description

Enables all features in an organization. This enables the use of organization policies that can restrict the services and actions that can be called in each account. Until you enable all features, you have access only to consolidated billing, and you canât use any of the advanced account administration features that Organizations supports. For more information, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *Organizations User Guide* .

### Warning

This operation is required only for organizations that were created explicitly with only the consolidated billing features enabled. Calling this operation sends a handshake to every invited account in the organization. The feature set change can be finalized and the additional features enabled only after all administrators in the invited accounts approve the change by accepting the handshake.

After you enable all features, you can separately enable or disable individual policy types in a root using  EnablePolicyType and  DisablePolicyType . To see the status of policy types in a root, use  ListRoots .

After all invited member accounts accept the handshake, you finalize the feature set change by accepting the handshake that contains `"Action": "ENABLE_ALL_FEATURES"` . This completes the change.

After you enable all features in your organization, the management account in the organization can apply policies on all member accounts. These policies can restrict what users and even administrators in those accounts can do. The management account can apply policies that prevent accounts from leaving the organization. Ensure that your account administrators are aware of this.

This operation can be called only from the organizationâs management account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/EnableAllFeatures)

## Synopsis

```
enable-all-features
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

**To enable all features in an organization**

This example shows the administrator asking all the invited accounts in the organization to approve enabled all features in the organization. AWS Organizations sends an email to the address that is registered with every invited member account asking the owner to approve the change to all features by accepting the handshake that is sent. After all invited member accounts accept the handshake, the organization administrator can finalize the change to all features, and those with appropriate permissions can create policies and apply them to roots, OUs, and accounts:

```
aws organizations enable-all-features
```

The output is a handshake object that is sent to all invited member accounts for approval:

```
{
        "Handshake": {
                "Action": "ENABLE_ALL_FEATURES",
                "Arn":"arn:aws:organizations::111111111111:handshake/o-exampleorgid/enable_all_features/h-examplehandshakeid111",
                "ExpirationTimestamp":1.483127868609E9,
                "Id":"h-examplehandshakeid111",
                "Parties": [
                        {
                                "id":"o-exampleorgid",
                                "type":"ORGANIZATION"
                        }
                ],
                "requestedTimestamp":1.481831868609E9,
                "resources": [
                        {
                                "type":"ORGANIZATION",
                                "value":"o-exampleorgid"
                        }
                ],
                "state":"REQUESTED"
        }
}
```

## Output

Handshake -> (structure)

A structure that contains details about the handshake created to support this request to enable all features in the organization.

Id -> (string)

The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID string requires âh-â followed by from 8 to 32 lowercase letters or digits.

Arn -> (string)

The Amazon Resource Name (ARN) of a handshake.

For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the *Amazon Web Services Service Authorization Reference* .

Parties -> (list)

Information about the two accounts that are participating in the handshake.

(structure)

Identifies a participant in a handshake.

Id -> (string)

The unique identifier (ID) for the party.

The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID string requires âh-â followed by from 8 to 32 lowercase letters or digits.

Type -> (string)

The type of party.

State -> (string)

The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

- **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
- **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
- **CANCELED** : This handshake is no longer active because it was canceled by the originating account.
- **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.
- **DECLINED** : This handshake is no longer active because it was declined by the recipient account.
- **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).

RequestedTimestamp -> (timestamp)

The date and time that the handshake request was made.

ExpirationTimestamp -> (timestamp)

The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action -> (string)

The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

- **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the management account to only non-member accounts.
- **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the management account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organizationâs management account and approval is inferred.
- **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the `ENABLE_ALL_FEATURES` invitation. It is sent only to the management account and signals the master that it can finalize the process to enable all features.

Resources -> (list)

Additional information that is needed to process the handshake.

(structure)

Contains additional data that is needed to process a handshake.

Value -> (string)

The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type -> (string)

The type of information being passed, specifying how the value is to be interpreted by the other party:

- `ACCOUNT` - Specifies an Amazon Web Services account ID number.
- `ORGANIZATION` - Specifies an organization ID number.
- `EMAIL` - Specifies the email address that is associated with the account that receives the handshake.
- `OWNER_EMAIL` - Specifies the email address associated with the management account. Included as information about an organization.
- `OWNER_NAME` - Specifies the name associated with the management account. Included as information about an organization.
- `NOTES` - Additional text provided by the handshake initiator and intended for the recipient to read.

Resources -> (list)

When needed, contains an additional array of `HandshakeResource` objects.

(structure)

Contains additional data that is needed to process a handshake.

Value -> (string)

The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type -> (string)

The type of information being passed, specifying how the value is to be interpreted by the other party:

- `ACCOUNT` - Specifies an Amazon Web Services account ID number.
- `ORGANIZATION` - Specifies an organization ID number.
- `EMAIL` - Specifies the email address that is associated with the account that receives the handshake.
- `OWNER_EMAIL` - Specifies the email address associated with the management account. Included as information about an organization.
- `OWNER_NAME` - Specifies the name associated with the management account. Included as information about an organization.
- `NOTES` - Additional text provided by the handshake initiator and intended for the recipient to read.