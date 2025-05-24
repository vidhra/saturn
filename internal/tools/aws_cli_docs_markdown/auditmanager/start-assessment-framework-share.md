# start-assessment-framework-shareÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/start-assessment-framework-share.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/start-assessment-framework-share.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# start-assessment-framework-share

## Description

Creates a share request for a custom framework in Audit Manager.

The share request specifies a recipient and notifies them that a custom framework is available. Recipients have 120 days to accept or decline the request. If no action is taken, the share request expires.

When you create a share request, Audit Manager stores a snapshot of your custom framework in the US East (N. Virginia) Amazon Web Services Region. Audit Manager also stores a backup of the same snapshot in the US West (Oregon) Amazon Web Services Region.

Audit Manager deletes the snapshot and the backup snapshot when one of the following events occurs:

- The sender revokes the share request.
- The recipient declines the share request.
- The recipient encounters an error and doesnât successfully accept the share request.
- The share request expires before the recipient responds to the request.

When a sender [resends a share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-resend) , the snapshot is replaced with an updated version that corresponds with the latest version of the custom framework.

When a recipient accepts a share request, the snapshot is replicated into their Amazon Web Services account under the Amazon Web Services Region that was specified in the share request.

### Warning

When you invoke the `StartAssessmentFrameworkShare` API, you are about to share a custom framework with another Amazon Web Services account. You may not share a custom framework that is derived from a standard framework if the standard framework is designated as not eligible for sharing by Amazon Web Services, unless you have obtained permission to do so from the owner of the standard framework. To learn more about which standard frameworks are eligible for sharing, see [Framework sharing eligibility](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html#eligibility) in the *Audit Manager User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/StartAssessmentFrameworkShare)

## Synopsis

```
start-assessment-framework-share
--framework-id <value>
--destination-account <value>
--destination-region <value>
[--comment <value>]
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

`--framework-id` (string)

The unique identifier for the custom framework to be shared.

`--destination-account` (string)

The Amazon Web Services account of the recipient.

`--destination-region` (string)

The Amazon Web Services Region of the recipient.

`--comment` (string)

An optional comment from the sender about the share request.

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

assessmentFrameworkShareRequest -> (structure)

The share request thatâs created by the `StartAssessmentFrameworkShare` API.

id -> (string)

The unique identifier for the share request.

frameworkId -> (string)

The unique identifier for the shared custom framework.

frameworkName -> (string)

The name of the custom framework that the share request is for.

frameworkDescription -> (string)

The description of the shared custom framework.

status -> (string)

The status of the share request.

sourceAccount -> (string)

The Amazon Web Services account of the sender.

destinationAccount -> (string)

The Amazon Web Services account of the recipient.

destinationRegion -> (string)

The Amazon Web Services Region of the recipient.

expirationTime -> (timestamp)

The time when the share request expires.

creationTime -> (timestamp)

The time when the share request was created.

lastUpdated -> (timestamp)

Specifies when the share request was last updated.

comment -> (string)

An optional comment from the sender about the share request.

standardControlsCount -> (integer)

The number of standard controls that are part of the shared custom framework.

customControlsCount -> (integer)

The number of custom controls that are part of the shared custom framework.

complianceType -> (string)

The compliance type that the shared custom framework supports, such as CIS or HIPAA.