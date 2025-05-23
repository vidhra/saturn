# list-origin-access-controlsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-origin-access-controls.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-origin-access-controls.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# list-origin-access-controls

## Description

Gets the list of CloudFront origin access controls (OACs) in this Amazon Web Services account.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send another request that specifies the `NextMarker` value from the current response as the `Marker` value in the next request.

### Note

If youâre not using origin access controls for your Amazon Web Services account, the `ListOriginAccessControls` operation doesnât return the `Items` element in the response.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/ListOriginAccessControls)

## Synopsis

```
list-origin-access-controls
[--marker <value>]
[--max-items <value>]
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

`--marker` (string)

Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this fieldâs value to the value of `NextMarker` from the current pageâs response.

`--max-items` (string)

The maximum number of origin access controls that you want in the response.

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

OriginAccessControlList -> (structure)

A list of origin access controls.

Marker -> (string)

The value of the `Marker` field that was provided in the request.

NextMarker -> (string)

If there are more items in the list than are in this response, this element is present. It contains the value to use in the `Marker` field of another request to continue listing origin access controls.

MaxItems -> (integer)

The maximum number of origin access controls requested.

IsTruncated -> (boolean)

If there are more items in the list than are in this response, this value is `true` .

Quantity -> (integer)

The number of origin access controls returned in the response.

Items -> (list)

Contains the origin access controls in the list.

(structure)

A CloudFront origin access control.

Id -> (string)

The unique identifier of the origin access control.

Description -> (string)

A description of the origin access control.

Name -> (string)

A unique name that identifies the origin access control.

SigningProtocol -> (string)

The signing protocol of the origin access control. The signing protocol determines how CloudFront signs (authenticates) requests. The only valid value is `sigv4` .

SigningBehavior -> (string)

A value that specifies which requests CloudFront signs (adds authentication information to). This field can have one of the following values:

- `never` â CloudFront doesnât sign any origin requests.
- `always` â CloudFront signs all origin requests, overwriting the `Authorization` header from the viewer request if necessary.
- `no-override` â If the viewer request doesnât contain the `Authorization` header, CloudFront signs the origin request. If the viewer request contains the `Authorization` header, CloudFront doesnât sign the origin request, but instead passes along the `Authorization` header that it received in the viewer request.

OriginAccessControlOriginType -> (string)

The type of origin that this origin access control is for.