# update-resource-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-readiness/update-resource-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-readiness/update-resource-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53-recovery-readiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-readiness/index.html#cli-aws-route53-recovery-readiness) ]

# update-resource-set

## Description

Updates a resource set.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-recovery-readiness-2019-12-02/UpdateResourceSet)

## Synopsis

```
update-resource-set
--resource-set-name <value>
--resource-set-type <value>
--resources <value>
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

`--resource-set-name` (string)

Name of a resource set.

`--resource-set-type` (string)

The resource type of the resources in the resource set. Enter one of the following values for resource type:

AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource

`--resources` (list)

A list of resource objects.

(structure)

The resource element of a resource set.

ComponentId -> (string)

The component identifier of the resource, generated when DNS target resource is used.

DnsTargetResource -> (structure)

The DNS target resource.

DomainName -> (string)

The domain name that acts as an ingress point to a portion of the customer application.

HostedZoneArn -> (string)

The hosted zone Amazon Resource Name (ARN) that contains the DNS record with the provided name of the target resource.

RecordSetId -> (string)

The Route 53 record set ID that uniquely identifies a DNS record, given a name and a type.

RecordType -> (string)

The type of DNS record of the target resource.

TargetResource -> (structure)

The target resource of the DNS target resource.

NLBResource -> (structure)

The Network Load Balancer Resource.

Arn -> (string)

The Network Load Balancer resource Amazon Resource Name (ARN).

R53Resource -> (structure)

The Route 53 resource.

DomainName -> (string)

The DNS target domain name.

RecordSetId -> (string)

The Route 53 Resource Record Set ID.

ReadinessScopes -> (list)

A list of recovery group Amazon Resource Names (ARNs) and cell ARNs that this resource is contained within.

(string)

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services resource.

JSON Syntax:

```
[
  {
    "ComponentId": "string",
    "DnsTargetResource": {
      "DomainName": "string",
      "HostedZoneArn": "string",
      "RecordSetId": "string",
      "RecordType": "string",
      "TargetResource": {
        "NLBResource": {
          "Arn": "string"
        },
        "R53Resource": {
          "DomainName": "string",
          "RecordSetId": "string"
        }
      }
    },
    "ReadinessScopes": ["string", ...],
    "ResourceArn": "string"
  }
  ...
]
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

## Output

ResourceSetArn -> (string)

The Amazon Resource Name (ARN) for the resource set.

ResourceSetName -> (string)

The name of the resource set.

ResourceSetType -> (string)

The resource type of the resources in the resource set. Enter one of the following values for resource type:

AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource

Resources -> (list)

A list of resource objects.

(structure)

The resource element of a resource set.

ComponentId -> (string)

The component identifier of the resource, generated when DNS target resource is used.

DnsTargetResource -> (structure)

The DNS target resource.

DomainName -> (string)

The domain name that acts as an ingress point to a portion of the customer application.

HostedZoneArn -> (string)

The hosted zone Amazon Resource Name (ARN) that contains the DNS record with the provided name of the target resource.

RecordSetId -> (string)

The Route 53 record set ID that uniquely identifies a DNS record, given a name and a type.

RecordType -> (string)

The type of DNS record of the target resource.

TargetResource -> (structure)

The target resource of the DNS target resource.

NLBResource -> (structure)

The Network Load Balancer Resource.

Arn -> (string)

The Network Load Balancer resource Amazon Resource Name (ARN).

R53Resource -> (structure)

The Route 53 resource.

DomainName -> (string)

The DNS target domain name.

RecordSetId -> (string)

The Route 53 Resource Record Set ID.

ReadinessScopes -> (list)

A list of recovery group Amazon Resource Names (ARNs) and cell ARNs that this resource is contained within.

(string)

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services resource.

Tags -> (map)

A collection of tags associated with a resource.

key -> (string)

value -> (string)