# describe-environmentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloud9](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html#cli-aws-cloud9) ]

# describe-environments

## Description

Gets information about Cloud9 development environments.

### Warning

Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. [Learn moreâ](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/DescribeEnvironments)

## Synopsis

```
describe-environments
--environment-ids <value>
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

`--environment-ids` (list)

The IDs of individual environments to get information about.

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

**To get information about AWS Cloud9 development environments**

This example gets information about the specified AWS Cloud9 development environments.

Command:

```
aws cloud9 describe-environments --environment-ids 685f892f431b45c2b28cb69eadcdb0EX 349c86d4579e4e7298d500ff57a6b2EX
```

Output:

```
{
  "environments": [
    {
      "id": "685f892f431b45c2b28cb69eadcdb0EX",
      "name": "my-demo-ec2-env",
      "description": "Created from CodeStar.",
      "type": "ec2",
      "arn": "arn:aws:cloud9:us-east-1:123456789012:environment:685f892f431b45c2b28cb69eadcdb0EX",
      "ownerArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "lifecycle": {
        "status": "CREATED"
      }
    },
    {
      "id": "349c86d4579e4e7298d500ff57a6b2EX",
      "name": my-demo-ssh-env",
      "description": "",
      "type": "ssh",
      "arn": "arn:aws:cloud9:us-east-1:123456789012:environment:349c86d4579e4e7298d500ff57a6b2EX",
      "ownerArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "lifecycle": {
        "status": "CREATED"
      }
    }
  ]
}
```

## Output

environments -> (list)

Information about the environments that are returned.

(structure)

Information about an Cloud9 development environment.

id -> (string)

The ID of the environment.

name -> (string)

The name of the environment.

description -> (string)

The description for the environment.

type -> (string)

The type of environment. Valid values include the following:

- `ec2` : An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the environment.
- `ssh` : Your own server connects to the environment.

connectionType -> (string)

The connection type used for connecting to an Amazon EC2 environment. `CONNECT_SSH` is selected by default.

arn -> (string)

The Amazon Resource Name (ARN) of the environment.

ownerArn -> (string)

The Amazon Resource Name (ARN) of the environment owner.

lifecycle -> (structure)

The state of the environment in its creation or deletion lifecycle.

status -> (string)

The current creation or deletion lifecycle state of the environment.

- `CREATING` : The environment is in the process of being created.
- `CREATED` : The environment was successfully created.
- `CREATE_FAILED` : The environment failed to be created.
- `DELETING` : The environment is in the process of being deleted.
- `DELETE_FAILED` : The environment failed to delete.

reason -> (string)

Any informational message about the lifecycle state of the environment.

failureResource -> (string)

If the environment failed to delete, the Amazon Resource Name (ARN) of the related Amazon Web Services resource.

managedCredentialsStatus -> (string)

Describes the status of Amazon Web Services managed temporary credentials for the Cloud9 environment. Available values are:

- `ENABLED_ON_CREATE`
- `ENABLED_BY_OWNER`
- `DISABLED_BY_DEFAULT`
- `DISABLED_BY_OWNER`
- `DISABLED_BY_COLLABORATOR`
- `PENDING_REMOVAL_BY_COLLABORATOR`
- `PENDING_REMOVAL_BY_OWNER`
- `FAILED_REMOVAL_BY_COLLABORATOR`
- `ENABLED_BY_OWNER`
- `DISABLED_BY_DEFAULT`