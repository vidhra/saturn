# list-managed-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/list-managed-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/list-managed-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [arc-zonal-shift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/index.html#cli-aws-arc-zonal-shift) ]

# list-managed-resources

## Description

Lists all the resources in your Amazon Web Services account in this Amazon Web Services Region that are managed for zonal shifts in Amazon Route 53 Application Recovery Controller, and information about them. The information includes the zonal autoshift status for the resource, as well as the Amazon Resource Name (ARN), the Availability Zones that each resource is deployed in, and the resource name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/arc-zonal-shift-2022-10-30/ListManagedResources)

`list-managed-resources` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
list-managed-resources
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

## Output

items -> (list)

The items in the response list.

(structure)

A complex structure for a managed resource in an Amazon Web Services account with information about zonal shifts and autoshifts.

A managed resource is a load balancer that has been registered with ARC by Elastic Load Balancing. You can start a zonal shift in ARC for a managed resource to temporarily move traffic for the resource away from an Availability Zone in an Amazon Web Services Region. You can also configure zonal autoshift for a managed resource.

### Note

At this time, managed resources are Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.

appliedWeights -> (map)

A collection of key-value pairs that indicate whether resources are active in Availability Zones or not. The key name is the Availability Zone where the resource is deployed. The value is 1 or 0.

key -> (string)

value -> (float)

arn -> (string)

The Amazon Resource Name (ARN) for the managed resource.

autoshifts -> (list)

An array of the autoshifts that have been completed for a resource.

(structure)

A complex structure that lists an autoshift that is currently active for a managed resource and information about the autoshift.

For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

appliedStatus -> (string)

The `appliedStatus` field specifies which application traffic shift is in effect for a resource when there is more than one active traffic shift. There can be more than one application traffic shift in progress at the same time - that is, practice run zonal shifts, customer-initiated zonal shifts, or an autoshift. The `appliedStatus` field for a shift that is in progress for a resource can have one of two values: `APPLIED` or `NOT_APPLIED` . The zonal shift or autoshift that is currently in effect for the resource has an `appliedStatus` set to `APPLIED` .

The overall principle for precedence is that zonal shifts that you start as a customer take precedence autoshifts, which take precedence over practice runs. That is, customer-initiated zonal shifts > autoshifts > practice run zonal shifts.

For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

awayFrom -> (string)

The Availability Zone (for example, `use1-az1` ) that traffic is shifted away from for a resource, when Amazon Web Services starts an autoshift. Until the autoshift ends, traffic for the resource is instead directed to other Availability Zones in the Amazon Web Services Region. An autoshift can end for a resource, for example, when Amazon Web Services ends the autoshift for the Availability Zone or when you disable zonal autoshift for the resource.

startTime -> (timestamp)

The time (UTC) when the autoshift started.

availabilityZones -> (list)

The Availability Zones that a resource is deployed in.

(string)

name -> (string)

The name of the managed resource.

practiceRunStatus -> (string)

This status tracks whether a practice run configuration exists for a resource. When you configure a practice run for a resource so that a practice run configuration exists, ARC sets this value to `ENABLED` . If a you have not configured a practice run for the resource, or delete a practice run configuration, ARC sets the value to `DISABLED` .

ARC updates this status; you canât set a practice run status to `ENABLED` or `DISABLED` .

zonalAutoshiftStatus -> (string)

The status of autoshift for a resource. When you configure zonal autoshift for a resource, you can set the value of the status to `ENABLED` or `DISABLED` .

zonalShifts -> (list)

An array of the zonal shifts for a resource.

(structure)

A complex structure that lists the zonal shifts for a managed resource and their statuses for the resource.

appliedStatus -> (string)

The `appliedStatus` field specifies which application traffic shift is in effect for a resource when there is more than one active traffic shift. There can be more than one application traffic shift in progress at the same time - that is, practice run zonal shifts, customer-initiated zonal shifts, or an autoshift. The `appliedStatus` field for a shift that is in progress for a resource can have one of two values: `APPLIED` or `NOT_APPLIED` . The zonal shift or autoshift that is currently in effect for the resource has an `appliedStatus` set to `APPLIED` .

The overall principle for precedence is that zonal shifts that you start as a customer take precedence autoshifts, which take precedence over practice runs. That is, customer-initiated zonal shifts > autoshifts > practice run zonal shifts.

For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

awayFrom -> (string)

The Availability Zone (for example, `use1-az1` ) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the Amazon Web Services Region.

comment -> (string)

A comment that you enter for a customer-initiated zonal shift. Only the latest comment is retained; no comment history is maintained. That is, a new comment overwrites any existing comment string.

expiryTime -> (timestamp)

The expiry time (expiration time) for a customer-initiated zonal shift. A zonal shift is temporary and must be set to expire when you start the zonal shift. You can initially set a zonal shift to expire in a maximum of three days (72 hours). However, you can update a zonal shift to set a new expiration at any time.

When you start a zonal shift, you specify how long you want it to be active, which ARC converts to an expiry time (expiration time). You can cancel a zonal shift when youâre ready to restore traffic to the Availability Zone, or just wait for it to expire. Or you can update the zonal shift to specify another length of time to expire in.

practiceRunOutcome -> (string)

The outcome, or end state, returned for a practice run. The following values can be returned:

- **PENDING:** Outcome value when a practice run is in progress.
- **SUCCEEDED:** Outcome value when the outcome alarm specified for the practice run configuration does not go into an `ALARM` state during the practice run, and the practice run was not interrupted before it completed the expected 30 minute zonal shift.
- **INTERRUPTED:** Outcome value when the practice run was stopped before the expected 30 minute zonal shift duration, or there was another problem with the practice run that created an inconclusive outcome.
- **FAILED:** Outcome value when the outcome alarm specified for the practice run configuration goes into an `ALARM` state during the practice run, and the practice run was not interrupted before it completed.

For more information about practice run outcomes, see [Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.configure.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

resourceIdentifier -> (string)

The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.

At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.

shiftType -> (string)

Defines the zonal shift type.

startTime -> (timestamp)

The time (UTC) when the zonal shift starts.

zonalShiftId -> (string)

The identifier of a zonal shift.

nextToken -> (string)

Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous callâs `nextToken` response to request the next page of results.