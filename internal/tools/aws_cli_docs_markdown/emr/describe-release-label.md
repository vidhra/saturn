# describe-release-labelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-release-label.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-release-label.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# describe-release-label

## Description

Provides Amazon EMR release label details, such as the releases available the Region where the API request is run, and the available applications for a specific Amazon EMR release label. Can also list Amazon EMR releases that support a specified version of Spark.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeReleaseLabel)

## Synopsis

```
describe-release-label
[--release-label <value>]
[--next-token <value>]
[--max-results <value>]
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

`--release-label` (string)

The target release label to be described.

`--next-token` (string)

The pagination token. Reserved for future use. Currently set to null.

`--max-results` (integer)

Reserved for future use. Currently set to null.

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

ReleaseLabel -> (string)

The target release label described in the response.

Applications -> (list)

The list of applications available for the target release label. `Name` is the name of the application. `Version` is the concise version of the application.

(structure)

The returned release label application names or versions.

Name -> (string)

The returned release label application name. For example, `hadoop` .

Version -> (string)

The returned release label application version. For example, `3.2.1` .

NextToken -> (string)

The pagination token. Reserved for future use. Currently set to null.

AvailableOSReleases -> (list)

The list of available Amazon Linux release versions for an Amazon EMR release. Contains a Label field that is formatted as shown in ` *Amazon Linux 2 Release Notes* [https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-al2](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-al2).html`__ . For example, [2.0.20220218.1](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20220218.html) .

(structure)

The Amazon Linux release specified for a cluster in the RunJobFlow request.

Label -> (string)

The Amazon Linux release specified for a cluster in the RunJobFlow request. The format is as shown in ` *Amazon Linux 2 Release Notes* [https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20220218](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20220218).html`__ . For example, 2.0.20220218.1.