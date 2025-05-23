# update-contact-routing-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact-routing-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact-routing-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# update-contact-routing-data

## Description

Updates routing priority and age on the contact (**QueuePriority** and **QueueTimeAdjustmentInSeconds** ). These properties can be used to change a customerâs position in the queue. For example, you can move a contact to the back of the queue by setting a lower routing priority relative to other contacts in queue; or you can move a contact to the front of the queue by increasing the routing age which will make the contact look artificially older and therefore higher up in the first-in-first-out routing order. Note that adjusting the routing age of a contact affects only its position in queue, and not its actual queue wait time as reported through metrics. These properties can also be updated by using [the Set routing priority / age flow block](https://docs.aws.amazon.com/connect/latest/adminguide/change-routing-priority.html) .

### Note

Either **QueuePriority** or **QueueTimeAdjustmentInSeconds** should be provided within the request body, but not both.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateContactRoutingData)

## Synopsis

```
update-contact-routing-data
--instance-id <value>
--contact-id <value>
[--queue-time-adjustment-seconds <value>]
[--queue-priority <value>]
[--routing-criteria <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--contact-id` (string)

The identifier of the contact in this instance of Amazon Connect.

`--queue-time-adjustment-seconds` (integer)

The number of seconds to add or subtract from the contactâs routing age. Contacts are routed to agents on a first-come, first-serve basis. This means that changing their amount of time in queue compared to others also changes their position in queue.

`--queue-priority` (long)

Priority of the contact in the queue. The default priority for new contacts is 5. You can raise the priority of a contact compared to other contacts in the queue by assigning them a higher priority, such as 1 or 2.

`--routing-criteria` (structure)

Updates the routing criteria on the contact. These properties can be used to change how a contact is routed within the queue.

Steps -> (list)

When Amazon Connect does not find an available agent meeting the requirements in a step for a given step duration, the routing criteria will move on to the next step sequentially until a join is completed with an agent. When all steps are exhausted, the contact will be offered to any agent in the queue.

(structure)

Step defines the list of agents to be routed or route based on the agent requirements such as ProficiencyLevel, Name, or Value.

Expiry -> (structure)

An object to specify the expiration of a routing step.

DurationInSeconds -> (integer)

The number of seconds that the contact will be routed only to agents matching this routing step, if expiry was configured for this routing step.

Expression -> (structure)

A tagged union to specify expression for a routing step.

AttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

AndExpression -> (list)

List of routing expressions which will be AND-ed together.

(structure)

A tagged union to specify expression for a routing step.

AttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

AndExpression -> (list)

List of routing expressions which will be AND-ed together.

( â¦ recursive â¦ )

OrExpression -> (list)

List of routing expressions which will be OR-ed together.

( â¦ recursive â¦ )

NotAttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

OrExpression -> (list)

List of routing expressions which will be OR-ed together.

(structure)

A tagged union to specify expression for a routing step.

AttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

AndExpression -> (list)

List of routing expressions which will be AND-ed together.

( â¦ recursive â¦ )

OrExpression -> (list)

List of routing expressions which will be OR-ed together.

( â¦ recursive â¦ )

NotAttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

NotAttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

JSON Syntax:

```
{
  "Steps": [
    {
      "Expiry": {
        "DurationInSeconds": integer
      },
      "Expression": {
        "AttributeCondition": {
          "Name": "string",
          "Value": "string",
          "ProficiencyLevel": float,
          "Range": {
            "MinProficiencyLevel": float,
            "MaxProficiencyLevel": float
          },
          "MatchCriteria": {
            "AgentsCriteria": {
              "AgentIds": ["string", ...]
            }
          },
          "ComparisonOperator": "string"
        },
        "AndExpression": [
          {
            "AttributeCondition": {
              "Name": "string",
              "Value": "string",
              "ProficiencyLevel": float,
              "Range": {
                "MinProficiencyLevel": float,
                "MaxProficiencyLevel": float
              },
              "MatchCriteria": {
                "AgentsCriteria": {
                  "AgentIds": ["string", ...]
                }
              },
              "ComparisonOperator": "string"
            },
            "AndExpression": [
              { ... recursive ... }
              ...
            ],
            "OrExpression": [
              { ... recursive ... }
              ...
            ],
            "NotAttributeCondition": {
              "Name": "string",
              "Value": "string",
              "ProficiencyLevel": float,
              "Range": {
                "MinProficiencyLevel": float,
                "MaxProficiencyLevel": float
              },
              "MatchCriteria": {
                "AgentsCriteria": {
                  "AgentIds": ["string", ...]
                }
              },
              "ComparisonOperator": "string"
            }
          }
          ...
        ],
        "OrExpression": [
          {
            "AttributeCondition": {
              "Name": "string",
              "Value": "string",
              "ProficiencyLevel": float,
              "Range": {
                "MinProficiencyLevel": float,
                "MaxProficiencyLevel": float
              },
              "MatchCriteria": {
                "AgentsCriteria": {
                  "AgentIds": ["string", ...]
                }
              },
              "ComparisonOperator": "string"
            },
            "AndExpression": [
              { ... recursive ... }
              ...
            ],
            "OrExpression": [
              { ... recursive ... }
              ...
            ],
            "NotAttributeCondition": {
              "Name": "string",
              "Value": "string",
              "ProficiencyLevel": float,
              "Range": {
                "MinProficiencyLevel": float,
                "MaxProficiencyLevel": float
              },
              "MatchCriteria": {
                "AgentsCriteria": {
                  "AgentIds": ["string", ...]
                }
              },
              "ComparisonOperator": "string"
            }
          }
          ...
        ],
        "NotAttributeCondition": {
          "Name": "string",
          "Value": "string",
          "ProficiencyLevel": float,
          "Range": {
            "MinProficiencyLevel": float,
            "MaxProficiencyLevel": float
          },
          "MatchCriteria": {
            "AgentsCriteria": {
              "AgentIds": ["string", ...]
            }
          },
          "ComparisonOperator": "string"
        }
      }
    }
    ...
  ]
}
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

## Output

None