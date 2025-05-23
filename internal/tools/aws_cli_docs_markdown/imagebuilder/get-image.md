# get-imageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# get-image

## Description

Gets an image.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/GetImage)

## Synopsis

```
get-image
--image-build-version-arn <value>
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

`--image-build-version-arn` (string)

The Amazon Resource Name (ARN) of the image that you want to get.

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

**To get image details**

The following `get-image` example lists the details of an image by specifying its ARN.

```
aws imagebuilder get-image \
    --image-build-version-arn arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1
```

Output:

```
{
    "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "image": {
        "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1",
        "name": "MyBasicRecipe",
        "version": "2019.12.03/1",
        "platform": "Windows",
        "state": {
            "status": "BUILDING"
        },
        "imageRecipe": {
            "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03",
            "name": "MyBasicRecipe",
            "description": "This example image recipe creates a Windows 2016 image.",
            "platform": "Windows",
            "version": "2019.12.03",
            "components": [
                {
                    "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myexamplecomponent/2019.12.02/1"
                },
                {
                    "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myimportedcomponent/1.0.0/1"
                }
            ],
            "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/windows-server-2016-english-full-base-x86/2019.12.17/1",
            "dateCreated": "2020-02-14T19:46:16.904Z",
            "tags": {}
        },
        "infrastructureConfiguration": {
            "arn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure",
            "name": "MyExampleInfrastructure",
            "description": "An example that will retain instances of failed builds",
            "instanceTypes": [
                "m5.large",
                "m5.xlarge"
            ],
            "instanceProfileName": "EC2InstanceProfileForImageFactory",
            "securityGroupIds": [
                "sg-a1b2c3d4"
            ],
            "subnetId": "subnet-a1b2c3d4",
            "logging": {
                "s3Logs": {
                    "s3BucketName": "bucket-name",
                    "s3KeyPrefix": "bucket-path"
                }
            },
            "keyPair": "Sam",
            "terminateInstanceOnFailure": false,
            "snsTopicArn": "arn:aws:sns:us-west-2:123456789012:sns-name",
            "dateCreated": "2020-02-14T21:21:05.098Z",
            "tags": {}
        },
        "imageTestsConfiguration": {
            "imageTestsEnabled": true,
            "timeoutMinutes": 720
        },
        "dateCreated": "2020-02-14T23:14:13.597Z",
        "outputResources": {
            "amis": []
        },
        "tags": {}
    }
}
```

For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html) in the *EC2 Image Builder Users Guide*.

## Output

requestId -> (string)

The request ID that uniquely identifies this request.

image -> (structure)

The image object.

arn -> (string)

The Amazon Resource Name (ARN) of the image.

### Note

Semantic versioning is included in each objectâs Amazon Resource Name (ARN), at the level that applies to that object as follows:

- Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.
- Version ARNs have only the first three nodes: <major>.<minor>.<patch>
- Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.

type -> (string)

Specifies whether this image produces an AMI or a container image.

name -> (string)

The name of the image.

version -> (string)

The semantic version of the image.

### Note

The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.

**Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

**Filtering:** With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.

platform -> (string)

The image operating system platform, such as Linux or Windows.

enhancedImageMetadataEnabled -> (boolean)

Indicates whether Image Builder collects additional information about the image, such as the operating system (OS) version and package list.

osVersion -> (string)

The operating system version for instances that launch from this image. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.

state -> (structure)

The state of the image.

status -> (string)

The status of the image.

reason -> (string)

The reason for the status of the image.

imageRecipe -> (structure)

For images that distribute an AMI, this is the image recipe that Image Builder used to create the image. For container images, this is empty.

arn -> (string)

The Amazon Resource Name (ARN) of the image recipe.

type -> (string)

Specifies which type of image is created by the recipe - an AMI or a container image.

name -> (string)

The name of the image recipe.

description -> (string)

The description of the image recipe.

platform -> (string)

The platform of the image recipe.

owner -> (string)

The owner of the image recipe.

version -> (string)

The version of the image recipe.

components -> (list)

The components that are included in the image recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.

(structure)

Configuration details of the component.

componentArn -> (string)

The Amazon Resource Name (ARN) of the component.

parameters -> (list)

A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

(structure)

Contains a key/value pair that sets the named component parameter.

name -> (string)

The name of the component parameter to set.

value -> (list)

Sets the value for the named component parameter.

(string)

parentImage -> (string)

The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:

- AMI ID
- Image Builder image Amazon Resource Name (ARN)
- Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:` , followed by the parameter name or ARN.
- Amazon Web Services Marketplace product ID

blockDeviceMappings -> (list)

The block device mappings to apply when creating images from this recipe.

(structure)

Defines block device mappings for the instance used to configure your image.

deviceName -> (string)

The device to which these mappings apply.

ebs -> (structure)

Use to manage Amazon EBS-specific configuration for this mapping.

encrypted -> (boolean)

Use to configure device encryption.

deleteOnTermination -> (boolean)

Use to configure delete on termination of the associated device.

iops -> (integer)

Use to configure device IOPS.

kmsKeyId -> (string)

Use to configure the KMS key to use when encrypting the device.

snapshotId -> (string)

The snapshot that defines the device contents.

volumeSize -> (integer)

Use to override the deviceâs volume size.

volumeType -> (string)

Use to override the deviceâs volume type.

throughput -> (integer)

**For GP3 volumes only** â The throughput in MiB/s that the volume supports.

virtualName -> (string)

Use to manage instance ephemeral devices.

noDevice -> (string)

Use to remove a mapping from the base image.

dateCreated -> (string)

The date on which this image recipe was created.

tags -> (map)

The tags of the image recipe.

key -> (string)

value -> (string)

workingDirectory -> (string)

The working directory to be used during build and test workflows.

additionalInstanceConfiguration -> (structure)

Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration. Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.

systemsManagerAgent -> (structure)

Contains settings for the Systems Manager agent on your build instance.

uninstallAfterBuild -> (boolean)

Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI. If this is set to true, then the agent is removed from the final image. If itâs set to false, then the agent is left in, so that it is included in the new AMI. The default value is false.

userDataOverride -> (string)

Use this property to provide commands or a command script to run when you launch your build instance.

The userDataOverride property replaces any commands that Image Builder might have added to ensure that Systems Manager is installed on your Linux build instance. If you override the user data, make sure that you add commands to install Systems Manager, if it is not pre-installed on your base image.

### Note

The user data is always base 64 encoded. For example, the following commands are encoded as `IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhci$` :

*#!/bin/bash*

mkdir -p /var/bb/

touch /var

containerRecipe -> (structure)

For container images, this is the container recipe that Image Builder used to create the image. For images that distribute an AMI, this is empty.

arn -> (string)

The Amazon Resource Name (ARN) of the container recipe.

### Note

Semantic versioning is included in each objectâs Amazon Resource Name (ARN), at the level that applies to that object as follows:

- Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.
- Version ARNs have only the first three nodes: <major>.<minor>.<patch>
- Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.

containerType -> (string)

Specifies the type of container, such as Docker.

name -> (string)

The name of the container recipe.

description -> (string)

The description of the container recipe.

platform -> (string)

The system platform for the container, such as Windows or Linux.

owner -> (string)

The owner of the container recipe.

version -> (string)

The semantic version of the container recipe.

### Note

The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.

**Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

**Filtering:** With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.

components -> (list)

Build and test components that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.

(structure)

Configuration details of the component.

componentArn -> (string)

The Amazon Resource Name (ARN) of the component.

parameters -> (list)

A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

(structure)

Contains a key/value pair that sets the named component parameter.

name -> (string)

The name of the component parameter to set.

value -> (list)

Sets the value for the named component parameter.

(string)

instanceConfiguration -> (structure)

A group of options that can be used to configure an instance for building and testing container images.

image -> (string)

The base image for a container build and test instance. This can contain an AMI ID or it can specify an Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:` , followed by the parameter name or ARN.

If not specified, Image Builder uses the appropriate ECS-optimized AMI as a base image.

blockDeviceMappings -> (list)

Defines the block devices to attach for building an instance from this Image Builder AMI.

(structure)

Defines block device mappings for the instance used to configure your image.

deviceName -> (string)

The device to which these mappings apply.

ebs -> (structure)

Use to manage Amazon EBS-specific configuration for this mapping.

encrypted -> (boolean)

Use to configure device encryption.

deleteOnTermination -> (boolean)

Use to configure delete on termination of the associated device.

iops -> (integer)

Use to configure device IOPS.

kmsKeyId -> (string)

Use to configure the KMS key to use when encrypting the device.

snapshotId -> (string)

The snapshot that defines the device contents.

volumeSize -> (integer)

Use to override the deviceâs volume size.

volumeType -> (string)

Use to override the deviceâs volume type.

throughput -> (integer)

**For GP3 volumes only** â The throughput in MiB/s that the volume supports.

virtualName -> (string)

Use to manage instance ephemeral devices.

noDevice -> (string)

Use to remove a mapping from the base image.

dockerfileTemplateData -> (string)

Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.

kmsKeyId -> (string)

Identifies which KMS key is used to encrypt the container image for distribution to the target Region.

encrypted -> (boolean)

A flag that indicates if the target container is encrypted.

parentImage -> (string)

The base image for customizations specified in the container recipe. This can contain an Image Builder image resource ARN or a container image URI, for example `amazonlinux:latest` .

dateCreated -> (string)

The date when this container recipe was created.

tags -> (map)

Tags that are attached to the container recipe.

key -> (string)

value -> (string)

workingDirectory -> (string)

The working directory for use during build and test workflows.

targetRepository -> (structure)

The destination repository for the container image.

service -> (string)

Specifies the service in which this image was registered.

repositoryName -> (string)

The name of the container repository where the output container image is stored. This name is prefixed by the repository location. For example, `<repository location url>/repository_name` .

sourcePipelineName -> (string)

The name of the image pipeline that created this image.

sourcePipelineArn -> (string)

The Amazon Resource Name (ARN) of the image pipeline that created this image.

infrastructureConfiguration -> (structure)

The infrastructure that Image Builder used to create this image.

arn -> (string)

The Amazon Resource Name (ARN) of the infrastructure configuration.

name -> (string)

The name of the infrastructure configuration.

description -> (string)

The description of the infrastructure configuration.

instanceTypes -> (list)

The instance types of the infrastructure configuration.

(string)

instanceProfileName -> (string)

The instance profile of the infrastructure configuration.

securityGroupIds -> (list)

The security group IDs of the infrastructure configuration.

(string)

subnetId -> (string)

The subnet ID of the infrastructure configuration.

logging -> (structure)

The logging configuration of the infrastructure configuration.

s3Logs -> (structure)

The Amazon S3 logging configuration.

s3BucketName -> (string)

The S3 bucket in which to store the logs.

s3KeyPrefix -> (string)

The Amazon S3 path to the bucket where the logs are stored.

keyPair -> (string)

The Amazon EC2 key pair of the infrastructure configuration.

terminateInstanceOnFailure -> (boolean)

The terminate instance on failure configuration of the infrastructure configuration.

snsTopicArn -> (string)

The Amazon Resource Name (ARN) for the SNS topic to which we send image build event notifications.

### Note

EC2 Image Builder is unable to send notifications to SNS topics that are encrypted using keys from other accounts. The key that is used to encrypt the SNS topic must reside in the account that the Image Builder service runs under.

dateCreated -> (string)

The date on which the infrastructure configuration was created.

dateUpdated -> (string)

The date on which the infrastructure configuration was last updated.

resourceTags -> (map)

The tags attached to the resource created by Image Builder.

key -> (string)

value -> (string)

instanceMetadataOptions -> (structure)

The instance metadata option settings for the infrastructure configuration.

httpTokens -> (string)

Indicates whether a signed token header is required for instance metadata retrieval requests. The values affect the response as follows:

- **required** â When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases.
- **optional** â You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned.

The default setting is **optional** .

httpPutResponseHopLimit -> (integer)

Limit the number of hops that an instance metadata request can traverse to reach its destination. The default is one hop. However, if HTTP tokens are required, container image builds need a minimum of two hops.

tags -> (map)

The tags of the infrastructure configuration.

key -> (string)

value -> (string)

placement -> (structure)

The instance placement settings that define where the instances that are launched from your image will run.

availabilityZone -> (string)

The Availability Zone where your build and test instances will launch.

tenancy -> (string)

The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware. An instance with a tenancy of `host` runs on a Dedicated Host.

If tenancy is set to `host` , then you can optionally specify one target for placement â either host ID or host resource group ARN. If automatic placement is enabled for your host, and you donât specify any placement target, Amazon EC2 will try to find an available host for your build and test instances.

hostId -> (string)

The ID of the Dedicated Host on which build and test instances run. This only applies if `tenancy` is `host` . If you specify the host ID, you must not specify the resource group ARN. If you specify both, Image Builder returns an error.

hostResourceGroupArn -> (string)

The Amazon Resource Name (ARN) of the host resource group in which to launch build and test instances. This only applies if `tenancy` is `host` . If you specify the resource group ARN, you must not specify the host ID. If you specify both, Image Builder returns an error.

distributionConfiguration -> (structure)

The distribution configuration that Image Builder used to create this image.

arn -> (string)

The Amazon Resource Name (ARN) of the distribution configuration.

name -> (string)

The name of the distribution configuration.

description -> (string)

The description of the distribution configuration.

distributions -> (list)

The distribution objects that apply Region-specific settings for the deployment of the image to targeted Regions.

(structure)

Defines the settings for a specific Region.

region -> (string)

The target Region.

amiDistributionConfiguration -> (structure)

The specific AMI settings; for example, launch permissions or AMI tags.

name -> (string)

The name of the output AMI.

description -> (string)

The description of the AMI distribution configuration. Minimum and maximum length are in characters.

targetAccountIds -> (list)

The ID of an account to which you want to distribute an image.

(string)

amiTags -> (map)

The tags to apply to AMIs distributed to this Region.

key -> (string)

value -> (string)

kmsKeyId -> (string)

The KMS key identifier used to encrypt the distributed image.

launchPermission -> (structure)

Launch permissions can be used to configure which Amazon Web Services accounts can use the AMI to launch instances.

userIds -> (list)

The Amazon Web Services account ID.

(string)

userGroups -> (list)

The name of the group.

(string)

organizationArns -> (list)

The ARN for an Amazon Web Services Organization that you want to share your AMI with. For more information, see [What is Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) .

(string)

organizationalUnitArns -> (list)

The ARN for an Organizations organizational unit (OU) that you want to share your AMI with. For more information about key concepts for Organizations, see [Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) .

(string)

containerDistributionConfiguration -> (structure)

Container distribution settings for encryption, licensing, and sharing in a specific Region.

description -> (string)

The description of the container distribution configuration.

containerTags -> (list)

Tags that are attached to the container distribution configuration.

(string)

targetRepository -> (structure)

The destination repository for the container distribution configuration.

service -> (string)

Specifies the service in which this image was registered.

repositoryName -> (string)

The name of the container repository where the output container image is stored. This name is prefixed by the repository location. For example, `<repository location url>/repository_name` .

licenseConfigurationArns -> (list)

The License Manager Configuration to associate with the AMI in the specified Region.

(string)

launchTemplateConfigurations -> (list)

A group of launchTemplateConfiguration settings that apply to image distribution for specified accounts.

(structure)

Identifies an Amazon EC2 launch template to use for a specific account.

launchTemplateId -> (string)

Identifies the Amazon EC2 launch template to use.

accountId -> (string)

The account ID that this configuration applies to.

setDefaultVersion -> (boolean)

Set the specified Amazon EC2 launch template as the default launch template for the specified account.

s3ExportConfiguration -> (structure)

Configure export settings to deliver disk images created from your image build, using a file format that is compatible with your VMs in that Region.

roleName -> (string)

The name of the role that grants VM Import/Export permission to export images to your S3 bucket.

diskImageFormat -> (string)

Export the updated image to one of the following supported disk image formats:

- **Virtual Hard Disk (VHD)** â Compatible with Citrix Xen and Microsoft Hyper-V virtualization products.
- **Stream-optimized ESX Virtual Machine Disk (VMDK)** â Compatible with VMware ESX and VMware vSphere versions 4, 5, and 6.
- **Raw** â Raw format.

s3Bucket -> (string)

The S3 bucket in which to store the output disk images for your VM.

s3Prefix -> (string)

The Amazon S3 path for the bucket where the output disk images for your VM are stored.

fastLaunchConfigurations -> (list)

The Windows faster-launching configurations to use for AMI distribution.

(structure)

Define and configure faster launching for output Windows AMIs.

enabled -> (boolean)

A Boolean that represents the current state of faster launching for the Windows AMI. Set to `true` to start using Windows faster launching, or `false` to stop using it.

snapshotConfiguration -> (structure)

Configuration settings for managing the number of snapshots that are created from pre-provisioned instances for the Windows AMI when faster launching is enabled.

targetResourceCount -> (integer)

The number of pre-provisioned snapshots to keep on hand for a fast-launch enabled Windows AMI.

maxParallelLaunches -> (integer)

The maximum number of parallel instances that are launched for creating resources.

launchTemplate -> (structure)

The launch template that the fast-launch enabled Windows AMI uses when it launches Windows instances to create pre-provisioned snapshots.

launchTemplateId -> (string)

The ID of the launch template to use for faster launching for a Windows AMI.

launchTemplateName -> (string)

The name of the launch template to use for faster launching for a Windows AMI.

launchTemplateVersion -> (string)

The version of the launch template to use for faster launching for a Windows AMI.

accountId -> (string)

The owner account ID for the fast-launch enabled Windows AMI.

ssmParameterConfigurations -> (list)

Contains settings to update Amazon Web Services Systems Manager (SSM) Parameter Store Parameters with output AMI IDs from the build by target Region.

(structure)

Configuration for a single Parameter in the Amazon Web Services Systems Manager (SSM) Parameter Store in a given Region.

amiAccountId -> (string)

Specify the account that will own the Parameter in a given Region. During distribution, this account must be specified in distribution settings as a target account for the Region.

parameterName -> (string)

This is the name of the Parameter in the target Region or account. The image distribution creates the Parameter if it doesnât already exist. Otherwise, it updates the parameter.

dataType -> (string)

The data type specifies what type of value the Parameter contains. We recommend that you use data type `aws:ec2:image` .

timeoutMinutes -> (integer)

The maximum duration in minutes for this distribution configuration.

dateCreated -> (string)

The date on which this distribution configuration was created.

dateUpdated -> (string)

The date on which this distribution configuration was last updated.

tags -> (map)

The tags of the distribution configuration.

key -> (string)

value -> (string)

imageTestsConfiguration -> (structure)

The image tests that ran when that Image Builder created this image.

imageTestsEnabled -> (boolean)

Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.

timeoutMinutes -> (integer)

The maximum time in minutes that tests are permitted to run.

### Note

The timeout property is not currently active. This value is ignored.

dateCreated -> (string)

The date on which Image Builder created this image.

outputResources -> (structure)

The output resources that Image Builder produces for this image.

amis -> (list)

The Amazon EC2 AMIs created by this image.

(structure)

Details of an Amazon EC2 AMI.

region -> (string)

The Amazon Web Services Region of the Amazon EC2 AMI.

image -> (string)

The AMI ID of the Amazon EC2 AMI.

name -> (string)

The name of the Amazon EC2 AMI.

description -> (string)

The description of the Amazon EC2 AMI. Minimum and maximum length are in characters.

state -> (structure)

Image status and the reason for that status.

status -> (string)

The status of the image.

reason -> (string)

The reason for the status of the image.

accountId -> (string)

The account ID of the owner of the AMI.

containers -> (list)

Container images that the pipeline has generated and stored in the output repository.

(structure)

A container encapsulates the runtime environment for an application.

region -> (string)

Containers and container images are Region-specific. This is the Region context for the container.

imageUris -> (list)

A list of URIs for containers created in the context Region.

(string)

tags -> (map)

The tags that apply to this image.

key -> (string)

value -> (string)

buildType -> (string)

Indicates the type of build that created this image. The build can be initiated in the following ways:

- **USER_INITIATED** â A manual pipeline build request.
- **SCHEDULED** â A pipeline build initiated by a cron expression in the Image Builder pipeline, or from EventBridge.
- **IMPORT** â A VM import created the image to use as the base image for the recipe.
- **IMPORT_ISO** â An ISO disk import created the image.

imageSource -> (string)

The origin of the base image that Image Builder used to build this image.

scanState -> (structure)

Contains information about the current state of scans for this image.

status -> (string)

The current state of vulnerability scans for the image.

reason -> (string)

The reason for the scan status for the image.

imageScanningConfiguration -> (structure)

Contains settings for vulnerability scans.

imageScanningEnabled -> (boolean)

A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.

ecrConfiguration -> (structure)

Contains Amazon ECR settings for vulnerability scans.

repositoryName -> (string)

The name of the container repository that Amazon Inspector scans to identify findings for your container images. The name includes the path for the repository location. If you donât provide this information, Image Builder creates a repository in your account named `image-builder-image-scanning-repository` for vulnerability scans of your output container images.

containerTags -> (list)

Tags for Image Builder to apply to the output container image that Amazon Inspector scans. Tags can help you identify and manage your scanned images.

(string)

deprecationTime -> (timestamp)

The time when deprecation occurs for an image resource. This can be a past or future date.

lifecycleExecutionId -> (string)

Identifies the last runtime instance of the lifecycle policy to take action on the image.

executionRole -> (string)

The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.

workflows -> (list)

Contains the build and test workflows that are associated with the image.

(structure)

Contains control settings and configurable inputs for a workflow resource.

workflowArn -> (string)

The Amazon Resource Name (ARN) of the workflow resource.

parameters -> (list)

Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.

(structure)

Contains a key/value pair that sets the named workflow parameter.

name -> (string)

The name of the workflow parameter to set.

value -> (list)

Sets the value for the named workflow parameter.

(string)

parallelGroup -> (string)

Test workflows are defined within named runtime groups called parallel groups. The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.

onFailure -> (string)

The action to take if the workflow fails.