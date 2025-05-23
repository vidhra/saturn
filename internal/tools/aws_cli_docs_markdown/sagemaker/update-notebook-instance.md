# update-notebook-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-notebook-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-notebook-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# update-notebook-instance

## Description

Updates a notebook instance. NotebookInstance updates include upgrading or downgrading the ML compute instance used for your notebook instance to accommodate changes in your workload requirements.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateNotebookInstance)

## Synopsis

```
update-notebook-instance
--notebook-instance-name <value>
[--instance-type <value>]
[--role-arn <value>]
[--lifecycle-config-name <value>]
[--disassociate-lifecycle-config | --no-disassociate-lifecycle-config]
[--volume-size-in-gb <value>]
[--default-code-repository <value>]
[--additional-code-repositories <value>]
[--accelerator-types <value>]
[--disassociate-accelerator-types | --no-disassociate-accelerator-types]
[--disassociate-default-code-repository | --no-disassociate-default-code-repository]
[--disassociate-additional-code-repositories | --no-disassociate-additional-code-repositories]
[--root-access <value>]
[--instance-metadata-service-configuration <value>]
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

`--notebook-instance-name` (string)

The name of the notebook instance to update.

`--instance-type` (string)

The Amazon ML compute instance type.

Possible values:

- `ml.t2.medium`
- `ml.t2.large`
- `ml.t2.xlarge`
- `ml.t2.2xlarge`
- `ml.t3.medium`
- `ml.t3.large`
- `ml.t3.xlarge`
- `ml.t3.2xlarge`
- `ml.m4.xlarge`
- `ml.m4.2xlarge`
- `ml.m4.4xlarge`
- `ml.m4.10xlarge`
- `ml.m4.16xlarge`
- `ml.m5.xlarge`
- `ml.m5.2xlarge`
- `ml.m5.4xlarge`
- `ml.m5.12xlarge`
- `ml.m5.24xlarge`
- `ml.m5d.large`
- `ml.m5d.xlarge`
- `ml.m5d.2xlarge`
- `ml.m5d.4xlarge`
- `ml.m5d.8xlarge`
- `ml.m5d.12xlarge`
- `ml.m5d.16xlarge`
- `ml.m5d.24xlarge`
- `ml.c4.xlarge`
- `ml.c4.2xlarge`
- `ml.c4.4xlarge`
- `ml.c4.8xlarge`
- `ml.c5.xlarge`
- `ml.c5.2xlarge`
- `ml.c5.4xlarge`
- `ml.c5.9xlarge`
- `ml.c5.18xlarge`
- `ml.c5d.xlarge`
- `ml.c5d.2xlarge`
- `ml.c5d.4xlarge`
- `ml.c5d.9xlarge`
- `ml.c5d.18xlarge`
- `ml.p2.xlarge`
- `ml.p2.8xlarge`
- `ml.p2.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.8xlarge`
- `ml.p3.16xlarge`
- `ml.p3dn.24xlarge`
- `ml.g4dn.xlarge`
- `ml.g4dn.2xlarge`
- `ml.g4dn.4xlarge`
- `ml.g4dn.8xlarge`
- `ml.g4dn.12xlarge`
- `ml.g4dn.16xlarge`
- `ml.r5.large`
- `ml.r5.xlarge`
- `ml.r5.2xlarge`
- `ml.r5.4xlarge`
- `ml.r5.8xlarge`
- `ml.r5.12xlarge`
- `ml.r5.16xlarge`
- `ml.r5.24xlarge`
- `ml.g5.xlarge`
- `ml.g5.2xlarge`
- `ml.g5.4xlarge`
- `ml.g5.8xlarge`
- `ml.g5.16xlarge`
- `ml.g5.12xlarge`
- `ml.g5.24xlarge`
- `ml.g5.48xlarge`
- `ml.inf1.xlarge`
- `ml.inf1.2xlarge`
- `ml.inf1.6xlarge`
- `ml.inf1.24xlarge`
- `ml.trn1.2xlarge`
- `ml.trn1.32xlarge`
- `ml.trn1n.32xlarge`
- `ml.inf2.xlarge`
- `ml.inf2.8xlarge`
- `ml.inf2.24xlarge`
- `ml.inf2.48xlarge`
- `ml.p4d.24xlarge`
- `ml.p4de.24xlarge`
- `ml.p5.48xlarge`
- `ml.m6i.large`
- `ml.m6i.xlarge`
- `ml.m6i.2xlarge`
- `ml.m6i.4xlarge`
- `ml.m6i.8xlarge`
- `ml.m6i.12xlarge`
- `ml.m6i.16xlarge`
- `ml.m6i.24xlarge`
- `ml.m6i.32xlarge`
- `ml.m7i.large`
- `ml.m7i.xlarge`
- `ml.m7i.2xlarge`
- `ml.m7i.4xlarge`
- `ml.m7i.8xlarge`
- `ml.m7i.12xlarge`
- `ml.m7i.16xlarge`
- `ml.m7i.24xlarge`
- `ml.m7i.48xlarge`
- `ml.c6i.large`
- `ml.c6i.xlarge`
- `ml.c6i.2xlarge`
- `ml.c6i.4xlarge`
- `ml.c6i.8xlarge`
- `ml.c6i.12xlarge`
- `ml.c6i.16xlarge`
- `ml.c6i.24xlarge`
- `ml.c6i.32xlarge`
- `ml.c7i.large`
- `ml.c7i.xlarge`
- `ml.c7i.2xlarge`
- `ml.c7i.4xlarge`
- `ml.c7i.8xlarge`
- `ml.c7i.12xlarge`
- `ml.c7i.16xlarge`
- `ml.c7i.24xlarge`
- `ml.c7i.48xlarge`
- `ml.r6i.large`
- `ml.r6i.xlarge`
- `ml.r6i.2xlarge`
- `ml.r6i.4xlarge`
- `ml.r6i.8xlarge`
- `ml.r6i.12xlarge`
- `ml.r6i.16xlarge`
- `ml.r6i.24xlarge`
- `ml.r6i.32xlarge`
- `ml.r7i.large`
- `ml.r7i.xlarge`
- `ml.r7i.2xlarge`
- `ml.r7i.4xlarge`
- `ml.r7i.8xlarge`
- `ml.r7i.12xlarge`
- `ml.r7i.16xlarge`
- `ml.r7i.24xlarge`
- `ml.r7i.48xlarge`
- `ml.m6id.large`
- `ml.m6id.xlarge`
- `ml.m6id.2xlarge`
- `ml.m6id.4xlarge`
- `ml.m6id.8xlarge`
- `ml.m6id.12xlarge`
- `ml.m6id.16xlarge`
- `ml.m6id.24xlarge`
- `ml.m6id.32xlarge`
- `ml.c6id.large`
- `ml.c6id.xlarge`
- `ml.c6id.2xlarge`
- `ml.c6id.4xlarge`
- `ml.c6id.8xlarge`
- `ml.c6id.12xlarge`
- `ml.c6id.16xlarge`
- `ml.c6id.24xlarge`
- `ml.c6id.32xlarge`
- `ml.r6id.large`
- `ml.r6id.xlarge`
- `ml.r6id.2xlarge`
- `ml.r6id.4xlarge`
- `ml.r6id.8xlarge`
- `ml.r6id.12xlarge`
- `ml.r6id.16xlarge`
- `ml.r6id.24xlarge`
- `ml.r6id.32xlarge`
- `ml.g6.xlarge`
- `ml.g6.2xlarge`
- `ml.g6.4xlarge`
- `ml.g6.8xlarge`
- `ml.g6.12xlarge`
- `ml.g6.16xlarge`
- `ml.g6.24xlarge`
- `ml.g6.48xlarge`

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that SageMaker AI can assume to access the notebook instance. For more information, see [SageMaker AI Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) .

### Note

To be able to pass this role to SageMaker AI, the caller of this API must have the `iam:PassRole` permission.

`--lifecycle-config-name` (string)

The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) .

`--disassociate-lifecycle-config` | `--no-disassociate-lifecycle-config` (boolean)

Set to `true` to remove the notebook instance lifecycle configuration currently associated with the notebook instance. This operation is idempotent. If you specify a lifecycle configuration that is not associated with the notebook instance when you call this method, it does not throw an error.

`--volume-size-in-gb` (integer)

The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB. ML storage volumes are encrypted, so SageMaker AI canât determine the amount of available free space on the volume. Because of this, you can increase the volume size when you update a notebook instance, but you canât decrease the volume size. If you want to decrease the size of the ML storage volume in use, create a new notebook instance with the desired size.

`--default-code-repository` (string)

The Git repository to associate with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in [Amazon Web Services CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html) .

`--additional-code-repositories` (list)

An array of up to three Git repositories to associate with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in [Amazon Web Services CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--accelerator-types` (list)

This parameter is no longer supported. Elastic Inference (EI) is no longer available.

This parameter was used to specify a list of the EI instance types to associate with this notebook instance.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ml.eia1.medium
  ml.eia1.large
  ml.eia1.xlarge
  ml.eia2.medium
  ml.eia2.large
  ml.eia2.xlarge
```

`--disassociate-accelerator-types` | `--no-disassociate-accelerator-types` (boolean)

This parameter is no longer supported. Elastic Inference (EI) is no longer available.

This parameter was used to specify a list of the EI instance types to remove from this notebook instance.

`--disassociate-default-code-repository` | `--no-disassociate-default-code-repository` (boolean)

The name or URL of the default Git repository to remove from this notebook instance. This operation is idempotent. If you specify a Git repository that is not associated with the notebook instance when you call this method, it does not throw an error.

`--disassociate-additional-code-repositories` | `--no-disassociate-additional-code-repositories` (boolean)

A list of names or URLs of the default Git repositories to remove from this notebook instance. This operation is idempotent. If you specify a Git repository that is not associated with the notebook instance when you call this method, it does not throw an error.

`--root-access` (string)

Whether root access is enabled or disabled for users of the notebook instance. The default value is `Enabled` .

### Note

If you set this to `Disabled` , users donât have root access on the notebook instance, but lifecycle configuration scripts still run with root permissions.

Possible values:

- `Enabled`
- `Disabled`

`--instance-metadata-service-configuration` (structure)

Information on the IMDS configuration of the notebook instance

MinimumInstanceMetadataServiceVersion -> (string)

Indicates the minimum IMDS version that the notebook instance supports. When passed as part of `CreateNotebookInstance` , if no value is selected, then it defaults to IMDSv1. This means that both IMDSv1 and IMDSv2 are supported. If passed as part of `UpdateNotebookInstance` , there is no default.

Shorthand Syntax:

```
MinimumInstanceMetadataServiceVersion=string
```

JSON Syntax:

```
{
  "MinimumInstanceMetadataServiceVersion": "string"
}
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

## Output

None