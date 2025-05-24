# list-workforcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workforces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workforces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-workforces

## Description

Use this operation to list all private and vendor workforces in an Amazon Web Services Region. Note that you can only have one private workforce per Amazon Web Services Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListWorkforces)

`list-workforces` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Workforces`

## Synopsis

```
list-workforces
[--sort-by <value>]
[--sort-order <value>]
[--name-contains <value>]
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

`--sort-by` (string)

Sort workforces using the workforce name or creation date.

Possible values:

- `Name`
- `CreateDate`

`--sort-order` (string)

Sort workforces in ascending or descending order.

Possible values:

- `Ascending`
- `Descending`

`--name-contains` (string)

A filter you can use to search for workforces using part of the workforce name.

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

Workforces -> (list)

A list containing information about your workforce.

(structure)

A single private workforce, which is automatically created when you create your first private work team. You can create one private work force in each Amazon Web Services Region. By default, any workforce-related API operation used in a specific region will apply to the workforce created in that region. To learn how to create a private workforce, see [Create a Private Workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html) .

WorkforceName -> (string)

The name of the private workforce.

WorkforceArn -> (string)

The Amazon Resource Name (ARN) of the private workforce.

LastUpdatedDate -> (timestamp)

The most recent date that [UpdateWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkforce.html) was used to successfully add one or more IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) ) to a private workforceâs allow list.

SourceIpConfig -> (structure)

A list of one to ten IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) ) to be added to the workforce allow list. By default, a workforce isnât restricted to specific IP addresses.

Cidrs -> (list)

A list of one to ten [Classless Inter-Domain Routing](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) (CIDR) values.

Maximum: Ten CIDR values

### Note

The following Length Constraints apply to individual CIDR values in the CIDR value list.

(string)

SubDomain -> (string)

The subdomain for your OIDC Identity Provider.

CognitoConfig -> (structure)

The configuration of an Amazon Cognito workforce. A single Cognito workforce is created using and corresponds to a single [Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) .

UserPool -> (string)

A [user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers.

ClientId -> (string)

The client ID for your Amazon Cognito user pool.

OidcConfig -> (structure)

The configuration of an OIDC Identity Provider (IdP) private workforce.

ClientId -> (string)

The OIDC IdP client ID used to configure your private workforce.

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

CreateDate -> (timestamp)

The date that the workforce is created.

WorkforceVpcConfig -> (structure)

The configuration of a VPC workforce.

VpcId -> (string)

The ID of the VPC that the workforce uses for communication.

SecurityGroupIds -> (list)

The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.

(string)

Subnets -> (list)

The ID of the subnets in the VPC that you want to connect.

(string)

VpcEndpointId -> (string)

The IDs for the VPC service endpoints of your VPC workforce when it is created and updated.

Status -> (string)

The status of your workforce.

FailureReason -> (string)

The reason your workforce failed.

NextToken -> (string)

A token to resume pagination.