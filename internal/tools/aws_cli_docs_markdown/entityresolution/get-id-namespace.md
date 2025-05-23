# get-id-namespaceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/get-id-namespace.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/get-id-namespace.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [entityresolution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/index.html#cli-aws-entityresolution) ]

# get-id-namespace

## Description

Returns the `IdNamespace` with a given name, if it exists.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/entityresolution-2018-05-10/GetIdNamespace)

`get-id-namespace` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
get-id-namespace
--id-namespace-name <value>
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

`--id-namespace-name` (string)

The name of the ID namespace.

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

idNamespaceName -> (string)

The name of the ID namespace.

idNamespaceArn -> (string)

The Amazon Resource Name (ARN) of the ID namespace.

description -> (string)

The description of the ID namespace.

inputSourceConfig -> (list)

A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName` .

(structure)

An object containing `InputSourceARN` and `SchemaName` .

inputSourceARN -> (string)

An Glue table Amazon Resource Name (ARN) or a matching workflow ARN for the input source table.

schemaName -> (string)

The name of the schema.

idMappingWorkflowProperties -> (list)

Determines the properties of `IdMappingWorkflow` where this `IdNamespace` can be used as a `Source` or a `Target` .

(structure)

An object containing `IdMappingType` , `ProviderProperties` , and `RuleBasedProperties` .

idMappingType -> (string)

The type of ID mapping.

ruleBasedProperties -> (structure)

An object which defines any additional configurations required by rule-based matching.

rules -> (list)

The rules for the ID namespace.

(structure)

An object containing `RuleName` , and `MatchingKeys` .

ruleName -> (string)

A name for the matching rule.

matchingKeys -> (list)

A list of `MatchingKeys` . The `MatchingKeys` must have been defined in the `SchemaMapping` . Two records are considered to match according to this rule if all of the `MatchingKeys` match.

(string)

ruleDefinitionTypes -> (list)

The sets of rules you can use in an ID mapping workflow. The limitations specified for the source and target must be compatible.

(string)

attributeMatchingModel -> (string)

The comparison type. You can either choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel` .

If you choose `MANY_TO_MANY` , the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A matches the value of `BusinessEmail` field of Profile B, the two profiles are matched on the `Email` attribute type.

If you choose `ONE_TO_ONE` , the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.

recordMatchingModels -> (list)

The type of matching record that is allowed to be used in an ID mapping workflow.

If the value is set to `ONE_SOURCE_TO_ONE_TARGET` , only one record in the source is matched to one record in the target.

If the value is set to `MANY_SOURCE_TO_ONE_TARGET` , all matching records in the source are matched to one record in the target.

(string)

providerProperties -> (structure)

An object which defines any additional configurations required by the provider service.

providerServiceArn -> (string)

The Amazon Resource Name (ARN) of the provider service.

providerConfiguration -> (document)

An object which defines any additional configurations required by the provider service.

type -> (string)

The type of ID namespace. There are two types: `SOURCE` and `TARGET` .

The `SOURCE` contains configurations for `sourceId` data that will be processed in an ID mapping workflow.

The `TARGET` contains a configuration of `targetId` to which all `sourceIds` will resolve to.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access the resources defined in this `IdNamespace` on your behalf as part of a workflow run.

createdAt -> (timestamp)

The timestamp of when the ID namespace was created.

updatedAt -> (timestamp)

The timestamp of when the ID namespace was last updated.

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)