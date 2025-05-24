# untag-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/untag-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/untag-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resourcegroupstaggingapi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/index.html#cli-aws-resourcegroupstaggingapi) ]

# untag-resources

## Description

Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:

- To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see the documentation for the service whose resource you want to untag.
- You can only tag resources that are located in the specified Amazon Web Services Region for the calling Amazon Web Services account.

**Minimum permissions**

In addition to the `tag:UntagResources` permission required by this operation, you must also have the remove tags permission defined by the service that created the resource. For example, to remove the tags from an Amazon EC2 instance using the `UntagResources` operation, you must have both of the following permissions:

- `tag:UntagResource`
- `ec2:DeleteTags`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/UntagResources)

## Synopsis

```
untag-resources
--resource-arn-list <value>
--tag-keys <value>
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

`--resource-arn-list` (list)

Specifies a list of ARNs of the resources that you want to remove tags from.

An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

(string)

Syntax:

```
"string" "string" ...
```

`--tag-keys` (list)

Specifies a list of tag keys that you want to remove from the specified resources.

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To remove a tag from a resource**

The following `untag-resources` example removes the specified tag keys and any associated values from the specified resource.

```
aws resourcegroupstaggingapi untag-resources \
    --resource-arn-list arn:aws:s3:::amzn-s3-demo-bucket \
    --tag-keys Environment CostCenter
```

Output:

```
{
    "FailedResourcesMap": {}
}
```

For more information, see [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html) in the *Resource Groups Tagging API Reference*.

## Output

FailedResourcesMap -> (map)

A map containing a key-value pair for each failed item that couldnât be untagged. The key is the ARN of the failed resource. The value is a `FailureInfo` object that contains an error code, a status code, and an error message. If there are no errors, the `FailedResourcesMap` is empty.

key -> (string)

value -> (structure)

Information about the errors that are returned for each failed resource. This information can include `InternalServiceException` and `InvalidParameterException` errors. It can also include any valid error code returned by the Amazon Web Services service that hosts the resource that the ARN key represents.

The following are common error codes that you might receive from other Amazon Web Services services:

- **InternalServiceException** â This can mean that the Resource Groups Tagging API didnât receive a response from another Amazon Web Services service. It can also mean that the resource type in the request is not supported by the Resource Groups Tagging API. In these cases, itâs safe to retry the request and then call [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) to verify the changes.
- **AccessDeniedException** â This can mean that you need permission to call the tagging operations in the Amazon Web Services service that contains the resource. For example, to use the Resource Groups Tagging API to tag a Amazon CloudWatch alarm resource, you need permission to call both ` `TagResources` [https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources).html`__  *and*  ` `TagResource` [https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource).html`__ in the CloudWatch API.

For more information on errors that are generated from other Amazon Web Services services, see the documentation for that service.

StatusCode -> (integer)

The HTTP status code of the common error.

ErrorCode -> (string)

The code of the common error. Valid values include `InternalServiceException` , `InvalidParameterException` , and any valid error code returned by the Amazon Web Services service that hosts the resource that you want to tag.

ErrorMessage -> (string)

The message of the common error.