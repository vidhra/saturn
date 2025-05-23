# describe-registration-versionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registration-versions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registration-versions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint-sms-voice-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/index.html#cli-aws-pinpoint-sms-voice-v2) ]

# describe-registration-versions

## Description

Retrieves the specified registration version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)

`describe-registration-versions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `RegistrationVersions`

## Synopsis

```
describe-registration-versions
--registration-id <value>
[--version-numbers <value>]
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

`--registration-id` (string)

The unique identifier for the registration.

`--version-numbers` (list)

An array of registration version numbers.

(long)

Syntax:

```
long long ...
```

`--filters` (list)

An array of RegistrationVersionFilter objects to filter the results.

(structure)

The filter definition for filtering registration versions that meets a specified criteria.

Name -> (string)

The name of the attribute to filter on.

Values -> (list)

An array of values to filter on.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "registration-version-status",
    "Values": ["string", ...]
  }
  ...
]
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

RegistrationArn -> (string)

The Amazon Resource Name (ARN) for the registration.

RegistrationId -> (string)

The unique identifier for the registration.

RegistrationVersions -> (list)

An array of RegistrationVersions objects.

(structure)

Provides information about the specified version of the registration.

VersionNumber -> (long)

The version number of the registration.

RegistrationVersionStatus -> (string)

The status of the registration.

- `APPROVED` : Your registration has been approved.
- `ARCHIVED` : Your previously approved registration version moves into this status when a more recently submitted version is approved.
- `DENIED` : You must fix your registration and resubmit it.
- `DISCARDED` : Youâve abandon this version of their registration to start over with a new version.
- `DRAFT` : The initial status of a registration version after itâs created.
- `REQUIRES_AUTHENTICATION` : You need to complete email authentication.
- `REVIEWING` : Your registration has been accepted and is being reviewed.
- `REVOKED` : Your previously approved registration has been revoked.
- `SUBMITTED` : Your registration has been submitted.

RegistrationVersionStatusHistory -> (structure)

The **RegistrationVersionStatusHistory** object contains the time stamps for when the reservations status changes.

DraftTimestamp -> (timestamp)

The time when the registration was in the draft state, in [UNIX epoch time](https://www.epochconverter.com/) format.

SubmittedTimestamp -> (timestamp)

The time when the registration was in the submitted state, in [UNIX epoch time](https://www.epochconverter.com/) format.

ReviewingTimestamp -> (timestamp)

The time when the registration was in the reviewing state, in [UNIX epoch time](https://www.epochconverter.com/) format.

RequiresAuthenticationTimestamp -> (timestamp)

The time when the registration was in the requires authentication state, in [UNIX epoch time](https://www.epochconverter.com/) format.

ApprovedTimestamp -> (timestamp)

The time when the registration was in the approved state, in [UNIX epoch time](https://www.epochconverter.com/) format.

DiscardedTimestamp -> (timestamp)

The time when the registration was in the discarded state, in [UNIX epoch time](https://www.epochconverter.com/) format.

DeniedTimestamp -> (timestamp)

The time when the registration was in the denied state, in [UNIX epoch time](https://www.epochconverter.com/) format.

RevokedTimestamp -> (timestamp)

The time when the registration was in the revoked state, in [UNIX epoch time](https://www.epochconverter.com/) format.

ArchivedTimestamp -> (timestamp)

The time when the registration was in the archived state, in [UNIX epoch time](https://www.epochconverter.com/) format.

DeniedReasons -> (list)

An array of RegistrationDeniedReasonInformation objects.

(structure)

Provides the reason a registration was rejected.

Reason -> (string)

The reason a registration was rejected.

ShortDescription -> (string)

A short description of the rejection reason.

LongDescription -> (string)

A long description of the rejection reason.

DocumentationTitle -> (string)

The title of the document.

DocumentationLink -> (string)

The link to the document.

NextToken -> (string)

The token to be used for the next set of paginated results. You donât need to supply a value for this field in the initial request.