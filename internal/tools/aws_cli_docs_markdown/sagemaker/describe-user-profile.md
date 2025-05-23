# describe-user-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-user-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-user-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-user-profile

## Description

Describes a user profile. For more information, see `CreateUserProfile` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeUserProfile)

## Synopsis

```
describe-user-profile
--domain-id <value>
--user-profile-name <value>
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

The domain ID.

`--user-profile-name` (string)

The user profile name. This value is not case sensitive.

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

DomainId -> (string)

The ID of the domain that contains the profile.

UserProfileArn -> (string)

The user profile Amazon Resource Name (ARN).

UserProfileName -> (string)

The user profile name.

HomeEfsFileSystemUid -> (string)

The ID of the userâs profile in the Amazon Elastic File System volume.

Status -> (string)

The status.

LastModifiedTime -> (timestamp)

The last modified time.

CreationTime -> (timestamp)

The creation time.

FailureReason -> (string)

The failure reason.

SingleSignOnUserIdentifier -> (string)

The IAM Identity Center user identifier.

SingleSignOnUserValue -> (string)

The IAM Identity Center user value.

UserSettings -> (structure)

A collection of settings.

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