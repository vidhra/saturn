# assume-rootÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-root.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-root.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/index.html#cli-aws-sts) ]

# assume-root

## Description

Returns a set of short term credentials you can use to perform privileged tasks on a member account in your organization.

Before you can launch a privileged session, you must have centralized root access in your organization. For steps to enable this feature, see [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) in the *IAM User Guide* .

### Note

The STS global endpoint is not supported for AssumeRoot. You must send this request to a Regional STS endpoint. For more information, see [Endpoints](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html#sts-endpoints) .

You can track AssumeRoot in CloudTrail logs to determine what actions were performed in a session. For more information, see [Track privileged tasks in CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html) in the *IAM User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/AssumeRoot)

## Synopsis

```
assume-root
--target-principal <value>
--task-policy-arn <value>
[--duration-seconds <value>]
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

`--target-principal` (string)

The member account principal ARN or account ID.

`--task-policy-arn` (structure)

The identity based policy that scopes the session to the privileged tasks that can be performed. You can use one of following Amazon Web Services managed policies to scope root session actions.

- [IAMAuditRootUserCredentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMAuditRootUserCredentials)
- [IAMCreateRootUserPassword](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMCreateRootUserPassword)
- [IAMDeleteRootUserCredentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMDeleteRootUserCredentials)
- [S3UnlockBucketPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-S3UnlockBucketPolicy)
- [SQSUnlockQueuePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-SQSUnlockQueuePolicy)

arn -> (string)

The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

Shorthand Syntax:

```
arn=string
```

JSON Syntax:

```
{
  "arn": "string"
}
```

`--duration-seconds` (integer)

The duration, in seconds, of the privileged session. The value can range from 0 seconds up to the maximum session duration of 900 seconds (15 minutes). If you specify a value higher than this setting, the operation fails.

By default, the value is set to `900` seconds.

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

**To launch a privileged session**

The following `assume-root` command retrieves a set of short-term credentials you can use to remove a misconfigured Amazon S3 bucket policy for a member account in your organization.

```
aws sts assume-root \
    --duration-seconds 900 \
    --target-principal 111122223333 \
    --task-policy-arn arn=arn:aws:iam::aws:policy/root-task/S3UnlockBucketPolicy
```

Output:

```
{
    "Credentials": {
        "SecretAccessKey": "9drTJvcXLB89EXAMPLELB8923FB892xMFI",
        "SessionToken": "AQoXdzELDDY//////////wEaoAK1wvxJY12r2IrDFT2IvAzTCn3zHoZ7YNtpiQLF0MqZye/qwjzP2iEXAMPLEbw/m3hsj8VBTkPORGvr9jM5sgP+w9IZWZnU+LWhmg+a5fDi2oTGUYcdg9uexQ4mtCHIHfi4citgqZTgco40Yqr4lIlo4V2b2Dyauk0eYFNebHtYlFVgAUj+7Indz3LU0aTWk1WKIjHmmMCIoTkyYp/k7kUG7moeEYKSitwQIi6Gjn+nyzM+PtoA3685ixzv0R7i5rjQi0YE0lf1oeie3bDiNHncmzosRM6SFiPzSvp6h/32xQuZsjcypmwsPSDtTPYcs0+YN/8BRi2/IcrxSpnWEXAMPLEXSDFTAQAM6Dl9zR0tXoybnlrZIwMLlMi1Kcgo5OytwU=",
        "Expiration": "2024-11-15T00:05:07Z",
        "AccessKeyId": "ASIAJEXAMPLEXEG2JICEA"
    },
    "SourceIdentity": "Alice",
}
```

The output of the command contains an access key, secret key, and session token that you can use to  to perform privileged actions in the member account. For more information, see [Perform a privileged task on an AWS Organizations member account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html) in the *AWS IAM User Guide*.

## Output

Credentials -> (structure)

The temporary security credentials, which include an access key ID, a secret access key, and a security token.

### Note

The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.

AccessKeyId -> (string)

The access key ID that identifies the temporary security credentials.

SecretAccessKey -> (string)

The secret access key that can be used to sign requests.

SessionToken -> (string)

The token that users must pass to the service API to use the temporary credentials.

Expiration -> (timestamp)

The date on which the current credentials expire.

SourceIdentity -> (string)

The source identity specified by the principal that is calling the `AssumeRoot` operation.

You can use the `aws:SourceIdentity` condition key to control access based on the value of source identity. For more information about using source identity, see [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html) in the *IAM User Guide* .

The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-