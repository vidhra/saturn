# create-environment-ec2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-ec2.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-ec2.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloud9](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html#cli-aws-cloud9) ]

# create-environment-ec2

## Description

Creates an Cloud9 development environment, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.

### Warning

Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. [Learn moreâ](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/CreateEnvironmentEC2)

## Synopsis

```
create-environment-ec2
--name <value>
[--description <value>]
[--client-request-token <value>]
--instance-type <value>
[--subnet-id <value>]
--image-id <value>
[--automatic-stop-time-minutes <value>]
[--owner-arn <value>]
[--tags <value>]
[--connection-type <value>]
[--dry-run | --no-dry-run]
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

`--name` (string)

The name of the environment to create.

This name is visible to other IAM users in the same Amazon Web Services account.

`--description` (string)

The description of the environment to create.

`--client-request-token` (string)

A unique, case-sensitive string that helps Cloud9 to ensure this operation completes no more than one time.

For more information, see [Client Tokens](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference* .

`--instance-type` (string)

The type of instance to connect to the environment (for example, `t2.micro` ).

`--subnet-id` (string)

The ID of the subnet in Amazon VPC that Cloud9 will use to communicate with the Amazon EC2 instance.

`--image-id` (string)

The identifier for the Amazon Machine Image (AMI) thatâs used to create the EC2 instance. To choose an AMI for the instance, you must specify a valid AMI alias or a valid Amazon EC2 Systems Manager (SSM) path.

We recommend using Amazon Linux 2023 as the AMI to create your environment as it is fully supported.

From December 16, 2024, Ubuntu 18.04 will be removed from the list of available `imageIds` for Cloud9. This change is necessary as Ubuntu 18.04 has ended standard support on May 31, 2023. This change will only affect direct API consumers, and not Cloud9 console users.

Since Ubuntu 18.04 has ended standard support as of May 31, 2023, we recommend you choose Ubuntu 22.04.

**AMI aliases**

- Amazon Linux 2: `amazonlinux-2-x86_64`
- Amazon Linux 2023 (recommended): `amazonlinux-2023-x86_64`
- Ubuntu 18.04: `ubuntu-18.04-x86_64`
- Ubuntu 22.04: `ubuntu-22.04-x86_64`

**SSM paths**

- Amazon Linux 2: `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
- Amazon Linux 2023 (recommended): `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2023-x86_64`
- Ubuntu 18.04: `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
- Ubuntu 22.04: `resolve:ssm:/aws/service/cloud9/amis/ubuntu-22.04-x86_64`

`--automatic-stop-time-minutes` (integer)

The number of minutes until the running instance is shut down after the environment has last been used.

`--owner-arn` (string)

The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any IAM principal. If this value is not specified, the ARN defaults to this environmentâs creator.

`--tags` (list)

An array of key-value pairs that will be associated with the new Cloud9 development environment.

(structure)

Metadata that is associated with Amazon Web Services resources. In particular, a name-value pair that can be associated with an Cloud9 development environment. There are two types of tags: *user tags* and *system tags* . A user tag is created by the user. A system tag is automatically created by Amazon Web Services services. A system tag is prefixed with `"aws:"` and cannot be modified by the user.

Key -> (string)

The **name** part of a tag.

Value -> (string)

The **value** part of a tag.

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

`--connection-type` (string)

The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` (default) and `CONNECT_SSM` (connected through Amazon EC2 Systems Manager).

For more information, see [Accessing no-ingress EC2 instances with Amazon EC2 Systems Manager](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html) in the *Cloud9 User Guide* .

Possible values:

- `CONNECT_SSH`
- `CONNECT_SSM`

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

**To create an AWS Cloud9 EC2 development environment**

This following `create-environment-ec2` example creates an AWS Cloud9 development environment with the specified settings, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.

```
aws cloud9 create-environment-ec2 \
    --name my-demo-env \
    --description "My demonstration development environment." \
    --instance-type t2.micro --image-id amazonlinux-2023-x86_64 \
    --subnet-id subnet-1fab8aEX \
    --automatic-stop-time-minutes 60 \
    --owner-arn arn:aws:iam::123456789012:user/MyDemoUser
```

Output:

```
{
    "environmentId": "8a34f51ce1e04a08882f1e811bd706EX"
}
```

For more information, see [Creating an EC2 Environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html) in the *AWS Cloud9 User Guide*.

## Output

environmentId -> (string)

The ID of the environment that was created.