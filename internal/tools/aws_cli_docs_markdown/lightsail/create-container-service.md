# create-container-serviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-container-service.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-container-service.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# create-container-service

## Description

Creates an Amazon Lightsail container service.

A Lightsail container service is a compute resource to which you can deploy containers. For more information, see [Container services in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-services) in the *Lightsail Dev Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateContainerService)

## Synopsis

```
create-container-service
--service-name <value>
--power <value>
--scale <value>
[--tags <value>]
[--public-domain-names <value>]
[--deployment <value>]
[--private-registry-access <value>]
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

`--service-name` (string)

The name for the container service.

The name that you specify for your container service will make up part of its default domain. The default domain of a container service is typically `https://<ServiceName>.<RandomGUID>.<AWSRegion>.cs.amazonlightsail.com` . If the name of your container service is `container-service-1` , and itâs located in the US East (Ohio) Amazon Web Services Region (`us-east-2` ), then the domain for your container service will be like the following example: `https://container-service-1.ur4EXAMPLE2uq.us-east-2.cs.amazonlightsail.com`

The following are the requirements for container service names:

- Must be unique within each Amazon Web Services Region in your Lightsail account.
- Must contain 1 to 63 characters.
- Must contain only alphanumeric characters and hyphens.
- A hyphen (-) can separate words but cannot be at the start or end of the name.

`--power` (string)

The power specification for the container service.

The power specifies the amount of memory, vCPUs, and base monthly cost of each node of the container service. The `power` and `scale` of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the `power` with the `scale` (the number of nodes) of the service.

Use the `GetContainerServicePowers` action to get a list of power options that you can specify using this parameter, and their base monthly cost.

Possible values:

- `nano`
- `micro`
- `small`
- `medium`
- `large`
- `xlarge`

`--scale` (integer)

The scale specification for the container service.

The scale specifies the allocated compute nodes of the container service. The `power` and `scale` of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the `power` with the `scale` (the number of nodes) of the service.

`--tags` (list)

The tag keys and optional values to add to the container service during create.

Use the `TagResource` action to tag a resource after itâs created.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--public-domain-names` (map)

The public domain names to use with the container service, such as `example.com` and `www.example.com` .

You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.

If you donât specify public domain names, then you can use the default domain of the container service.

### Warning

You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the `CreateCertificate` action to create a certificate for the public domain names you want to use with your container service.

You can specify public domain names using a string to array map as shown in the example later on this page.

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
  ...}
```

`--deployment` (structure)

An object that describes a deployment for the container service.

A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, the environment variables to apply, and the launch command to run. It also specifies the container that will serve as the public endpoint of the deployment and its settings, such as the HTTP or HTTPS port to use, and the health check configuration.

containers -> (map)

An object that describes the configuration for the containers of the deployment.

key -> (string)

value -> (structure)

Describes the settings of a container that will be launched, or that is launched, to an Amazon Lightsail container service.

image -> (string)

The name of the image used for the container.

Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (`:` ). For example, if your container service name is `container-service-1` , the container image label is `mystaticsite` , and you want to use the third (`3` ) version of the registered container image, then you should specify `:container-service-1.mystaticsite.3` . To use the latest version of a container image, specify `latest` instead of a version number (for example, `:container-service-1.mystaticsite.latest` ). Lightsail will automatically use the highest numbered version of the registered container image.

Container images sourced from a public registry like Docker Hub donât start with a colon. For example, `nginx:latest` or `nginx` .

command -> (list)

The launch command for the container.

(string)

environment -> (map)

The environment variables of the container.

key -> (string)

value -> (string)

ports -> (map)

The open firewall ports of the container.

key -> (string)

value -> (string)

publicEndpoint -> (structure)

An object that describes the endpoint of the deployment.

containerName -> (string)

The name of the container for the endpoint.

containerPort -> (integer)

The port of the container to which traffic is forwarded to.

healthCheck -> (structure)

An object that describes the health check configuration of the container.

healthyThreshold -> (integer)

The number of consecutive health checks successes required before moving the container to the `Healthy` state. The default value is `2` .

unhealthyThreshold -> (integer)

The number of consecutive health check failures required before moving the container to the `Unhealthy` state. The default value is `2` .

timeoutSeconds -> (integer)

The amount of time, in seconds, during which no response means a failed health check. You can specify between 2 and 60 seconds. The default value is `2` .

intervalSeconds -> (integer)

The approximate interval, in seconds, between health checks of an individual container. You can specify between 5 and 300 seconds. The default value is `5` .

path -> (string)

The path on the container on which to perform the health check. The default value is `/` .

successCodes -> (string)

The HTTP codes to use when checking for a successful response from a container. You can specify values between `200` and `499` . You can specify multiple values (for example, `200,202` ) or a range of values (for example, `200-299` ).

Shorthand Syntax:

```
containers={KeyName1={image=string,command=[string,string],environment={KeyName1=string,KeyName2=string},ports={KeyName1=string,KeyName2=string}},KeyName2={image=string,command=[string,string],environment={KeyName1=string,KeyName2=string},ports={KeyName1=string,KeyName2=string}}},publicEndpoint={containerName=string,containerPort=integer,healthCheck={healthyThreshold=integer,unhealthyThreshold=integer,timeoutSeconds=integer,intervalSeconds=integer,path=string,successCodes=string}}
```

JSON Syntax:

```
{
  "containers": {"string": {
        "image": "string",
        "command": ["string", ...],
        "environment": {"string": "string"
          ...},
        "ports": {"string": "HTTP"|"HTTPS"|"TCP"|"UDP"
          ...}
      }
    ...},
  "publicEndpoint": {
    "containerName": "string",
    "containerPort": integer,
    "healthCheck": {
      "healthyThreshold": integer,
      "unhealthyThreshold": integer,
      "timeoutSeconds": integer,
      "intervalSeconds": integer,
      "path": "string",
      "successCodes": "string"
    }
  }
}
```

`--private-registry-access` (structure)

An object to describe the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.

For more information, see [Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access) in the *Amazon Lightsail Developer Guide* .

ecrImagePullerRole -> (structure)

An object to describe a request to activate or deactivate the role that you can use to grant an Amazon Lightsail container service access to Amazon Elastic Container Registry (Amazon ECR) private repositories.

isActive -> (boolean)

A Boolean value that indicates whether to activate the role.

Shorthand Syntax:

```
ecrImagePullerRole={isActive=boolean}
```

JSON Syntax:

```
{
  "ecrImagePullerRole": {
    "isActive": true|false
  }
}
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

containerService -> (structure)

An object that describes a container service.

containerServiceName -> (string)

The name of the container service.

arn -> (string)

The Amazon Resource Name (ARN) of the container service.

createdAt -> (timestamp)

The timestamp when the container service was created.

location -> (structure)

An object that describes the location of the container service, such as the Amazon Web Services Region and Availability Zone.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The Lightsail resource type of the container service.

tags -> (list)

The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

power -> (string)

The power specification of the container service.

The power specifies the amount of RAM, the number of vCPUs, and the base price of the container service.

powerId -> (string)

The ID of the power of the container service.

state -> (string)

The current state of the container service.

The following container service states are possible:

- `PENDING` - The container service is being created.
- `READY` - The container service is running but it does not have an active container deployment.
- `DEPLOYING` - The container service is launching a container deployment.
- `RUNNING` - The container service is running and it has an active container deployment.
- `UPDATING` - The container service capacity or its custom domains are being updated.
- `DELETING` - The container service is being deleted.
- `DISABLED` - The container service is disabled, and its active deployment and containers, if any, are shut down.

stateDetail -> (structure)

An object that describes the current state of the container service.

### Note

The state detail is populated only when a container service is in a `PENDING` , `DEPLOYING` , or `UPDATING` state.

code -> (string)

The state code of the container service.

The following state codes are possible:

- The following state codes are possible if your container service is in a `DEPLOYING` or `UPDATING` state:
- `CREATING_SYSTEM_RESOURCES` - The system resources for your container service are being created.
- `CREATING_NETWORK_INFRASTRUCTURE` - The network infrastructure for your container service are being created.
- `PROVISIONING_CERTIFICATE` - The SSL/TLS certificate for your container service is being created.
- `PROVISIONING_SERVICE` - Your container service is being provisioned.
- `CREATING_DEPLOYMENT` - Your deployment is being created on your container service.
- `EVALUATING_HEALTH_CHECK` - The health of your deployment is being evaluated.
- `ACTIVATING_DEPLOYMENT` - Your deployment is being activated.
- The following state codes are possible if your container service is in a `PENDING` state:
- `CERTIFICATE_LIMIT_EXCEEDED` - The SSL/TLS certificate required for your container service exceeds the maximum number of certificates allowed for your account.
- `UNKNOWN_ERROR` - An error was experienced when your container service was being created.

message -> (string)

A message that provides more information for the state code.

### Note

The state detail is populated only when a container service is in a `PENDING` , `DEPLOYING` , or `UPDATING` state.

scale -> (integer)

The scale specification of the container service.

The scale specifies the allocated compute nodes of the container service.

currentDeployment -> (structure)

An object that describes the current container deployment of the container service.

version -> (integer)

The version number of the deployment.

state -> (string)

The state of the deployment.

A deployment can be in one of the following states:

- `ACTIVATING` - The deployment is being created.
- `ACTIVE` - The deployment was successfully created, and itâs currently running on the container service. The container service can have only one deployment in an active state at a time.
- `INACTIVE` - The deployment was previously successfully created, but it is not currently running on the container service.
- `FAILED` - The deployment failed. Use the `GetContainerLog` action to view the log events for the containers in the deployment to try to determine the reason for the failure.

containers -> (map)

An object that describes the configuration for the containers of the deployment.

key -> (string)

value -> (structure)

Describes the settings of a container that will be launched, or that is launched, to an Amazon Lightsail container service.

image -> (string)

The name of the image used for the container.

Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (`:` ). For example, if your container service name is `container-service-1` , the container image label is `mystaticsite` , and you want to use the third (`3` ) version of the registered container image, then you should specify `:container-service-1.mystaticsite.3` . To use the latest version of a container image, specify `latest` instead of a version number (for example, `:container-service-1.mystaticsite.latest` ). Lightsail will automatically use the highest numbered version of the registered container image.

Container images sourced from a public registry like Docker Hub donât start with a colon. For example, `nginx:latest` or `nginx` .

command -> (list)

The launch command for the container.

(string)

environment -> (map)

The environment variables of the container.

key -> (string)

value -> (string)

ports -> (map)

The open firewall ports of the container.

key -> (string)

value -> (string)

publicEndpoint -> (structure)

An object that describes the endpoint of the deployment.

containerName -> (string)

The name of the container entry of the deployment that the endpoint configuration applies to.

containerPort -> (integer)

The port of the specified container to which traffic is forwarded to.

healthCheck -> (structure)

An object that describes the health check configuration of the container.

healthyThreshold -> (integer)

The number of consecutive health checks successes required before moving the container to the `Healthy` state. The default value is `2` .

unhealthyThreshold -> (integer)

The number of consecutive health check failures required before moving the container to the `Unhealthy` state. The default value is `2` .

timeoutSeconds -> (integer)

The amount of time, in seconds, during which no response means a failed health check. You can specify between 2 and 60 seconds. The default value is `2` .

intervalSeconds -> (integer)

The approximate interval, in seconds, between health checks of an individual container. You can specify between 5 and 300 seconds. The default value is `5` .

path -> (string)

The path on the container on which to perform the health check. The default value is `/` .

successCodes -> (string)

The HTTP codes to use when checking for a successful response from a container. You can specify values between `200` and `499` . You can specify multiple values (for example, `200,202` ) or a range of values (for example, `200-299` ).

createdAt -> (timestamp)

The timestamp when the deployment was created.

nextDeployment -> (structure)

An object that describes the next deployment of the container service.

This value is `null` when there is no deployment in a `pending` state.

version -> (integer)

The version number of the deployment.

state -> (string)

The state of the deployment.

A deployment can be in one of the following states:

- `ACTIVATING` - The deployment is being created.
- `ACTIVE` - The deployment was successfully created, and itâs currently running on the container service. The container service can have only one deployment in an active state at a time.
- `INACTIVE` - The deployment was previously successfully created, but it is not currently running on the container service.
- `FAILED` - The deployment failed. Use the `GetContainerLog` action to view the log events for the containers in the deployment to try to determine the reason for the failure.

containers -> (map)

An object that describes the configuration for the containers of the deployment.

key -> (string)

value -> (structure)

Describes the settings of a container that will be launched, or that is launched, to an Amazon Lightsail container service.

image -> (string)

The name of the image used for the container.

Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (`:` ). For example, if your container service name is `container-service-1` , the container image label is `mystaticsite` , and you want to use the third (`3` ) version of the registered container image, then you should specify `:container-service-1.mystaticsite.3` . To use the latest version of a container image, specify `latest` instead of a version number (for example, `:container-service-1.mystaticsite.latest` ). Lightsail will automatically use the highest numbered version of the registered container image.

Container images sourced from a public registry like Docker Hub donât start with a colon. For example, `nginx:latest` or `nginx` .

command -> (list)

The launch command for the container.

(string)

environment -> (map)

The environment variables of the container.

key -> (string)

value -> (string)

ports -> (map)

The open firewall ports of the container.

key -> (string)

value -> (string)

publicEndpoint -> (structure)

An object that describes the endpoint of the deployment.

containerName -> (string)

The name of the container entry of the deployment that the endpoint configuration applies to.

containerPort -> (integer)

The port of the specified container to which traffic is forwarded to.

healthCheck -> (structure)

An object that describes the health check configuration of the container.

healthyThreshold -> (integer)

The number of consecutive health checks successes required before moving the container to the `Healthy` state. The default value is `2` .

unhealthyThreshold -> (integer)

The number of consecutive health check failures required before moving the container to the `Unhealthy` state. The default value is `2` .

timeoutSeconds -> (integer)

The amount of time, in seconds, during which no response means a failed health check. You can specify between 2 and 60 seconds. The default value is `2` .

intervalSeconds -> (integer)

The approximate interval, in seconds, between health checks of an individual container. You can specify between 5 and 300 seconds. The default value is `5` .

path -> (string)

The path on the container on which to perform the health check. The default value is `/` .

successCodes -> (string)

The HTTP codes to use when checking for a successful response from a container. You can specify values between `200` and `499` . You can specify multiple values (for example, `200,202` ) or a range of values (for example, `200-299` ).

createdAt -> (timestamp)

The timestamp when the deployment was created.

isDisabled -> (boolean)

A Boolean value indicating whether the container service is disabled.

principalArn -> (string)

The principal ARN of the container service.

The principal ARN can be used to create a trust relationship between your standard Amazon Web Services account and your Lightsail container service. This allows you to give your service permission to access resources in your standard Amazon Web Services account.

privateDomainName -> (string)

The private domain name of the container service.

The private domain name is accessible only by other resources within the default virtual private cloud (VPC) of your Lightsail account.

publicDomainNames -> (map)

The public domain name of the container service, such as `example.com` and `www.example.com` .

You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.

If you donât specify public domain names, then you can use the default domain of the container service.

### Warning

You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the `CreateCertificate` action to create a certificate for the public domain names you want to use with your container service.

See `CreateContainerService` or `UpdateContainerService` for information about how to specify public domain names for your Lightsail container service.

key -> (string)

value -> (list)

(string)

url -> (string)

The publicly accessible URL of the container service.

If no public endpoint is specified in the `currentDeployment` , this URL returns a 404 response.

privateRegistryAccess -> (structure)

An object that describes the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.

For more information, see [Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access) in the *Amazon Lightsail Developer Guide* .

ecrImagePullerRole -> (structure)

An object that describes the activation status of the role that you can use to grant a Lightsail container service access to Amazon ECR private repositories. If the role is activated, the Amazon Resource Name (ARN) of the role is also listed.

isActive -> (boolean)

A Boolean value that indicates whether the role is activated.

principalArn -> (string)

The Amazon Resource Name (ARN) of the role, if it is activated.