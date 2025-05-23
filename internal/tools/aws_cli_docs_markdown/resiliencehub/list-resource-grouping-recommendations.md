# list-resource-grouping-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-resource-grouping-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-resource-grouping-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# list-resource-grouping-recommendations

## Description

Lists the resource grouping recommendations suggested by Resilience Hub for your application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/ListResourceGroupingRecommendations)

`list-resource-grouping-recommendations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `groupingRecommendations`

## Synopsis

```
list-resource-grouping-recommendations
[--app-arn <value>]
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

`--app-arn` (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

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

groupingRecommendations -> (list)

List of resource grouping recommendations generated by Resilience Hub.

(structure)

Creates a new grouping recommendation.

confidenceLevel -> (string)

Indicates the confidence level of Resilience Hub on the grouping recommendation.

creationTime -> (timestamp)

Indicates the creation time of the grouping recommendation.

groupingAppComponent -> (structure)

Indicates the name of the recommended Application Component (AppComponent).

appComponentId -> (string)

Indicates the identifier of an AppComponent.

appComponentName -> (string)

Indicates the name of an AppComponent.

appComponentType -> (string)

Indicates the type of an AppComponent.

groupingRecommendationId -> (string)

Indicates all the reasons available for rejecting a grouping recommendation.

recommendationReasons -> (list)

Indicates all the reasons available for rejecting a grouping recommendation.

(string)

rejectionReason -> (string)

Indicates the reason you had selected while rejecting a grouping recommendation.

resources -> (list)

Indicates the resources that are grouped in a recommended AppComponent.

(structure)

Indicates the resource that will be grouped in the recommended Application Component (AppComponent).

logicalResourceId -> (structure)

Indicates the logical identifier of the resource.

eksSourceName -> (string)

Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.

### Note

This parameter accepts values in âeks-cluster/namespaceâ format.

identifier -> (string)

Identifier of the resource.

logicalStackName -> (string)

The name of the CloudFormation stack this resource belongs to.

resourceGroupName -> (string)

The name of the resource group that this resource belongs to.

terraformSourceName -> (string)

The name of the Terraform S3 state file this resource belongs to.

physicalResourceId -> (structure)

Indicates the physical identifier of the resource.

awsAccountId -> (string)

The Amazon Web Services account that owns the physical resource.

awsRegion -> (string)

The Amazon Web Services Region that the physical resource is located in.

identifier -> (string)

Identifier of the physical resource.

type -> (string)

Specifies the type of physical resource identifier.

Arn

The resource identifier is an Amazon Resource Name (ARN) and it can identify the following list of resources:

- `AWS::ECS::Service`
- `AWS::EFS::FileSystem`
- `AWS::ElasticLoadBalancingV2::LoadBalancer`
- `AWS::Lambda::Function`
- `AWS::SNS::Topic`

Native

The resource identifier is an Resilience Hub-native identifier and it can identify the following list of resources:

- `AWS::ApiGateway::RestApi`
- `AWS::ApiGatewayV2::Api`
- `AWS::AutoScaling::AutoScalingGroup`
- `AWS::DocDB::DBCluster`
- `AWS::DocDB::DBGlobalCluster`
- `AWS::DocDB::DBInstance`
- `AWS::DynamoDB::GlobalTable`
- `AWS::DynamoDB::Table`
- `AWS::EC2::EC2Fleet`
- `AWS::EC2::Instance`
- `AWS::EC2::NatGateway`
- `AWS::EC2::Volume`
- `AWS::ElasticLoadBalancing::LoadBalancer`
- `AWS::RDS::DBCluster`
- `AWS::RDS::DBInstance`
- `AWS::RDS::GlobalCluster`
- `AWS::Route53::RecordSet`
- `AWS::S3::Bucket`
- `AWS::SQS::Queue`

resourceName -> (string)

Indicates the resource name.

resourceType -> (string)

Indicates the resource type.

sourceAppComponentIds -> (list)

Indicates the identifier of the source AppComponents in which the resources were previously grouped into.

(string)

score -> (double)

Indicates the confidence level of the grouping recommendation.

status -> (string)

Indicates the status of grouping resources into AppComponents.

nextToken -> (string)

Null, or the token from a previous call to get the next set of results.