# list-byoip-cidrsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-byoip-cidrs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-byoip-cidrs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [globalaccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/index.html#cli-aws-globalaccelerator) ]

# list-byoip-cidrs

## Description

Lists the IP address ranges that were specified in calls to [ProvisionByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/ProvisionByoipCidr.html) , including the current state and a history of state changes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/ListByoipCidrs)

`list-byoip-cidrs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ByoipCidrs`

## Synopsis

```
list-byoip-cidrs
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

ByoipCidrs -> (list)

Information about your address ranges.

(structure)

Information about an IP address range that is provisioned for use with your Amazon Web Services resources through bring your own IP address (BYOIP).

The following describes each BYOIP `State` that your IP address range can be in.

- **PENDING_PROVISIONING** â Youâve submitted a request to provision an IP address range but it is not yet provisioned with Global Accelerator.
- **READY** â The address range is provisioned with Global Accelerator and can be advertised.
- **PENDING_ADVERTISING** â Youâve submitted a request for Global Accelerator to advertise an address range but it is not yet being advertised.
- **ADVERTISING** â The address range is being advertised by Global Accelerator.
- **PENDING_WITHDRAWING** â Youâve submitted a request to withdraw an address range from being advertised but it is still being advertised by Global Accelerator.
- **PENDING_DEPROVISIONING** â Youâve submitted a request to deprovision an address range from Global Accelerator but it is still provisioned.
- **DEPROVISIONED** â The address range is deprovisioned from Global Accelerator.
- **FAILED_PROVISION** â The request to provision the address range from Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact Amazon Web Services support.
- **FAILED_ADVERTISING** â The request for Global Accelerator to advertise the address range was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact Amazon Web Services support.
- **FAILED_WITHDRAW** â The request to withdraw the address range from advertising by Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact Amazon Web Services support.
- **FAILED_DEPROVISION** â The request to deprovision the address range from Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact Amazon Web Services support.

Cidr -> (string)

The address range, in CIDR notation.

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the Global Accelerator Developer Guide.

State -> (string)

The state of the address pool.

Events -> (list)

A history of status changes for an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).

(structure)

A complex type that contains a `Message` and a `Timestamp` value for changes that you make in the status of an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).

Message -> (string)

A string that contains an `Event` message describing changes that you make in the status of an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).

Timestamp -> (timestamp)

A timestamp for when you make a status change for an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).

NextToken -> (string)

The token for the next page of results.