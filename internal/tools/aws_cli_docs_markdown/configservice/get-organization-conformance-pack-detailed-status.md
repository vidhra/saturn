# get-organization-conformance-pack-detailed-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-organization-conformance-pack-detailed-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-organization-conformance-pack-detailed-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# get-organization-conformance-pack-detailed-status

## Description

Returns detailed status for each member account within an organization for a given organization conformance pack.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)

`get-organization-conformance-pack-detailed-status` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `OrganizationConformancePackDetailedStatuses`

## Synopsis

```
get-organization-conformance-pack-detailed-status
--organization-conformance-pack-name <value>
[--filters <value>]
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

`--organization-conformance-pack-name` (string)

The name of organization conformance pack for which you want status details for member accounts.

`--filters` (structure)

An `OrganizationResourceDetailedStatusFilters` object.

AccountId -> (string)

The 12-digit account ID of the member account within an organization.

Status -> (string)

Indicates deployment status for conformance pack in a member account. When management account calls `PutOrganizationConformancePack` action for the first time, conformance pack status is created in the member account. When management account calls `PutOrganizationConformancePack` action for the second time, conformance pack status is updated in the member account. Conformance pack status is deleted when the management account deletes `OrganizationConformancePack` and disables service access for `config-multiaccountsetup.amazonaws.com` .

Config sets the state of the conformance pack to:

- `CREATE_SUCCESSFUL` when conformance pack has been created in the member account.
- `CREATE_IN_PROGRESS` when conformance pack is being created in the member account.
- `CREATE_FAILED` when conformance pack creation has failed in the member account.
- `DELETE_FAILED` when conformance pack deletion has failed in the member account.
- `DELETE_IN_PROGRESS` when conformance pack is being deleted in the member account.
- `DELETE_SUCCESSFUL` when conformance pack has been deleted in the member account.
- `UPDATE_SUCCESSFUL` when conformance pack has been updated in the member account.
- `UPDATE_IN_PROGRESS` when conformance pack is being updated in the member account.
- `UPDATE_FAILED` when conformance pack deletion has failed in the member account.

Shorthand Syntax:

```
AccountId=string,Status=string
```

JSON Syntax:

```
{
  "AccountId": "string",
  "Status": "CREATE_SUCCESSFUL"|"CREATE_IN_PROGRESS"|"CREATE_FAILED"|"DELETE_SUCCESSFUL"|"DELETE_FAILED"|"DELETE_IN_PROGRESS"|"UPDATE_SUCCESSFUL"|"UPDATE_IN_PROGRESS"|"UPDATE_FAILED"
}
```

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

OrganizationConformancePackDetailedStatuses -> (list)

A list of `OrganizationConformancePackDetailedStatus` objects.

(structure)

Organization conformance pack creation or deletion status in each member account. This includes the name of the conformance pack, the status, error code and error message when the conformance pack creation or deletion failed.

AccountId -> (string)

The 12-digit account ID of a member account.

ConformancePackName -> (string)

The name of conformance pack deployed in the member account.

Status -> (string)

Indicates deployment status for conformance pack in a member account. When management account calls `PutOrganizationConformancePack` action for the first time, conformance pack status is created in the member account. When management account calls `PutOrganizationConformancePack` action for the second time, conformance pack status is updated in the member account. Conformance pack status is deleted when the management account deletes `OrganizationConformancePack` and disables service access for `config-multiaccountsetup.amazonaws.com` .

Config sets the state of the conformance pack to:

- `CREATE_SUCCESSFUL` when conformance pack has been created in the member account.
- `CREATE_IN_PROGRESS` when conformance pack is being created in the member account.
- `CREATE_FAILED` when conformance pack creation has failed in the member account.
- `DELETE_FAILED` when conformance pack deletion has failed in the member account.
- `DELETE_IN_PROGRESS` when conformance pack is being deleted in the member account.
- `DELETE_SUCCESSFUL` when conformance pack has been deleted in the member account.
- `UPDATE_SUCCESSFUL` when conformance pack has been updated in the member account.
- `UPDATE_IN_PROGRESS` when conformance pack is being updated in the member account.
- `UPDATE_FAILED` when conformance pack deletion has failed in the member account.

ErrorCode -> (string)

An error code that is returned when conformance pack creation or deletion failed in the member account.

ErrorMessage -> (string)

An error message indicating that conformance pack account creation or deletion has failed due to an error in the member account.

LastUpdateTime -> (timestamp)

The timestamp of the last status update.

NextToken -> (string)

The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.