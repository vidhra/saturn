# create-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# create-environment

## Description

Deploy a new environment. An Proton environment is created from an environment template that defines infrastructure and resources that can be shared across services.

**You can provision environments using the following methods:**

- Amazon Web Services-managed provisioning: Proton makes direct calls to provision your resources.
- Self-managed provisioning: Proton makes pull requests on your repository to provide compiled infrastructure as code (IaC) files that your IaC engine uses to provision resources.

For more information, see [Environments](https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html) and [Provisioning methods](https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html) in the *Proton User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/CreateEnvironment)

## Synopsis

```
create-environment
[--codebuild-role-arn <value>]
[--component-role-arn <value>]
[--description <value>]
[--environment-account-connection-id <value>]
--name <value>
[--proton-service-role-arn <value>]
[--provisioning-repository <value>]
--spec <value>
[--tags <value>]
--template-major-version <value>
[--template-minor-version <value>]
--template-name <value>
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

`--codebuild-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.

To use CodeBuild-based provisioning for the environment or for any service instance running in the environment, specify either the `environmentAccountConnectionId` or `codebuildRoleArn` parameter.

`--component-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.

You must specify `componentRoleArn` to allow directly defined components to be associated with this environment.

For more information about components, see [Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the *Proton User Guide* .

`--description` (string)

A description of the environment thatâs being created and deployed.

`--environment-account-connection-id` (string)

The ID of the environment account connection that you provide if youâre provisioning your environment infrastructure resources to an environment account. For more information, see [Environment account connections](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html) in the *Proton User guide* .

To use Amazon Web Services-managed provisioning for the environment, specify either the `environmentAccountConnectionId` or `protonServiceRoleArn` parameter and omit the `provisioningRepository` parameter.

`--name` (string)

The name of the environment.

`--proton-service-role-arn` (string)

The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make calls to other services on your behalf.

To use Amazon Web Services-managed provisioning for the environment, specify either the `environmentAccountConnectionId` or `protonServiceRoleArn` parameter and omit the `provisioningRepository` parameter.

`--provisioning-repository` (structure)

The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see  CreateRepository .

To use self-managed provisioning for the environment, specify this parameter and omit the `environmentAccountConnectionId` and `protonServiceRoleArn` parameters.

branch -> (string)

The repository branch.

name -> (string)

The repository name.

provider -> (string)

The repository provider.

Shorthand Syntax:

```
branch=string,name=string,provider=string
```

JSON Syntax:

```
{
  "branch": "string",
  "name": "string",
  "provider": "GITHUB"|"GITHUB_ENTERPRISE"|"BITBUCKET"
}
```

`--spec` (string)

A YAML formatted string that provides inputs as defined in the environment template bundle schema file. For more information, see [Environments](https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html) in the *Proton User Guide* .

`--tags` (list)

An optional list of metadata items that you can associate with the Proton environment. A tag is a key-value pair.

For more information, see [Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the *Proton User Guide* .

(structure)

A description of a resource tag.

key -> (string)

The key of the resource tag.

value -> (string)

The value of the resource tag.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--template-major-version` (string)

The major version of the environment template.

`--template-minor-version` (string)

The minor version of the environment template.

`--template-name` (string)

The name of the environment template. For more information, see [Environment Templates](https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html) in the *Proton User Guide* .

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

The environment detail data thatâs returned by Proton.

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