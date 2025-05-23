# list-workteamsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workteams.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workteams.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-workteams

## Description

Gets a list of private work teams that you have defined in a region. The list may be empty if no work team satisfies the filter specified in the `NameContains` parameter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListWorkteams)

`list-workteams` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Workteams`

## Synopsis

```
list-workteams
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

The field to sort results by. The default is `CreationTime` .

Possible values:

- `Name`
- `CreateDate`

`--sort-order` (string)

The sort order for results. The default is `Ascending` .

Possible values:

- `Ascending`
- `Descending`

`--name-contains` (string)

A string in the work teamâs name. This filter returns only work teams whose name contains the specified string.

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

Workteams -> (list)

An array of `Workteam` objects, each describing a work team.

(structure)

Provides details about a labeling work team.

WorkteamName -> (string)

The name of the work team.

MemberDefinitions -> (list)

A list of `MemberDefinition` objects that contains objects that identify the workers that make up the work team.

Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use `CognitoMemberDefinition` . For workforces created using your own OIDC identity provider (IdP) use `OidcMemberDefinition` .

(structure)

Defines an Amazon Cognito or your own OIDC IdP user group that is part of a work team.

CognitoMemberDefinition -> (structure)

The Amazon Cognito user group that is part of the work team.

UserPool -> (string)

An identifier for a user pool. The user pool must be in the same region as the service that you are calling.

UserGroup -> (string)

An identifier for a user group.

ClientId -> (string)

An identifier for an application client. You must create the app client ID using Amazon Cognito.

OidcMemberDefinition -> (structure)

A list user groups that exist in your OIDC Identity Provider (IdP). One to ten groups can be used to create a single private work team. When you add a user group to the list of `Groups` , you can add that user group to one or more private work teams. If you add a user group to a private work team, all workers in that user group are added to the work team.

Groups -> (list)

A list of comma seperated strings that identifies user groups in your OIDC IdP. Each user group is made up of a group of private workers.

(string)

WorkteamArn -> (string)

The Amazon Resource Name (ARN) that identifies the work team.

WorkforceArn -> (string)

The Amazon Resource Name (ARN) of the workforce.

ProductListingIds -> (list)

The Amazon Marketplace identifier for a vendorâs work team.

(string)

Description -> (string)

A description of the work team.

SubDomain -> (string)

The URI of the labeling jobâs user interface. Workers open this URI to start labeling your data objects.

CreateDate -> (timestamp)

The date and time that the work team was created (timestamp).

LastUpdatedDate -> (timestamp)

The date and time that the work team was last updated (timestamp).

NotificationConfiguration -> (structure)

Configures SNS notifications of available or expiring work items for work teams.

NotificationTopicArn -> (string)

The ARN for the Amazon SNS topic to which notifications should be published.

WorkerAccessConfiguration -> (structure)

Describes any access constraints that have been defined for Amazon S3 resources.

S3Presign -> (structure)

Defines any Amazon S3 resource constraints.

IamPolicyConstraints -> (structure)

Use this parameter to specify the allowed request source. Possible sources are either `SourceIp` or `VpcSourceIp` .

SourceIp -> (string)

When `SourceIp` is `Enabled` the workerâs IP address when a task is rendered in the worker portal is added to the IAM policy as a `Condition` used to generate the Amazon S3 presigned URL. This IP address is checked by Amazon S3 and must match in order for the Amazon S3 resource to be rendered in the worker portal.

VpcSourceIp -> (string)

When `VpcSourceIp` is `Enabled` the workerâs IP address when a task is rendered in private worker portal inside the VPC is added to the IAM policy as a `Condition` used to generate the Amazon S3 presigned URL. To render the task successfully Amazon S3 checks that the presigned URL is being accessed over an Amazon S3 VPC Endpoint, and that the workerâs IP address matches the IP address in the IAM policy. To learn more about configuring private worker portal, see [Use Amazon VPC mode from a private worker portal](https://docs.aws.amazon.com/sagemaker/latest/dg/samurai-vpc-worker-portal.html) .

NextToken -> (string)

If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of work teams, use it in the subsequent request.