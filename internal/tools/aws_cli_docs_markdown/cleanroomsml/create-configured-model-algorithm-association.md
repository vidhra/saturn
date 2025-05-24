# create-configured-model-algorithm-associationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-configured-model-algorithm-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-configured-model-algorithm-association.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanroomsml](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/index.html#cli-aws-cleanroomsml) ]

# create-configured-model-algorithm-association

## Description

Associates a configured model algorithm to a collaboration for use by any member of the collaboration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithmAssociation)

## Synopsis

```
create-configured-model-algorithm-association
--membership-identifier <value>
--configured-model-algorithm-arn <value>
--name <value>
[--description <value>]
[--privacy-configuration <value>]
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

The membership ID of the member who is associating this configured model algorithm.

`--configured-model-algorithm-arn` (string)

The Amazon Resource Name (ARN) of the configured model algorithm that you want to associate.

`--name` (string)

The name of the configured model algorithm association.

`--description` (string)

The description of the configured model algorithm association.

`--privacy-configuration` (structure)

Specifies the privacy configuration information for the configured model algorithm association. This information includes the maximum data size that can be exported.

policies -> (structure)

The privacy configuration policies for a configured model algorithm association.

trainedModels -> (structure)

Specifies who will receive the trained models.

containerLogs -> (list)

The container for the logs of the trained model.

(structure)

Provides the information necessary for a user to access the logs.

allowedAccountIds -> (list)

A list of account IDs that are allowed to access the logs.

(string)

filterPattern -> (string)

A regular expression pattern that is used to parse the logs and return information that matches the pattern.

containerMetrics -> (structure)

The container for the metrics of the trained model.

noiseLevel -> (string)

The noise level for the generated metrics.

trainedModelExports -> (structure)

Specifies who will receive the trained model export.

maxSize -> (structure)

The maximum size of the data that can be exported.

unit -> (string)

The unit of measurement for the data size.

value -> (double)

The maximum size of the dataset to export.

filesToExport -> (list)

The files that are exported during the trained model export job.

(string)

trainedModelInferenceJobs -> (structure)

Specifies who will receive the trained model inference jobs.

containerLogs -> (list)

The logs container for the trained model inference job.

(structure)

Provides the information necessary for a user to access the logs.

allowedAccountIds -> (list)

A list of account IDs that are allowed to access the logs.

(string)

filterPattern -> (string)

A regular expression pattern that is used to parse the logs and return information that matches the pattern.

maxOutputSize -> (structure)

The maximum allowed size of the output of the trained model inference job.

unit -> (string)

The measurement unit to use.

value -> (double)

The maximum output size value.

JSON Syntax:

```
{
  "policies": {
    "trainedModels": {
      "containerLogs": [
        {
          "allowedAccountIds": ["string", ...],
          "filterPattern": "string"
        }
        ...
      ],
      "containerMetrics": {
        "noiseLevel": "HIGH"|"MEDIUM"|"LOW"|"NONE"
      }
    },
    "trainedModelExports": {
      "maxSize": {
        "unit": "GB",
        "value": double
      },
      "filesToExport": ["MODEL"|"OUTPUT", ...]
    },
    "trainedModelInferenceJobs": {
      "containerLogs": [
        {
          "allowedAccountIds": ["string", ...],
          "filterPattern": "string"
        }
        ...
      ],
      "maxOutputSize": {
        "unit": "GB",
        "value": double
      }
    }
  }
}
```

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

configuredModelAlgorithmAssociationArn -> (string)

The Amazon Resource Name (ARN) of the configured model algorithm association.