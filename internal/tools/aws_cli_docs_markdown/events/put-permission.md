# put-permissionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-permission.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-permission.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html#cli-aws-events) ]

# put-permission

## Description

Running `PutPermission` permits the specified Amazon Web Services account or Amazon Web Services organization to put events to the specified *event bus* . Amazon EventBridge rules in your account are triggered by these events arriving to an event bus in your account.

For another account to send events to your account, that external account must have an EventBridge rule with your accountâs event bus as a target.

To enable multiple Amazon Web Services accounts to put events to your event bus, run `PutPermission` once for each of these accounts. Or, if all the accounts are members of the same Amazon Web Services organization, you can run `PutPermission` once specifying `Principal` as â*â and specifying the Amazon Web Services organization ID in `Condition` , to grant permissions to all accounts in that organization.

If you grant permissions using an organization, then accounts in that organization must specify a `RoleArn` with proper permissions when they use `PutTarget` to add your accountâs event bus as a target. For more information, see [Sending and Receiving Events Between Amazon Web Services Accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html) in the *Amazon EventBridge User Guide* .

The permission policy on the event bus cannot exceed 10 KB in size.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/PutPermission)

## Synopsis

```
put-permission
[--event-bus-name <value>]
[--action <value>]
[--principal <value>]
[--statement-id <value>]
[--condition <value>]
[--policy <value>]
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

`--event-bus-name` (string)

The name of the event bus associated with the rule. If you omit this, the default event bus is used.

`--action` (string)

The action that you are enabling the other account to perform.

`--principal` (string)

The 12-digit Amazon Web Services account ID that you are permitting to put events to your default event bus. Specify â*â to permit any account to put events to your default event bus.

If you specify â*â without specifying `Condition` , avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an `account` field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.

`--statement-id` (string)

An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this `StatementId` when you run [RemovePermission](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemovePermission.html) .

### Note

Each `StatementId` must be unique.

`--condition` (structure)

This parameter enables you to limit the permission to accounts that fulfill a certain condition, such as being a member of a certain Amazon Web Services organization. For more information about Amazon Web Services Organizations, see [What Is Amazon Web Services Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) in the *Amazon Web Services Organizations User Guide* .

If you specify `Condition` with an Amazon Web Services organization ID, and specify â*â as the value for `Principal` , you grant permission to all the accounts in the named organization.

The `Condition` is a JSON string which must contain `Type` , `Key` , and `Value` fields.

Type -> (string)

Specifies the type of condition. Currently the only supported value is `StringEquals` .

Key -> (string)

Specifies the key for the condition. Currently the only supported key is `aws:PrincipalOrgID` .

Value -> (string)

Specifies the value for the key. Currently, this must be the ID of the organization.

Shorthand Syntax:

```
Type=string,Key=string,Value=string
```

JSON Syntax:

```
{
  "Type": "string",
  "Key": "string",
  "Value": "string"
}
```

`--policy` (string)

A JSON string that describes the permission policy statement. You can include a `Policy` parameter in the request instead of using the `StatementId` , `Action` , `Principal` , or `Condition` parameters.

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

None