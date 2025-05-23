# create-ml-input-channelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-ml-input-channel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-ml-input-channel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanroomsml](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/index.html#cli-aws-cleanroomsml) ]

# create-ml-input-channel

## Description

Provides the information to create an ML input channel. An ML input channel is the result of a query that can be used for ML modeling.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanroomsml-2023-09-06/CreateMLInputChannel)

## Synopsis

```
create-ml-input-channel
--membership-identifier <value>
--configured-model-algorithm-associations <value>
--input-channel <value>
--name <value>
--retention-in-days <value>
[--description <value>]
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

The membership ID of the member that is creating the ML input channel.

`--configured-model-algorithm-associations` (list)

The associated configured model algorithms that are necessary to create this ML input channel.

(string)

Syntax:

```
"string" "string" ...
```

`--input-channel` (structure)

The input data that is used to create this ML input channel.

dataSource -> (tagged union structure)

The data source that is used to create the ML input channel.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `protectedQueryInputParameters`.

protectedQueryInputParameters -> (structure)

Provides information necessary to perform the protected query.

sqlParameters -> (structure)

The parameters for the SQL type Protected Query.

queryString -> (string)

The query string to be submitted.

analysisTemplateArn -> (string)

The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.

parameters -> (map)

The protected query SQL parameters.

key -> (string)

value -> (string)

computeConfiguration -> (tagged union structure)

Provides configuration information for the workers that will perform the protected query.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `worker`.

worker -> (structure)

The worker instances that will perform the compute work.

type -> (string)

The instance type of the compute workers that are used.

number -> (integer)

The number of compute workers that are used.

roleArn -> (string)

The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the `dataSource` field the input channel.

Passing a role across AWS accounts is not allowed. If you pass a role that isnât in your account, you get an `AccessDeniedException` error.

JSON Syntax:

```
{
  "dataSource": {
    "protectedQueryInputParameters": {
      "sqlParameters": {
        "queryString": "string",
        "analysisTemplateArn": "string",
        "parameters": {"string": "string"
          ...}
      },
      "computeConfiguration": {
        "worker": {
          "type": "CR.1X"|"CR.4X",
          "number": integer
        }
      }
    }
  },
  "roleArn": "string"
}
```

`--name` (string)

The name of the ML input channel.

`--retention-in-days` (integer)

The number of days that the data in the ML input channel is retained.

`--description` (string)

The description of the ML input channel.

`--kms-key-arn` (string)

The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.

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

mlInputChannelArn -> (string)

The Amazon Resource Name (ARN) of the ML input channel.