# create-notebook-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-notebook-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-notebook-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-notebook-instance

## Description

Creates an SageMaker AI notebook instance. A notebook instance is a machine learning (ML) compute instance running on a Jupyter notebook.

In a `CreateNotebookInstance` request, specify the type of ML compute instance that you want to run. SageMaker AI launches the instance, installs common libraries that you can use to explore datasets for model training, and attaches an ML storage volume to the notebook instance.

SageMaker AI also provides a set of example notebooks. Each notebook demonstrates how to use SageMaker AI with a specific algorithm or with a machine learning framework.

After receiving the request, SageMaker AI does the following:

- Creates a network interface in the SageMaker AI VPC.
- (Option) If you specified `SubnetId` , SageMaker AI creates a network interface in your own VPC, which is inferred from the subnet ID that you provide in the input. When creating this network interface, SageMaker AI attaches the security group that you specified in the request to the network interface that it creates in your VPC.
- Launches an EC2 instance of the type specified in the request in the SageMaker AI VPC. If you specified `SubnetId` of your VPC, SageMaker AI specifies both network interfaces when launching this instance. This enables inbound traffic from your own VPC to the notebook instance, assuming that the security groups allow it.

After creating the notebook instance, SageMaker AI returns its Amazon Resource Name (ARN). You canât change the name of a notebook instance after you create it.

After SageMaker AI creates the notebook instance, you can connect to the Jupyter server and work in Jupyter notebooks. For example, you can write code to explore a dataset that you can use for model training, train a model, host models by creating SageMaker AI endpoints, and validate hosted models.

For more information, see [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateNotebookInstance)

## Synopsis

```
create-notebook-instance
--notebook-instance-name <value>
--instance-type <value>
[--subnet-id <value>]
[--security-group-ids <value>]
--role-arn <value>
[--kms-key-id <value>]
[--tags <value>]
[--lifecycle-config-name <value>]
[--direct-internet-access <value>]
[--volume-size-in-gb <value>]
[--accelerator-types <value>]
[--default-code-repository <value>]
[--additional-code-repositories <value>]
[--root-access <value>]
[--platform-identifier <value>]
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

The name of the new notebook instance.

`--instance-type` (string)

The type of ML compute instance to launch for the notebook instance.

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

`--subnet-id` (string)

The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance.

`--security-group-ids` (list)

The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.

(string)

Syntax:

```
"string" "string" ...
```

`--role-arn` (string)

When you send any requests to Amazon Web Services resources from the notebook instance, SageMaker AI assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so SageMaker AI can perform these tasks. The policy must allow the SageMaker AI service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see [SageMaker AI Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) .

### Note

To be able to pass this role to SageMaker AI, the caller of this API must have the `iam:PassRole` permission.

`--kms-key-id` (string)

The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service key that SageMaker AI uses to encrypt data on the storage volume attached to your notebook instance. The KMS key you provide must be enabled. For information, see [Enabling and Disabling Keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) in the *Amazon Web Services Key Management Service Developer Guide* .

`--tags` (list)

An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

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

`--lifecycle-config-name` (string)

The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) .

`--direct-internet-access` (string)

Sets whether SageMaker AI provides internet access to the notebook instance. If you set this to `Disabled` this notebook instance is able to access resources only in your VPC, and is not be able to connect to SageMaker AI training and endpoint services unless you configure a NAT Gateway in your VPC.

For more information, see [Notebook Instances Are Internet-Enabled by Default](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access) . You can set the value of this parameter to `Disabled` only if you set a value for the `SubnetId` parameter.

Possible values:

- `Enabled`
- `Disabled`

`--volume-size-in-gb` (integer)

The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.

`--accelerator-types` (list)

This parameter is no longer supported. Elastic Inference (EI) is no longer available.

This parameter was used to specify a list of EI instance types to associate with this notebook instance.

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

`--default-code-repository` (string)

A Git repository to associate with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in [Amazon Web Services CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html) .

`--additional-code-repositories` (list)

An array of up to three Git repositories to associate with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in [Amazon Web Services CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--root-access` (string)

Whether root access is enabled or disabled for users of the notebook instance. The default value is `Enabled` .

### Note

Lifecycle configurations need root access to be able to set up a notebook instance. Because of this, lifecycle configurations associated with a notebook instance always run with root access even if you disable root access for users.

Possible values:

- `Enabled`
- `Disabled`

`--platform-identifier` (string)

The platform identifier of the notebook instance runtime environment.

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

NotebookInstanceArn -> (string)

The Amazon Resource Name (ARN) of the notebook instance.