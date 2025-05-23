# create-filterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# create-filter

## Description

Creates a filter using the specified finding criteria. The maximum number of saved filters per Amazon Web Services account per Region is 100. For more information, see [Quotas for GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_limits.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateFilter)

## Synopsis

```
create-filter
--detector-id <value>
--name <value>
[--description <value>]
[--action <value>]
[--rank <value>]
--finding-criteria <value>
[--client-token <value>]
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

`--detector-id` (string)

The detector ID associated with the GuardDuty account for which you want to create a filter.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--name` (string)

The name of the filter. Valid characters include period (.), underscore (_), dash (-), and alphanumeric characters. A whitespace is considered to be an invalid character.

`--description` (string)

The description of the filter. Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses (`{ }` , `[ ]` , and `( )` ), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.

`--action` (string)

Specifies the action that is to be applied to the findings that match the filter.

Possible values:

- `NOOP`
- `ARCHIVE`

`--rank` (integer)

Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.

`--finding-criteria` (structure)

Represents the criteria to be used in the filter for querying findings.

You can only use the following attributes to query findings:

- accountId
- id
- region
- severity To filter on the basis of severity, the API and CLI use the following input list for the [FindingCriteria](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingCriteria.html) condition:
- **Low** : `["1", "2", "3"]`
- **Medium** : `["4", "5", "6"]`
- **High** : `["7", "8"]`
- **Critical** : `["9", "10"]`

For more information, see [Findings severity levels](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html) in the *Amazon GuardDuty User Guide* .

- type
- updatedAt Type: ISO 8601 string format: YYYY-MM-DDTHH:MM:SS.SSSZ or YYYY-MM-DDTHH:MM:SSZ depending on whether the value contains milliseconds.
- resource.accessKeyDetails.accessKeyId
- resource.accessKeyDetails.principalId
- resource.accessKeyDetails.userName
- resource.accessKeyDetails.userType
- resource.instanceDetails.iamInstanceProfile.id
- resource.instanceDetails.imageId
- resource.instanceDetails.instanceId
- resource.instanceDetails.tags.key
- resource.instanceDetails.tags.value
- resource.instanceDetails.networkInterfaces.ipv6Addresses
- resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress
- resource.instanceDetails.networkInterfaces.publicDnsName
- resource.instanceDetails.networkInterfaces.publicIp
- resource.instanceDetails.networkInterfaces.securityGroups.groupId
- resource.instanceDetails.networkInterfaces.securityGroups.groupName
- resource.instanceDetails.networkInterfaces.subnetId
- resource.instanceDetails.networkInterfaces.vpcId
- resource.instanceDetails.outpostArn
- resource.resourceType
- resource.s3BucketDetails.publicAccess.effectivePermissions
- resource.s3BucketDetails.name
- resource.s3BucketDetails.tags.key
- resource.s3BucketDetails.tags.value
- resource.s3BucketDetails.type
- service.action.actionType
- service.action.awsApiCallAction.api
- service.action.awsApiCallAction.callerType
- service.action.awsApiCallAction.errorCode
- service.action.awsApiCallAction.remoteIpDetails.city.cityName
- service.action.awsApiCallAction.remoteIpDetails.country.countryName
- service.action.awsApiCallAction.remoteIpDetails.ipAddressV4
- service.action.awsApiCallAction.remoteIpDetails.ipAddressV6
- service.action.awsApiCallAction.remoteIpDetails.organization.asn
- service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg
- service.action.awsApiCallAction.serviceName
- service.action.dnsRequestAction.domain
- service.action.dnsRequestAction.domainWithSuffix
- service.action.networkConnectionAction.blocked
- service.action.networkConnectionAction.connectionDirection
- service.action.networkConnectionAction.localPortDetails.port
- service.action.networkConnectionAction.protocol
- service.action.networkConnectionAction.remoteIpDetails.city.cityName
- service.action.networkConnectionAction.remoteIpDetails.country.countryName
- service.action.networkConnectionAction.remoteIpDetails.ipAddressV4
- service.action.networkConnectionAction.remoteIpDetails.ipAddressV6
- service.action.networkConnectionAction.remoteIpDetails.organization.asn
- service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg
- service.action.networkConnectionAction.remotePortDetails.port
- service.action.awsApiCallAction.remoteAccountDetails.affiliated
- service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV4
- service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV6
- service.action.kubernetesApiCallAction.namespace
- service.action.kubernetesApiCallAction.remoteIpDetails.organization.asn
- service.action.kubernetesApiCallAction.requestUri
- service.action.kubernetesApiCallAction.statusCode
- service.action.networkConnectionAction.localIpDetails.ipAddressV4
- service.action.networkConnectionAction.localIpDetails.ipAddressV6
- service.action.networkConnectionAction.protocol
- service.action.awsApiCallAction.serviceName
- service.action.awsApiCallAction.remoteAccountDetails.accountId
- service.additionalInfo.threatListName
- service.resourceRole
- resource.eksClusterDetails.name
- resource.kubernetesDetails.kubernetesWorkloadDetails.name
- resource.kubernetesDetails.kubernetesWorkloadDetails.namespace
- resource.kubernetesDetails.kubernetesUserDetails.username
- resource.kubernetesDetails.kubernetesWorkloadDetails.containers.image
- resource.kubernetesDetails.kubernetesWorkloadDetails.containers.imagePrefix
- service.ebsVolumeScanDetails.scanId
- service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.name
- service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.severity
- service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.hash
- resource.ecsClusterDetails.name
- resource.ecsClusterDetails.taskDetails.containers.image
- resource.ecsClusterDetails.taskDetails.definitionArn
- resource.containerDetails.image
- resource.rdsDbInstanceDetails.dbInstanceIdentifier
- resource.rdsDbInstanceDetails.dbClusterIdentifier
- resource.rdsDbInstanceDetails.engine
- resource.rdsDbUserDetails.user
- resource.rdsDbInstanceDetails.tags.key
- resource.rdsDbInstanceDetails.tags.value
- service.runtimeDetails.process.executableSha256
- service.runtimeDetails.process.name
- service.runtimeDetails.process.executablePath
- resource.lambdaDetails.functionName
- resource.lambdaDetails.functionArn
- resource.lambdaDetails.tags.key
- resource.lambdaDetails.tags.value

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

`--client-token` (string)

The idempotency token for the create request.

`--tags` (map)

The tags to be added to a new filter resource.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To create a new filter in the current region**

The following `create-filter` example creates a filter that matches all Portscan findings for instance created from a specific image. This does not suppress those findings.

```
aws guardduty create-filter \
    --detector-id b6b992d6d2f48e64bc59180bfexample \
    --name myFilterExample \
    --finding-criteria '{"Criterion": {"type": {"Eq": ["Recon:EC2/Portscan"]},"resource.instanceDetails.imageId": {"Eq": ["ami-0a7a207083example"]}}}'
```

Output:

```
{
    "Name": "myFilterExample"
}
```

For more information, see [Filtering GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html) in the *GuardDuty User Guide*.

**Example 2: To create a new filter and suppress findings in the current region**

The following `create-filter` example creates a filter that matches all Portscan findings for instance created from a specific image. This filter archives those findings so that they do not appear in your current findings.

```
aws guardduty create-filter \
    --detector-id b6b992d6d2f48e64bc59180bfexample \
    --action ARCHIVE \
    --name myFilterSecondExample \
    --finding-criteria '{"Criterion": {"type": {"Eq": ["Recon:EC2/Portscan"]},"resource.instanceDetails.imageId": {"Eq": ["ami-0a7a207083example"]}}}'
```

Output:

```
{
    "Name": "myFilterSecondExample"
}
```

For more information, see [Filtering GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html) in the *GuardDuty User Guide*.

## Output

Name -> (string)

The name of the successfully created filter.