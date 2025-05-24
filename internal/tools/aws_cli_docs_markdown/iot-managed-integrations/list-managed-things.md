# list-managed-thingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-managed-integrations/list-managed-things.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-managed-integrations/list-managed-things.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot-managed-integrations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-managed-integrations/index.html#cli-aws-iot-managed-integrations) ]

# list-managed-things

## Description

List all of the associations and statuses for a managed thing by its owner.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-managed-integrations-2025-03-03/ListManagedThings)

`list-managed-things` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`

## Synopsis

```
list-managed-things
[--owner-filter <value>]
[--credential-locker-filter <value>]
[--role-filter <value>]
[--parent-controller-identifier-filter <value>]
[--connector-policy-id-filter <value>]
[--serial-number-filter <value>]
[--provisioning-status-filter <value>]
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

`--owner-filter` (string)

Filter on device owners when listing managed things.

`--credential-locker-filter` (string)

Filter on a credential locker for a managed thing.

`--role-filter` (string)

Filter on the type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.

Possible values:

- `CONTROLLER`
- `DEVICE`

`--parent-controller-identifier-filter` (string)

Filter on a parent controller id for a managed thing.

`--connector-policy-id-filter` (string)

Filter on a connector policy id for a managed thing.

`--serial-number-filter` (string)

Filter on the serial number of the device.

`--provisioning-status-filter` (string)

Filter on the status of the device.

Possible values:

- `UNASSOCIATED`
- `PRE_ASSOCIATED`
- `DISCOVERED`
- `ACTIVATED`
- `DELETION_FAILED`
- `DELETE_IN_PROGRESS`
- `ISOLATED`
- `DELETED`

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

Items -> (list)

The list of managed things.

(structure)

Structure representing one managed thing.

Id -> (string)

The id of the device.

Arn -> (string)

The Amazon Resource Name (ARN) of the managed thing.

AdvertisedProductId -> (string)

The id of the advertised product.

Brand -> (string)

The brand of the device.

Classification -> (string)

The classification of the managed thing such as light bulb or thermostat.

ConnectorDeviceId -> (string)

The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).

### Note

This parameter is used for cloud-to-cloud devices only.

ConnectorPolicyId -> (string)

The id of the connector policy.

### Note

This parameter is used for cloud-to-cloud devices only.

Model -> (string)

The model of the device.

Name -> (string)

The name of the managed thing representing the physical device.

Owner -> (string)

Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.

CredentialLockerId -> (string)

The identifier of the credential locker for the managed thing.

ParentControllerId -> (string)

Id of the controller device used for the discovery job.

ProvisioningStatus -> (string)

The provisioning status of the device in the provisioning workflow for onboarding to IoT managed integrations.

Role -> (string)

The type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.

SerialNumber -> (string)

The serial number of the device.

CreatedAt -> (timestamp)

The timestamp value of when the device creation request occurred.

UpdatedAt -> (timestamp)

The timestamp value of when the managed thing was last updated at.

ActivatedAt -> (timestamp)

The timestampe value of when the managed thing was activated at.

NextToken -> (string)

A token that can be used to retrieve the next set of results.