# get-associated-resourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-associated-resource.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-associated-resource.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog-appregistry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/index.html#cli-aws-servicecatalog-appregistry) ]

# get-associated-resource

## Description

Gets the resource associated with the application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/AWS242AppRegistry-2020-06-24/GetAssociatedResource)

## Synopsis

```
get-associated-resource
--application <value>
--resource-type <value>
--resource <value>
[--next-token <value>]
[--resource-tag-status <value>]
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

`--application` (string)

The name, ID, or ARN of the application.

`--resource-type` (string)

The type of resource associated with the application.

Possible values:

- `CFN_STACK`
- `RESOURCE_TAG_VALUE`

`--resource` (string)

The name or ID of the resource associated with the application.

`--next-token` (string)

A unique pagination token for each page of results. Make the call again with the returned token to retrieve the next page of results.

`--resource-tag-status` (list)

States whether an application tag is applied, not applied, in the process of being applied, or skipped.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  SUCCESS
  FAILED
  IN_PROGRESS
  SKIPPED
```

`--max-results` (integer)

The maximum number of results to return. If the parameter is omitted, it defaults to 25. The value is optional.

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

resource -> (structure)

The resource associated with the application.

name -> (string)

The name of the resource.

arn -> (string)

The Amazon resource name (ARN) of the resource.

associationTime -> (timestamp)

The time the resource was associated with the application.

integrations -> (structure)

The service integration information about the resource.

resourceGroup -> (structure)

The information about the integration of Resource Groups.

state -> (string)

The state of the propagation process for the resource group. The states includes:

`CREATING` if the resource group is in the process of being created.

`CREATE_COMPLETE` if the resource group was created successfully.

`CREATE_FAILED` if the resource group failed to be created.

`UPDATING` if the resource group is in the process of being updated.

`UPDATE_COMPLETE` if the resource group updated successfully.

`UPDATE_FAILED` if the resource group could not update successfully.

arn -> (string)

The Amazon resource name (ARN) of the resource group.

errorMessage -> (string)

The error message that generates when the propagation process for the resource group fails.

options -> (list)

Determines whether an application tag is applied or skipped.

(string)

applicationTagResult -> (structure)

The result of the application thatâs tag applied to a resource.

applicationTagStatus -> (string)

The application tag is in the process of being applied to a resource, was successfully applied to a resource, or failed to apply to a resource.

errorMessage -> (string)

The message returned if the call fails.

resources -> (list)

The resources associated with an application

(structure)

The resource in a list of resources.

resourceArn -> (string)

The Amazon resource name (ARN) of the resource.

errorMessage -> (string)

The message returned if the call fails.

status -> (string)

The status of the list item.

resourceType -> (string)

Provides information about the AppRegistry resource type.

nextToken -> (string)

A unique pagination token for each page of results. Make the call again with the returned token to retrieve the next page of results.