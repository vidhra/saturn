# list-license-manager-report-generatorsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-license-manager-report-generators.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-license-manager-report-generators.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/index.html#cli-aws-license-manager) ]

# list-license-manager-report-generators

## Description

Lists the report generators for your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseManagerReportGenerators)

## Synopsis

```
list-license-manager-report-generators
[--filters <value>]
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

`--filters` (list)

Filters to scope the results. The following filters are supported:

- `LicenseConfigurationArn`

(structure)

A filter name and value pair that is used to return more specific results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

Name -> (string)

Name of the filter. Filter names are case-sensitive.

Values -> (list)

The value of the filter, which is case-sensitive. You can only specify one value for the filter.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--next-token` (string)

Token for the next set of results.

`--max-results` (integer)

Maximum number of results to return in a single call.

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

ReportGenerators -> (list)

A report generator that creates periodic reports about your license configurations.

(structure)

Describe the details of a report generator.

ReportGeneratorName -> (string)

Name of the report generator.

ReportType -> (list)

Type of reports that are generated.

(string)

ReportContext -> (structure)

License configuration type for this generator.

licenseConfigurationArns -> (list)

Amazon Resource Name (ARN) of the license configuration that this generator reports on.

(string)

ReportFrequency -> (structure)

Details about how frequently reports are generated.

value -> (integer)

Number of times within the frequency period that a report is generated. The only supported value is `1` .

period -> (string)

Time period between each report. The period can be daily, weekly, or monthly.

LicenseManagerReportGeneratorArn -> (string)

Amazon Resource Name (ARN) of the report generator.

LastRunStatus -> (string)

Status of the last report generation attempt.

LastRunFailureReason -> (string)

Failure message for the last report generation attempt.

LastReportGenerationTime -> (string)

Time the last report was generated at.

ReportCreatorAccount -> (string)

The Amazon Web Services account ID used to create the report generator.

Description -> (string)

Description of the report generator.

S3Location -> (structure)

Details of the S3 bucket that report generator reports are published to.

bucket -> (string)

Name of the S3 bucket reports are published to.

keyPrefix -> (string)

Prefix of the S3 bucket reports are published to.

CreateTime -> (string)

Time the report was created.

Tags -> (list)

Tags associated with the report generator.

(structure)

Details about the tags for a resource. For more information about tagging support in License Manager, see the [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html) operation.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

NextToken -> (string)

Token for the next set of results.