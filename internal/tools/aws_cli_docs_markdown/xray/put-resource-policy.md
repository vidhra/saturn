# put-resource-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-resource-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-resource-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [xray](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/index.html#cli-aws-xray) ]

# put-resource-policy

## Description

Sets the resource policy to grant one or more Amazon Web Services services and accounts permissions to access X-Ray. Each resource policy will be associated with a specific Amazon Web Services account. Each Amazon Web Services account can have a maximum of 5 resource policies, and each policy name must be unique within that account. The maximum size of each resource policy is 5KB.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/PutResourcePolicy)

## Synopsis

```
put-resource-policy
--policy-name <value>
--policy-document <value>
[--policy-revision-id <value>]
[--bypass-policy-lockout-check | --no-bypass-policy-lockout-check]
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

`--policy-name` (string)

The name of the resource policy. Must be unique within a specific Amazon Web Services account.

`--policy-document` (string)

The resource policy document, which can be up to 5kb in size.

`--policy-revision-id` (string)

Specifies a specific policy revision, to ensure an atomic create operation. By default the resource policy is created if it does not exist, or updated with an incremented revision id. The revision id is unique to each policy in the account.

If the policy revision id does not match the latest revision id, the operation will fail with an `InvalidPolicyRevisionIdException` exception. You can also provide a `PolicyRevisionId` of 0. In this case, the operation will fail with an `InvalidPolicyRevisionIdException` exception if a resource policy with the same name already exists.

`--bypass-policy-lockout-check` | `--no-bypass-policy-lockout-check` (boolean)

A flag to indicate whether to bypass the resource policy lockout safety check.

### Warning

Setting this value to true increases the risk that the policy becomes unmanageable. Do not set this value to true indiscriminately.

Use this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent `PutResourcePolicy` request.

The default value is false.

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

ResourcePolicy -> (structure)

The resource policy document, as provided in the `PutResourcePolicyRequest` .

PolicyName -> (string)

The name of the resource policy. Must be unique within a specific Amazon Web Services account.

PolicyDocument -> (string)

The resource policy document, which can be up to 5kb in size.

PolicyRevisionId -> (string)

Returns the current policy revision id for this policy name.

LastUpdatedTime -> (timestamp)

When the policy was last updated, in Unix time seconds.