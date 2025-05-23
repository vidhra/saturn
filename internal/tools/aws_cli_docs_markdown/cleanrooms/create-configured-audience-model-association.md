# create-configured-audience-model-associationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/create-configured-audience-model-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/create-configured-audience-model-association.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# create-configured-audience-model-association

## Description

Provides the details necessary to create a configured audience model association.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)

## Synopsis

```
create-configured-audience-model-association
--membership-identifier <value>
--configured-audience-model-arn <value>
--configured-audience-model-association-name <value>
--manage-resource-policies | --no-manage-resource-policies
[--tags <value>]
[--description <value>]
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

`--membership-identifier` (string)

A unique identifier for one of your memberships for a collaboration. The configured audience model is associated to the collaboration that this membership belongs to. Accepts a membership ID.

`--configured-audience-model-arn` (string)

A unique identifier for the configured audience model that you want to associate.

`--configured-audience-model-association-name` (string)

The name of the configured audience model association.

`--manage-resource-policies` | `--no-manage-resource-policies` (boolean)

When `TRUE` , indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When `FALSE` , indicates that the configured audience model resource owner will manage permissions related to the given collaboration.

Setting this to `TRUE` requires you to have permissions to create, update, and delete the resource policy for the `cleanrooms-ml` resource when you call the  DeleteConfiguredAudienceModelAssociation resource. In addition, if you are the collaboration creator and specify `TRUE` , you must have the same permissions when you call the  DeleteMember and  DeleteCollaboration APIs.

`--tags` (map)

An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

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

`--description` (string)

A description of the configured audience model association.

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

configuredAudienceModelAssociation -> (structure)

Information about the configured audience model association.

id -> (string)

A unique identifier of the configured audience model association.

arn -> (string)

The Amazon Resource Name (ARN) of the configured audience model association.

configuredAudienceModelArn -> (string)

The Amazon Resource Name (ARN) of the configured audience model that was used for this configured audience model association.

membershipId -> (string)

A unique identifier for the membership that contains this configured audience model association.

membershipArn -> (string)

The Amazon Resource Name (ARN) of the membership that contains this configured audience model association.

collaborationId -> (string)

A unique identifier of the collaboration that contains this configured audience model association.

collaborationArn -> (string)

The Amazon Resource Name (ARN) of the collaboration that contains this configured audience model association.

name -> (string)

The name of the configured audience model association.

manageResourcePolicies -> (boolean)

When `TRUE` , indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When `FALSE` , indicates that the configured audience model resource owner will manage permissions related to the given collaboration.

description -> (string)

The description of the configured audience model association.

createTime -> (timestamp)

The time at which the configured audience model association was created.

updateTime -> (timestamp)

The most recent time at which the configured audience model association was updated.