# update-recipeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-recipe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-recipe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [databrew](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/index.html#cli-aws-databrew) ]

# update-recipe

## Description

Modifies the definition of the `LATEST_WORKING` version of a DataBrew recipe.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/databrew-2017-07-25/UpdateRecipe)

## Synopsis

```
update-recipe
[--description <value>]
--name <value>
[--steps <value>]
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

A description of the recipe.

`--name` (string)

The name of the recipe to be updated.

`--steps` (list)

One or more steps to be performed by the recipe. Each step consists of an action, and the conditions under which the action should succeed.

(structure)

Represents a single step from a DataBrew recipe to be performed.

Action -> (structure)

The particular action to be performed in the recipe step.

Operation -> (string)

The name of a valid DataBrew transformation to be performed on the data.

Parameters -> (map)

Contextual parameters for the transformation.

key -> (string)

value -> (string)

ConditionExpressions -> (list)

One or more conditions that must be met for the recipe step to succeed.

### Note

All of the conditions in the array must be met. In other words, all of the conditions must be combined using a logical AND operation.

(structure)

Represents an individual condition that evaluates to true or false.

Conditions are used with recipe actions. The action is only performed for column values where the condition evaluates to true.

If a recipe requires more than one condition, then the recipe must specify multiple `ConditionExpression` elements. Each condition is applied to the rows in a dataset first, before the recipe action is performed.

Condition -> (string)

A specific condition to apply to a recipe action. For more information, see [Recipe structure](https://docs.aws.amazon.com/databrew/latest/dg/recipes.html#recipes.structure) in the *Glue DataBrew Developer Guide* .

Value -> (string)

A value that the condition must evaluate to for the condition to succeed.

TargetColumn -> (string)

A column to apply this condition to.

Shorthand Syntax:

```
Action={Operation=string,Parameters={KeyName1=string,KeyName2=string}},ConditionExpressions=[{Condition=string,Value=string,TargetColumn=string},{Condition=string,Value=string,TargetColumn=string}] ...
```

JSON Syntax:

```
[
  {
    "Action": {
      "Operation": "string",
      "Parameters": {"string": "string"
        ...}
    },
    "ConditionExpressions": [
      {
        "Condition": "string",
        "Value": "string",
        "TargetColumn": "string"
      }
      ...
    ]
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

## Output

Name -> (string)

The name of the recipe that was updated.