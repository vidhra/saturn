# create-traffic-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/create-traffic-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/create-traffic-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mailmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/index.html#cli-aws-mailmanager) ]

# create-traffic-policy

## Description

Provision a new traffic policy resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mailmanager-2023-10-17/CreateTrafficPolicy)

## Synopsis

```
create-traffic-policy
[--client-token <value>]
--default-action <value>
[--max-message-size-bytes <value>]
--policy-statements <value>
[--tags <value>]
--traffic-policy-name <value>
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

`--client-token` (string)

A unique token that Amazon SES uses to recognize subsequent retries of the same request.

`--default-action` (string)

Default action instructs the traï¬c policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements

Possible values:

- `ALLOW`
- `DENY`

`--max-message-size-bytes` (integer)

The maximum message size in bytes of email which is allowed in by this traffic policyâanything larger will be blocked.

`--policy-statements` (list)

Conditional statements for filtering email traffic.

(structure)

The structure containing traffic policy conditions and actions.

Action -> (string)

The action that informs a traffic policy resource to either allow or block the email if it matches a condition in the policy statement.

Conditions -> (list)

The list of conditions to apply to incoming messages for filtering email traffic.

(tagged union structure)

The email traffic filtering conditions which are contained in a traffic policy resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BooleanExpression`, `IpExpression`, `Ipv6Expression`, `StringExpression`, `TlsExpression`.

BooleanExpression -> (structure)

This represents a boolean type condition matching on the incoming mail. It performs the boolean operation configured in âOperatorâ and evaluates the âProtocolâ object against the âValueâ.

Evaluate -> (tagged union structure)

The operand on which to perform a boolean condition operation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Analysis`, `IsInAddressList`.

Analysis -> (structure)

The structure type for a boolean condition stating the Add On ARN and its returned value.

Analyzer -> (string)

The Amazon Resource Name (ARN) of an Add On.

ResultField -> (string)

The returned value from an Add On.

IsInAddressList -> (structure)

The structure type for a boolean condition that provides the address lists to evaluate incoming traffic on.

AddressLists -> (list)

The address lists that will be used for evaluation.

(string)

Attribute -> (string)

The email attribute that needs to be evaluated against the address list.

Operator -> (string)

The matching operator for a boolean condition expression.

IpExpression -> (structure)

This represents an IP based condition matching on the incoming mail. It performs the operation configured in âOperatorâ and evaluates the âProtocolâ object against the âValueâ.

Evaluate -> (tagged union structure)

The left hand side argument of an IP condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Attribute`.

Attribute -> (string)

An enum type representing the allowed attribute types for an IP condition.

Operator -> (string)

The matching operator for an IP condition expression.

Values -> (list)

The right hand side argument of an IP condition expression.

(string)

Ipv6Expression -> (structure)

This represents an IPv6 based condition matching on the incoming mail. It performs the operation configured in âOperatorâ and evaluates the âProtocolâ object against the âValueâ.

Evaluate -> (tagged union structure)

The left hand side argument of an IPv6 condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Attribute`.

Attribute -> (string)

An enum type representing the allowed attribute types for an IPv6 condition.

Operator -> (string)

The matching operator for an IPv6 condition expression.

Values -> (list)

The right hand side argument of an IPv6 condition expression.

(string)

StringExpression -> (structure)

This represents a string based condition matching on the incoming mail. It performs the string operation configured in âOperatorâ and evaluates the âProtocolâ object against the âValueâ.

Evaluate -> (tagged union structure)

The left hand side argument of a string condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Analysis`, `Attribute`.

Analysis -> (structure)

The structure type for a string condition stating the Add On ARN and its returned value.

Analyzer -> (string)

The Amazon Resource Name (ARN) of an Add On.

ResultField -> (string)

The returned value from an Add On.

Attribute -> (string)

The enum type representing the allowed attribute types for a string condition.

Operator -> (string)

The matching operator for a string condition expression.

Values -> (list)

The right hand side argument of a string condition expression.

(string)

TlsExpression -> (structure)

This represents a TLS based condition matching on the incoming mail. It performs the operation configured in âOperatorâ and evaluates the âProtocolâ object against the âValueâ.

Evaluate -> (tagged union structure)

The left hand side argument of a TLS condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Attribute`.

Attribute -> (string)

The enum type representing the allowed attribute types for the TLS condition.

Operator -> (string)

The matching operator for a TLS condition expression.

Value -> (string)

The right hand side argument of a TLS condition expression.

JSON Syntax:

```
[
  {
    "Action": "ALLOW"|"DENY",
    "Conditions": [
      {
        "BooleanExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "string",
              "ResultField": "string"
            },
            "IsInAddressList": {
              "AddressLists": ["string", ...],
              "Attribute": "RECIPIENT"
            }
          },
          "Operator": "IS_TRUE"|"IS_FALSE"
        },
        "IpExpression": {
          "Evaluate": {
            "Attribute": "SENDER_IP"
          },
          "Operator": "CIDR_MATCHES"|"NOT_CIDR_MATCHES",
          "Values": ["string", ...]
        },
        "Ipv6Expression": {
          "Evaluate": {
            "Attribute": "SENDER_IPV6"
          },
          "Operator": "CIDR_MATCHES"|"NOT_CIDR_MATCHES",
          "Values": ["string", ...]
        },
        "StringExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "string",
              "ResultField": "string"
            },
            "Attribute": "RECIPIENT"
          },
          "Operator": "EQUALS"|"NOT_EQUALS"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS",
          "Values": ["string", ...]
        },
        "TlsExpression": {
          "Evaluate": {
            "Attribute": "TLS_PROTOCOL"
          },
          "Operator": "MINIMUM_TLS_VERSION"|"IS",
          "Value": "TLS1_2"|"TLS1_3"
        }
      }
      ...
    ]
  }
  ...
]
```

`--tags` (list)

The tags used to organize, track, or control access for the resource. For example, { âtagsâ: {âkey1â:âvalue1â, âkey2â:âvalue2â} }.

(structure)

A key-value pair (the value is optional), that you can define and assign to Amazon Web Services resources.

Key -> (string)

The key of the key-value tag.

Value -> (string)

The value of the key-value tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--traffic-policy-name` (string)

A user-friendly name for the traffic policy resource.

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

TrafficPolicyId -> (string)

The identifier of the traffic policy resource.