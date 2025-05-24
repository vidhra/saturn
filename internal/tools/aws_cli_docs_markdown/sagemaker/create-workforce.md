# create-workforceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workforce.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workforce.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-workforce

## Description

Use this operation to create a workforce. This operation will return an error if a workforce already exists in the Amazon Web Services Region that you specify. You can only create one workforce in each Amazon Web Services Region per Amazon Web Services account.

If you want to create a new workforce in an Amazon Web Services Region where a workforce already exists, use the [DeleteWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkforce.html) API operation to delete the existing workforce and then use `CreateWorkforce` to create a new workforce.

To create a private workforce using Amazon Cognito, you must specify a Cognito user pool in `CognitoConfig` . You can also create an Amazon Cognito workforce using the Amazon SageMaker console. For more information, see [Create a Private Workforce (Amazon Cognito)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html) .

To create a private workforce using your own OIDC Identity Provider (IdP), specify your IdP configuration in `OidcConfig` . Your OIDC IdP must support *groups* because groups are used by Ground Truth and Amazon A2I to create work teams. For more information, see [Create a Private Workforce (OIDC IdP)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private-oidc.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateWorkforce)

## Synopsis

```
create-workforce
[--cognito-config <value>]
[--oidc-config <value>]
[--source-ip-config <value>]
--workforce-name <value>
[--tags <value>]
[--workforce-vpc-config <value>]
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

`--cognito-config` (structure)

Use this parameter to configure an Amazon Cognito private workforce. A single Cognito workforce is created using and corresponds to a single [Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) .

Do not use `OidcConfig` if you specify values for `CognitoConfig` .

UserPool -> (string)

A [user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers.

ClientId -> (string)

The client ID for your Amazon Cognito user pool.

Shorthand Syntax:

```
UserPool=string,ClientId=string
```

JSON Syntax:

```
{
  "UserPool": "string",
  "ClientId": "string"
}
```

`--oidc-config` (structure)

Use this parameter to configure a private workforce using your own OIDC Identity Provider.

Do not use `CognitoConfig` if you specify values for `OidcConfig` .

ClientId -> (string)

The OIDC IdP client ID used to configure your private workforce.

ClientSecret -> (string)

The OIDC IdP client secret used to configure your private workforce.

Issuer -> (string)

The OIDC IdP issuer used to configure your private workforce.

AuthorizationEndpoint -> (string)

The OIDC IdP authorization endpoint used to configure your private workforce.

TokenEndpoint -> (string)

The OIDC IdP token endpoint used to configure your private workforce.

UserInfoEndpoint -> (string)

The OIDC IdP user information endpoint used to configure your private workforce.

LogoutEndpoint -> (string)

The OIDC IdP logout endpoint used to configure your private workforce.

JwksUri -> (string)

The OIDC IdP JSON Web Key Set (Jwks) URI used to configure your private workforce.

Scope -> (string)

An array of string identifiers used to refer to the specific pieces of user data or claims that the client application wants to access.

AuthenticationRequestExtraParams -> (map)

A string to string map of identifiers specific to the custom identity provider (IdP) being used.

key -> (string)

value -> (string)

Shorthand Syntax:

```
ClientId=string,ClientSecret=string,Issuer=string,AuthorizationEndpoint=string,TokenEndpoint=string,UserInfoEndpoint=string,LogoutEndpoint=string,JwksUri=string,Scope=string,AuthenticationRequestExtraParams={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "ClientId": "string",
  "ClientSecret": "string",
  "Issuer": "string",
  "AuthorizationEndpoint": "string",
  "TokenEndpoint": "string",
  "UserInfoEndpoint": "string",
  "LogoutEndpoint": "string",
  "JwksUri": "string",
  "Scope": "string",
  "AuthenticationRequestExtraParams": {"string": "string"
    ...}
}
```

`--source-ip-config` (structure)

A list of IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) ). Used to create an allow list of IP addresses for a private workforce. Workers will only be able to log in to their worker portal from an IP address within this range. By default, a workforce isnât restricted to specific IP addresses.

Cidrs -> (list)

A list of one to ten [Classless Inter-Domain Routing](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) (CIDR) values.

Maximum: Ten CIDR values

### Note

The following Length Constraints apply to individual CIDR values in the CIDR value list.

(string)

Shorthand Syntax:

```
Cidrs=string,string
```

JSON Syntax:

```
{
  "Cidrs": ["string", ...]
}
```

`--workforce-name` (string)

The name of the private workforce.

`--tags` (list)

An array of key-value pairs that contain metadata to help you categorize and organize our workforce. Each tag consists of a key and a value, both of which you define.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--workforce-vpc-config` (structure)

Use this parameter to configure a workforce using VPC.

VpcId -> (string)

The ID of the VPC that the workforce uses for communication.

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . The security groups must be for the same VPC as specified in the subnet.

(string)

Subnets -> (list)

The ID of the subnets in the VPC that you want to connect.

(string)

Shorthand Syntax:

```
VpcId=string,SecurityGroupIds=string,string,Subnets=string,string
```

JSON Syntax:

```
{
  "VpcId": "string",
  "SecurityGroupIds": ["string", ...],
  "Subnets": ["string", ...]
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

WorkforceArn -> (string)

The Amazon Resource Name (ARN) of the workforce.