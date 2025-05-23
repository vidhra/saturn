# start-change-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/start-change-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/start-change-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [marketplace-catalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/index.html#cli-aws-marketplace-catalog) ]

# start-change-set

## Description

Allows you to request changes for your entities. Within a single `ChangeSet` , you canât start the same change type against the same entity multiple times. Additionally, when a `ChangeSet` is running, all the entities targeted by the different changes are locked until the change set has completed (either succeeded, cancelled, or failed). If you try to start a change set containing a change against an entity that is already locked, you will receive a `ResourceInUseException` error.

For example, you canât start the `ChangeSet` described in the [example](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_Examples) later in this topic because it contains two changes to run the same change type (`AddRevisions` ) against the same entity (`entity-id@1` ).

For more information about working with change sets, see [Working with change sets](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets) . For information about change types for single-AMI products, see [Working with single-AMI products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products) . Also, for more information about change types available for container-based products, see [Working with container products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/marketplace-catalog-2018-09-17/StartChangeSet)

`start-change-set` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
start-change-set
--catalog <value>
--change-set <value>
[--change-set-name <value>]
[--client-request-token <value>]
[--change-set-tags <value>]
[--intent <value>]
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

`--catalog` (string)

The catalog related to the request. Fixed value: `AWSMarketplace`

`--change-set` (list)

Array of `change` object.

(structure)

An object that contains the `ChangeType` , `Details` , and `Entity` .

ChangeType -> (string)

Change types are single string values that describe your intention for the change. Each change type is unique for each `EntityType` provided in the changeâs scope. For more information about change types available for single-AMI products, see [Working with single-AMI products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products) . Also, for more information about change types available for container-based products, see [Working with container products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products) .

Entity -> (structure)

The entity to be changed.

Type -> (string)

The type of entity.

Identifier -> (string)

The identifier for the entity.

EntityTags -> (list)

The tags associated with the change.

(structure)

A list of objects specifying each key name and value.

Key -> (string)

The key associated with the tag.

Value -> (string)

The value associated with the tag.

Details -> (string)

This object contains details specific to the change type of the requested change. For more information about change types available for single-AMI products, see [Working with single-AMI products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products) . Also, for more information about change types available for container-based products, see [Working with container products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products) .

DetailsDocument -> (document)

Alternative field that accepts a JSON value instead of a string for `ChangeType` details. You can use either `Details` or `DetailsDocument` , but not both.

ChangeName -> (string)

Optional name for the change.

Shorthand Syntax:

```
ChangeType=string,Entity={Type=string,Identifier=string},EntityTags=[{Key=string,Value=string},{Key=string,Value=string}],Details=string,ChangeName=string ...
```

JSON Syntax:

```
[
  {
    "ChangeType": "string",
    "Entity": {
      "Type": "string",
      "Identifier": "string"
    },
    "EntityTags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ],
    "Details": "string",
    "DetailsDocument": {...},
    "ChangeName": "string"
  }
  ...
]
```

`--change-set-name` (string)

Optional case sensitive string of up to 100 ASCII characters. The change set name can be used to filter the list of change sets.

`--client-request-token` (string)

A unique token to identify the request to ensure idempotency.

`--change-set-tags` (list)

A list of objects specifying each key name and value for the `ChangeSetTags` property.

(structure)

A list of objects specifying each key name and value.

Key -> (string)

The key associated with the tag.

Value -> (string)

The value associated with the tag.

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

`--intent` (string)

The intent related to the request. The default is `APPLY` . To test your request before applying changes to your entities, use `VALIDATE` . This feature is currently available for adding versions to single-AMI products. For more information, see [Add a new version](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#ami-add-version) .

Possible values:

- `VALIDATE`
- `APPLY`

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

ChangeSetId -> (string)

Unique identifier generated for the request.

ChangeSetArn -> (string)

The ARN associated to the unique identifier generated for the request.