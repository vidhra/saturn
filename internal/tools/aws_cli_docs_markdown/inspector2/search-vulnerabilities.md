# search-vulnerabilitiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/search-vulnerabilities.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/search-vulnerabilities.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# search-vulnerabilities

## Description

Lists Amazon Inspector coverage details for a specific vulnerability.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/SearchVulnerabilities)

`search-vulnerabilities` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `vulnerabilities`

## Synopsis

```
search-vulnerabilities
--filter-criteria <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--filter-criteria` (structure)

The criteria used to filter the results of a vulnerability search.

vulnerabilityIds -> (list)

The IDs for specific vulnerabilities.

(string)

Shorthand Syntax:

```
vulnerabilityIds=string,string
```

JSON Syntax:

```
{
  "vulnerabilityIds": ["string", ...]
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

## Output

nextToken -> (string)

The pagination parameter to be used on the next list operation to retrieve more items.

vulnerabilities -> (list)

Details about the listed vulnerability.

(structure)

Contains details about a specific vulnerability Amazon Inspector can detect.

atigData -> (structure)

An object that contains information about the Amazon Web Services Threat Intel Group (ATIG) details for the vulnerability.

firstSeen -> (timestamp)

The date and time this vulnerability was first observed.

lastSeen -> (timestamp)

The date and time this vulnerability was last observed.

targets -> (list)

The commercial sectors this vulnerability targets.

(string)

ttps -> (list)

The [MITRE ATT&CK](https://attack.mitre.org/) tactics, techniques, and procedures (TTPs) associated with vulnerability.

(string)

cisaData -> (structure)

An object that contains the Cybersecurity and Infrastructure Security Agency (CISA) details for the vulnerability.

action -> (string)

The remediation action recommended by CISA for this vulnerability.

dateAdded -> (timestamp)

The date and time CISA added this vulnerability to their catalogue.

dateDue -> (timestamp)

The date and time CISA expects a fix to have been provided vulnerability.

cvss2 -> (structure)

An object that contains the Common Vulnerability Scoring System (CVSS) Version 2 details for the vulnerability.

baseScore -> (double)

The CVSS v2 base score for the vulnerability.

scoringVector -> (string)

The scoring vector associated with the CVSS v2 score.

cvss3 -> (structure)

An object that contains the Common Vulnerability Scoring System (CVSS) Version 3 details for the vulnerability.

baseScore -> (double)

The CVSS v3 base score for the vulnerability.

scoringVector -> (string)

The scoring vector associated with the CVSS v3 score.

cwes -> (list)

The Common Weakness Enumeration (CWE) associated with the vulnerability.

(string)

description -> (string)

A description of the vulnerability.

detectionPlatforms -> (list)

Platforms that the vulnerability can be detected on.

(string)

epss -> (structure)

An object that contains the Exploit Prediction Scoring System (EPSS) score for a vulnerability.

score -> (double)

The Exploit Prediction Scoring System (EPSS) score.

exploitObserved -> (structure)

An object that contains details on when the exploit was observed.

firstSeen -> (timestamp)

The date an time when the exploit was first seen.

lastSeen -> (timestamp)

The date an time when the exploit was last seen.

id -> (string)

The ID for the specific vulnerability.

referenceUrls -> (list)

Links to various resources with more information on this vulnerability.

(string)

relatedVulnerabilities -> (list)

A list of related vulnerabilities.

(string)

source -> (string)

The source of the vulnerability information. Possible results are `RHEL` , `AMAZON_CVE` , `DEBIAN` or `NVD` .

sourceUrl -> (string)

A link to the official source material for this vulnerability.

vendorCreatedAt -> (timestamp)

The date and time when the vendor created this vulnerability.

vendorSeverity -> (string)

The severity assigned by the vendor.

vendorUpdatedAt -> (timestamp)

The date and time when the vendor last updated this vulnerability.