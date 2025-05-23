# describe-scaling-policiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-scaling-policies.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-scaling-policies.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# describe-scaling-policies

## Description

Retrieves all scaling policies applied to a fleet.

To get a fleetâs scaling policies, specify the fleet ID. You can filter this request by policy status, such as to retrieve only active scaling policies. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, set of `ScalingPolicy` objects is returned for the fleet.

A fleet may have all of its scaling policies suspended. This operation does not affect the status of the scaling policies, which remains ACTIVE.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeScalingPolicies)

`describe-scaling-policies` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ScalingPolicies`

## Synopsis

```
describe-scaling-policies
--fleet-id <value>
[--status-filter <value>]
[--location <value>]
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

`--fleet-id` (string)

A unique identifier for the fleet for which to retrieve scaling policies. You can use either the fleet ID or ARN value.

`--status-filter` (string)

Scaling policy status to filter results on. A scaling policy is only in force when in an `ACTIVE` status.

- **ACTIVE** â The scaling policy is currently in force.
- **UPDATEREQUESTED** â A request to update the scaling policy has been received.
- **UPDATING** â A change is being made to the scaling policy.
- **DELETEREQUESTED** â A request to delete the scaling policy has been received.
- **DELETING** â The scaling policy is being deleted.
- **DELETED** â The scaling policy has been deleted.
- **ERROR** â An error occurred in creating the policy. It should be removed and recreated.

Possible values:

- `ACTIVE`
- `UPDATE_REQUESTED`
- `UPDATING`
- `DELETE_REQUESTED`
- `DELETING`
- `DELETED`
- `ERROR`

`--location` (string)

The fleet location. If you donât specify this value, the response contains the scaling policies of every location in the fleet.

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

ScalingPolicies -> (list)

A collection of objects containing the scaling policies matching the request.

(structure)

Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.

FleetId -> (string)

A unique identifier for the fleet that is associated with this scaling policy.

FleetArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` .

Name -> (string)

A descriptive label that is associated with a fleetâs scaling policy. Policy names do not need to be unique.

Status -> (string)

Current status of the scaling policy. The scaling policy can be in force only when in an `ACTIVE` status. Scaling policies can be suspended for individual fleets. If the policy is suspended for a fleet, the policy status does not change.

- **ACTIVE** â The scaling policy can be used for auto-scaling a fleet.
- **UPDATE_REQUESTED** â A request to update the scaling policy has been received.
- **UPDATING** â A change is being made to the scaling policy.
- **DELETE_REQUESTED** â A request to delete the scaling policy has been received.
- **DELETING** â The scaling policy is being deleted.
- **DELETED** â The scaling policy has been deleted.
- **ERROR** â An error occurred in creating the policy. It should be removed and recreated.

ScalingAdjustment -> (integer)

Amount of adjustment to make, based on the scaling adjustment type.

ScalingAdjustmentType -> (string)

The type of adjustment to make to a fleetâs instance count.

- **ChangeInCapacity** â add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
- **ExactCapacity** â set the instance count to the scaling adjustment value.
- **PercentChangeInCapacity** â increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.

ComparisonOperator -> (string)

Comparison operator to use when measuring a metric against the threshold value.

Threshold -> (double)

Metric value used to trigger a scaling event.

EvaluationPeriods -> (integer)

Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.

MetricName -> (string)

Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see [Monitor Amazon GameLift with Amazon CloudWatch](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html) .

- **ActivatingGameSessions** â Game sessions in the process of being created.
- **ActiveGameSessions** â Game sessions that are currently running.
- **ActiveInstances** â Fleet instances that are currently running at least one game session.
- **AvailableGameSessions** â Additional game sessions that fleet could host simultaneously, given current capacity.
- **AvailablePlayerSessions** â Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
- **CurrentPlayerSessions** â Player slots in active game sessions that are being used by a player or are reserved for a player.
- **IdleInstances** â Active instances that are currently hosting zero game sessions.
- **PercentAvailableGameSessions** â Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
- **PercentIdleInstances** â Percentage of the total number of active instances that are hosting zero game sessions.
- **QueueDepth** â Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
- **WaitTime** â Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.

PolicyType -> (string)

The type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to âPercentAvailableGameSessionsâ and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

TargetConfiguration -> (structure)

An object that contains settings for a target-based scaling policy.

TargetValue -> (double)

Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleetâs buffer (the percent of capacity that should be idle and ready for new game sessions).

UpdateStatus -> (string)

The current status of the fleetâs scaling policies in a requested fleet location. The status `PENDING_UPDATE` indicates that an update was requested for the fleet but has not yet been completed for the location.

Location -> (string)

The fleet location.

NextToken -> (string)

A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.