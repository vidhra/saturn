# list-servicesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/list-services.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/list-services.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [application-signals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/index.html#cli-aws-application-signals) ]

# list-services

## Description

Returns a list of services that have been discovered by Application Signals. A service represents a minimum logical and transactional unit that completes a business function. Services are discovered through Application Signals instrumentation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/application-signals-2024-04-15/ListServices)

`list-services` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ServiceSummaries`

## Synopsis

```
list-services
--start-time <value>
--end-time <value>
[--include-linked-accounts | --no-include-linked-accounts]
[--aws-account-id <value>]
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

`--start-time` (timestamp)

The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`

Your requested start time will be rounded to the nearest hour.

`--end-time` (timestamp)

The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`

Your requested start time will be rounded to the nearest hour.

`--include-linked-accounts` | `--no-include-linked-accounts` (boolean)

If you are using this operation in a monitoring account, specify `true` to include services from source accounts in the returned data. `</p>`

`--aws-account-id` (string)

Amazon Web Services Account ID.

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

StartTime -> (timestamp)

The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`

This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.

EndTime -> (timestamp)

The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`

This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.

ServiceSummaries -> (list)

An array of structures, where each structure contains some information about a service. To get complete information about a service, use [GetService](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetService.html) .

(structure)

This structure contains information about one of your services that was discovered by Application Signals

KeyAttributes -> (map)

This is a string-to-string map that help identify the objects discovered by Application Signals. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

AttributeMaps -> (list)

This structure contains one or more string-to-string maps that help identify this service. It can include *platform attributes* , *application attributes* , and *telemetry attributes* .

Platform attributes contain information the serviceâs platform.

- `PlatformType` defines the hosted-in platform.
- `EKS.Cluster` is the name of the Amazon EKS cluster.
- `K8s.Cluster` is the name of the self-hosted Kubernetes cluster.
- `K8s.Namespace` is the name of the Kubernetes namespace in either Amazon EKS or Kubernetes clusters.
- `K8s.Workload` is the name of the Kubernetes workload in either Amazon EKS or Kubernetes clusters.
- `K8s.Node` is the name of the Kubernetes node in either Amazon EKS or Kubernetes clusters.
- `K8s.Pod` is the name of the Kubernetes pod in either Amazon EKS or Kubernetes clusters.
- `EC2.AutoScalingGroup` is the name of the Amazon EC2 Auto Scaling group.
- `EC2.InstanceId` is the ID of the Amazon EC2 instance.
- `Host` is the name of the host, for all platform types.

Application attributes contain information about the application.

- `AWS.Application` is the applicationâs name in Amazon Web Services Service Catalog AppRegistry.
- `AWS.Application.ARN` is the applicationâs ARN in Amazon Web Services Service Catalog AppRegistry.

Telemetry attributes contain telemetry information.

- `Telemetry.SDK` is the fingerprint of the OpenTelemetry SDK version for instrumented services.
- `Telemetry.Agent` is the fingerprint of the agent used to collect and send telemetry data.
- `Telemetry.Source` Specifies the point of application where the telemetry was collected or specifies what was used for the source of telemetry data.

(map)

key -> (string)

value -> (string)

MetricReferences -> (list)

An array of structures that each contain information about one metric associated with this service.

(structure)

This structure contains information about one CloudWatch metric associated with this entity discovered by Application Signals.

Namespace -> (string)

The namespace of the metric. For more information, see [CloudWatchNamespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricType -> (string)

Used to display the appropriate statistics in the CloudWatch console.

Dimensions -> (list)

An array of one or more dimensions that further define the metric. For more information, see [CloudWatchDimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

MetricName -> (string)

The name of the metric.

AccountId -> (string)

Amazon Web Services account ID.

NextToken -> (string)

Include this value in your next use of this API to get next set of services.