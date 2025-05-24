# import-model-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/import-model-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/import-model-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# import-model-version

## Description

Imports a model that has been trained successfully.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/ImportModelVersion)

## Synopsis

```
import-model-version
--source-model-version-arn <value>
[--model-name <value>]
--dataset-name <value>
[--labels-input-configuration <value>]
[--client-token <value>]
[--role-arn <value>]
[--server-side-kms-key-id <value>]
[--tags <value>]
[--inference-data-import-strategy <value>]
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

`--source-model-version-arn` (string)

The Amazon Resource Name (ARN) of the model version to import.

`--model-name` (string)

The name for the machine learning model to be created. If the model already exists, Amazon Lookout for Equipment creates a new version. If you do not specify this field, it is filled with the name of the source model.

`--dataset-name` (string)

The name of the dataset for the machine learning model being imported.

`--labels-input-configuration` (structure)

Contains the configuration information for the S3 location being used to hold label data.

S3InputConfiguration -> (structure)

Contains location information for the S3 location being used for label data.

Bucket -> (string)

The name of the S3 bucket holding the label data.

Prefix -> (string)

The prefix for the S3 bucket used for the label data.

LabelGroupName -> (string)

The name of the label group to be used for label data.

Shorthand Syntax:

```
S3InputConfiguration={Bucket=string,Prefix=string},LabelGroupName=string
```

JSON Syntax:

```
{
  "S3InputConfiguration": {
    "Bucket": "string",
    "Prefix": "string"
  },
  "LabelGroupName": "string"
}
```

`--client-token` (string)

A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one.

`--role-arn` (string)

The Amazon Resource Name (ARN) of a role with permission to access the data source being used to create the machine learning model.

`--server-side-kms-key-id` (string)

Provides the identifier of the KMS key key used to encrypt model data by Amazon Lookout for Equipment.

`--tags` (list)

The tags associated with the machine learning model to be created.

(structure)

A tag is a key-value pair that can be added to a resource as metadata.

Key -> (string)

The key for the specified tag.

Value -> (string)

The value for the specified tag.

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

`--inference-data-import-strategy` (string)

Indicates how to import the accumulated inference data when a model version is imported. The possible values are as follows:

- NO_IMPORT â Donât import the data.
- ADD_WHEN_EMPTY â Only import the data from the source model if there is no existing data in the target model.
- OVERWRITE â Import the data from the source model and overwrite the existing data in the target model.

Possible values:

- `NO_IMPORT`
- `ADD_WHEN_EMPTY`
- `OVERWRITE`

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

ModelName -> (string)

The name for the machine learning model.

ModelArn -> (string)

The Amazon Resource Name (ARN) of the model being created.

ModelVersionArn -> (string)

The Amazon Resource Name (ARN) of the model version being created.

ModelVersion -> (long)

The version of the model being created.

Status -> (string)

The status of the `ImportModelVersion` operation.