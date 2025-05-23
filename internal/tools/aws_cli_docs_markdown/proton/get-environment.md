# get-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# get-environment

## Description

Get detailed data for an environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/GetEnvironment)

## Synopsis

```
get-environment
--name <value>
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

The name of the environment that you want to get the detailed data for.

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

environment -> (structure)

The detailed data of the requested environment.

arn -> (string)

The Amazon Resource Name (ARN) of the environment.

codebuildRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.

componentRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.

The environment must have a `componentRoleArn` to allow directly defined components to be associated with the environment.

For more information about components, see [Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the *Proton User Guide* .

createdAt -> (timestamp)

The time when the environment was created.

deploymentStatus -> (string)

The environment deployment status.

deploymentStatusMessage -> (string)

An environment deployment status message.

description -> (string)

The description of the environment.

environmentAccountConnectionId -> (string)

The ID of the environment account connection thatâs used to provision infrastructure resources in an environment account.

environmentAccountId -> (string)

The ID of the environment account that the environment infrastructure resources are provisioned in.

lastAttemptedDeploymentId -> (string)

The ID of the last attempted deployment of this environment.

lastDeploymentAttemptedAt -> (timestamp)

The time when a deployment of the environment was last attempted.

lastDeploymentSucceededAt -> (timestamp)

The time when the environment was last deployed successfully.

lastSucceededDeploymentId -> (string)

The ID of the last successful deployment of this environment.

name -> (string)

The name of the environment.

protonServiceRoleArn -> (string)

The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make calls to other services on your behalf.

provisioning -> (string)

When included, indicates that the environment template is for customer provisioned and managed infrastructure.

provisioningRepository -> (structure)

The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see [CreateRepository](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateRepository.html) .

arn -> (string)

The Amazon Resource Name (ARN) of the linked repository.

branch -> (string)

The repository branch.

name -> (string)

The repository name.

provider -> (string)

The repository provider.

spec -> (string)

The environment spec.

templateMajorVersion -> (string)

The major version of the environment template.

templateMinorVersion -> (string)

The minor version of the environment template.

templateName -> (string)

The Amazon Resource Name (ARN) of the environment template.