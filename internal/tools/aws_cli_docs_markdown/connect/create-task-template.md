# create-task-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-task-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-task-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# create-task-template

## Description

Creates a new task template in the specified Amazon Connect instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/CreateTaskTemplate)

## Synopsis

```
create-task-template
--instance-id <value>
--name <value>
[--description <value>]
[--contact-flow-id <value>]
[--self-assign-flow-id <value>]
[--constraints <value>]
[--defaults <value>]
[--status <value>]
--fields <value>
[--client-token <value>]
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

`--name` (string)

The name of the task template.

`--description` (string)

The description of the task template.

`--contact-flow-id` (string)

The identifier of the flow that runs by default when a task is created by referencing this template.

`--self-assign-flow-id` (string)

The ContactFlowId for the flow that will be run if this template is used to create a self-assigned task.

`--constraints` (structure)

Constraints that are applicable to the fields listed.

RequiredFields -> (list)

Lists the fields that are required to be filled by agents.

(structure)

Information about a required field.

Id -> (structure)

The unique identifier for the field.

Name -> (string)

The name of the task template field.

ReadOnlyFields -> (list)

Lists the fields that are read-only to agents, and cannot be edited.

(structure)

Indicates a field that is read-only to an agent.

Id -> (structure)

Identifier of the read-only field.

Name -> (string)

The name of the task template field.

InvisibleFields -> (list)

Lists the fields that are invisible to agents.

(structure)

A field that is invisible to an agent.

Id -> (structure)

Identifier of the invisible field.

Name -> (string)

The name of the task template field.

JSON Syntax:

```
{
  "RequiredFields": [
    {
      "Id": {
        "Name": "string"
      }
    }
    ...
  ],
  "ReadOnlyFields": [
    {
      "Id": {
        "Name": "string"
      }
    }
    ...
  ],
  "InvisibleFields": [
    {
      "Id": {
        "Name": "string"
      }
    }
    ...
  ]
}
```

`--defaults` (structure)

The default values for fields when a task is created by referencing this template.

DefaultFieldValues -> (list)

Default value for the field.

(structure)

Describes a default field and its corresponding value.

Id -> (structure)

Identifier of a field.

Name -> (string)

The name of the task template field.

DefaultValue -> (string)

Default value for the field.

JSON Syntax:

```
{
  "DefaultFieldValues": [
    {
      "Id": {
        "Name": "string"
      },
      "DefaultValue": "string"
    }
    ...
  ]
}
```

`--status` (string)

Marks a template as `ACTIVE` or `INACTIVE` for a task to refer to it. Tasks can only be created from `ACTIVE` templates. If a template is marked as `INACTIVE` , then a task that refers to this template cannot be created.

Possible values:

- `ACTIVE`
- `INACTIVE`

`--fields` (list)

Fields that are part of the template.

(structure)

Describes a single task template field.

Id -> (structure)

The unique identifier for the field.

Name -> (string)

The name of the task template field.

Description -> (string)

The description of the field.

Type -> (string)

Indicates the type of field.

SingleSelectOptions -> (list)

A list of options for a single select field.

(string)

Shorthand Syntax:

```
Id={Name=string},Description=string,Type=string,SingleSelectOptions=string,string ...
```

JSON Syntax:

```
[
  {
    "Id": {
      "Name": "string"
    },
    "Description": "string",
    "Type": "NAME"|"DESCRIPTION"|"SCHEDULED_TIME"|"QUICK_CONNECT"|"URL"|"NUMBER"|"TEXT"|"TEXT_AREA"|"DATE_TIME"|"BOOLEAN"|"SINGLE_SELECT"|"EMAIL"|"SELF_ASSIGN"|"EXPIRY_DURATION",
    "SingleSelectOptions": ["string", ...]
  }
  ...
]
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) .

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

Id -> (string)

The identifier of the task template resource.

Arn -> (string)

The Amazon Resource Name (ARN) for the task template resource.