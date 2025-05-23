# create-marketplace-model-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/create-marketplace-model-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/create-marketplace-model-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/index.html#cli-aws-bedrock) ]

# create-marketplace-model-endpoint

## Description

Creates an endpoint for a model from Amazon Bedrock Marketplace. The endpoint is hosted by Amazon SageMaker.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-2023-04-20/CreateMarketplaceModelEndpoint)

## Synopsis

```
create-marketplace-model-endpoint
--model-source-identifier <value>
--endpoint-config <value>
[--accept-eula | --no-accept-eula]
--endpoint-name <value>
[--client-request-token <value>]
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

`--model-source-identifier` (string)

The ARN of the model from Amazon Bedrock Marketplace that you want to deploy to the endpoint.

`--endpoint-config` (tagged union structure)

The configuration for the endpoint, including the number and type of instances to use.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `sageMaker`.

sageMaker -> (structure)

The configuration specific to Amazon SageMaker for the endpoint.

initialInstanceCount -> (integer)

The number of Amazon EC2 compute instances to deploy for initial endpoint creation.

instanceType -> (string)

The Amazon EC2 compute instance type to deploy for hosting the model.

executionRole -> (string)

The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on Amazon EC2 compute instances or for batch transform jobs.

kmsEncryptionKey -> (string)

The Amazon Web Services KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the Amazon EC2 compute instance that hosts the endpoint.

vpc -> (structure)

The VPC configuration for the endpoint.

subnetIds -> (list)

An array of IDs for each subnet in the VPC to use.

(string)

securityGroupIds -> (list)

An array of IDs for each security group in the VPC to use.

(string)

JSON Syntax:

```
{
  "sageMaker": {
    "initialInstanceCount": integer,
    "instanceType": "string",
    "executionRole": "string",
    "kmsEncryptionKey": "string",
    "vpc": {
      "subnetIds": ["string", ...],
      "securityGroupIds": ["string", ...]
    }
  }
}
```

`--accept-eula` | `--no-accept-eula` (boolean)

Indicates whether you accept the end-user license agreement (EULA) for the model. Set to `true` to accept the EULA.

`--endpoint-name` (string)

The name of the endpoint. This name must be unique within your Amazon Web Services account and region.

`--client-request-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If youâre not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.

`--tags` (list)

An array of key-value pairs to apply to the underlying Amazon SageMaker endpoint. You can use these tags to organize and identify your Amazon Web Services resources.

(structure)

Definition of the key/value pair for a tag.

key -> (string)

Key for the tag.

value -> (string)

Value for the tag.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
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

marketplaceModelEndpoint -> (structure)

Details about the created endpoint.

endpointArn -> (string)

The Amazon Resource Name (ARN) of the endpoint.

modelSourceIdentifier -> (string)

The ARN of the model from Amazon Bedrock Marketplace that is deployed on this endpoint.

status -> (string)

The overall status of the endpoint in Amazon Bedrock Marketplace (e.g., ACTIVE, INACTIVE).

statusMessage -> (string)

Additional information about the overall status, if available.

createdAt -> (timestamp)

The timestamp when the endpoint was registered.

updatedAt -> (timestamp)

The timestamp when the endpoint was last updated.

endpointConfig -> (tagged union structure)

The configuration of the endpoint, including the number and type of instances used.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `sageMaker`.

sageMaker -> (structure)

The configuration specific to Amazon SageMaker for the endpoint.

initialInstanceCount -> (integer)

The number of Amazon EC2 compute instances to deploy for initial endpoint creation.

instanceType -> (string)

The Amazon EC2 compute instance type to deploy for hosting the model.

executionRole -> (string)

The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on Amazon EC2 compute instances or for batch transform jobs.

kmsEncryptionKey -> (string)

The Amazon Web Services KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the Amazon EC2 compute instance that hosts the endpoint.

vpc -> (structure)

The VPC configuration for the endpoint.

subnetIds -> (list)

An array of IDs for each subnet in the VPC to use.

(string)

securityGroupIds -> (list)

An array of IDs for each security group in the VPC to use.

(string)

endpointStatus -> (string)

The current status of the endpoint (e.g., Creating, InService, Updating, Failed).

endpointStatusMessage -> (string)

Additional information about the endpoint status, if available.