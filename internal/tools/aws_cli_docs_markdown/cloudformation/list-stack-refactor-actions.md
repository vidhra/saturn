# list-stack-refactor-actionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-refactor-actions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-refactor-actions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# list-stack-refactor-actions

## Description

Lists the stack refactor actions that will be taken after calling the  ExecuteStackRefactor action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackRefactorActions)

`list-stack-refactor-actions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `StackRefactorActions`

## Synopsis

```
list-stack-refactor-actions
--stack-refactor-id <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--stack-refactor-id` (string)

The ID associated with the stack refactor created from the  CreateStackRefactor action.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

StackRefactorActions -> (list)

The stack refactor actions.

(structure)

Describes the stack and the action that CloudFormation will perform on it if you execute the stack refactor.

Action -> (string)

The action that CloudFormation takes on the stack.

Entity -> (string)

The type that will be evaluated in the `StackRefactorAction` . The following are potential `Entity` types:

- `Stack`
- `Resource`

PhysicalResourceId -> (string)

The name or unique identifier associated with the physical instance of the resource.

ResourceIdentifier -> (string)

A key-value pair that identifies the target resource. The key is an identifier property (for example, `BucketName` for `AWS::S3::Bucket` resources) and the value is the actual property value (for example, `MyS3Bucket` ).

Description -> (string)

A description to help you identify the refactor.

Detection -> (string)

The detection type is one of the following:

- Auto: CloudFormation figured out the mapping on its own.
- Manual: The customer provided the mapping in the `ResourceMapping` parameter.

DetectionReason -> (string)

The description of the detection type.

TagResources -> (list)

Assigns one or more tags to specified resources.

(structure)

The Tag type enables you to specify a key-value pair that can be used to store information about an CloudFormation stack.

Key -> (string)

*Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services have the reserved prefix: `aws:` .

Value -> (string)

*Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.

UntagResources -> (list)

Removes one or more tags to specified resources.

(string)

ResourceMapping -> (structure)

The mapping for the stack resource `Source` and stack resource `Destination` .

Source -> (structure)

The source stack `StackName` and `LogicalResourceId` for the resource being refactored.

StackName -> (string)

The name associated with the stack.

LogicalResourceId -> (string)

The logical name of the resource specified in the template.

Destination -> (structure)

The destination stack `StackName` and `LogicalResourceId` for the resource being refactored.

StackName -> (string)

The name associated with the stack.

LogicalResourceId -> (string)

The logical name of the resource specified in the template.

NextToken -> (string)

If the request doesnât return all the remaining results, `NextToken` is set to a token. To retrieve the next set of results, call this action again and assign that token to the request objectâs `NextToken` parameter. If the request returns all results, `NextToken` is set to `null` .