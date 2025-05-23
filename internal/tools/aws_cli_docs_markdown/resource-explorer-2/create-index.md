# create-indexÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/create-index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/create-index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resource-explorer-2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/index.html#cli-aws-resource-explorer-2) ]

# create-index

## Description

Turns on Amazon Web Services Resource Explorer in the Amazon Web Services Region in which you called this operation by creating an index. Resource Explorer begins discovering the resources in this Region and stores the details about the resources in the index so that they can be queried by using the  Search operation. You can create only one index in a Region.

### Note

This operation creates only a *local* index. To promote the local index in one Amazon Web Services Region into the aggregator index for the Amazon Web Services account, use the  UpdateIndexType operation. For more information, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) in the *Amazon Web Services Resource Explorer User Guide* .

For more details about what happens when you turn on Resource Explorer in an Amazon Web Services Region, see [Turn on Resource Explorer to index your resources in an Amazon Web Services Region](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-activate.html) in the *Amazon Web Services Resource Explorer User Guide* .

If this is the first Amazon Web Services Region in which youâve created an index for Resource Explorer, then this operation also [creates a service-linked role](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html) in your Amazon Web Services account that allows Resource Explorer to enumerate your resources to populate the index.

- **Action** : `resource-explorer-2:CreateIndex` **Resource** : The ARN of the index (as it will exist after the operation completes) in the Amazon Web Services Region and account in which youâre trying to create the index. Use the wildcard character (`*` ) at the end of the string to match the eventual UUID. For example, the following `Resource` element restricts the role or user to creating an index in only the `us-east-2` Region of the specified account.  `"Resource": "arn:aws:resource-explorer-2:us-west-2:*<account-id>* :index/*"`   Alternatively, you can use `"Resource": "*"` to allow the role or user to create an index in any Region.
- **Action** : `iam:CreateServiceLinkedRole` **Resource** : No specific resource (*).  This permission is required only the first time you create an index to turn on Resource Explorer in the account. Resource Explorer uses this to create the [service-linked role needed to index the resources in your account](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html) . Resource Explorer uses the same service-linked role for all additional indexes you create afterwards.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resource-explorer-2-2022-07-28/CreateIndex)

## Synopsis

```
create-index
[--client-token <value>]
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

`--client-token` (string)

This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a [UUID-type value](https://wikipedia.org/wiki/Universally_unique_identifier) to ensure the uniqueness of your index.

`--tags` (map)

The specified tags are attached only to the index created in this Amazon Web Services Region. The tags arenât attached to any of the resources listed in the index.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To turn on Resource Explorer in an AWS Region by creating an index**

The following `create-index` example creates a local index in the AWS Region in which the operation is called. The AWS CLI automatically generates a random `client-token` parameter value and includes it in the call to AWS if you donât specify a value.

```
aws resource-explorer-2 create-index \
    --region us-east-1
```

Output:

```
{
    "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222c",
    "CreatedAt": "2022-11-01T20:00:59.149Z",
    "State": "CREATING"
}
```

After you create a local index, you can convert it into the aggregator index for the account by running the [update-index-type](https://docs.aws.amazon.com/cli/latest/reference/resource-explorer-2/update-index-type.html) command.

For more information, see [Turning on Resource Explorer in an AWS Region to index your resources](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-register.html) in the *AWS Resource Explorer Users Guide*.

## Output

Arn -> (string)

The ARN of the new local index for the Region. You can reference this ARN in IAM permission policies to authorize the following operations:  DeleteIndex |  GetIndex |  UpdateIndexType |  CreateView

CreatedAt -> (timestamp)

The date and timestamp when the index was created.

State -> (string)

Indicates the current state of the index. You can check for changes to the state for asynchronous operations by calling the  GetIndex operation.

### Note

The state can remain in the `CREATING` or `UPDATING` state for several hours as Resource Explorer discovers the information about your resources and populates the index.