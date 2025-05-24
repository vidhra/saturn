# update-infrastructure-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# update-infrastructure-configuration

## Description

Updates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)

## Synopsis

```
update-infrastructure-configuration
--infrastructure-configuration-arn <value>
[--description <value>]
[--instance-types <value>]
--instance-profile-name <value>
[--security-group-ids <value>]
[--subnet-id <value>]
[--logging <value>]
[--key-pair <value>]
[--terminate-instance-on-failure | --no-terminate-instance-on-failure]
[--sns-topic-arn <value>]
[--resource-tags <value>]
[--instance-metadata-options <value>]
[--placement <value>]
[--client-token <value>]
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

`--infrastructure-configuration-arn` (string)

The Amazon Resource Name (ARN) of the infrastructure configuration that you want to update.

`--description` (string)

The description of the infrastructure configuration.

`--instance-types` (list)

The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. The service will pick one of these instance types based on availability.

(string)

Syntax:

```
"string" "string" ...
```

`--instance-profile-name` (string)

The instance profile to associate with the instance used to customize your Amazon EC2 AMI.

`--security-group-ids` (list)

The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.

(string)

Syntax:

```
"string" "string" ...
```

`--subnet-id` (string)

The subnet ID to place the instance used to customize your Amazon EC2 AMI in.

`--logging` (structure)

The logging configuration of the infrastructure configuration.

s3Logs -> (structure)

The Amazon S3 logging configuration.

s3BucketName -> (string)

The S3 bucket in which to store the logs.

s3KeyPrefix -> (string)

The Amazon S3 path to the bucket where the logs are stored.

Shorthand Syntax:

```
s3Logs={s3BucketName=string,s3KeyPrefix=string}
```

JSON Syntax:

```
{
  "s3Logs": {
    "s3BucketName": "string",
    "s3KeyPrefix": "string"
  }
}
```

`--key-pair` (string)

The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.

`--terminate-instance-on-failure` | `--no-terminate-instance-on-failure` (boolean)

The terminate instance on failure setting of the infrastructure configuration. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails.

`--sns-topic-arn` (string)

The Amazon Resource Name (ARN) for the SNS topic to which we send image build event notifications.

### Note

EC2 Image Builder is unable to send notifications to SNS topics that are encrypted using keys from other accounts. The key that is used to encrypt the SNS topic must reside in the account that the Image Builder service runs under.

`--resource-tags` (map)

The tags attached to the resource created by Image Builder.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--instance-metadata-options` (structure)

The instance metadata options that you can set for the HTTP requests that pipeline builds use to launch EC2 build and test instances. For more information about instance metadata options, see one of the following links:

- [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 User Guide* * for Linux instances.
- [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 Windows Guide* * for Windows instances.

httpTokens -> (string)

Indicates whether a signed token header is required for instance metadata retrieval requests. The values affect the response as follows:

- **required** â When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases.
- **optional** â You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned.

The default setting is **optional** .

httpPutResponseHopLimit -> (integer)

Limit the number of hops that an instance metadata request can traverse to reach its destination. The default is one hop. However, if HTTP tokens are required, container image builds need a minimum of two hops.

Shorthand Syntax:

```
httpTokens=string,httpPutResponseHopLimit=integer
```

JSON Syntax:

```
{
  "httpTokens": "string",
  "httpPutResponseHopLimit": integer
}
```

`--placement` (structure)

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

Shorthand Syntax:

```
availabilityZone=string,tenancy=string,hostId=string,hostResourceGroupArn=string
```

JSON Syntax:

```
{
  "availabilityZone": "string",
  "tenancy": "default"|"dedicated"|"host",
  "hostId": "string",
  "hostResourceGroupArn": "string"
}
```

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference* .

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

**To update an infrastructure configuration**

The following `update-infrastructure-configuration` example updates an infrastructure configuration using a JSON file.

```
aws imagebuilder update-infrastructure-configuration \
    --cli-input-json file:/update-infrastructure-configuration.json
```

Contents of `update-infrastructure-configuration.json`:

```
{
    "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure",
    "description": "An example that will terminate instances of failed builds",
    "instanceTypes": [
        "m5.large", "m5.2xlarge"
    ],
    "instanceProfileName": "EC2InstanceProfileForImageFactory",
    "securityGroupIds": [
        "sg-a48c95ef"
    ],
    "subnetId": "subnet-a48c95ef",
    "logging": {
        "s3Logs": {
            "s3BucketName": "bucket-name",
            "s3KeyPrefix": "bucket-path"
        }
    },
    "terminateInstanceOnFailure": true,
    "snsTopicArn": "arn:aws:sns:us-west-2:123456789012:sns-name"
}
```

Output:

```
{
    "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html) in the *EC2 Image Builder Users Guide*.

## Output

requestId -> (string)

The request ID that uniquely identifies this request.

clientToken -> (string)

The client token that uniquely identifies the request.

infrastructureConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the infrastructure configuration that was updated by this request.