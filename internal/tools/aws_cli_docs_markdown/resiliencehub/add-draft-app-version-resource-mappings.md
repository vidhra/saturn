# add-draft-app-version-resource-mappingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/add-draft-app-version-resource-mappings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/add-draft-app-version-resource-mappings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# add-draft-app-version-resource-mappings

## Description

Adds the source of resource-maps to the draft version of an application. During assessment, Resilience Hub will use these resource-maps to resolve the latest physical ID for each resource in the application template. For more information about different types of resources supported by Resilience Hub and how to add them in your application, see [Step 2: How is your application managed?](https://docs.aws.amazon.com/resilience-hub/latest/userguide/how-app-manage.html) in the Resilience Hub User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)

## Synopsis

```
add-draft-app-version-resource-mappings
--app-arn <value>
--resource-mappings <value>
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

`--app-arn` (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

`--resource-mappings` (list)

Mappings used to map logical resources from the template to physical resources. You can use the mapping type `CFN_STACK` if the application template uses a logical stack name. Or you can map individual resources by using the mapping type `RESOURCE` . We recommend using the mapping type `CFN_STACK` if the application is backed by a CloudFormation stack.

(structure)

Defines a resource mapping.

appRegistryAppName -> (string)

Name of the application this resource is mapped to when the `mappingType` is `AppRegistryApp` .

eksSourceName -> (string)

Name of the Amazon Elastic Kubernetes Service cluster and namespace that this resource is mapped to when the `mappingType` is `EKS` .

### Note

This parameter accepts values in âeks-cluster/namespaceâ format.

logicalStackName -> (string)

Name of the CloudFormation stack this resource is mapped to when the `mappingType` is `CfnStack` .

mappingType -> (string)

Specifies the type of resource mapping.

physicalResourceId -> (structure)

Identifier of the physical resource.

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

resourceGroupName -> (string)

Name of the Resource Groups that this resource is mapped to when the `mappingType` is `ResourceGroup` .

resourceName -> (string)

Name of the resource that this resource is mapped to when the `mappingType` is `Resource` .

terraformSourceName -> (string)

Name of the Terraform source that this resource is mapped to when the `mappingType` is `Terraform` .

Shorthand Syntax:

```
appRegistryAppName=string,eksSourceName=string,logicalStackName=string,mappingType=string,physicalResourceId={awsAccountId=string,awsRegion=string,identifier=string,type=string},resourceGroupName=string,resourceName=string,terraformSourceName=string ...
```

JSON Syntax:

```
[
  {
    "appRegistryAppName": "string",
    "eksSourceName": "string",
    "logicalStackName": "string",
    "mappingType": "CfnStack"|"Resource"|"AppRegistryApp"|"ResourceGroup"|"Terraform"|"EKS",
    "physicalResourceId": {
      "awsAccountId": "string",
      "awsRegion": "string",
      "identifier": "string",
      "type": "Arn"|"Native"
    },
    "resourceGroupName": "string",
    "resourceName": "string",
    "terraformSourceName": "string"
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

appArn -> (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

appVersion -> (string)

The version of the application.

resourceMappings -> (list)

List of sources that are used to map a logical resource from the template to a physical resource. You can use sources such as CloudFormation, Terraform state files, AppRegistry applications, or Amazon EKS.

(structure)

Defines a resource mapping.

appRegistryAppName -> (string)

Name of the application this resource is mapped to when the `mappingType` is `AppRegistryApp` .

eksSourceName -> (string)

Name of the Amazon Elastic Kubernetes Service cluster and namespace that this resource is mapped to when the `mappingType` is `EKS` .

### Note

This parameter accepts values in âeks-cluster/namespaceâ format.

logicalStackName -> (string)

Name of the CloudFormation stack this resource is mapped to when the `mappingType` is `CfnStack` .

mappingType -> (string)

Specifies the type of resource mapping.

physicalResourceId -> (structure)

Identifier of the physical resource.

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

resourceGroupName -> (string)

Name of the Resource Groups that this resource is mapped to when the `mappingType` is `ResourceGroup` .

resourceName -> (string)

Name of the resource that this resource is mapped to when the `mappingType` is `Resource` .

terraformSourceName -> (string)

Name of the Terraform source that this resource is mapped to when the `mappingType` is `Terraform` .