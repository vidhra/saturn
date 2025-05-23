# list-service-deploymentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-service-deployments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-service-deployments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# list-service-deployments

## Description

This operation lists all the service deployments that meet the specified filter criteria.

A service deployment happens when you release a software update for the service. You route traffic from the running service revisions to the new service revison and control the number of running tasks.

This API returns the values that you use for the request parameters in [DescribeServiceRevisions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListServiceDeployments)

## Synopsis

```
list-service-deployments
--service <value>
[--cluster <value>]
[--status <value>]
[--created-at <value>]
[--next-token <value>]
[--max-results <value>]
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

`--service` (string)

The ARN or name of the service

`--cluster` (string)

The cluster that hosts the service. This can either be the cluster name or ARN. Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. If you donât specify a cluster, `default` is used.

`--status` (list)

An optional filter you can use to narrow the results. If you do not specify a status, then all status values are included in the result.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  PENDING
  SUCCESSFUL
  STOPPED
  STOP_REQUESTED
  IN_PROGRESS
  ROLLBACK_REQUESTED
  ROLLBACK_IN_PROGRESS
  ROLLBACK_SUCCESSFUL
  ROLLBACK_FAILED
```

`--created-at` (structure)

An optional filter you can use to narrow the results by the service creation date. If you do not specify a value, the result includes all services created before the current time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

before -> (timestamp)

Include service deployments in the result that were created before this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

after -> (timestamp)

Include service deployments in the result that were created after this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

Shorthand Syntax:

```
before=timestamp,after=timestamp
```

JSON Syntax:

```
{
  "before": timestamp,
  "after": timestamp
}
```

`--next-token` (string)

The `nextToken` value returned from a `ListServiceDeployments` request indicating that more results are available to fulfill the request and further calls are needed. If you provided `maxResults` , itâs possible the number of results is fewer than `maxResults` .

`--max-results` (integer)

The maximum number of service deployment results that `ListServiceDeployments` returned in paginated output. When this parameter is used, `ListServiceDeployments` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListServiceDeployments` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isnât used, then `ListServiceDeployments` returns up to 20 results and a `nextToken` value if applicable.

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

**To list service deployments**

The following `list-service-deployments` example retrieves the service deployments for the service named `example-service`.

```
aws ecs list-service-deployments \
    --service arn:aws:ecs:us-east-1:123456789012:service/example-cluster/example-service
```

Output:

```
{
    "serviceDeployments": [
        {
            "serviceDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:service-deployment/example-cluster/example-service/ejGvqq2ilnbKT9qj0vLJe",
            "serviceArn": "arn:aws:ecs:us-east-1:123456789012:service/example-cluster/example-service",
            "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/example-cluster",
            "startedAt": "2024-10-31T08:03:32.510000-04:00",
            "createdAt": "2024-10-31T08:03:30.917000-04:00",
            "finishedAt": "2024-10-31T08:05:04.527000-04:00",
            "targetServiceRevisionArn": "arn:aws:ecs:us-east-1:123456789012:service-revision/example-cluster/example-service/1485800978477494678",
            "status": "SUCCESSFUL"
        }
    ]
}
```

For more information, see [View service history using Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html) in the *Amazon ECS Developer Guide*.

## Output

serviceDeployments -> (list)

An overview of the service deployment, including the following properties:

- The ARN of the service deployment.
- The ARN of the service being deployed.
- The ARN of the cluster that hosts the service in the service deployment.
- The time that the service deployment started.
- The time that the service deployment completed.
- The service deployment status.
- Information about why the service deployment is in the current state.
- The ARN of the service revision that is being deployed.

(structure)

The service deployment properties that are retured when you call `ListServiceDeployments` .

This provides a high-level overview of the service deployment.

serviceDeploymentArn -> (string)

The ARN of the service deployment.

serviceArn -> (string)

The ARN of the service for this service deployment.

clusterArn -> (string)

The ARN of the cluster that hosts the service.

startedAt -> (timestamp)

The time that the service deployment statred. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

createdAt -> (timestamp)

The time that the service deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

finishedAt -> (timestamp)

The time that the service deployment completed. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

targetServiceRevisionArn -> (string)

The ARN of the service revision being deplyed.

status -> (string)

The status of the service deployment

statusReason -> (string)

Information about why the service deployment is in the current status. For example, the circuit breaker detected a deployment failure.

nextToken -> (string)

The `nextToken` value to include in a future `ListServiceDeployments` request. When the results of a `ListServiceDeployments` request exceed `maxResults` , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.