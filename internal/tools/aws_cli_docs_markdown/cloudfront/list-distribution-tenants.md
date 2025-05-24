# list-distribution-tenantsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distribution-tenants.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distribution-tenants.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# list-distribution-tenants

## Description

Lists the distribution tenants in your Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/ListDistributionTenants)

`list-distribution-tenants` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DistributionTenantList`

## Synopsis

```
list-distribution-tenants
[--association-filter <value>]
[--max-items <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--association-filter` (structure)

Filter by the associated distribution ID or connection group ID.

DistributionId -> (string)

The distribution ID to filter by. You can find distribution tenants associated with a specific distribution.

ConnectionGroupId -> (string)

The ID of the connection group to filter by. You can find distribution tenants associated with a specific connection group.

Shorthand Syntax:

```
DistributionId=string,ConnectionGroupId=string
```

JSON Syntax:

```
{
  "DistributionId": "string",
  "ConnectionGroupId": "string"
}
```

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

NextMarker -> (string)

A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.

DistributionTenantList -> (list)

The list of distribution tenants that you retrieved.

(structure)

A summary of the information about a distribution tenant.

Id -> (string)

The ID of the distribution tenant.

DistributionId -> (string)

The identifier for the multi-tenant distribution. For example: `EDFDVBD632BHDS5` .

Name -> (string)

The name of the distribution tenant.

Arn -> (string)

The Amazon Resource Name (ARN) of the distribution tenant.

Domains -> (list)

The domains associated with the distribution tenant.

(structure)

The details about the domain result.

Domain -> (string)

The specified domain.

Status -> (string)

Whether the domain is active or inactive.

ConnectionGroupId -> (string)

The ID of the connection group ID for the distribution tenant. If you donât specify a connection group, CloudFront uses the default connection group.

Customizations -> (structure)

Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.

WebAcl -> (structure)

The WAF web ACL.

Action -> (string)

The action for the WAF web ACL customization. You can specify `override` to specify a separate WAF web ACL for the distribution tenant. If you specify `disable` , the distribution tenant wonât have WAF web ACL protections and wonât inherit from the multi-tenant distribution.

Arn -> (string)

The Amazon Resource Name (ARN) of the WAF web ACL.

Certificate -> (structure)

The Certificate Manager (ACM) certificate.

Arn -> (string)

The Amazon Resource Name (ARN) of the ACM certificate.

GeoRestrictions -> (structure)

The geographic restrictions.

RestrictionType -> (string)

The method that you want to use to restrict distribution of your content by country:

- `none` : No geographic restriction is enabled, meaning access to content is not restricted by client geo location.
- `blacklist` : The `Location` elements specify the countries in which you donât want CloudFront to distribute your content.
- `whitelist` : The `Location` elements specify the countries in which you want CloudFront to distribute your content.

Locations -> (list)

The locations for geographic restrictions.

(string)

CreatedTime -> (timestamp)

The date and time when the distribution tenant was created.

LastModifiedTime -> (timestamp)

The date and time when the distribution tenant was updated.

ETag -> (string)

The current version of the distribution tenant.

Enabled -> (boolean)

Indicates whether the distribution tenants are in an enabled state. If disabled, the distribution tenant wonât service traffic.

Status -> (string)

The status of the distribution tenant.