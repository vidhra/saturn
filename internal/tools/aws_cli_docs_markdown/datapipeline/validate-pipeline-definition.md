# validate-pipeline-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/validate-pipeline-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/validate-pipeline-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datapipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/index.html#cli-aws-datapipeline) ]

# validate-pipeline-definition

## Description

Validates the specified pipeline definition to ensure that it is well formed and can be run without error.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/ValidatePipelineDefinition)

## Synopsis

```
validate-pipeline-definition
--pipeline-id <value>
--pipeline-objects <value>
[--parameter-objects <value>]
[--parameter-values <value>]
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

`--pipeline-id` (string)

The ID of the pipeline.

`--pipeline-objects` (list)

The objects that define the pipeline changes to validate against the pipeline.

(structure)

Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

id -> (string)

The ID of the object.

name -> (string)

The name of the object.

fields -> (list)

Key-value pairs that define the properties of the object.

(structure)

A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (`StringValue` ) or a reference to another object (`RefValue` ) but not as both.

key -> (string)

The field identifier.

stringValue -> (string)

The field value, expressed as a String.

refValue -> (string)

The field value, expressed as the identifier of another object.

Shorthand Syntax:

```
id=string,name=string,fields=[{key=string,stringValue=string,refValue=string},{key=string,stringValue=string,refValue=string}] ...
```

JSON Syntax:

```
[
  {
    "id": "string",
    "name": "string",
    "fields": [
      {
        "key": "string",
        "stringValue": "string",
        "refValue": "string"
      }
      ...
    ]
  }
  ...
]
```

`--parameter-objects` (list)

The parameter objects used with the pipeline.

(structure)

Contains information about a parameter object.

id -> (string)

The ID of the parameter object.

attributes -> (list)

The attributes of the parameter object.

(structure)

The attributes allowed or specified with a parameter object.

key -> (string)

The field identifier.

stringValue -> (string)

The field value, expressed as a String.

Shorthand Syntax:

```
id=string,attributes=[{key=string,stringValue=string},{key=string,stringValue=string}] ...
```

JSON Syntax:

```
[
  {
    "id": "string",
    "attributes": [
      {
        "key": "string",
        "stringValue": "string"
      }
      ...
    ]
  }
  ...
]
```

`--parameter-values` (list)

The parameter values used with the pipeline.

(structure)

A value or list of parameter values.

id -> (string)

The ID of the parameter value.

stringValue -> (string)

The field value, expressed as a String.

Shorthand Syntax:

```
id=string,stringValue=string ...
```

JSON Syntax:

```
[
  {
    "id": "string",
    "stringValue": "string"
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

validationErrors -> (list)

Any validation errors that were found.

(structure)

Defines a validation error. Validation errors prevent pipeline activation. The set of validation errors that can be returned are defined by AWS Data Pipeline.

id -> (string)

The identifier of the object that contains the validation error.

errors -> (list)

A description of the validation error.

(string)

validationWarnings -> (list)

Any validation warnings that were found.

(structure)

Defines a validation warning. Validation warnings do not prevent pipeline activation. The set of validation warnings that can be returned are defined by AWS Data Pipeline.

id -> (string)

The identifier of the object that contains the validation warning.

warnings -> (list)

A description of the validation warning.

(string)

errored -> (boolean)

Indicates whether there were validation errors.