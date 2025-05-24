# describe-projectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-project.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-project.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-project

## Description

Describes the details of a project.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeProject)

## Synopsis

```
describe-project
--project-name <value>
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

`--project-name` (string)

The name of the project to describe.

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

ProjectArn -> (string)

The Amazon Resource Name (ARN) of the project.

ProjectName -> (string)

The name of the project.

ProjectId -> (string)

The ID of the project.

ProjectDescription -> (string)

The description of the project.

ServiceCatalogProvisioningDetails -> (structure)

Information used to provision a service catalog product. For information, see [What is Amazon Web Services Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) .

ProductId -> (string)

The ID of the product to provision.

ProvisioningArtifactId -> (string)

The ID of the provisioning artifact.

PathId -> (string)

The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path.

ProvisioningParameters -> (list)

A list of key value pairs that you specify when you provision a product.

(structure)

A key value pair used when you provision a project as a service catalog product. For information, see [What is Amazon Web Services Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) .

Key -> (string)

The key that identifies a provisioning parameter.

Value -> (string)

The value of the provisioning parameter.

ServiceCatalogProvisionedProductDetails -> (structure)

Information about a provisioned service catalog product.

ProvisionedProductId -> (string)

The ID of the provisioned product.

ProvisionedProductStatusMessage -> (string)

The current status of the product.

- `AVAILABLE` - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
- `UNDER_CHANGE` - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
- `TAINTED` - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
- `ERROR` - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
- `PLAN_IN_PROGRESS` - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.

ProjectStatus -> (string)

The status of the project.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

CreationTime -> (timestamp)

The time when the project was created.

LastModifiedTime -> (timestamp)

The timestamp when project was last modified.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.