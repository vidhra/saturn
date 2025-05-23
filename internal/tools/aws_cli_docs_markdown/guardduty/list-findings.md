# list-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# list-findings

## Description

Lists GuardDuty findings for the specified detector ID.

There might be regional differences because some flags might not be available in all the Regions where GuardDuty is currently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFindings)

`list-findings` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `FindingIds`

## Synopsis

```
list-findings
--detector-id <value>
[--finding-criteria <value>]
[--sort-criteria <value>]
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

`--detector-id` (string)

The ID of the detector that specifies the GuardDuty service whose findings you want to list.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--finding-criteria` (structure)

Represents the criteria used for querying findings. Valid values include:

- JSON field name
- accountId
- region
- confidence
- id
- resource.accessKeyDetails.accessKeyId
- resource.accessKeyDetails.principalId
- resource.accessKeyDetails.userName
- resource.accessKeyDetails.userType
- resource.instanceDetails.iamInstanceProfile.id
- resource.instanceDetails.imageId
- resource.instanceDetails.instanceId
- resource.instanceDetails.networkInterfaces.ipv6Addresses
- resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress
- resource.instanceDetails.networkInterfaces.publicDnsName
- resource.instanceDetails.networkInterfaces.publicIp
- resource.instanceDetails.networkInterfaces.securityGroups.groupId
- resource.instanceDetails.networkInterfaces.securityGroups.groupName
- resource.instanceDetails.networkInterfaces.subnetId
- resource.instanceDetails.networkInterfaces.vpcId
- resource.instanceDetails.tags.key
- resource.instanceDetails.tags.value
- resource.resourceType
- service.action.actionType
- service.action.awsApiCallAction.api
- service.action.awsApiCallAction.callerType
- service.action.awsApiCallAction.remoteIpDetails.city.cityName
- service.action.awsApiCallAction.remoteIpDetails.country.countryName
- service.action.awsApiCallAction.remoteIpDetails.ipAddressV4
- service.action.awsApiCallAction.remoteIpDetails.organization.asn
- service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg
- service.action.awsApiCallAction.serviceName
- service.action.dnsRequestAction.domain
- service.action.dnsRequestAction.domainWithSuffix
- service.action.networkConnectionAction.blocked
- service.action.networkConnectionAction.connectionDirection
- service.action.networkConnectionAction.localPortDetails.port
- service.action.networkConnectionAction.protocol
- service.action.networkConnectionAction.remoteIpDetails.country.countryName
- service.action.networkConnectionAction.remoteIpDetails.ipAddressV4
- service.action.networkConnectionAction.remoteIpDetails.organization.asn
- service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg
- service.action.networkConnectionAction.remotePortDetails.port
- service.additionalInfo.threatListName
- service.archived When this attribute is set to âtrueâ, only archived findings are listed. When itâs set to âfalseâ, only unarchived findings are listed. When this attribute is not set, all existing findings are listed.
- service.ebsVolumeScanDetails.scanId
- service.resourceRole
- severity
- type
- updatedAt Type: Timestamp in Unix Epoch millisecond format: 1486685375000

Criterion -> (map)

Represents a map of finding properties that match specified conditions and values when querying findings.

key -> (string)

value -> (structure)

Contains information about the condition.

Eq -> (list)

Represents the *equal* condition to be applied to a single field when querying for findings.

(string)

Neq -> (list)

Represents the *not equal* condition to be applied to a single field when querying for findings.

(string)

Gt -> (integer)

Represents a *greater than* condition to be applied to a single field when querying for findings.

Gte -> (integer)

Represents a *greater than or equal* condition to be applied to a single field when querying for findings.

Lt -> (integer)

Represents a *less than* condition to be applied to a single field when querying for findings.

Lte -> (integer)

Represents a *less than or equal* condition to be applied to a single field when querying for findings.

Equals -> (list)

Represents an *equal*  condition to be applied to a single field when querying for findings.

(string)

NotEquals -> (list)

Represents a *not equal*  condition to be applied to a single field when querying for findings.

(string)

GreaterThan -> (long)

Represents a *greater than* condition to be applied to a single field when querying for findings.

GreaterThanOrEqual -> (long)

Represents a *greater than or equal* condition to be applied to a single field when querying for findings.

LessThan -> (long)

Represents a *less than* condition to be applied to a single field when querying for findings.

LessThanOrEqual -> (long)

Represents a *less than or equal* condition to be applied to a single field when querying for findings.

Shorthand Syntax:

```
Criterion={KeyName1={Eq=[string,string],Neq=[string,string],Gt=integer,Gte=integer,Lt=integer,Lte=integer,Equals=[string,string],NotEquals=[string,string],GreaterThan=long,GreaterThanOrEqual=long,LessThan=long,LessThanOrEqual=long},KeyName2={Eq=[string,string],Neq=[string,string],Gt=integer,Gte=integer,Lt=integer,Lte=integer,Equals=[string,string],NotEquals=[string,string],GreaterThan=long,GreaterThanOrEqual=long,LessThan=long,LessThanOrEqual=long}}
```

JSON Syntax:

```
{
  "Criterion": {"string": {
        "Eq": ["string", ...],
        "Neq": ["string", ...],
        "Gt": integer,
        "Gte": integer,
        "Lt": integer,
        "Lte": integer,
        "Equals": ["string", ...],
        "NotEquals": ["string", ...],
        "GreaterThan": long,
        "GreaterThanOrEqual": long,
        "LessThan": long,
        "LessThanOrEqual": long
      }
    ...}
}
```

`--sort-criteria` (structure)

Represents the criteria used for sorting findings.

AttributeName -> (string)

Represents the finding attribute, such as `accountId` , that sorts the findings.

OrderBy -> (string)

The order by which the sorted findings are to be displayed.

Shorthand Syntax:

```
AttributeName=string,OrderBy=string
```

JSON Syntax:

```
{
  "AttributeName": "string",
  "OrderBy": "ASC"|"DESC"
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

**Example 1: To list all findings for the current region**

The following `list-findings` example displays a list of all findingIds for the current region sorted by severity from highest to lowest.

```
aws guardduty list-findings \
    --detector-id 12abc34d567e8fa901bc2d34eexample \
    --sort-criteria '{"AttributeName": "severity","OrderBy":"DESC"}'
```

Output:

```
{
    "FindingIds": [
        "04b8ab50fd29c64fc771b232dexample",
        "5ab8ab50fd21373735c826d3aexample",
        "90b93de7aba69107f05bbe60bexample",
        ...
    ]
}
```

For more information, see [Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html) in the GuardDuty User Guide.

**Example 2: To list findings for the current region matching a specific finding criteria**

The following `list-findings` example displays a list of all findingIds that match a specified finding type.

```
aws guardduty list-findings \
    --detector-id 12abc34d567e8fa901bc2d34eexample \
    --finding-criteria  '{"Criterion":{"type": {"Eq":["UnauthorizedAccess:EC2/SSHBruteForce"]}}}'
```

Output:

```
{
    "FindingIds": [
        "90b93de7aba69107f05bbe60bexample",
        "6eb9430d7023d30774d6f05e3example",
        "2eb91a2d060ac9a21963a5848example",
        "44b8ab50fd2b0039a9e48f570example",
        "9eb8ab4cd2b7e5b66ba4f5e96example",
        "e0b8ab3a38e9b0312cc390ceeexample"
    ]
}
```

For more information, see [Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html) in the GuardDuty User Guide.

**Example 3: To list findings for the current region matching a specific set of finding criteria defined within a JSON file**

The following `list-findings` example displays a list of all findingIds that are not archived, and involve the IAM user named âtestuserâ, as specified in a JSON file.

```
aws guardduty list-findings \
    --detector-id 12abc34d567e8fa901bc2d34eexample \
    --finding-criteria  file://myfile.json
```

Contents of `myfile.json`:

```
{"Criterion": {
    "resource.accessKeyDetails.userName":{
                "Eq":[
                    "testuser"
                    ]
                },
    "service.archived": {
                "Eq": [
                    "false"
                ]
            }
        }
}
```

Output:

```
{
    "FindingIds": [
        "1ab92989eaf0e742df4a014d5example"
    ]
}
```

For more information, see [Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html) in the GuardDuty User Guide.

## Output

FindingIds -> (list)

The IDs of the findings that youâre listing.

(string)

NextToken -> (string)

The pagination parameter to be used on the next list operation to retrieve more items.