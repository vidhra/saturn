# create-spaceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-space

## Description

Creates a private space or a space used for real time collaboration in a domain.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateSpace)

## Synopsis

```
create-space
--domain-id <value>
--space-name <value>
[--tags <value>]
[--space-settings <value>]
[--ownership-settings <value>]
[--space-sharing-settings <value>]
[--space-display-name <value>]
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

`--domain-id` (string)

The ID of the associated domain.

`--space-name` (string)

The name of the space.

`--tags` (list)

Tags to associated with the space. Each tag consists of a key and an optional value. Tag keys must be unique for each resource. Tags are searchable using the `Search` API.

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

`--space-settings` (structure)

A collection of space settings.

JupyterServerAppSettings -> (structure)

The JupyterServer app settings.

DefaultResourceSpec -> (structure)

The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the JupyterServer app. If you use the `LifecycleConfigArns` parameter, then this parameter is also required.

SageMakerImageArn -> (string)

The ARN of the SageMaker AI image that the image version belongs to.

SageMakerImageVersionArn -> (string)

The ARN of the image version created on the instance. To clear the value set for `SageMakerImageVersionArn` , pass `None` as the value.

SageMakerImageVersionAlias -> (string)

The SageMakerImageVersionAlias of the image to launch with. This value is in SemVer 2.0.0 versioning format.

InstanceType -> (string)

The instance type that the image version runs on.

### Note

**JupyterServer apps** only support the `system` value.

For **KernelGateway apps** , the `system` value is translated to `ml.t3.medium` . KernelGateway apps also support all other values for available instance types.

LifecycleConfigArn -> (string)

The Amazon Resource Name (ARN) of the Lifecycle Configuration attached to the Resource.

LifecycleConfigArns -> (list)

The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the JupyterServerApp. If you use this parameter, the `DefaultResourceSpec` parameter is also required.

### Note

To remove a Lifecycle Config, you must set `LifecycleConfigArns` to an empty list.

(string)

CodeRepositories -> (list)

A list of Git repositories that SageMaker AI automatically displays to users for cloning in the JupyterServer application.

(structure)

A Git repository that SageMaker AI automatically displays to users for cloning in the JupyterServer application.

RepositoryUrl -> (string)

The URL of the Git repository.

KernelGatewayAppSettings -> (structure)

The KernelGateway app settings.

DefaultResourceSpec -> (structure)

The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the KernelGateway app.

### Note

The Amazon SageMaker AI Studio UI does not use the default instance type value set here. The default instance type set here is used when Apps are created using the CLI or CloudFormation and the instance type parameter value is not passed.

SageMakerImageArn -> (string)

The ARN of the SageMaker AI image that the image version belongs to.

SageMakerImageVersionArn -> (string)

The ARN of the image version created on the instance. To clear the value set for `SageMakerImageVersionArn` , pass `None` as the value.

SageMakerImageVersionAlias -> (string)

The SageMakerImageVersionAlias of the image to launch with. This value is in SemVer 2.0.0 versioning format.

InstanceType -> (string)

The instance type that the image version runs on.

### Note

**JupyterServer apps** only support the `system` value.

For **KernelGateway apps** , the `system` value is translated to `ml.t3.medium` . KernelGateway apps also support all other values for available instance types.

LifecycleConfigArn -> (string)

The Amazon Resource Name (ARN) of the Lifecycle Configuration attached to the Resource.

CustomImages -> (list)

A list of custom SageMaker AI images that are configured to run as a KernelGateway app.

The maximum number of custom images are as follows.

- On a domain level: 200
- On a space level: 5
- On a user profile level: 5

(structure)

A custom SageMaker AI image. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html) .

ImageName -> (string)

The name of the CustomImage. Must be unique to your account.

ImageVersionNumber -> (integer)

The version number of the CustomImage.

AppImageConfigName -> (string)

The name of the AppImageConfig.

LifecycleConfigArns -> (list)

The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the the user profile or domain.

### Note

To remove a Lifecycle Config, you must set `LifecycleConfigArns` to an empty list.

(string)

CodeEditorAppSettings -> (structure)

The Code Editor application settings.

DefaultResourceSpec -> (structure)

Specifies the ARNâs of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.

### Note

When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn` , pass `None` as the value.

SageMakerImageArn -> (string)

The ARN of the SageMaker AI image that the image version belongs to.

SageMakerImageVersionArn -> (string)

The ARN of the image version created on the instance. To clear the value set for `SageMakerImageVersionArn` , pass `None` as the value.

SageMakerImageVersionAlias -> (string)

The SageMakerImageVersionAlias of the image to launch with. This value is in SemVer 2.0.0 versioning format.

InstanceType -> (string)

The instance type that the image version runs on.

### Note

**JupyterServer apps** only support the `system` value.

For **KernelGateway apps** , the `system` value is translated to `ml.t3.medium` . KernelGateway apps also support all other values for available instance types.

LifecycleConfigArn -> (string)

The Amazon Resource Name (ARN) of the Lifecycle Configuration attached to the Resource.

AppLifecycleManagement -> (structure)

Settings that are used to configure and manage the lifecycle of CodeEditor applications in a space.

IdleSettings -> (structure)

Settings related to idle shutdown of Studio applications.

IdleTimeoutInMinutes -> (integer)

The time that SageMaker waits after the application becomes idle before shutting it down.

JupyterLabAppSettings -> (structure)

The settings for the JupyterLab application.

DefaultResourceSpec -> (structure)

Specifies the ARNâs of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.

### Note

When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn` , pass `None` as the value.

SageMakerImageArn -> (string)

The ARN of the SageMaker AI image that the image version belongs to.

SageMakerImageVersionArn -> (string)

The ARN of the image version created on the instance. To clear the value set for `SageMakerImageVersionArn` , pass `None` as the value.

SageMakerImageVersionAlias -> (string)

The SageMakerImageVersionAlias of the image to launch with. This value is in SemVer 2.0.0 versioning format.

InstanceType -> (string)

The instance type that the image version runs on.

### Note

**JupyterServer apps** only support the `system` value.

For **KernelGateway apps** , the `system` value is translated to `ml.t3.medium` . KernelGateway apps also support all other values for available instance types.

LifecycleConfigArn -> (string)

The Amazon Resource Name (ARN) of the Lifecycle Configuration attached to the Resource.

CodeRepositories -> (list)

A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.

(structure)

A Git repository that SageMaker AI automatically displays to users for cloning in the JupyterServer application.

RepositoryUrl -> (string)

The URL of the Git repository.

AppLifecycleManagement -> (structure)

Settings that are used to configure and manage the lifecycle of JupyterLab applications in a space.

IdleSettings -> (structure)

Settings related to idle shutdown of Studio applications.

IdleTimeoutInMinutes -> (integer)

The time that SageMaker waits after the application becomes idle before shutting it down.

AppType -> (string)

The type of app created within the space.

If using the [UpdateSpace](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateSpace.html) API, you canât change the app type of your space by specifying a different value for this field.

SpaceStorageSettings -> (structure)

The storage settings for a space.

EbsStorageSettings -> (structure)

A collection of EBS storage settings for a space.

EbsVolumeSizeInGb -> (integer)

The size of an EBS storage volume for a space.

SpaceManagedResources -> (string)

If you enable this option, SageMaker AI creates the following resources on your behalf when you create the space:

- The user profile that possesses the space.
- The app that the space contains.

CustomFileSystems -> (list)

A file system, created by you, that you assign to a space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

(tagged union structure)

A file system, created by you, that you assign to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `EFSFileSystem`, `FSxLustreFileSystem`.

EFSFileSystem -> (structure)

A custom file system in Amazon EFS.

FileSystemId -> (string)

The ID of your Amazon EFS file system.

FSxLustreFileSystem -> (structure)

A custom file system in Amazon FSx for Lustre.

FileSystemId -> (string)

Amazon FSx for Lustre file system ID.

JSON Syntax:

```
{
  "JupyterServerAppSettings": {
    "DefaultResourceSpec": {
      "SageMakerImageArn": "string",
      "SageMakerImageVersionArn": "string",
      "SageMakerImageVersionAlias": "string",
      "InstanceType": "system"|"ml.t3.micro"|"ml.t3.small"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.geospatial.interactive"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.p5.48xlarge"|"ml.p5en.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge",
      "LifecycleConfigArn": "string"
    },
    "LifecycleConfigArns": ["string", ...],
    "CodeRepositories": [
      {
        "RepositoryUrl": "string"
      }
      ...
    ]
  },
  "KernelGatewayAppSettings": {
    "DefaultResourceSpec": {
      "SageMakerImageArn": "string",
      "SageMakerImageVersionArn": "string",
      "SageMakerImageVersionAlias": "string",
      "InstanceType": "system"|"ml.t3.micro"|"ml.t3.small"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.geospatial.interactive"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.p5.48xlarge"|"ml.p5en.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge",
      "LifecycleConfigArn": "string"
    },
    "CustomImages": [
      {
        "ImageName": "string",
        "ImageVersionNumber": integer,
        "AppImageConfigName": "string"
      }
      ...
    ],
    "LifecycleConfigArns": ["string", ...]
  },
  "CodeEditorAppSettings": {
    "DefaultResourceSpec": {
      "SageMakerImageArn": "string",
      "SageMakerImageVersionArn": "string",
      "SageMakerImageVersionAlias": "string",
      "InstanceType": "system"|"ml.t3.micro"|"ml.t3.small"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.geospatial.interactive"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.p5.48xlarge"|"ml.p5en.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge",
      "LifecycleConfigArn": "string"
    },
    "AppLifecycleManagement": {
      "IdleSettings": {
        "IdleTimeoutInMinutes": integer
      }
    }
  },
  "JupyterLabAppSettings": {
    "DefaultResourceSpec": {
      "SageMakerImageArn": "string",
      "SageMakerImageVersionArn": "string",
      "SageMakerImageVersionAlias": "string",
      "InstanceType": "system"|"ml.t3.micro"|"ml.t3.small"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.geospatial.interactive"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.p5.48xlarge"|"ml.p5en.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge",
      "LifecycleConfigArn": "string"
    },
    "CodeRepositories": [
      {
        "RepositoryUrl": "string"
      }
      ...
    ],
    "AppLifecycleManagement": {
      "IdleSettings": {
        "IdleTimeoutInMinutes": integer
      }
    }
  },
  "AppType": "JupyterServer"|"KernelGateway"|"DetailedProfiler"|"TensorBoard"|"CodeEditor"|"JupyterLab"|"RStudioServerPro"|"RSessionGateway"|"Canvas",
  "SpaceStorageSettings": {
    "EbsStorageSettings": {
      "EbsVolumeSizeInGb": integer
    }
  },
  "SpaceManagedResources": "ENABLED"|"DISABLED",
  "CustomFileSystems": [
    {
      "EFSFileSystem": {
        "FileSystemId": "string"
      },
      "FSxLustreFileSystem": {
        "FileSystemId": "string"
      }
    }
    ...
  ]
}
```

`--ownership-settings` (structure)

A collection of ownership settings.

OwnerUserProfileName -> (string)

The user profile who is the owner of the space.

Shorthand Syntax:

```
OwnerUserProfileName=string
```

JSON Syntax:

```
{
  "OwnerUserProfileName": "string"
}
```

`--space-sharing-settings` (structure)

A collection of space sharing settings.

SharingType -> (string)

Specifies the sharing type of the space.

Shorthand Syntax:

```
SharingType=string
```

JSON Syntax:

```
{
  "SharingType": "Private"|"Shared"
}
```

`--space-display-name` (string)

The name of the space that appears in the SageMaker Studio UI.

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

SpaceArn -> (string)

The spaceâs Amazon Resource Name (ARN).