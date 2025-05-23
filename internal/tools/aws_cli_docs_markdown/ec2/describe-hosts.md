# describe-hostsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-hosts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-hosts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-hosts

## Description

Describes the specified Dedicated Hosts or all your Dedicated Hosts.

The results describe only the Dedicated Hosts in the Region youâre currently using. All listed instances consume capacity on your Dedicated Host. Dedicated Hosts that have recently been released are listed with the state `released` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeHosts)

`describe-hosts` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Hosts`

## Synopsis

```
describe-hosts
[--host-ids <value>]
[--filter <value>]
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

`--host-ids` (list)

The IDs of the Dedicated Hosts. The IDs are used for targeted instance launches.

(string)

Syntax:

```
"string" "string" ...
```

`--filter` (list)

The filters.

- `auto-placement` - Whether auto-placement is enabled or disabled (`on` | `off` ).
- `availability-zone` - The Availability Zone of the host.
- `client-token` - The idempotency token that you provided when you allocated the host.
- `host-reservation-id` - The ID of the reservation assigned to this host.
- `instance-type` - The instance type size that the Dedicated Host is configured to support.
- `state` - The allocation state of the Dedicated Host (`available` | `under-assessment` | `permanent-failure` | `released` | `released-permanent-failure` ).
- `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

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

**To view details about Dedicated Hosts**

The following `describe-hosts` example displays details for the `available` Dedicated Hosts in your AWS account.

```
aws ec2 describe-hosts --filter "Name=state,Values=available"
```

Output:

```
{
    "Hosts": [
        {
            "HostId": "h-07879acf49EXAMPLE",
            "Tags": [
                {
                    "Value": "production",
                    "Key": "purpose"
                }
            ],
            "HostProperties": {
                "Cores": 48,
                "TotalVCpus": 96,
                "InstanceType": "m5.large",
                "Sockets": 2
            },
            "Instances": [],
            "State": "available",
            "AvailabilityZone": "eu-west-1a",
            "AvailableCapacity": {
                "AvailableInstanceCapacity": [
                    {
                        "AvailableCapacity": 48,
                        "InstanceType": "m5.large",
                        "TotalCapacity": 48
                    }
                ],
                "AvailableVCpus": 96
            },
            "HostRecovery": "on",
            "AllocationTime": "2019-08-19T08:57:44.000Z",
            "AutoPlacement": "off"
        }
    ]
}
```

For more information, see [Viewing Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-managing) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.

## Output

Hosts -> (list)

Information about the Dedicated Hosts.

(structure)

Describes the properties of the Dedicated Host.

AutoPlacement -> (string)

Whether auto-placement is on or off.

AvailabilityZone -> (string)

The Availability Zone of the Dedicated Host.

AvailableCapacity -> (structure)

Information about the instances running on the Dedicated Host.

AvailableInstanceCapacity -> (list)

The number of instances that can be launched onto the Dedicated Host depending on the hostâs available capacity. For Dedicated Hosts that support multiple instance types, this parameter represents the number of instances for each instance size that is supported on the host.

(structure)

Information about the number of instances that can be launched onto the Dedicated Host.

AvailableCapacity -> (integer)

The number of instances that can be launched onto the Dedicated Host based on the hostâs available capacity.

InstanceType -> (string)

The instance type supported by the Dedicated Host.

TotalCapacity -> (integer)

The total number of instances that can be launched onto the Dedicated Host if there are no instances running on it.

AvailableVCpus -> (integer)

The number of vCPUs available for launching instances onto the Dedicated Host.

ClientToken -> (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

HostId -> (string)

The ID of the Dedicated Host.

HostProperties -> (structure)

The hardware specifications of the Dedicated Host.

Cores -> (integer)

The number of cores on the Dedicated Host.

InstanceType -> (string)

The instance type supported by the Dedicated Host. For example, `m5.large` . If the host supports multiple instance types, no **instanceType** is returned.

InstanceFamily -> (string)

The instance family supported by the Dedicated Host. For example, `m5` .

Sockets -> (integer)

The number of sockets on the Dedicated Host.

TotalVCpus -> (integer)

The total number of vCPUs on the Dedicated Host.

HostReservationId -> (string)

The reservation ID of the Dedicated Host. This returns a `null` response if the Dedicated Host doesnât have an associated reservation.

Instances -> (list)

The IDs and instance type that are currently running on the Dedicated Host.

(structure)

Describes an instance running on a Dedicated Host.

InstanceId -> (string)

The ID of instance that is running on the Dedicated Host.

InstanceType -> (string)

The instance type (for example, `m3.medium` ) of the running instance.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the instance.

State -> (string)

The Dedicated Hostâs state.

AllocationTime -> (timestamp)

The time that the Dedicated Host was allocated.

ReleaseTime -> (timestamp)

The time that the Dedicated Host was released.

Tags -> (list)

Any tags assigned to the Dedicated Host.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

HostRecovery -> (string)

Indicates whether host recovery is enabled or disabled for the Dedicated Host.

AllowsMultipleInstanceTypes -> (string)

Indicates whether the Dedicated Host supports multiple instance types of the same instance family. If the value is `on` , the Dedicated Host supports multiple instance types in the instance family. If the value is `off` , the Dedicated Host supports a single instance type only.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the Dedicated Host.

AvailabilityZoneId -> (string)

The ID of the Availability Zone in which the Dedicated Host is allocated.

MemberOfServiceLinkedResourceGroup -> (boolean)

Indicates whether the Dedicated Host is in a host resource group. If **memberOfServiceLinkedResourceGroup** is `true` , the host is in a host resource group; otherwise, it is not.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which the Dedicated Host is allocated.

HostMaintenance -> (string)

Indicates whether host maintenance is enabled or disabled for the Dedicated Host.

AssetId -> (string)

The ID of the Outpost hardware asset on which the Dedicated Host is allocated.

NextToken -> (string)

The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.