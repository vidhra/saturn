# create-membersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [detective](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/index.html#cli-aws-detective) ]

# create-members

## Description

`CreateMembers` is used to send invitations to accounts. For the organization behavior graph, the Detective administrator account uses `CreateMembers` to enable organization accounts as member accounts.

For invited accounts, `CreateMembers` sends a request to invite the specified Amazon Web Services accounts to be member accounts in the behavior graph. This operation can only be called by the administrator account for a behavior graph.

`CreateMembers` verifies the accounts and then invites the verified accounts. The administrator can optionally specify to not send invitation emails to the member accounts. This would be used when the administrator manages their member accounts centrally.

For organization accounts in the organization behavior graph, `CreateMembers` attempts to enable the accounts. The organization accounts do not receive invitations.

The request provides the behavior graph ARN and the list of accounts to invite or to enable.

The response separates the requested accounts into two lists:

- The accounts that `CreateMembers` was able to process. For invited accounts, includes member accounts that are being verified, that have passed verification and are to be invited, and that have failed verification. For organization accounts in the organization behavior graph, includes accounts that can be enabled and that cannot be enabled.
- The accounts that `CreateMembers` was unable to process. This list includes accounts that were already invited to be member accounts in the behavior graph.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/detective-2018-10-26/CreateMembers)

## Synopsis

```
create-members
--graph-arn <value>
[--message <value>]
[--disable-email-notification | --no-disable-email-notification]
--accounts <value>
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

`--graph-arn` (string)

The ARN of the behavior graph.

`--message` (string)

Customized message text to include in the invitation email message to the invited member accounts.

`--disable-email-notification` | `--no-disable-email-notification` (boolean)

if set to `true` , then the invited accounts do not receive email notifications. By default, this is set to `false` , and the invited accounts receive email notifications.

Organization accounts in the organization behavior graph do not receive email notifications.

`--accounts` (list)

The list of Amazon Web Services accounts to invite or to enable. You can invite or enable up to 50 accounts at a time. For each invited account, the account list contains the account identifier and the Amazon Web Services account root user email address. For organization accounts in the organization behavior graph, the email address is not required.

(structure)

An Amazon Web Services account that is the administrator account of or a member of a behavior graph.

AccountId -> (string)

The account identifier of the Amazon Web Services account.

EmailAddress -> (string)

The Amazon Web Services account root user email address for the Amazon Web Services account.

Shorthand Syntax:

```
AccountId=string,EmailAddress=string ...
```

JSON Syntax:

```
[
  {
    "AccountId": "string",
    "EmailAddress": "string"
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

**To invite member accounts to a behavior graph**

The following `create-members` example invites two AWS accounts to become member accounts in the behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234. For each account, the request provides the AWS account ID and the account root user email address. The request includes a custom message to insert into the invitation email.

```
aws detective create-members \
    --accounts AccountId=444455556666,EmailAddress=mmajor@example.com AccountId=123456789012,EmailAddress=jstiles@example.com \
    --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234 \
    --message "This is Paul Santos. I need to add your account to the data we use for security investigation in Amazon Detective. If you have any questions, contact me at psantos@example.com."
```

Output:

```
{
    "Members": [
    {
        "AccountId": "444455556666",
        "AdministratorId": "111122223333",
        "EmailAddress": "mmajor@example.com",
        "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234",
        "InvitedTime": 1579826107000,
        "MasterId": "111122223333",
        "Status": "INVITED",
        "UpdatedTime": 1579826107000
   },
   {
        "AccountId": "123456789012",
        "AdministratorId": "111122223333",
        "EmailAddress": "jstiles@example.com",
        "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234",
        "InvitedTime": 1579826107000,
        "MasterId": "111122223333",
        "Status": "VERIFICATION_IN_PROGRESS",
        "UpdatedTime": 1579826107000
     }
    ],
    "UnprocessedAccounts": [ ]
}
```

For more information, see [`Inviting member accounts to a behavior graph<https://docs.aws.amazon.com/detective/latest/adminguide/graph-admin-add-member-accounts.html>`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html#id1) in the *Amazon Detective Administration Guide*.

**To invite member accounts without sending invitation emails**

The following `create-members` example invites two AWS accounts to become member accounts in the behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234. For each account, the request provides the AWS account ID and the account root user email address. The member accounts do not receive invitation emails.

```
aws detective create-members \
    --accounts AccountId=444455556666,EmailAddress=mmajor@example.com AccountId=123456789012,EmailAddress=jstiles@example.com \
    --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234 \
    --disable-email-notification
```

Output:

```
{
    "Members": [
    {
        "AccountId": "444455556666",
        "AdministratorId": "111122223333",
        "EmailAddress": "mmajor@example.com",
        "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234",
        "InvitedTime": 1579826107000,
        "MasterId": "111122223333",
        "Status": "INVITED",
        "UpdatedTime": 1579826107000
   },
   {
        "AccountId": "123456789012",
        "AdministratorId": "111122223333",
        "EmailAddress": "jstiles@example.com",
        "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234",
        "InvitedTime": 1579826107000,
        "MasterId": "111122223333",
        "Status": "VERIFICATION_IN_PROGRESS",
        "UpdatedTime": 1579826107000
     }
    ],
    "UnprocessedAccounts": [ ]
}
```

For more information, see [`Inviting member accounts to a behavior graph<https://docs.aws.amazon.com/detective/latest/adminguide/graph-admin-add-member-accounts.html>`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html#id1) in the *Amazon Detective Administration Guide*.

## Output

Members -> (list)

The set of member account invitation or enablement requests that Detective was able to process. This includes accounts that are being verified, that failed verification, and that passed verification and are being sent an invitation or are being enabled.

(structure)

Details about a member account in a behavior graph.

AccountId -> (string)

The Amazon Web Services account identifier for the member account.

EmailAddress -> (string)

The Amazon Web Services account root user email address for the member account.

GraphArn -> (string)

The ARN of the behavior graph.

MasterId -> (string)

The Amazon Web Services account identifier of the administrator account for the behavior graph.

AdministratorId -> (string)

The Amazon Web Services account identifier of the administrator account for the behavior graph.

Status -> (string)

The current membership status of the member account. The status can have one of the following values:

- `INVITED` - For invited accounts only. Indicates that the member was sent an invitation but has not yet responded.
- `VERIFICATION_IN_PROGRESS` - For invited accounts only, indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier donât match, then the member cannot be added to the behavior graph. For organization accounts in the organization behavior graph, indicates that Detective is verifying that the account belongs to the organization.
- `VERIFICATION_FAILED` - For invited accounts only. Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
- `ENABLED` - Indicates that the member account currently contributes data to the behavior graph. For invited accounts, the member account accepted the invitation. For organization accounts in the organization behavior graph, the Detective administrator account enabled the organization account as a member account.
- `ACCEPTED_BUT_DISABLED` - The account accepted the invitation, or was enabled by the Detective administrator account, but is prevented from contributing data to the behavior graph. `DisabledReason` provides the reason why the member account is not enabled.

Invited accounts that declined an invitation or that were removed from the behavior graph are not included. In the organization behavior graph, organization accounts that the Detective administrator account did not enable are not included.

DisabledReason -> (string)

For member accounts with a status of `ACCEPTED_BUT_DISABLED` , the reason that the member account is not enabled.

The reason can have one of the following values:

- `VOLUME_TOO_HIGH` - Indicates that adding the member account would cause the data volume for the behavior graph to be too high.
- `VOLUME_UNKNOWN` - Indicates that Detective is unable to verify the data volume for the member account. This is usually because the member account is not enrolled in Amazon GuardDuty.

InvitedTime -> (timestamp)

For invited accounts, the date and time that Detective sent the invitation to the account. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z` .

UpdatedTime -> (timestamp)

The date and time that the member account was last updated. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z` .

VolumeUsageInBytes -> (long)

The data volume in bytes per day for the member account.

VolumeUsageUpdatedTime -> (timestamp)

The data and time when the member account data volume was last updated. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z` .

PercentOfGraphUtilization -> (double)

The member account data volume as a percentage of the maximum allowed data volume. 0 indicates 0 percent, and 100 indicates 100 percent.

Note that this is not the percentage of the behavior graph data volume.

For example, the data volume for the behavior graph is 80 GB per day. The maximum data volume is 160 GB per day. If the data volume for the member account is 40 GB per day, then `PercentOfGraphUtilization` is 25. It represents 25% of the maximum allowed data volume.

PercentOfGraphUtilizationUpdatedTime -> (timestamp)

The date and time when the graph utilization percentage was last updated. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z` .

InvitationType -> (string)

The type of behavior graph membership.

For an organization account in the organization behavior graph, the type is `ORGANIZATION` .

For an account that was invited to a behavior graph, the type is `INVITATION` .

VolumeUsageByDatasourcePackage -> (map)

Details on the volume of usage for each data source package in a behavior graph.

key -> (string)

value -> (structure)

Information on the usage of a data source package in the behavior graph.

VolumeUsageInBytes -> (long)

Total volume of data in bytes per day ingested for a given data source package.

VolumeUsageUpdateTime -> (timestamp)

The data and time when the member account data volume was last updated. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z` .

DatasourcePackageIngestStates -> (map)

The state of a data source package for the behavior graph.

key -> (string)

value -> (string)

UnprocessedAccounts -> (list)

The list of accounts for which Detective was unable to process the invitation or enablement request. For each account, the list provides the reason why the request could not be processed. The list includes accounts that are already member accounts in the behavior graph.

(structure)

A member account that was included in a request but for which the request could not be processed.

AccountId -> (string)

The Amazon Web Services account identifier of the member account that was not processed.

Reason -> (string)

The reason that the member account request could not be processed.