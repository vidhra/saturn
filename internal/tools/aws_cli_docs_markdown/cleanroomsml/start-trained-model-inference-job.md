# start-trained-model-inference-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/start-trained-model-inference-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/start-trained-model-inference-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanroomsml](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/index.html#cli-aws-cleanroomsml) ]

# start-trained-model-inference-job

## Description

Defines the information necessary to begin a trained model inference job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)

## Synopsis

```
start-trained-model-inference-job
--membership-identifier <value>
--name <value>
--trained-model-arn <value>
[--configured-model-algorithm-association-arn <value>]
--resource-config <value>
--output-configuration <value>
--data-source <value>
[--description <value>]
[--container-execution-parameters <value>]
[--environment <value>]
[--kms-key-arn <value>]
[--tags <value>]
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

`--membership-identifier` (string)

The membership ID of the membership that contains the trained model inference job.

`--name` (string)

The name of the trained model inference job.

`--trained-model-arn` (string)

The Amazon Resource Name (ARN) of the trained model that is used for this trained model inference job.

`--configured-model-algorithm-association-arn` (string)

The Amazon Resource Name (ARN) of the configured model algorithm association that is used for this trained model inference job.

`--resource-config` (structure)

Defines the resource configuration for the trained model inference job.

instanceType -> (string)

The type of instance that is used to perform model inference.

instanceCount -> (integer)

The number of instances to use.

Shorthand Syntax:

```
instanceType=string,instanceCount=integer
```

JSON Syntax:

```
{
  "instanceType": "ml.r7i.48xlarge"|"ml.r6i.16xlarge"|"ml.m6i.xlarge"|"ml.m5.4xlarge"|"ml.p2.xlarge"|"ml.m4.16xlarge"|"ml.r7i.16xlarge"|"ml.m7i.xlarge"|"ml.m6i.12xlarge"|"ml.r7i.8xlarge"|"ml.r7i.large"|"ml.m7i.12xlarge"|"ml.m6i.24xlarge"|"ml.m7i.24xlarge"|"ml.r6i.8xlarge"|"ml.r6i.large"|"ml.g5.2xlarge"|"ml.m5.large"|"ml.p3.16xlarge"|"ml.m7i.48xlarge"|"ml.m6i.16xlarge"|"ml.p2.16xlarge"|"ml.g5.4xlarge"|"ml.m7i.16xlarge"|"ml.c4.2xlarge"|"ml.c5.2xlarge"|"ml.c6i.32xlarge"|"ml.c4.4xlarge"|"ml.g5.8xlarge"|"ml.c6i.xlarge"|"ml.c5.4xlarge"|"ml.g4dn.xlarge"|"ml.c7i.xlarge"|"ml.c6i.12xlarge"|"ml.g4dn.12xlarge"|"ml.c7i.12xlarge"|"ml.c6i.24xlarge"|"ml.g4dn.2xlarge"|"ml.c7i.24xlarge"|"ml.c7i.2xlarge"|"ml.c4.8xlarge"|"ml.c6i.2xlarge"|"ml.g4dn.4xlarge"|"ml.c7i.48xlarge"|"ml.c7i.4xlarge"|"ml.c6i.16xlarge"|"ml.c5.9xlarge"|"ml.g4dn.16xlarge"|"ml.c7i.16xlarge"|"ml.c6i.4xlarge"|"ml.c5.xlarge"|"ml.c4.xlarge"|"ml.g4dn.8xlarge"|"ml.c7i.8xlarge"|"ml.c7i.large"|"ml.g5.xlarge"|"ml.c6i.8xlarge"|"ml.c6i.large"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.m7i.2xlarge"|"ml.c5.18xlarge"|"ml.g5.48xlarge"|"ml.m6i.2xlarge"|"ml.g5.16xlarge"|"ml.m7i.4xlarge"|"ml.p3.2xlarge"|"ml.r6i.32xlarge"|"ml.m6i.4xlarge"|"ml.m5.xlarge"|"ml.m4.10xlarge"|"ml.r6i.xlarge"|"ml.m5.12xlarge"|"ml.m4.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.xlarge"|"ml.r6i.12xlarge"|"ml.m5.24xlarge"|"ml.r7i.12xlarge"|"ml.m7i.8xlarge"|"ml.m7i.large"|"ml.r6i.24xlarge"|"ml.r6i.2xlarge"|"ml.m4.2xlarge"|"ml.r7i.24xlarge"|"ml.r7i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.large"|"ml.m5.2xlarge"|"ml.p2.8xlarge"|"ml.r6i.4xlarge"|"ml.m6i.32xlarge"|"ml.p3.8xlarge"|"ml.m4.4xlarge",
  "instanceCount": integer
}
```

`--output-configuration` (structure)

Defines the output configuration information for the trained model inference job.

accept -> (string)

The MIME type used to specify the output data.

members -> (list)

Defines the members that can receive inference output.

(structure)

Defines who will receive inference results.

accountId -> (string)

The account ID of the member that can receive inference results.

Shorthand Syntax:

```
accept=string,members=[{accountId=string},{accountId=string}]
```

JSON Syntax:

```
{
  "accept": "string",
  "members": [
    {
      "accountId": "string"
    }
    ...
  ]
}
```

`--data-source` (structure)

Defines the data source that is used for the trained model inference job.

mlInputChannelArn -> (string)

The Amazon Resource Name (ARN) of the ML input channel for this model inference data source.

Shorthand Syntax:

```
mlInputChannelArn=string
```

JSON Syntax:

```
{
  "mlInputChannelArn": "string"
}
```

`--description` (string)

The description of the trained model inference job.

`--container-execution-parameters` (structure)

The execution parameters for the container.

maxPayloadInMB -> (integer)

The maximum size of the inference container payload, specified in MB.

Shorthand Syntax:

```
maxPayloadInMB=integer
```

JSON Syntax:

```
{
  "maxPayloadInMB": integer
}
```

`--environment` (map)

The environment variables to set in the Docker container.

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

`--kms-key-arn` (string)

The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the ML inference job and associated data.

`--tags` (map)

The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50.
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8.
- Maximum value length - 256 Unicode characters in UTF-8.
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case sensitive.
- Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.

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

trainedModelInferenceJobArn -> (string)

The Amazon Resource Name (ARN) of the trained model inference job.