# list-image-scan-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-scan-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-scan-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# list-image-scan-findings

## Description

Returns a list of image scan findings for your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/ListImageScanFindings)

## Synopsis

```
list-image-scan-findings
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
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

An array of name value pairs that you can use to filter your results. You can use the following filters to streamline results:

- `imageBuildVersionArn`
- `imagePipelineArn`
- `vulnerabilityId`
- `severity`

If you donât request a filter, then all findings in your account are listed.

(structure)

A name value pair that Image Builder applies to streamline results from the vulnerability scan findings list action.

name -> (string)

The name of the image scan finding filter. Filter names are case-sensitive.

values -> (list)

The filter values. Filter values are case-sensitive.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum items to return in a request.

`--next-token` (string)

A token to specify where to start paginating. This is the nextToken from a previously truncated response.

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

requestId -> (string)

The request ID that uniquely identifies this request.

findings -> (list)

The image scan findings for your account that meet your request filter criteria.

(structure)

Contains details about a vulnerability scan finding.

awsAccountId -> (string)

The Amazon Web Services account ID thatâs associated with the finding.

imageBuildVersionArn -> (string)

The Amazon Resource Name (ARN) of the image build version thatâs associated with the finding.

imagePipelineArn -> (string)

The Amazon Resource Name (ARN) of the image pipeline thatâs associated with the finding.

type -> (string)

The type of the finding. Image Builder looks for findings of the type `PACKAGE_VULNERABILITY` that apply to output images, and excludes other types.

description -> (string)

The description of the finding.

title -> (string)

The title of the finding.

remediation -> (structure)

An object that contains the details about how to remediate the finding.

recommendation -> (structure)

An object that contains information about the recommended course of action to remediate the finding.

text -> (string)

The recommended course of action to remediate the finding.

url -> (string)

A link to more information about the recommended remediation for this vulnerability.

severity -> (string)

The severity of the finding.

firstObservedAt -> (timestamp)

The date and time when the finding was first observed.

updatedAt -> (timestamp)

The timestamp when the finding was last updated.

inspectorScore -> (double)

The score that Amazon Inspector assigned for the finding.

inspectorScoreDetails -> (structure)

An object that contains details of the Amazon Inspector score.

adjustedCvss -> (structure)

An object that contains details about an adjustment that Amazon Inspector made to the CVSS score for the finding.

scoreSource -> (string)

The source for the CVSS score.

cvssSource -> (string)

The source of the finding.

version -> (string)

The CVSS version that generated the score.

score -> (double)

The CVSS score.

scoringVector -> (string)

A vector that measures the severity of the vulnerability.

adjustments -> (list)

An object that contains details about an adjustment that Amazon Inspector made to the CVSS score for the finding.

(structure)

Details about an adjustment that Amazon Inspector made to the CVSS score for a finding.

metric -> (string)

The metric that Amazon Inspector used to adjust the CVSS score.

reason -> (string)

The reason for the CVSS score adjustment.

packageVulnerabilityDetails -> (structure)

An object that contains the details of a package vulnerability finding.

vulnerabilityId -> (string)

A unique identifier for this vulnerability.

vulnerablePackages -> (list)

The packages that this vulnerability impacts.

(structure)

Information about a vulnerable package that Amazon Inspector identifies in a finding.

name -> (string)

The name of the vulnerable package.

version -> (string)

The version of the vulnerable package.

sourceLayerHash -> (string)

The source layer hash of the vulnerable package.

epoch -> (integer)

The epoch of the vulnerable package.

release -> (string)

The release of the vulnerable package.

arch -> (string)

The architecture of the vulnerable package.

packageManager -> (string)

The package manager of the vulnerable package.

filePath -> (string)

The file path of the vulnerable package.

fixedInVersion -> (string)

The version of the package that contains the vulnerability fix.

remediation -> (string)

The code to run in your environment to update packages with a fix available.

source -> (string)

The source of the vulnerability information.

cvss -> (list)

CVSS scores for one or more vulnerabilities that Amazon Inspector identified for a package.

(structure)

Amazon Inspector generates a risk score for each finding. This score helps you to prioritize findings, to focus on the most critical findings and the most vulnerable resources. The score uses the Common Vulnerability Scoring System (CVSS) format. This format is a modification of the base CVSS score that the National Vulnerability Database (NVD) provides. For more information about severity levels, see [Severity levels for Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html) in the *Amazon Inspector User Guide* .

baseScore -> (double)

The CVSS base score.

scoringVector -> (string)

The vector string of the CVSS score.

version -> (string)

The CVSS version that generated the score.

source -> (string)

The source of the CVSS score.

relatedVulnerabilities -> (list)

Vulnerabilities that are often related to the findings for the package.

(string)

sourceUrl -> (string)

A link to the source of the vulnerability information.

vendorSeverity -> (string)

The severity that the vendor assigned to this vulnerability type.

vendorCreatedAt -> (timestamp)

The date and time when this vulnerability was first added to the vendorâs database.

vendorUpdatedAt -> (timestamp)

The date and time when the vendor last updated this vulnerability in their database.

referenceUrls -> (list)

Links to web pages that contain details about the vulnerabilities that Amazon Inspector identified for the package.

(string)

fixAvailable -> (string)

Details about whether a fix is available for any of the packages that are identified in the finding through a version update.

nextToken -> (string)

The next token used for paginated responses. When this field isnât empty, there are additional elements that the service hasnât included in this request. Use this token with the next request to retrieve additional objects.