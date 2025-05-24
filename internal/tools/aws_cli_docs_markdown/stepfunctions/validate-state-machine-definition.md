# validate-state-machine-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/validate-state-machine-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/validate-state-machine-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# validate-state-machine-definition

## Description

Validates the syntax of a state machine definition specified in [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) (ASL), a JSON-based, structured language.

You can validate that a state machine definition is correct without creating a state machine resource.

Suggested uses for `ValidateStateMachineDefinition` :

- Integrate automated checks into your code review or Continuous Integration (CI) process to check state machine definitions before starting deployments.
- Run validation from a Git pre-commit hook to verify the definition before committing to your source repository.

Validation will look for problems in your state machine definition and return a **result** and a list of **diagnostic elements** .

The **result** value will be `OK` when your workflow definition can be successfully created or updated. Note the result can be `OK` even when diagnostic warnings are present in the response. The **result** value will be `FAIL` when the workflow definition contains errors that would prevent you from creating or updating your state machine.

The list of [ValidateStateMachineDefinitionDiagnostic](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinitionDiagnostic.html) data elements can contain zero or more **WARNING** and/or **ERROR** elements.

### Note

The **ValidateStateMachineDefinition API** might add new diagnostics in the future, adjust diagnostic codes, or change the message wording. Your automated processes should only rely on the value of the **result** field value (OK, FAIL). Do **not** rely on the exact order, count, or wording of diagnostic messages.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ValidateStateMachineDefinition)

## Synopsis

```
validate-state-machine-definition
--definition <value>
[--type <value>]
[--severity <value>]
[--max-results <value>]
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

`--definition` (string)

The Amazon States Language definition of the state machine. For more information, see [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) (ASL).

`--type` (string)

The target type of state machine for this definition. The default is `STANDARD` .

Possible values:

- `STANDARD`
- `EXPRESS`

`--severity` (string)

Minimum level of diagnostics to return. `ERROR` returns only `ERROR` diagnostics, whereas `WARNING` returns both `WARNING` and `ERROR` diagnostics. The default is `ERROR` .

Possible values:

- `ERROR`
- `WARNING`

`--max-results` (integer)

The maximum number of diagnostics that are returned per call. The default and maximum value is 100. Setting the value to 0 will also use the default of 100.

If the number of diagnostics returned in the response exceeds `maxResults` , the value of the `truncated` field in the response will be set to `true` .

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

result -> (string)

The result value will be `OK` when no syntax errors are found, or `FAIL` if the workflow definition does not pass verification.

diagnostics -> (list)

An array of diagnostic errors and warnings found during validation of the state machine definition. Since **warnings** do not prevent deploying your workflow definition, the **result** value could be `OK` even when warning diagnostics are present in the response.

(structure)

Describes potential issues found during state machine validation. Rather than raise an exception, validation will return a list of **diagnostic elements** containing diagnostic information.

### Note

The [ValidateStateMachineDefinitionlAPI](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinition.html) might add new diagnostics in the future, adjust diagnostic codes, or change the message wording. Your automated processes should only rely on the value of the **result** field value (OK, FAIL). Do **not** rely on the exact order, count, or wording of diagnostic messages.

**List of warning codes**

NO_DOLLAR

No `.$` on a field that appears to be a JSONPath or Intrinsic Function.

NO_PATH

Field value looks like a path, but field name does not end with âPathâ.

PASS_RESULT_IS_STATIC

Attempt to use a path in the result of a pass state.

**List of error codes**

INVALID_JSON_DESCRIPTION

JSON syntax problem found.

MISSING_DESCRIPTION

Received a null or empty workflow input.

SCHEMA_VALIDATION_FAILED

Schema validation reported errors.

INVALID_RESOURCE

The value of a Task-state resource field is invalid.

MISSING_END_STATE

The workflow does not have a terminal state.

DUPLICATE_STATE_NAME

The same state name appears more than once.

INVALID_STATE_NAME

The state name does not follow the naming convention.

STATE_MACHINE_NAME_EMPTY

The state machine name has not been specified.

STATE_MACHINE_NAME_INVALID

The state machine name does not follow the naming convention.

STATE_MACHINE_NAME_TOO_LONG

The state name exceeds the allowed length.

STATE_MACHINE_NAME_ALREADY_EXISTS

The state name already exists.

DUPLICATE_LABEL_NAME

A label name appears more than once.

INVALID_LABEL_NAME

You have provided an invalid label name.

MISSING_TRANSITION_TARGET

The value of âNextâ field doesnât match a known state name.

TOO_DEEPLY_NESTED

The states are too deeply nested.

severity -> (string)

A value of `ERROR` means that you cannot create or update a state machine with this definition.

`WARNING` level diagnostics alert you to potential issues, but they will not prevent you from creating or updating your state machine.

code -> (string)

Identifying code for the diagnostic.

message -> (string)

Message describing the diagnostic condition.

location -> (string)

Location of the issue in the state machine, if available.

For errors specific to a field, the location could be in the format: `/States/<StateName>/<FieldName>` , for example: `/States/FailState/ErrorPath` .

truncated -> (boolean)

The result value will be `true` if the number of diagnostics found in the workflow definition exceeds `maxResults` . When all diagnostics results are returned, the value will be `false` .