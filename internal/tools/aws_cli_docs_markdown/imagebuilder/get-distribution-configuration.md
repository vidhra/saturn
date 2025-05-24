# get-distribution-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-distribution-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-distribution-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# get-distribution-configuration

## Description

Gets a distribution configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/GetDistributionConfiguration)

## Synopsis

```
get-distribution-configuration
--distribution-configuration-arn <value>
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

`--distribution-configuration-arn` (string)

The Amazon Resource Name (ARN) of the distribution configuration that you want to retrieve.

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

**To get the details of a distribution configuration**

The following `get-distribution-configuration` example displays the details of a distribution configuration by specifying its ARN.

```
aws imagebuilder get-distribution-configuration \
    --distribution-configuration-arn arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution
```

Output:

```
{
    "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "distributionConfiguration": {
        "arn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution",
        "name": "MyExampleDistribution",
        "description": "Copies AMI to eu-west-1 and exports to S3",
        "distributions": [
            {
                "region": "us-west-2",
                "amiDistributionConfiguration": {
                    "name": "Name {{imagebuilder:buildDate}}",
                    "description": "An example image name with parameter references",
                    "amiTags": {
                        "KeyName": "{{ssm:parameter_name}}"
                    },
                    "launchPermission": {
                        "userIds": [
                            "123456789012"
                        ]
                    }
                }
            },
            {
                "region": "eu-west-1",
                "amiDistributionConfiguration": {
                    "name": "My {{imagebuilder:buildVersion}} image {{imagebuilder:buildDate}}",
                    "amiTags": {
                        "KeyName": "Value"
                    },
                    "launchPermission": {
                        "userIds": [
                            "123456789012"
                        ]
                    }
                }
            }
        ],
        "dateCreated": "2020-02-19T18:40:10.529Z",
        "tags": {}
    }
}
```

For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html) in the *EC2 Image Builder Users Guide*.

## Output

requestId -> (string)

The request ID that uniquely identifies this request.

distributionConfiguration -> (structure)

The distribution configuration object.

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