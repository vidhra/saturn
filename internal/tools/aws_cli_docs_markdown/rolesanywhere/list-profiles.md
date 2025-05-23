# list-profilesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/list-profiles.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/list-profiles.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rolesanywhere](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/index.html#cli-aws-rolesanywhere) ]

# list-profiles

## Description

Lists all profiles in the authenticated account and Amazon Web Services Region.

**Required permissions:** `rolesanywhere:ListProfiles` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rolesanywhere-2018-05-10/ListProfiles)

`list-profiles` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `profiles`

## Synopsis

```
list-profiles
[--page-size <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--page-size` (integer)

The number of resources in the paginated list.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

nextToken -> (string)

A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.

profiles -> (list)

A list of profiles.

(structure)

The state of the profile after a read or write operation.

acceptRoleSessionName -> (boolean)

Used to determine if a custom role session name will be accepted in a temporary credential request.

attributeMappings -> (list)

A mapping applied to the authenticating end-entity certificate.

(structure)

A mapping applied to the authenticating end-entity certificate.

certificateField -> (string)

Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.

mappingRules -> (list)

A list of mapping entries for every supported specifier or sub-field.

(structure)

A single mapping entry for each supported specifier or sub-field.

specifier -> (string)

Specifier within a certificate field, such as CN, OU, or UID from the Subject field.

createdAt -> (timestamp)

The ISO-8601 timestamp when the profile was created.

createdBy -> (string)

The Amazon Web Services account that created the profile.

durationSeconds -> (integer)

Used to determine how long sessions vended using this profile are valid for. See the `Expiration` section of the [CreateSession API documentation](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object) page for more details. In requests, if this value is not provided, the default value will be 3600.

enabled -> (boolean)

Indicates whether the profile is enabled.

managedPolicyArns -> (list)

A list of managed policy ARNs that apply to the vended session credentials.

(string)

name -> (string)

The name of the profile.

profileArn -> (string)

The ARN of the profile.

profileId -> (string)

The unique identifier of the profile.

requireInstanceProperties -> (boolean)

Specifies whether instance properties are required in temporary credential requests with this profile.

roleArns -> (list)

A list of IAM roles that this profile can assume in a temporary credential request.

(string)

sessionPolicy -> (string)

A session policy that applies to the trust boundary of the vended session credentials.

updatedAt -> (timestamp)

The ISO-8601 timestamp when the profile was last updated.