# update-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/update-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/update-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connectcases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/index.html#cli-aws-connectcases) ]

# update-template

## Description

Updates the attributes of an existing template. The template attributes that can be modified include `name` , `description` , `layoutConfiguration` , `requiredFields` , and `status` . At least one of these attributes must not be null. If a null value is provided for a given attribute, that attribute is ignored and its current value is preserved.

Other template APIs are:

- [CreateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html)
- [DeleteTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html)
- [GetTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html)
- [ListTemplates](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connectcases-2022-10-03/UpdateTemplate)

## Synopsis

```
update-template
[--description <value>]
--domain-id <value>
[--layout-configuration <value>]
[--name <value>]
[--required-fields <value>]
[--rules <value>]
[--status <value>]
--template-id <value>
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

`--description` (string)

A brief description of the template.

`--domain-id` (string)

The unique identifier of the Cases domain.

`--layout-configuration` (structure)

Configuration of layouts associated to the template.

defaultLayout -> (string)

Unique identifier of a layout.

Shorthand Syntax:

```
defaultLayout=string
```

JSON Syntax:

```
{
  "defaultLayout": "string"
}
```

`--name` (string)

The name of the template. It must be unique per domain.

`--required-fields` (list)

A list of fields that must contain a value for a case to be successfully created with this template.

(structure)

List of fields that must have a value provided to create a case.

fieldId -> (string)

Unique identifier of a field.

Shorthand Syntax:

```
fieldId=string ...
```

JSON Syntax:

```
[
  {
    "fieldId": "string"
  }
  ...
]
```

`--rules` (list)

A list of case rules (also known as [case field conditions](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html) ) on a template.

(structure)

An association representing a case rule acting upon a field. In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html) .

caseRuleId -> (string)

Unique identifier of a case rule.

fieldId -> (string)

Unique identifier of a field.

Shorthand Syntax:

```
caseRuleId=string,fieldId=string ...
```

JSON Syntax:

```
[
  {
    "caseRuleId": "string",
    "fieldId": "string"
  }
  ...
]
```

`--status` (string)

The status of the template.

Possible values:

- `Active`
- `Inactive`

`--template-id` (string)

A unique identifier for the template.

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