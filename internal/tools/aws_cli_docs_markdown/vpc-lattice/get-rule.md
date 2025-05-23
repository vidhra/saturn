# get-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [vpc-lattice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/index.html#cli-aws-vpc-lattice) ]

# get-rule

## Description

Retrieves information about the specified listener rules. You can also retrieve information about the default listener rule. For more information, see [Listener rules](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules) in the *Amazon VPC Lattice User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/vpc-lattice-2022-11-30/GetRule)

## Synopsis

```
get-rule
--listener-identifier <value>
--rule-identifier <value>
--service-identifier <value>
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

`--listener-identifier` (string)

The ID or ARN of the listener.

`--rule-identifier` (string)

The ID or ARN of the listener rule.

`--service-identifier` (string)

The ID or ARN of the service.

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

action -> (tagged union structure)

The action for the default rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixedResponse`, `forward`.

fixedResponse -> (structure)

The fixed response action. The rule returns a custom HTTP response.

statusCode -> (integer)

The HTTP response code.

forward -> (structure)

The forward action. Traffic that matches the rule is forwarded to the specified target groups.

targetGroups -> (list)

The target groups. Traffic matching the rule is forwarded to the specified target groups. With forward actions, you can assign a weight that controls the prioritization and selection of each target group. This means that requests are distributed to individual target groups based on their weights. For example, if two target groups have the same weight, each target group receives half of the traffic.

The default value is 1. This means that if only one target group is provided, there is no need to set the weight; 100% of the traffic goes to that target group.

(structure)

Describes the weight of a target group.

targetGroupIdentifier -> (string)

The ID or ARN of the target group.

weight -> (integer)

Only required if you specify multiple target groups for a forward action. The weight determines how requests are distributed to the target group. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group. If thereâs only one target group specified, then the default value is 100.

arn -> (string)

The Amazon Resource Name (ARN) of the listener.

createdAt -> (timestamp)

The date and time that the listener rule was created, in ISO-8601 format.

id -> (string)

The ID of the listener.

isDefault -> (boolean)

Indicates whether this is the default rule.

lastUpdatedAt -> (timestamp)

The date and time that the listener rule was last updated, in ISO-8601 format.

match -> (tagged union structure)

The rule match.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `httpMatch`.

httpMatch -> (structure)

The HTTP criteria that a rule must match.

headerMatches -> (list)

The header matches. Matches incoming requests with rule based on request header value before applying rule action.

(structure)

Describes the constraints for a header match. Matches incoming requests with rule based on request header value before applying rule action.

caseSensitive -> (boolean)

Indicates whether the match is case sensitive.

match -> (tagged union structure)

The header match type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `contains`, `exact`, `prefix`.

contains -> (string)

A contains type match.

exact -> (string)

An exact type match.

prefix -> (string)

A prefix type match. Matches the value with the prefix.

name -> (string)

The name of the header.

method -> (string)

The HTTP method type.

pathMatch -> (structure)

The path match.

caseSensitive -> (boolean)

Indicates whether the match is case sensitive.

match -> (tagged union structure)

The type of path match.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `exact`, `prefix`.

exact -> (string)

An exact match of the path.

prefix -> (string)

A prefix match of the path.

name -> (string)

The name of the listener.

priority -> (integer)

The priority level for the specified rule.