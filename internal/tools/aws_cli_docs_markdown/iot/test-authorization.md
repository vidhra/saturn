# test-authorizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/test-authorization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/test-authorization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# test-authorization

## Description

Tests if a specified principal is authorized to perform an IoT action on a specified resource. Use this to test and debug the authorization behavior of devices that connect to the IoT device gateway.

Requires permission to access the [TestAuthorization](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/TestAuthorization)

## Synopsis

```
test-authorization
[--principal <value>]
[--cognito-identity-pool-id <value>]
--auth-infos <value>
[--client-id <value>]
[--policy-names-to-add <value>]
[--policy-names-to-skip <value>]
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

`--principal` (string)

The principal. Valid principals are CertificateArn (arn:aws:iot:*region* :*accountId* :cert/*certificateId* ), thingGroupArn (arn:aws:iot:*region* :*accountId* :thinggroup/*groupName* ) and CognitoId (*region* :*id* ).

`--cognito-identity-pool-id` (string)

The Cognito identity pool ID.

`--auth-infos` (list)

A list of authorization info objects. Simulating authorization will create a response for each `authInfo` object in the list.

(structure)

A collection of authorization information.

actionType -> (string)

The type of action for which the principal is being authorized.

resources -> (list)

The resources for which the principal is being authorized to perform the specified action.

(string)

Shorthand Syntax:

```
actionType=string,resources=string,string ...
```

JSON Syntax:

```
[
  {
    "actionType": "PUBLISH"|"SUBSCRIBE"|"RECEIVE"|"CONNECT",
    "resources": ["string", ...]
  }
  ...
]
```

`--client-id` (string)

The MQTT client ID.

`--policy-names-to-add` (list)

When testing custom authorization, the policies specified here are treated as if they are attached to the principal being authorized.

(string)

Syntax:

```
"string" "string" ...
```

`--policy-names-to-skip` (list)

When testing custom authorization, the policies specified here are treated as if they are not attached to the principal being authorized.

(string)

Syntax:

```
"string" "string" ...
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

**To test your AWS IoT policies**

The following `test-authorization` example tests the AWS IoT policies associated with the specified principal.

```
aws iot test-authorization \
    --auth-infos actionType=CONNECT,resources=arn:aws:iot:us-east-1:123456789012:client/client1 \
    --principal arn:aws:iot:us-west-2:123456789012:cert/aab1068f7f43ac3e3cae4b3a8aa3f308d2a750e6350507962e32c1eb465d9775
```

Output:

```
{
    "authResults": [
        {
            "authInfo": {
                "actionType": "CONNECT",
                "resources": [
                    "arn:aws:iot:us-east-1:123456789012:client/client1"
                ]
            },
            "allowed": {
                "policies": [
                    {
                        "policyName": "TestPolicyAllowed",
                        "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TestPolicyAllowed"
                    }
                ]
            },
            "denied": {
                "implicitDeny": {
                    "policies": [
                        {
                            "policyName": "TestPolicyDenied",
                            "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TestPolicyDenied"
                        }
                    ]
                },
                "explicitDeny": {
                    "policies": [
                        {
                            "policyName": "TestPolicyExplicitDenied",
                            "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TestPolicyExplicitDenied"
                        }
                    ]
                }
            },
            "authDecision": "IMPLICIT_DENY",
            "missingContextValues": []
        }
    ]
}
```

For more information, see [TestAuthorization](https://docs.aws.amazon.com/iot/latest/apireference/API_TestAuthorization.html) in the *AWS IoT API Reference*.

## Output

authResults -> (list)

The authentication results.

(structure)

The authorizer result.

authInfo -> (structure)

Authorization information.

actionType -> (string)

The type of action for which the principal is being authorized.

resources -> (list)

The resources for which the principal is being authorized to perform the specified action.

(string)

allowed -> (structure)

The policies and statements that allowed the specified action.

policies -> (list)

A list of policies that allowed the authentication.

(structure)

Describes an IoT policy.

policyName -> (string)

The policy name.

policyArn -> (string)

The policy ARN.

denied -> (structure)

The policies and statements that denied the specified action.

implicitDeny -> (structure)

Information that implicitly denies the authorization. When a policy doesnât explicitly deny or allow an action on a resource it is considered an implicit deny.

policies -> (list)

Policies that donât contain a matching allow or deny statement for the specified action on the specified resource.

(structure)

Describes an IoT policy.

policyName -> (string)

The policy name.

policyArn -> (string)

The policy ARN.

explicitDeny -> (structure)

Information that explicitly denies the authorization.

policies -> (list)

The policies that denied the authorization.

(structure)

Describes an IoT policy.

policyName -> (string)

The policy name.

policyArn -> (string)

The policy ARN.

authDecision -> (string)

The final authorization decision of this scenario. Multiple statements are taken into account when determining the authorization decision. An explicit deny statement can override multiple allow statements.

missingContextValues -> (list)

Contains any missing context values found while evaluating policy.

(string)