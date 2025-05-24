# create-matching-workflowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/create-matching-workflow.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/create-matching-workflow.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [entityresolution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/index.html#cli-aws-entityresolution) ]

# create-matching-workflow

## Description

Creates a `MatchingWorkflow` object which stores the configuration of the data processing job to be run. It is important to note that there should not be a pre-existing `MatchingWorkflow` with the same name. To modify an existing workflow, utilize the `UpdateMatchingWorkflow` API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/entityresolution-2018-05-10/CreateMatchingWorkflow)

`create-matching-workflow` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
create-matching-workflow
--workflow-name <value>
[--description <value>]
--input-source-config <value>
--output-source-config <value>
--resolution-techniques <value>
[--incremental-run-config <value>]
--role-arn <value>
[--tags <value>]
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

`--workflow-name` (string)

The name of the workflow. There canât be multiple `MatchingWorkflows` with the same name.

`--description` (string)

A description of the workflow.

`--input-source-config` (list)

A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName` .

(structure)

An object containing `InputSourceARN` , `SchemaName` , and `ApplyNormalization` .

inputSourceARN -> (string)

An Glue table Amazon Resource Name (ARN) for the input source table.

schemaName -> (string)

The name of the schema to be retrieved.

applyNormalization -> (boolean)

Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an `AttributeType` of `PHONE_NUMBER` , and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.

Shorthand Syntax:

```
inputSourceARN=string,schemaName=string,applyNormalization=boolean ...
```

JSON Syntax:

```
[
  {
    "inputSourceARN": "string",
    "schemaName": "string",
    "applyNormalization": true|false
  }
  ...
]
```

`--output-source-config` (list)

A list of `OutputSource` objects, each of which contains fields `OutputS3Path` , `ApplyNormalization` , and `Output` .

(structure)

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed` . Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

outputS3Path -> (string)

The S3 path to which Entity Resolution will write the output table.

KMSArn -> (string)

Customer KMS ARN for encryption at rest. If not provided, system will use an Entity Resolution managed KMS key.

output -> (list)

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed` . Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

(structure)

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed` . Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

name -> (string)

A name of a column to be written to the output. This must be an `InputField` name in the schema mapping.

hashed -> (boolean)

Enables the ability to hash the column values in the output.

applyNormalization -> (boolean)

Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an `AttributeType` of `PHONE_NUMBER` , and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.

Shorthand Syntax:

```
outputS3Path=string,KMSArn=string,output=[{name=string,hashed=boolean},{name=string,hashed=boolean}],applyNormalization=boolean ...
```

JSON Syntax:

```
[
  {
    "outputS3Path": "string",
    "KMSArn": "string",
    "output": [
      {
        "name": "string",
        "hashed": true|false
      }
      ...
    ],
    "applyNormalization": true|false
  }
  ...
]
```

`--resolution-techniques` (structure)

An object which defines the `resolutionType` and the `ruleBasedProperties` .

resolutionType -> (string)

The type of matching. There are three types of matching: `RULE_MATCHING` , `ML_MATCHING` , and `PROVIDER` .

ruleBasedProperties -> (structure)

An object which defines the list of matching rules to run and has a field `Rules` , which is a list of rule objects.

rules -> (list)

A list of `Rule` objects, each of which have fields `RuleName` and `MatchingKeys` .

(structure)

An object containing `RuleName` , and `MatchingKeys` .

ruleName -> (string)

A name for the matching rule.

matchingKeys -> (list)

A list of `MatchingKeys` . The `MatchingKeys` must have been defined in the `SchemaMapping` . Two records are considered to match according to this rule if all of the `MatchingKeys` match.

(string)

attributeMatchingModel -> (string)

The comparison type. You can either choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel` .

If you choose `MANY_TO_MANY` , the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A and the value of `BusinessEmail` field of Profile B matches, the two profiles are matched on the `Email` attribute type.

If you choose `ONE_TO_ONE` , the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.

matchPurpose -> (string)

An indicator of whether to generate IDs and index the data or not.

If you choose `IDENTIFIER_GENERATION` , the process generates IDs and indexes the data.

If you choose `INDEXING` , the process indexes the data without generating IDs.

providerProperties -> (structure)

The properties of the provider service.

providerServiceArn -> (string)

The ARN of the provider service.

providerConfiguration -> (document)

The required configuration fields to use with the provider service.

intermediateSourceConfiguration -> (structure)

The Amazon S3 location that temporarily stores your data while it processes. Your information wonât be saved permanently.

intermediateS3Path -> (string)

The Amazon S3 location (bucket and prefix). For example: `s3://provider_bucket/DOC-EXAMPLE-BUCKET`

JSON Syntax:

```
{
  "resolutionType": "RULE_MATCHING"|"ML_MATCHING"|"PROVIDER",
  "ruleBasedProperties": {
    "rules": [
      {
        "ruleName": "string",
        "matchingKeys": ["string", ...]
      }
      ...
    ],
    "attributeMatchingModel": "ONE_TO_ONE"|"MANY_TO_MANY",
    "matchPurpose": "IDENTIFIER_GENERATION"|"INDEXING"
  },
  "providerProperties": {
    "providerServiceArn": "string",
    "providerConfiguration": {...},
    "intermediateSourceConfiguration": {
      "intermediateS3Path": "string"
    }
  }
}
```

`--incremental-run-config` (structure)

An object which defines an incremental run type and has only `incrementalRunType` as a field.

incrementalRunType -> (string)

The type of incremental run. It takes only one value: `IMMEDIATE` .

Shorthand Syntax:

```
incrementalRunType=string
```

JSON Syntax:

```
{
  "incrementalRunType": "IMMEDIATE"
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.

`--tags` (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

workflowName -> (string)

The name of the workflow.

workflowArn -> (string)

The ARN (Amazon Resource Name) that Entity Resolution generated for the `MatchingWorkflow` .

description -> (string)

A description of the workflow.

inputSourceConfig -> (list)

A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName` .

(structure)

An object containing `InputSourceARN` , `SchemaName` , and `ApplyNormalization` .

inputSourceARN -> (string)

An Glue table Amazon Resource Name (ARN) for the input source table.

schemaName -> (string)

The name of the schema to be retrieved.

applyNormalization -> (boolean)

Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an `AttributeType` of `PHONE_NUMBER` , and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.

outputSourceConfig -> (list)

A list of `OutputSource` objects, each of which contains fields `OutputS3Path` , `ApplyNormalization` , and `Output` .

(structure)

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed` . Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

outputS3Path -> (string)

The S3 path to which Entity Resolution will write the output table.

KMSArn -> (string)

Customer KMS ARN for encryption at rest. If not provided, system will use an Entity Resolution managed KMS key.

output -> (list)

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed` . Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

(structure)

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed` . Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

name -> (string)

A name of a column to be written to the output. This must be an `InputField` name in the schema mapping.

hashed -> (boolean)

Enables the ability to hash the column values in the output.

applyNormalization -> (boolean)

Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an `AttributeType` of `PHONE_NUMBER` , and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.

resolutionTechniques -> (structure)

An object which defines the `resolutionType` and the `ruleBasedProperties` .

resolutionType -> (string)

The type of matching. There are three types of matching: `RULE_MATCHING` , `ML_MATCHING` , and `PROVIDER` .

ruleBasedProperties -> (structure)

An object which defines the list of matching rules to run and has a field `Rules` , which is a list of rule objects.

rules -> (list)

A list of `Rule` objects, each of which have fields `RuleName` and `MatchingKeys` .

(structure)

An object containing `RuleName` , and `MatchingKeys` .

ruleName -> (string)

A name for the matching rule.

matchingKeys -> (list)

A list of `MatchingKeys` . The `MatchingKeys` must have been defined in the `SchemaMapping` . Two records are considered to match according to this rule if all of the `MatchingKeys` match.

(string)

attributeMatchingModel -> (string)

The comparison type. You can either choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel` .

If you choose `MANY_TO_MANY` , the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A and the value of `BusinessEmail` field of Profile B matches, the two profiles are matched on the `Email` attribute type.

If you choose `ONE_TO_ONE` , the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.

matchPurpose -> (string)

An indicator of whether to generate IDs and index the data or not.

If you choose `IDENTIFIER_GENERATION` , the process generates IDs and indexes the data.

If you choose `INDEXING` , the process indexes the data without generating IDs.

providerProperties -> (structure)

The properties of the provider service.

providerServiceArn -> (string)

The ARN of the provider service.

providerConfiguration -> (document)

The required configuration fields to use with the provider service.

intermediateSourceConfiguration -> (structure)

The Amazon S3 location that temporarily stores your data while it processes. Your information wonât be saved permanently.

intermediateS3Path -> (string)

The Amazon S3 location (bucket and prefix). For example: `s3://provider_bucket/DOC-EXAMPLE-BUCKET`

incrementalRunConfig -> (structure)

An object which defines an incremental run type and has only `incrementalRunType` as a field.

incrementalRunType -> (string)

The type of incremental run. It takes only one value: `IMMEDIATE` .

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.