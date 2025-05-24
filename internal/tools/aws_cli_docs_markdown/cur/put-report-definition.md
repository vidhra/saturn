# put-report-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/put-report-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/put-report-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cur](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html#cli-aws-cur) ]

# put-report-definition

## Description

Creates a new report using the description that you provide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/PutReportDefinition)

## Synopsis

```
put-report-definition
--report-definition <value>
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

`--report-definition` (structure)

Represents the output of the PutReportDefinition operation. The content consists of the detailed metadata and data file information.

ReportName -> (string)

The name of the report that you want to create. The name must be unique, is case sensitive, and canât include spaces.

TimeUnit -> (string)

The length of time covered by the report.

Format -> (string)

The format that Amazon Web Services saves the report in.

Compression -> (string)

The compression format that Amazon Web Services uses for the report.

AdditionalSchemaElements -> (list)

A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs.

(string)

Whether or not Amazon Web Services includes resource IDs in the report.

S3Bucket -> (string)

The S3 bucket where Amazon Web Services delivers the report.

S3Prefix -> (string)

The prefix that Amazon Web Services adds to the report name when Amazon Web Services delivers the report. Your prefix canât include spaces.

S3Region -> (string)

The region of the S3 bucket that Amazon Web Services delivers the report into.

AdditionalArtifacts -> (list)

A list of manifests that you want Amazon Web Services to create for this report.

(string)

The types of manifest that you want Amazon Web Services to create for this report.

RefreshClosedReports -> (boolean)

Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.

ReportVersioning -> (string)

Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.

BillingViewArn -> (string)

The Amazon resource name of the billing view. The `BillingViewArn` is needed to create Amazon Web Services Cost and Usage Report for each billing group maintained in the Amazon Web Services Billing Conductor service. The `BillingViewArn` for a billing group can be constructed as: `arn:aws:billing::payer-account-id:billingview/billing-group-primary-account-id`

ReportStatus -> (structure)

The status of the report.

lastDelivery -> (string)

A timestamp that gives the date of a report delivery.

lastStatus -> (string)

An enum that gives the status of a report delivery.

Shorthand Syntax:

```
ReportName=string,TimeUnit=string,Format=string,Compression=string,AdditionalSchemaElements=string,string,S3Bucket=string,S3Prefix=string,S3Region=string,AdditionalArtifacts=string,string,RefreshClosedReports=boolean,ReportVersioning=string,BillingViewArn=string,ReportStatus={lastDelivery=string,lastStatus=string}
```

JSON Syntax:

```
{
  "ReportName": "string",
  "TimeUnit": "HOURLY"|"DAILY"|"MONTHLY",
  "Format": "textORcsv"|"Parquet",
  "Compression": "ZIP"|"GZIP"|"Parquet",
  "AdditionalSchemaElements": ["RESOURCES"|"SPLIT_COST_ALLOCATION_DATA"|"MANUAL_DISCOUNT_COMPATIBILITY", ...],
  "S3Bucket": "string",
  "S3Prefix": "string",
  "S3Region": "af-south-1"|"ap-east-1"|"ap-south-1"|"ap-south-2"|"ap-southeast-1"|"ap-southeast-2"|"ap-southeast-3"|"ap-northeast-1"|"ap-northeast-2"|"ap-northeast-3"|"ca-central-1"|"eu-central-1"|"eu-central-2"|"eu-west-1"|"eu-west-2"|"eu-west-3"|"eu-north-1"|"eu-south-1"|"eu-south-2"|"me-central-1"|"me-south-1"|"sa-east-1"|"us-east-1"|"us-east-2"|"us-west-1"|"us-west-2"|"cn-north-1"|"cn-northwest-1",
  "AdditionalArtifacts": ["REDSHIFT"|"QUICKSIGHT"|"ATHENA", ...],
  "RefreshClosedReports": true|false,
  "ReportVersioning": "CREATE_NEW_REPORT"|"OVERWRITE_REPORT",
  "BillingViewArn": "string",
  "ReportStatus": {
    "lastDelivery": "string",
    "lastStatus": "SUCCESS"|"ERROR_PERMISSIONS"|"ERROR_NO_BUCKET"
  }
}
```

`--tags` (list)

The tags to be assigned to the report definition resource.

(structure)

Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a report definition.

Key -> (string)

The key of the tag. Tag keys are case sensitive. Each report definition can only have up to one tag with the same key. If you try to add an existing tag with the same key, the existing tag value will be updated to the new value.

Value -> (string)

The value of the tag. Tag values are case-sensitive. This can be an empty string.

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

**To create an AWS Cost and Usage Reports**

The following `put-report-definition` example creates a daily AWS Cost and Usage Report that you can upload into Amazon Redshift or Amazon QuickSight.

```
aws cur put-report-definition --report-definition file://report-definition.json
```

Contents of `report-definition.json`:

```
{
    "ReportName": "ExampleReport",
    "TimeUnit": "DAILY",
    "Format": "textORcsv",
    "Compression": "ZIP",
    "AdditionalSchemaElements": [
        "RESOURCES"
    ],
    "S3Bucket": "example-s3-bucket",
    "S3Prefix": "exampleprefix",
    "S3Region": "us-east-1",
    "AdditionalArtifacts": [
        "REDSHIFT",
        "QUICKSIGHT"
    ]
}
```

## Output

None