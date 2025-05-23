# describe-image-scan-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-image-scan-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-image-scan-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html#cli-aws-ecr) ]

# describe-image-scan-findings

## Description

Returns the scan findings for the specified image.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeImageScanFindings)

`describe-image-scan-findings` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `imageScanFindings.findings`, `imageScanFindings.enhancedFindings`

## Synopsis

```
describe-image-scan-findings
[--registry-id <value>]
--repository-name <value>
--image-id <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--registry-id` (string)

The Amazon Web Services account ID associated with the registry that contains the repository in which to describe the image scan findings for. If you do not specify a registry, the default registry is assumed.

`--repository-name` (string)

The repository for the image for which to describe the scan findings.

`--image-id` (structure)

An object with identifying information for an image in an Amazon ECR repository.

imageDigest -> (string)

The `sha256` digest of the image manifest.

imageTag -> (string)

The tag used for the image.

Shorthand Syntax:

```
imageDigest=string,imageTag=string
```

JSON Syntax:

```
{
  "imageDigest": "string",
  "imageTag": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe the scan findings for an image**

The following `describe-image-scan-findings` example returns the image scan findings for an image using the image digest in the specified repository in the default registry for an account.

```
aws ecr describe-image-scan-findings \
    --repository-name sample-repo \
    --image-id imageDigest=sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6
```

Output:

```
{
    "imageScanFindings": {
      "findings": [
          {
              "name": "CVE-2019-5188",
              "description": "A code execution vulnerability exists in the directory rehashing functionality of E2fsprogs e2fsck 1.45.4. A specially crafted ext4 directory can cause an out-of-bounds write on the stack, resulting in code execution. An attacker can corrupt a partition to trigger this vulnerability.",
              "uri": "http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-5188",
              "severity": "MEDIUM",
              "attributes": [
                  {
                      "key": "package_version",
                      "value": "1.44.1-1ubuntu1.1"
                  },
                  {
                      "key": "package_name",
                      "value": "e2fsprogs"
                  },
                  {
                      "key": "CVSS2_VECTOR",
                      "value": "AV:L/AC:L/Au:N/C:P/I:P/A:P"
                  },
                  {
                      "key": "CVSS2_SCORE",
                      "value": "4.6"
                  }
              ]
          }
      ],
      "imageScanCompletedAt": 1579839105.0,
      "vulnerabilitySourceUpdatedAt": 1579811117.0,
      "findingSeverityCounts": {
          "MEDIUM": 1
      }
  },
  "registryId": "123456789012",
  "repositoryName": "sample-repo",
  "imageId": {
      "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6"
  },
  "imageScanStatus": {
      "status": "COMPLETE",
      "description": "The scan was completed successfully."
  }
}
```

For more information, see [Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in the *Amazon ECR User Guide*.

## Output

registryId -> (string)

The registry ID associated with the request.

repositoryName -> (string)

The repository name associated with the request.

imageId -> (structure)

An object with identifying information for an image in an Amazon ECR repository.

imageDigest -> (string)

The `sha256` digest of the image manifest.

imageTag -> (string)

The tag used for the image.

imageScanStatus -> (structure)

The current state of the scan.

status -> (string)

The current state of an image scan.

description -> (string)

The description of the image scan status.

imageScanFindings -> (structure)

The information contained in the image scan findings.

imageScanCompletedAt -> (timestamp)

The time of the last completed image scan.

vulnerabilitySourceUpdatedAt -> (timestamp)

The time when the vulnerability data was last scanned.

findingSeverityCounts -> (map)

The image vulnerability counts, sorted by severity.

key -> (string)

value -> (integer)

findings -> (list)

The findings from the image scan.

(structure)

Contains information about an image scan finding.

name -> (string)

The name associated with the finding, usually a CVE number.

description -> (string)

The description of the finding.

uri -> (string)

A link containing additional details about the security vulnerability.

severity -> (string)

The finding severity.

attributes -> (list)

A collection of attributes of the host from which the finding is generated.

(structure)

This data type is used in the  ImageScanFinding data type.

key -> (string)

The attribute key.

value -> (string)

The value assigned to the attribute key.

enhancedFindings -> (list)

Details about the enhanced scan findings from Amazon Inspector.

(structure)

The details of an enhanced image scan. This is returned when enhanced scanning is enabled for your private registry.

awsAccountId -> (string)

The Amazon Web Services account ID associated with the image.

description -> (string)

The description of the finding.

findingArn -> (string)

The Amazon Resource Number (ARN) of the finding.

firstObservedAt -> (timestamp)

The date and time that the finding was first observed.

lastObservedAt -> (timestamp)

The date and time that the finding was last observed.

packageVulnerabilityDetails -> (structure)

An object that contains the details of a package vulnerability finding.

cvss -> (list)

An object that contains details about the CVSS score of a finding.

(structure)

The CVSS score for a finding.

baseScore -> (double)

The base CVSS score used for the finding.

scoringVector -> (string)

The vector string of the CVSS score.

source -> (string)

The source of the CVSS score.

version -> (string)

The version of CVSS used for the score.

referenceUrls -> (list)

One or more URLs that contain details about this vulnerability type.

(string)

relatedVulnerabilities -> (list)

One or more vulnerabilities related to the one identified in this finding.

(string)

source -> (string)

The source of the vulnerability information.

sourceUrl -> (string)

A URL to the source of the vulnerability information.

vendorCreatedAt -> (timestamp)

The date and time that this vulnerability was first added to the vendorâs database.

vendorSeverity -> (string)

The severity the vendor has given to this vulnerability type.

vendorUpdatedAt -> (timestamp)

The date and time the vendor last updated this vulnerability in their database.

vulnerabilityId -> (string)

The ID given to this vulnerability.

vulnerablePackages -> (list)

The packages impacted by this vulnerability.

(structure)

Information on the vulnerable package identified by a finding.

arch -> (string)

The architecture of the vulnerable package.

epoch -> (integer)

The epoch of the vulnerable package.

filePath -> (string)

The file path of the vulnerable package.

name -> (string)

The name of the vulnerable package.

packageManager -> (string)

The package manager of the vulnerable package.

release -> (string)

The release of the vulnerable package.

sourceLayerHash -> (string)

The source layer hash of the vulnerable package.

version -> (string)

The version of the vulnerable package.

fixedInVersion -> (string)

The version of the package that contains the vulnerability fix.

remediation -> (structure)

An object that contains the details about how to remediate a finding.

recommendation -> (structure)

An object that contains information about the recommended course of action to remediate the finding.

url -> (string)

The URL address to the CVE remediation recommendations.

text -> (string)

The recommended course of action to remediate the finding.

resources -> (list)

Contains information on the resources involved in a finding.

(structure)

Details about the resource involved in a finding.

details -> (structure)

An object that contains details about the resource involved in a finding.

awsEcrContainerImage -> (structure)

An object that contains details about the Amazon ECR container image involved in the finding.

architecture -> (string)

The architecture of the Amazon ECR container image.

author -> (string)

The image author of the Amazon ECR container image.

imageHash -> (string)

The image hash of the Amazon ECR container image.

imageTags -> (list)

The image tags attached to the Amazon ECR container image.

(string)

platform -> (string)

The platform of the Amazon ECR container image.

pushedAt -> (timestamp)

The date and time the Amazon ECR container image was pushed.

registry -> (string)

The registry the Amazon ECR container image belongs to.

repositoryName -> (string)

The name of the repository the Amazon ECR container image resides in.

id -> (string)

The ID of the resource.

tags -> (map)

The tags attached to the resource.

key -> (string)

value -> (string)

type -> (string)

The type of resource.

score -> (double)

The Amazon Inspector score given to the finding.

scoreDetails -> (structure)

An object that contains details of the Amazon Inspector score.

cvss -> (structure)

An object that contains details about the CVSS score given to a finding.

adjustments -> (list)

An object that contains details about adjustment Amazon Inspector made to the CVSS score.

(structure)

Details on adjustments Amazon Inspector made to the CVSS score for a finding.

metric -> (string)

The metric used to adjust the CVSS score.

reason -> (string)

The reason the CVSS score has been adjustment.

score -> (double)

The CVSS score.

scoreSource -> (string)

The source for the CVSS score.

scoringVector -> (string)

The vector for the CVSS score.

version -> (string)

The CVSS version used in scoring.

severity -> (string)

The severity of the finding.

status -> (string)

The status of the finding.

title -> (string)

The title of the finding.

type -> (string)

The type of the finding.

updatedAt -> (timestamp)

The date and time the finding was last updated at.

fixAvailable -> (string)

Details on whether a fix is available through a version update. This value can be `YES` , `NO` , or `PARTIAL` . A `PARTIAL` fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.

exploitAvailable -> (string)

If a finding discovered in your environment has an exploit available.

nextToken -> (string)

The `nextToken` value to include in a future `DescribeImageScanFindings` request. When the results of a `DescribeImageScanFindings` request exceed `maxResults` , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.