# create-domainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-domain

## Description

Creates a `Domain` . A domain consists of an associated Amazon Elastic File System volume, a list of authorized users, and a variety of security, application, policy, and Amazon Virtual Private Cloud (VPC) configurations. Users within a domain can share notebook files and other artifacts with each other.

**EFS storage**

When a domain is created, an EFS volume is created for use by all of the users within the domain. Each user receives a private home directory within the EFS volume for notebooks, Git repositories, and data files.

SageMaker AI uses the Amazon Web Services Key Management Service (Amazon Web Services KMS) to encrypt the EFS volume attached to the domain with an Amazon Web Services managed key by default. For more control, you can specify a customer managed key. For more information, see [Protect Data at Rest Using Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest.html) .

**VPC configuration**

All traffic between the domain and the Amazon EFS volume is through the specified VPC and subnets. For other traffic, you can specify the `AppNetworkAccessType` parameter. `AppNetworkAccessType` corresponds to the network access type that you choose when you onboard to the domain. The following options are available:

- `PublicInternetOnly` - Non-EFS traffic goes through a VPC managed by Amazon SageMaker AI, which allows internet access. This is the default value.
- `VpcOnly` - All traffic is through the specified VPC and subnets. Internet access is disabled by default. To allow internet access, you must specify a NAT gateway. When internet access is disabled, you wonât be able to run a Amazon SageMaker AI Studio notebook or to train or host models unless your VPC has an interface endpoint to the SageMaker AI API and runtime or a NAT gateway and your security groups allow outbound connections.

### Warning

NFS traffic over TCP on port 2049 needs to be allowed in both inbound and outbound rules in order to launch a Amazon SageMaker AI Studio app successfully.

For more information, see [Connect Amazon SageMaker AI Studio Notebooks to Resources in a VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateDomain)

## Synopsis

```
create-domain
--domain-name <value>
--auth-mode <value>
--default-user-settings <value>
[--domain-settings <value>]
--subnet-ids <value>
--vpc-id <value>
[--tags <value>]
[--app-network-access-type <value>]
[--home-efs-file-system-kms-key-id <value>]
[--kms-key-id <value>]
[--app-security-group-management <value>]
[--tag-propagation <value>]
[--default-space-settings <value>]
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

`--domain-name` (string)

A name for the domain.

`--auth-mode` (string)

The mode of authentication that members use to access the domain.

Possible values:

- `SSO`
- `IAM`

`--default-user-settings` (structure)

The default settings to use to create a user profile when `UserSettings` isnât specified in the call to the `CreateUserProfile` API.

`SecurityGroups` is aggregated when specified in both calls. For all other settings in `UserSettings` , the values specified in `CreateUserProfile` take precedence over those specified in `CreateDomain` .

ExecutionRole -> (string)

The execution role for the user.

SageMaker applies this setting only to private spaces that the user creates in the domain. SageMaker doesnât apply this setting to shared spaces.

SecurityGroups -> (list)

The security groups for the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.

Optional when the `CreateDomain.AppNetworkAccessType` parameter is set to `PublicInternetOnly` .

Required when the `CreateDomain.AppNetworkAccessType` parameter is set to `VpcOnly` , unless specified as part of the `DefaultUserSettings` for the domain.

Amazon SageMaker AI adds a security group to allow NFS traffic from Amazon SageMaker AI Studio. Therefore, the number of security groups that you can specify is one less than the maximum number shown.

SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesnât apply these settings to shared spaces.

(string)

SharingSettings -> (structure)

Specifies options for sharing Amazon SageMaker AI Studio notebooks.

NotebookOutputOption -> (string)

Whether to include the notebook cell output when sharing the notebook. The default is `Disabled` .

S3OutputPath -> (string)

When `NotebookOutputOption` is `Allowed` , the Amazon S3 bucket used to store the shared notebook snapshots.

S3KmsKeyId -> (string)

When `NotebookOutputOption` is `Allowed` , the Amazon Web Services Key Management Service (KMS) encryption key ID used to encrypt the notebook cell output in the Amazon S3 bucket.

JupyterServerAppSettings -> (structure)

The Jupyter serverâs app settings.

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

The kernel gateway app settings.

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

TensorBoardAppSettings -> (structure)

The TensorBoard app settings.

DefaultResourceSpec -> (structure)

The default instance type and the Amazon Resource Name (ARN) of the SageMaker AI image created on the instance.

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

RStudioServerProAppSettings -> (structure)

A collection of settings that configure user interaction with the `RStudioServerPro` app.

AccessStatus -> (string)

Indicates whether the current user has access to the `RStudioServerPro` app.

UserGroup -> (string)

The level of permissions that the user has within the `RStudioServerPro` app. This value defaults to User. The Admin value allows the user access to the RStudio Administrative Dashboard.

RSessionAppSettings -> (structure)

A collection of settings that configure the `RSessionGateway` app.

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

CustomImages -> (list)

A list of custom SageMaker AI images that are configured to run as a RSession app.

(structure)

A custom SageMaker AI image. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html) .

ImageName -> (string)

The name of the CustomImage. Must be unique to your account.

ImageVersionNumber -> (integer)

The version number of the CustomImage.

AppImageConfigName -> (string)

The name of the AppImageConfig.

CanvasAppSettings -> (structure)

The Canvas app settings.

SageMaker applies these settings only to private spaces that SageMaker creates for the Canvas app.

TimeSeriesForecastingSettings -> (structure)

Time series forecast settings for the SageMaker Canvas application.

Status -> (string)

Describes whether time series forecasting is enabled or disabled in the Canvas application.

AmazonForecastRoleArn -> (string)

The IAM role that Canvas passes to Amazon Forecast for time series forecasting. By default, Canvas uses the execution role specified in the `UserProfile` that launches the Canvas application. If an execution role is not specified in the `UserProfile` , Canvas uses the execution role specified in the Domain that owns the `UserProfile` . To allow time series forecasting, this IAM role should have the [AmazonSageMakerCanvasForecastAccess](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-canvas.html#security-iam-awsmanpol-AmazonSageMakerCanvasForecastAccess) policy attached and `forecast.amazonaws.com` added in the trust relationship as a service principal.

ModelRegisterSettings -> (structure)

The model registry settings for the SageMaker Canvas application.

Status -> (string)

Describes whether the integration to the model registry is enabled or disabled in the Canvas application.

CrossAccountModelRegisterRoleArn -> (string)

The Amazon Resource Name (ARN) of the SageMaker model registry account. Required only to register model versions created by a different SageMaker Canvas Amazon Web Services account than the Amazon Web Services account in which SageMaker model registry is set up.

WorkspaceSettings -> (structure)

The workspace settings for the SageMaker Canvas application.

S3ArtifactPath -> (string)

The Amazon S3 bucket used to store artifacts generated by Canvas. Updating the Amazon S3 location impacts existing configuration settings, and Canvas users no longer have access to their artifacts. Canvas users must log out and log back in to apply the new location.

S3KmsKeyId -> (string)

The Amazon Web Services Key Management Service (KMS) encryption key ID that is used to encrypt artifacts generated by Canvas in the Amazon S3 bucket.

IdentityProviderOAuthSettings -> (list)

The settings for connecting to an external data source with OAuth.

(structure)

The Amazon SageMaker Canvas application setting where you configure OAuth for connecting to an external data source, such as Snowflake.

DataSourceName -> (string)

The name of the data source that youâre connecting to. Canvas currently supports OAuth for Snowflake and Salesforce Data Cloud.

Status -> (string)

Describes whether OAuth for a data source is enabled or disabled in the Canvas application.

SecretArn -> (string)

The ARN of an Amazon Web Services Secrets Manager secret that stores the credentials from your identity provider, such as the client ID and secret, authorization URL, and token URL.

DirectDeploySettings -> (structure)

The model deployment settings for the SageMaker Canvas application.

Status -> (string)

Describes whether model deployment permissions are enabled or disabled in the Canvas application.

KendraSettings -> (structure)

The settings for document querying.

Status -> (string)

Describes whether the document querying feature is enabled or disabled in the Canvas application.

GenerativeAiSettings -> (structure)

The generative AI settings for the SageMaker Canvas application.

AmazonBedrockRoleArn -> (string)

The ARN of an Amazon Web Services IAM role that allows fine-tuning of large language models (LLMs) in Amazon Bedrock. The IAM role should have Amazon S3 read and write permissions, as well as a trust relationship that establishes `bedrock.amazonaws.com` as a service principal.

EmrServerlessSettings -> (structure)

The settings for running Amazon EMR Serverless data processing jobs in SageMaker Canvas.

ExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services IAM role that is assumed for running Amazon EMR Serverless jobs in SageMaker Canvas. This role should have the necessary permissions to read and write data attached and a trust relationship with EMR Serverless.

Status -> (string)

Describes whether Amazon EMR Serverless job capabilities are enabled or disabled in the SageMaker Canvas application.

CodeEditorAppSettings -> (structure)

The Code Editor application settings.

SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesnât apply these settings to shared spaces.

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

CustomImages -> (list)

A list of custom SageMaker images that are configured to run as a Code Editor app.

(structure)

A custom SageMaker AI image. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html) .

ImageName -> (string)

The name of the CustomImage. Must be unique to your account.

ImageVersionNumber -> (integer)

The version number of the CustomImage.

AppImageConfigName -> (string)

The name of the AppImageConfig.

LifecycleConfigArns -> (list)

The Amazon Resource Name (ARN) of the Code Editor application lifecycle configuration.

(string)

AppLifecycleManagement -> (structure)

Settings that are used to configure and manage the lifecycle of CodeEditor applications.

IdleSettings -> (structure)

Settings related to idle shutdown of Studio applications.

LifecycleManagement -> (string)

Indicates whether idle shutdown is activated for the application type.

IdleTimeoutInMinutes -> (integer)

The time that SageMaker waits after the application becomes idle before shutting it down.

MinIdleTimeoutInMinutes -> (integer)

The minimum value in minutes that custom idle shutdown can be set to by the user.

MaxIdleTimeoutInMinutes -> (integer)

The maximum value in minutes that custom idle shutdown can be set to by the user.

BuiltInLifecycleConfigArn -> (string)

The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.

JupyterLabAppSettings -> (structure)

The settings for the JupyterLab application.

SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesnât apply these settings to shared spaces.

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

CustomImages -> (list)

A list of custom SageMaker images that are configured to run as a JupyterLab app.

(structure)

A custom SageMaker AI image. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html) .

ImageName -> (string)

The name of the CustomImage. Must be unique to your account.

ImageVersionNumber -> (integer)

The version number of the CustomImage.

AppImageConfigName -> (string)

The name of the AppImageConfig.

LifecycleConfigArns -> (list)

The Amazon Resource Name (ARN) of the lifecycle configurations attached to the user profile or domain. To remove a lifecycle config, you must set `LifecycleConfigArns` to an empty list.

(string)

CodeRepositories -> (list)

A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.

(structure)

A Git repository that SageMaker AI automatically displays to users for cloning in the JupyterServer application.

RepositoryUrl -> (string)

The URL of the Git repository.

AppLifecycleManagement -> (structure)

Indicates whether idle shutdown is activated for JupyterLab applications.

IdleSettings -> (structure)

Settings related to idle shutdown of Studio applications.

LifecycleManagement -> (string)

Indicates whether idle shutdown is activated for the application type.

IdleTimeoutInMinutes -> (integer)

The time that SageMaker waits after the application becomes idle before shutting it down.

MinIdleTimeoutInMinutes -> (integer)

The minimum value in minutes that custom idle shutdown can be set to by the user.

MaxIdleTimeoutInMinutes -> (integer)

The maximum value in minutes that custom idle shutdown can be set to by the user.

EmrSettings -> (structure)

The configuration parameters that specify the IAM roles assumed by the execution role of SageMaker (assumable roles) and the cluster instances or job execution environments (execution roles or runtime roles) to manage and access resources required for running Amazon EMR clusters or Amazon EMR Serverless applications.

AssumableRoleArns -> (list)

An array of Amazon Resource Names (ARNs) of the IAM roles that the execution role of SageMaker can assume for performing operations or tasks related to Amazon EMR clusters or Amazon EMR Serverless applications. These roles define the permissions and access policies required when performing Amazon EMR-related operations, such as listing, connecting to, or terminating Amazon EMR clusters or Amazon EMR Serverless applications. They are typically used in cross-account access scenarios, where the Amazon EMR resources (clusters or serverless applications) are located in a different Amazon Web Services account than the SageMaker domain.

(string)

ExecutionRoleArns -> (list)

An array of Amazon Resource Names (ARNs) of the IAM roles used by the Amazon EMR cluster instances or job execution environments to access other Amazon Web Services services and resources needed during the runtime of your Amazon EMR or Amazon EMR Serverless workloads, such as Amazon S3 for data access, Amazon CloudWatch for logging, or other Amazon Web Services services based on the particular workload requirements.

(string)

BuiltInLifecycleConfigArn -> (string)

The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.

SpaceStorageSettings -> (structure)

The storage settings for a space.

SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesnât apply these settings to shared spaces.

DefaultEbsStorageSettings -> (structure)

The default EBS storage settings for a space.

DefaultEbsVolumeSizeInGb -> (integer)

The default size of the EBS storage volume for a space.

MaximumEbsVolumeSizeInGb -> (integer)

The maximum size of the EBS storage volume for a space.

DefaultLandingUri -> (string)

The default experience that the user is directed to when accessing the domain. The supported values are:

- `studio::` : Indicates that Studio is the default experience. This value can only be passed if `StudioWebPortal` is set to `ENABLED` .
- `app:JupyterServer:` : Indicates that Studio Classic is the default experience.

StudioWebPortal -> (string)

Whether the user can access Studio. If this value is set to `DISABLED` , the user cannot access Studio, even if that is the default experience for the domain.

CustomPosixUserConfig -> (structure)

Details about the POSIX identity that is used for file system operations.

SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesnât apply these settings to shared spaces.

Uid -> (long)

The POSIX user ID.

Gid -> (long)

The POSIX group ID.

CustomFileSystemConfigs -> (list)

The settings for assigning a custom file system to a user profile. Permitted users can access this file system in Amazon SageMaker AI Studio.

SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesnât apply these settings to shared spaces.

(tagged union structure)

The settings for assigning a custom file system to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `EFSFileSystemConfig`, `FSxLustreFileSystemConfig`.

EFSFileSystemConfig -> (structure)

The settings for a custom Amazon EFS file system.

FileSystemId -> (string)

The ID of your Amazon EFS file system.

FileSystemPath -> (string)

The path to the file system directory that is accessible in Amazon SageMaker AI Studio. Permitted users can access only this directory and below.

FSxLustreFileSystemConfig -> (structure)

The settings for a custom Amazon FSx for Lustre file system.

FileSystemId -> (string)

The globally unique, 17-digit, ID of the file system, assigned by Amazon FSx for Lustre.

FileSystemPath -> (string)

The path to the file system directory that is accessible in Amazon SageMaker Studio. Permitted users can access only this directory and below.

StudioWebPortalSettings -> (structure)

Studio settings. If these settings are applied on a user level, they take priority over the settings applied on a domain level.

HiddenMlTools -> (list)

The machine learning tools that are hidden from the Studio left navigation pane.

(string)

HiddenAppTypes -> (list)

The [Applications supported in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-apps.html) that are hidden from the Studio left navigation pane.

(string)

HiddenInstanceTypes -> (list)

The instance types you are hiding from the Studio user interface.

(string)

HiddenSageMakerImageVersionAliases -> (list)

The version aliases you are hiding from the Studio user interface.

(structure)

The SageMaker images that are hidden from the Studio user interface. You must specify the SageMaker image name and version aliases.

SageMakerImageName -> (string)

The SageMaker image name that you are hiding from the Studio user interface.

VersionAliases -> (list)

The version aliases you are hiding from the Studio user interface.

(string)

AutoMountHomeEFS -> (string)

Indicates whether auto-mounting of an EFS volume is supported for the user profile. The `DefaultAsDomain` value is only supported for user profiles. Do not use the `DefaultAsDomain` value when setting this parameter for a domain.

SageMaker applies this setting only to private spaces that the user creates in the domain. SageMaker doesnât apply this setting to shared spaces.

JSON Syntax:

```
{
  "ExecutionRole": "string",
  "SecurityGroups": ["string", ...],
  "SharingSettings": {
    "NotebookOutputOption": "Allowed"|"Disabled",
    "S3OutputPath": "string",
    "S3KmsKeyId": "string"
  },
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
  "TensorBoardAppSettings": {
    "DefaultResourceSpec": {
      "SageMakerImageArn": "string",
      "SageMakerImageVersionArn": "string",
      "SageMakerImageVersionAlias": "string",
      "InstanceType": "system"|"ml.t3.micro"|"ml.t3.small"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.geospatial.interactive"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.p5.48xlarge"|"ml.p5en.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge",
      "LifecycleConfigArn": "string"
    }
  },
  "RStudioServerProAppSettings": {
    "AccessStatus": "ENABLED"|"DISABLED",
    "UserGroup": "R_STUDIO_ADMIN"|"R_STUDIO_USER"
  },
  "RSessionAppSettings": {
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
    ]
  },
  "CanvasAppSettings": {
    "TimeSeriesForecastingSettings": {
      "Status": "ENABLED"|"DISABLED",
      "AmazonForecastRoleArn": "string"
    },
    "ModelRegisterSettings": {
      "Status": "ENABLED"|"DISABLED",
      "CrossAccountModelRegisterRoleArn": "string"
    },
    "WorkspaceSettings": {
      "S3ArtifactPath": "string",
      "S3KmsKeyId": "string"
    },
    "IdentityProviderOAuthSettings": [
      {
        "DataSourceName": "SalesforceGenie"|"Snowflake",
        "Status": "ENABLED"|"DISABLED",
        "SecretArn": "string"
      }
      ...
    ],
    "DirectDeploySettings": {
      "Status": "ENABLED"|"DISABLED"
    },
    "KendraSettings": {
      "Status": "ENABLED"|"DISABLED"
    },
    "GenerativeAiSettings": {
      "AmazonBedrockRoleArn": "string"
    },
    "EmrServerlessSettings": {
      "ExecutionRoleArn": "string",
      "Status": "ENABLED"|"DISABLED"
    }
  },
  "CodeEditorAppSettings": {
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
    "LifecycleConfigArns": ["string", ...],
    "AppLifecycleManagement": {
      "IdleSettings": {
        "LifecycleManagement": "ENABLED"|"DISABLED",
        "IdleTimeoutInMinutes": integer,
        "MinIdleTimeoutInMinutes": integer,
        "MaxIdleTimeoutInMinutes": integer
      }
    },
    "BuiltInLifecycleConfigArn": "string"
  },
  "JupyterLabAppSettings": {
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
    "LifecycleConfigArns": ["string", ...],
    "CodeRepositories": [
      {
        "RepositoryUrl": "string"
      }
      ...
    ],
    "AppLifecycleManagement": {
      "IdleSettings": {
        "LifecycleManagement": "ENABLED"|"DISABLED",
        "IdleTimeoutInMinutes": integer,
        "MinIdleTimeoutInMinutes": integer,
        "MaxIdleTimeoutInMinutes": integer
      }
    },
    "EmrSettings": {
      "AssumableRoleArns": ["string", ...],
      "ExecutionRoleArns": ["string", ...]
    },
    "BuiltInLifecycleConfigArn": "string"
  },
  "SpaceStorageSettings": {
    "DefaultEbsStorageSettings": {
      "DefaultEbsVolumeSizeInGb": integer,
      "MaximumEbsVolumeSizeInGb": integer
    }
  },
  "DefaultLandingUri": "string",
  "StudioWebPortal": "ENABLED"|"DISABLED",
  "CustomPosixUserConfig": {
    "Uid": long,
    "Gid": long
  },
  "CustomFileSystemConfigs": [
    {
      "EFSFileSystemConfig": {
        "FileSystemId": "string",
        "FileSystemPath": "string"
      },
      "FSxLustreFileSystemConfig": {
        "FileSystemId": "string",
        "FileSystemPath": "string"
      }
    }
    ...
  ],
  "StudioWebPortalSettings": {
    "HiddenMlTools": ["DataWrangler"|"FeatureStore"|"EmrClusters"|"AutoMl"|"Experiments"|"Training"|"ModelEvaluation"|"Pipelines"|"Models"|"JumpStart"|"InferenceRecommender"|"Endpoints"|"Projects"|"InferenceOptimization"|"PerformanceEvaluation"|"LakeraGuard"|"Comet"|"DeepchecksLLMEvaluation"|"Fiddler"|"HyperPodClusters", ...],
    "HiddenAppTypes": ["JupyterServer"|"KernelGateway"|"DetailedProfiler"|"TensorBoard"|"CodeEditor"|"JupyterLab"|"RStudioServerPro"|"RSessionGateway"|"Canvas", ...],
    "HiddenInstanceTypes": ["system"|"ml.t3.micro"|"ml.t3.small"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.geospatial.interactive"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.p5.48xlarge"|"ml.p5en.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge", ...],
    "HiddenSageMakerImageVersionAliases": [
      {
        "SageMakerImageName": "sagemaker_distribution",
        "VersionAliases": ["string", ...]
      }
      ...
    ]
  },
  "AutoMountHomeEFS": "Enabled"|"Disabled"|"DefaultAsDomain"
}
```

`--domain-settings` (structure)

A collection of `Domain` settings.

SecurityGroupIds -> (list)

The security groups for the Amazon Virtual Private Cloud that the `Domain` uses for communication between Domain-level apps and user apps.

(string)

RStudioServerProDomainSettings -> (structure)

A collection of settings that configure the `RStudioServerPro` Domain-level app.

DomainExecutionRoleArn -> (string)

The ARN of the execution role for the `RStudioServerPro` Domain-level app.

RStudioConnectUrl -> (string)

A URL pointing to an RStudio Connect server.

RStudioPackageManagerUrl -> (string)

A URL pointing to an RStudio Package Manager server.

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

ExecutionRoleIdentityConfig -> (string)

The configuration for attaching a SageMaker AI user profile name to the execution role as a [sts:SourceIdentity key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html) .

DockerSettings -> (structure)

A collection of settings that configure the domainâs Docker interaction.

EnableDockerAccess -> (string)

Indicates whether the domain can access Docker.

VpcOnlyTrustedAccounts -> (list)

The list of Amazon Web Services accounts that are trusted when the domain is created in VPC-only mode.

(string)

AmazonQSettings -> (structure)

A collection of settings that configure the Amazon Q experience within the domain. The `AuthMode` that you use to create the domain must be `SSO` .

Status -> (string)

Whether Amazon Q has been enabled within the domain.

QProfileArn -> (string)

The ARN of the Amazon Q profile used within the domain.

UnifiedStudioSettings -> (structure)

The settings that apply to an SageMaker AI domain when you use it in Amazon SageMaker Unified Studio.

StudioWebPortalAccess -> (string)

Sets whether you can access the domain in Amazon SageMaker Studio:

ENABLED

You can access the domain in Amazon SageMaker Studio. If you migrate the domain to Amazon SageMaker Unified Studio, you can access it in both studio interfaces.

DISABLED

You canât access the domain in Amazon SageMaker Studio. If you migrate the domain to Amazon SageMaker Unified Studio, you can access it only in that studio interface.

To migrate a domain to Amazon SageMaker Unified Studio, you specify the UnifiedStudioSettings data type when you use the UpdateDomain action.

DomainAccountId -> (string)

The ID of the Amazon Web Services account that has the Amazon SageMaker Unified Studio domain. The default value, if you donât specify an ID, is the ID of the account that has the Amazon SageMaker AI domain.

DomainRegion -> (string)

The Amazon Web Services Region where the domain is located in Amazon SageMaker Unified Studio. The default value, if you donât specify a Region, is the Region where the Amazon SageMaker AI domain is located.

DomainId -> (string)

The ID of the Amazon SageMaker Unified Studio domain associated with this domain.

ProjectId -> (string)

The ID of the Amazon SageMaker Unified Studio project that corresponds to the domain.

EnvironmentId -> (string)

The ID of the environment that Amazon SageMaker Unified Studio associates with the domain.

ProjectS3Path -> (string)

The location where Amazon S3 stores temporary execution data and other artifacts for the project that corresponds to the domain.

Shorthand Syntax:

```
SecurityGroupIds=string,string,RStudioServerProDomainSettings={DomainExecutionRoleArn=string,RStudioConnectUrl=string,RStudioPackageManagerUrl=string,DefaultResourceSpec={SageMakerImageArn=string,SageMakerImageVersionArn=string,SageMakerImageVersionAlias=string,InstanceType=string,LifecycleConfigArn=string}},ExecutionRoleIdentityConfig=string,DockerSettings={EnableDockerAccess=string,VpcOnlyTrustedAccounts=[string,string]},AmazonQSettings={Status=string,QProfileArn=string},UnifiedStudioSettings={StudioWebPortalAccess=string,DomainAccountId=string,DomainRegion=string,DomainId=string,ProjectId=string,EnvironmentId=string,ProjectS3Path=string}
```

JSON Syntax:

```
{
  "SecurityGroupIds": ["string", ...],
  "RStudioServerProDomainSettings": {
    "DomainExecutionRoleArn": "string",
    "RStudioConnectUrl": "string",
    "RStudioPackageManagerUrl": "string",
    "DefaultResourceSpec": {
      "SageMakerImageArn": "string",
      "SageMakerImageVersionArn": "string",
      "SageMakerImageVersionAlias": "string",
      "InstanceType": "system"|"ml.t3.micro"|"ml.t3.small"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.geospatial.interactive"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.p5.48xlarge"|"ml.p5en.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge",
      "LifecycleConfigArn": "string"
    }
  },
  "ExecutionRoleIdentityConfig": "USER_PROFILE_NAME"|"DISABLED",
  "DockerSettings": {
    "EnableDockerAccess": "ENABLED"|"DISABLED",
    "VpcOnlyTrustedAccounts": ["string", ...]
  },
  "AmazonQSettings": {
    "Status": "ENABLED"|"DISABLED",
    "QProfileArn": "string"
  },
  "UnifiedStudioSettings": {
    "StudioWebPortalAccess": "ENABLED"|"DISABLED",
    "DomainAccountId": "string",
    "DomainRegion": "string",
    "DomainId": "string",
    "ProjectId": "string",
    "EnvironmentId": "string",
    "ProjectS3Path": "string"
  }
}
```

`--subnet-ids` (list)

The VPC subnets that the domain uses for communication.

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-id` (string)

The ID of the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.

`--tags` (list)

Tags to associated with the Domain. Each tag consists of a key and an optional value. Tag keys must be unique per resource. Tags are searchable using the `Search` API.

Tags that you specify for the Domain are also added to all Apps that the Domain launches.

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

`--app-network-access-type` (string)

Specifies the VPC used for non-EFS traffic. The default value is `PublicInternetOnly` .

- `PublicInternetOnly` - Non-EFS traffic is through a VPC managed by Amazon SageMaker AI, which allows direct internet access
- `VpcOnly` - All traffic is through the specified VPC and subnets

Possible values:

- `PublicInternetOnly`
- `VpcOnly`

`--home-efs-file-system-kms-key-id` (string)

Use `KmsKeyId` .

`--kms-key-id` (string)

SageMaker AI uses Amazon Web Services KMS to encrypt EFS and EBS volumes attached to the domain with an Amazon Web Services managed key by default. For more control, specify a customer managed key.

`--app-security-group-management` (string)

The entity that creates and manages the required security groups for inter-app communication in `VPCOnly` mode. Required when `CreateDomain.AppNetworkAccessType` is `VPCOnly` and `DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn` is provided. If setting up the domain for use with RStudio, this value must be set to `Service` .

Possible values:

- `Service`
- `Customer`

`--tag-propagation` (string)

Indicates whether custom tag propagation is supported for the domain. Defaults to `DISABLED` .

Possible values:

- `ENABLED`
- `DISABLED`

`--default-space-settings` (structure)

The default settings for shared spaces that users create in the domain.

ExecutionRole -> (string)

The ARN of the execution role for the space.

SecurityGroups -> (list)

The security group IDs for the Amazon VPC that the space uses for communication.

(string)

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

CustomImages -> (list)

A list of custom SageMaker images that are configured to run as a JupyterLab app.

(structure)

A custom SageMaker AI image. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html) .

ImageName -> (string)

The name of the CustomImage. Must be unique to your account.

ImageVersionNumber -> (integer)

The version number of the CustomImage.

AppImageConfigName -> (string)

The name of the AppImageConfig.

LifecycleConfigArns -> (list)

The Amazon Resource Name (ARN) of the lifecycle configurations attached to the user profile or domain. To remove a lifecycle config, you must set `LifecycleConfigArns` to an empty list.

(string)

CodeRepositories -> (list)

A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.

(structure)

A Git repository that SageMaker AI automatically displays to users for cloning in the JupyterServer application.

RepositoryUrl -> (string)

The URL of the Git repository.

AppLifecycleManagement -> (structure)

Indicates whether idle shutdown is activated for JupyterLab applications.

IdleSettings -> (structure)

Settings related to idle shutdown of Studio applications.

LifecycleManagement -> (string)

Indicates whether idle shutdown is activated for the application type.

IdleTimeoutInMinutes -> (integer)

The time that SageMaker waits after the application becomes idle before shutting it down.

MinIdleTimeoutInMinutes -> (integer)

The minimum value in minutes that custom idle shutdown can be set to by the user.

MaxIdleTimeoutInMinutes -> (integer)

The maximum value in minutes that custom idle shutdown can be set to by the user.

EmrSettings -> (structure)

The configuration parameters that specify the IAM roles assumed by the execution role of SageMaker (assumable roles) and the cluster instances or job execution environments (execution roles or runtime roles) to manage and access resources required for running Amazon EMR clusters or Amazon EMR Serverless applications.

AssumableRoleArns -> (list)

An array of Amazon Resource Names (ARNs) of the IAM roles that the execution role of SageMaker can assume for performing operations or tasks related to Amazon EMR clusters or Amazon EMR Serverless applications. These roles define the permissions and access policies required when performing Amazon EMR-related operations, such as listing, connecting to, or terminating Amazon EMR clusters or Amazon EMR Serverless applications. They are typically used in cross-account access scenarios, where the Amazon EMR resources (clusters or serverless applications) are located in a different Amazon Web Services account than the SageMaker domain.

(string)

ExecutionRoleArns -> (list)

An array of Amazon Resource Names (ARNs) of the IAM roles used by the Amazon EMR cluster instances or job execution environments to access other Amazon Web Services services and resources needed during the runtime of your Amazon EMR or Amazon EMR Serverless workloads, such as Amazon S3 for data access, Amazon CloudWatch for logging, or other Amazon Web Services services based on the particular workload requirements.

(string)

BuiltInLifecycleConfigArn -> (string)

The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.

SpaceStorageSettings -> (structure)

The default storage settings for a space.

DefaultEbsStorageSettings -> (structure)

The default EBS storage settings for a space.

DefaultEbsVolumeSizeInGb -> (integer)

The default size of the EBS storage volume for a space.

MaximumEbsVolumeSizeInGb -> (integer)

The maximum size of the EBS storage volume for a space.

CustomPosixUserConfig -> (structure)

Details about the POSIX identity that is used for file system operations.

Uid -> (long)

The POSIX user ID.

Gid -> (long)

The POSIX group ID.

CustomFileSystemConfigs -> (list)

The settings for assigning a custom file system to a domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

(tagged union structure)

The settings for assigning a custom file system to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `EFSFileSystemConfig`, `FSxLustreFileSystemConfig`.

EFSFileSystemConfig -> (structure)

The settings for a custom Amazon EFS file system.

FileSystemId -> (string)

The ID of your Amazon EFS file system.

FileSystemPath -> (string)

The path to the file system directory that is accessible in Amazon SageMaker AI Studio. Permitted users can access only this directory and below.

FSxLustreFileSystemConfig -> (structure)

The settings for a custom Amazon FSx for Lustre file system.

FileSystemId -> (string)

The globally unique, 17-digit, ID of the file system, assigned by Amazon FSx for Lustre.

FileSystemPath -> (string)

The path to the file system directory that is accessible in Amazon SageMaker Studio. Permitted users can access only this directory and below.

JSON Syntax:

```
{
  "ExecutionRole": "string",
  "SecurityGroups": ["string", ...],
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
  "JupyterLabAppSettings": {
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
    "LifecycleConfigArns": ["string", ...],
    "CodeRepositories": [
      {
        "RepositoryUrl": "string"
      }
      ...
    ],
    "AppLifecycleManagement": {
      "IdleSettings": {
        "LifecycleManagement": "ENABLED"|"DISABLED",
        "IdleTimeoutInMinutes": integer,
        "MinIdleTimeoutInMinutes": integer,
        "MaxIdleTimeoutInMinutes": integer
      }
    },
    "EmrSettings": {
      "AssumableRoleArns": ["string", ...],
      "ExecutionRoleArns": ["string", ...]
    },
    "BuiltInLifecycleConfigArn": "string"
  },
  "SpaceStorageSettings": {
    "DefaultEbsStorageSettings": {
      "DefaultEbsVolumeSizeInGb": integer,
      "MaximumEbsVolumeSizeInGb": integer
    }
  },
  "CustomPosixUserConfig": {
    "Uid": long,
    "Gid": long
  },
  "CustomFileSystemConfigs": [
    {
      "EFSFileSystemConfig": {
        "FileSystemId": "string",
        "FileSystemPath": "string"
      },
      "FSxLustreFileSystemConfig": {
        "FileSystemId": "string",
        "FileSystemPath": "string"
      }
    }
    ...
  ]
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

DomainArn -> (string)

The Amazon Resource Name (ARN) of the created domain.

DomainId -> (string)

The ID of the created domain.

Url -> (string)

The URL to the created domain.