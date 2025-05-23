# get-authorization-tokenÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/get-authorization-token.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/get-authorization-token.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecr-public](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/index.html#cli-aws-ecr-public) ]

# get-authorization-token

## Description

Retrieves an authorization token. An authorization token represents your IAM authentication credentials. You can use it to access any Amazon ECR registry that your IAM principal has access to. The authorization token is valid for 12 hours. This API requires the `ecr-public:GetAuthorizationToken` and `sts:GetServiceBearerToken` permissions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecr-public-2020-10-30/GetAuthorizationToken)

## Synopsis

```
get-authorization-token
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To retrieve an authorization token for any Amazon ECR public registry that the IAM principal has access**

The following `get-authorization-token` example gets an authorization token with the AWS CLI and sets it to an environment variable.

```
aws ecr-public get-authorization-token \
    --region us-east-1
```

Output:

```
{
    "authorizationData": {
        "authorizationToken": "QVdTOmV5SndZWGxzYjJKJFHDSFKJHERWUY65IOU36TRYEGFNSDLRIUOTUYTHJKLDFGOcmFUQk9OSFV2UVV4a0x6Sm1ZV0Z6TDFndlZtUjJSVmgxVEVObU9IZEdTWEZxU210c1JUQm5RWGxOUVV4NlNFUnROWG92ZWtGbWJFUjRkbWMyV0U5amFpczRNWGxTVkM5Tk5qWkVUM2RDYm05TVJqSkxjV3BsUVZvMmFYSm5iV1ZvVFdGSVRqVlFMMHN4VnpsTGVXbDFRWGRoTmpsbWFuQllhbVl6TkdGaGMwUjJha2xsYUhscWRscHZTRUpFVkVnNVQwNUdOVFpPY2xZclVFNVFVWGRSVFZvd04xUkhjVGxZZFVkQ1ZFZHBPRUptUzBVclYxQldMMjVMVkRsd2VFVlNSa1EzTWpWSlIxRkVWakJGZFZOVWEzaFBSVk5FWWpSc1lWZHZWMHBSYmxaMlJYWmhZekpaWVVOeFppdFlUa2xKU1RCdFUwdElVbXRJYlhGRk1WaFhNVTVRTkdwc1FYRlVNVWxZZUhkV05Xa3ZXWGd3ZUVZMWIyeE5VRU5QZEdSaWRHOU9lakZOZVdwTVZEUkNRVzlvYzNKSlpsRXhhR2cwWjJwRVJFVjNWalEzYjNCUmRIcEZUR1pYU1Rsc1kxSlNNbU5hUW5wRE1tOUpRMHR5Y1hkeGNXNDVMMmx4Um5GUlVGQnhjMVpQZG5WYUswOW9SQ3RPY0hwSlRsUk5lVXQyY0c1b1FsQjVZVEprVmtSdmJsQklOM05RU3pkNmQydERhMkZ5VmxSRmFVUndWVlE1ZGtsVWFXUkJWMFZEWVhoSFdXTk5VMXBTYTFreVRHZEVlVVZ0ZFRWRk4xTTVjRXBDUjBRMlYyTkdPVWhGWkVweVVGcEVaRFJxZUVablkwNXFaamh5YkVKWmJGSTNOVzFXSzFjdllXSTVTMWx2YUZacksxSnJWSFJ0Wml0T1NFSnpWVFZvV204eVFYbzFWRU5SYjNaR01Va3hPR3h2TWxkNVJsSmpUbTVSTjNjemJsUkdVRlZKVDBjeE9VeHlXVEpGVFRSS2NWbFdkVEJrV0VreFVsSktXbkpCVGtsMFdVZEJOMjltWjFFNGVHRktNbGRuWlVoUlNXNXdZV3A0VjI5M2FYZGljbE5tZGpkQ1ZYTmhOVFUyTDBzeVpteDBka0pUTVdkNGJ6TkxkSEJDYml0cE0waGhTbVpEZEZkQ00yOU1TM1pXTDNSVFlWaFpWelZXVWxjNFRXNXdhR3BhUmpoU1FuWnFkRlJMVW5abGRYRlNjVVJKZDBaSFpXUTRabEZUTUdOTVQwcFFkVXAyYjA5Tk9UaFlZMjEwVnpFMlpXdE9hMnBWV0hST1owUkpVV3R1VFU1dGJXWjNNVGc0VTAxUlNHZE9TbXRMY2tWYWJVeFljVVk0ZWpsTFdWWlRNbEZMVDJkMk1FaFBTMDl5YzJSM1NqTlplRGhUWVVOQlJGWnRlbkU1WTBKVFdqTktSR05WTkd0RGNEVjZNalJHVXpkVk9HTnVSa2xLUVd4SVJDODJXbGcyYldGemJVczJPRVp6TDBoNFMwWkRUMmdyYldGa1QwWjVhMlZQTm5SQ1l6QkpNbFpyVUhSaGVIbFVOR296VjFGVlQyMHpNeTlPWVVoSk1FdDBWalZFU2pneU5rcHNLemQxZDNwcVp6RlNja3AwVm10VU0yRnRWWGMzZDJnMFduSnFjVXczWTBjclNXeHFUVlUyVkZwWGNWY3ZSV0V6WW1oT2JIRklZVlJHU1RrMGEyOVJiMHBPVUhORk9FdERjbFJZY0daS2VVdHRZa2x5YjFORE4zSkJaWEJPZUU5eGR6WnhZMlY1WXprM1JtSkZhVFZFYkVFck5EUk9ZMWRyVEVNd1dqa2lMQ0prWVhSaGEyVjVJam9pWlhsS1VWSkdaMmxQYVVwV1ZXeENhVk5YVm14WFdFWk5VMjFrV21SRE9YaGFhWFF4VkhwS1MyTkljSHBVUms0MFlWaHNTbUpIYUhsWFZHdDZZVWhqZDFKRmFETldNbFYyWTJ0cmVVMUlTbHBWUjJONFRURlJNMDlHYUd4U01uaHVWRVJzUWxaV1pGZFJibkJLV1RCYU5HTXpUakpXTUhoWFRrWndhRTVyTVVwVFZFSkdWV3RzTUZaVVpEQlRSVGxyVkVkb2FGUlVVWHBaTVhCSFQxWmFOVlJxU20xaVZXUnVTM3BaTlZaV2NIcFdWMlJGVkcwMVRHSXdSakpXUnpoNlVsUm5kbUpzUmpGT2FUazFWVzFTY0dWR1FtOVdiVEZoVmpKc1NWRllhRmRTUkZwc1V6SkdSbUpWYkhCVlNFbDJWVzB4Ym1OVk1IWmFhelZ3WkZoa1FtVnFUa3BpTTJoTVRWVk9jMVo2V2t4aWJFWnJWRVUxVW1ONlp6QldWVFZPWW14c01sZFlZekprUjFwVFkxaE9kRnBXWkhaVFZWcGhWa2MxU2xWRlVtdFRiWE16WWpOVmVrNXFSa2RVTTJSd1QwaGtXbVJIVVhsbGJYQkRaRlp2ZGxvd1ZqWmlNbEl4Vkc1T2FtSldjRU5VU0ZVd1kwZDRjbU14WkhaVVYwNTRaRzV2TWxSVlVsQmpiSEJPVkc1VmVsZEZPVzVYYkVwWlUyNWtVbGRZWkZWaVdFWlNUVzF3VFZSSVFraE9XRnBwWVZoak0xUnJXak5OYm04eFpEQk9XbEZzYkhSTmEyaHpaRmRTUTJORVFUQlpWMk01VUZOSmMwbHJiRUpTUTBrMlNXNUZlbHA2U1RGVVZXeFVZekIwYVU5RWFEVmtiRVpzVVZWc2QxbHJWbmxOYW13MVZWaG9UazVzVWpWbFJHaDZZMjFHVkZVeFFubFZXRTVLVGpCMGFXSlZNWGhpUjBwTVlUSTVNRTVVYXpCTE0wVnlWakF4VG1WSE5VcGtSa0pRVld4V1UwOVdVWGhqTVc4eVZraFdlVnA2VGsxV01tUnhVV3Q0ZEdGcVRsUk5hMnN5V2tSV2FtUkdVakZqVm5CUFVrUlNjR0pHUm1GbGFscDRXV2x6Y2xFd1VYcGhSRnBZVmtaU2FVNXVSVFZYYlVaVFpXdHdkVmRZVGpaVGEyaDBWMnhDVlU0elZrWlRSRUpIVlVWa2MwNVlhRFZsUkVwelQwWkNSbE5WY0ZGWFNFWXhaVmMxVEZsVE9VeFdhMGt4V1ROS1Rrd3pXazFpYkhCdFVrUldWRlJHVlhaTmJVazBZbFZzUkV3d2N6UldSV2MxVDBWa05tSXpiM2hXVms1V1ZtMDFiRkZUT1hoUFJVcHpUMGRzU2xaSVJrTkxNVTVFWWtaa05WWnViRmRYVjJRd1RXcG5kMVJWUmpCa1JYQkdZVlYwZFZNeU1VVlpWVTVQV25wa1ExZHFVbE5sUjBaRVlWVTFXbVZwY3pSTE1HTTFVbFZGTlZwRll6UlRSMVoxVFcxb05XTnJkRUpWZWxsM1RETmplbUV4WkdGU1JsWm9ZVVpzZEdWR2JFTlVNblJYVkRCNE5HUXlkRXhaTWxKTlYxZDBWRTB5YUZwaFJsazFVMGR3Y0ZGVk9YaGxhekV6VVZRd09VbHVNRDBpTENKMlpYSnphVzl1SWpvaU15SXNJblI1Y0dVaU9pSkVRVlJCWDB0RldTSXNJbVY0Y0dseVlYUnBiMjRpT2pFM01qRTVOVGMzTmpKOQ==",
        "expiresAt": "2024-07-25T21:37:26.301000-04:00"
    }
}
```

For more information, see [Amazon ECR public registries](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html#registry_auth_http) in the *Amazon ECR Public*.

**Example 2: To retrieve an authorization token for any Amazon ECR public registry that the IAM principal has access**

The following `get-authorization-token` example gets an authorization token with the AWS CLI and sets it to an environment variable.

```
aws ecr-public get-authorization-token \
    --region us-east-1 \
    --output=text \
    --query 'authorizationData.authorizationToken'
```

Output:

```
QVdTOmV5SndZWGxzYjJKJFHDSFKJHERWUY65IOU36TRYEGFNSDLRIUOTUYTHJKLDFGOcmFUQk9OSFV2UVV4a0x6Sm1ZV0Z6TDFndlZtUjJSVmgxVEVObU9IZEdTWEZxU210c1JUQm5RWGxOUVV4NlNFUnROWG92ZWtGbWJFUjRkbWMyV0U5amFpczRNWGxTVkM5Tk5qWkVUM2RDYm05TVJqSkxjV3BsUVZvMmFYSm5iV1ZvVFdGSVRqVlFMMHN4VnpsTGVXbDFRWGRoTmpsbWFuQllhbVl6TkdGaGMwUjJha2xsYUhscWRscHZTRUpFVkVnNVQwNUdOVFpPY2xZclVFNVFVWGRSVFZvd04xUkhjVGxZZFVkQ1ZFZHBPRUptUzBVclYxQldMMjVMVkRsd2VFVlNSa1EzTWpWSlIxRkVWakJGZFZOVWEzaFBSVk5FWWpSc1lWZHZWMHBSYmxaMlJYWmhZekpaWVVOeFppdFlUa2xKU1RCdFUwdElVbXRJYlhGRk1WaFhNVTVRTkdwc1FYRlVNVWxZZUhkV05Xa3ZXWGd3ZUVZMWIyeE5VRU5QZEdSaWRHOU9lakZOZVdwTVZEUkNRVzlvYzNKSlpsRXhhR2cwWjJwRVJFVjNWalEzYjNCUmRIcEZUR1pYU1Rsc1kxSlNNbU5hUW5wRE1tOUpRMHR5Y1hkeGNXNDVMMmx4Um5GUlVGQnhjMVpQZG5WYUswOW9SQ3RPY0hwSlRsUk5lVXQyY0c1b1FsQjVZVEprVmtSdmJsQklOM05RU3pkNmQydERhMkZ5VmxSRmFVUndWVlE1ZGtsVWFXUkJWMFZEWVhoSFdXTk5VMXBTYTFreVRHZEVlVVZ0ZFRWRk4xTTVjRXBDUjBRMlYyTkdPVWhGWkVweVVGcEVaRFJxZUVablkwNXFaamh5YkVKWmJGSTNOVzFXSzFjdllXSTVTMWx2YUZacksxSnJWSFJ0Wml0T1NFSnpWVFZvV204eVFYbzFWRU5SYjNaR01Va3hPR3h2TWxkNVJsSmpUbTVSTjNjemJsUkdVRlZKVDBjeE9VeHlXVEpGVFRSS2NWbFdkVEJrV0VreFVsSktXbkpCVGtsMFdVZEJOMjltWjFFNGVHRktNbGRuWlVoUlNXNXdZV3A0VjI5M2FYZGljbE5tZGpkQ1ZYTmhOVFUyTDBzeVpteDBka0pUTVdkNGJ6TkxkSEJDYml0cE0waGhTbVpEZEZkQ00yOU1TM1pXTDNSVFlWaFpWelZXVWxjNFRXNXdhR3BhUmpoU1FuWnFkRlJMVW5abGRYRlNjVVJKZDBaSFpXUTRabEZUTUdOTVQwcFFkVXAyYjA5Tk9UaFlZMjEwVnpFMlpXdE9hMnBWV0hST1owUkpVV3R1VFU1dGJXWjNNVGc0VTAxUlNHZE9TbXRMY2tWYWJVeFljVVk0ZWpsTFdWWlRNbEZMVDJkMk1FaFBTMDl5YzJSM1NqTlplRGhUWVVOQlJGWnRlbkU1WTBKVFdqTktSR05WTkd0RGNEVjZNalJHVXpkVk9HTnVSa2xLUVd4SVJDODJXbGcyYldGemJVczJPRVp6TDBoNFMwWkRUMmdyYldGa1QwWjVhMlZQTm5SQ1l6QkpNbFpyVUhSaGVIbFVOR296VjFGVlQyMHpNeTlPWVVoSk1FdDBWalZFU2pneU5rcHNLemQxZDNwcVp6RlNja3AwVm10VU0yRnRWWGMzZDJnMFduSnFjVXczWTBjclNXeHFUVlUyVkZwWGNWY3ZSV0V6WW1oT2JIRklZVlJHU1RrMGEyOVJiMHBPVUhORk9FdERjbFJZY0daS2VVdHRZa2x5YjFORE4zSkJaWEJPZUU5eGR6WnhZMlY1WXprM1JtSkZhVFZFYkVFck5EUk9ZMWRyVEVNd1dqa2lMQ0prWVhSaGEyVjVJam9pWlhsS1VWSkdaMmxQYVVwV1ZXeENhVk5YVm14WFdFWk5VMjFrV21SRE9YaGFhWFF4VkhwS1MyTkljSHBVUms0MFlWaHNTbUpIYUhsWFZHdDZZVWhqZDFKRmFETldNbFYyWTJ0cmVVMUlTbHBWUjJONFRURlJNMDlHYUd4U01uaHVWRVJzUWxaV1pGZFJibkJLV1RCYU5HTXpUakpXTUhoWFRrWndhRTVyTVVwVFZFSkdWV3RzTUZaVVpEQlRSVGxyVkVkb2FGUlVVWHBaTVhCSFQxWmFOVlJxU20xaVZXUnVTM3BaTlZaV2NIcFdWMlJGVkcwMVRHSXdSakpXUnpoNlVsUm5kbUpzUmpGT2FUazFWVzFTY0dWR1FtOVdiVEZoVmpKc1NWRllhRmRTUkZwc1V6SkdSbUpWYkhCVlNFbDJWVzB4Ym1OVk1IWmFhelZ3WkZoa1FtVnFUa3BpTTJoTVRWVk9jMVo2V2t4aWJFWnJWRVUxVW1ONlp6QldWVFZPWW14c01sZFlZekprUjFwVFkxaE9kRnBXWkhaVFZWcGhWa2MxU2xWRlVtdFRiWE16WWpOVmVrNXFSa2RVTTJSd1QwaGtXbVJIVVhsbGJYQkRaRlp2ZGxvd1ZqWmlNbEl4Vkc1T2FtSldjRU5VU0ZVd1kwZDRjbU14WkhaVVYwNTRaRzV2TWxSVlVsQmpiSEJPVkc1VmVsZEZPVzVYYkVwWlUyNWtVbGRZWkZWaVdFWlNUVzF3VFZSSVFraE9XRnBwWVZoak0xUnJXak5OYm04eFpEQk9XbEZzYkhSTmEyaHpaRmRTUTJORVFUQlpWMk01VUZOSmMwbHJiRUpTUTBrMlNXNUZlbHA2U1RGVVZXeFVZekIwYVU5RWFEVmtiRVpzVVZWc2QxbHJWbmxOYW13MVZWaG9UazVzVWpWbFJHaDZZMjFHVkZVeFFubFZXRTVLVGpCMGFXSlZNWGhpUjBwTVlUSTVNRTVVYXpCTE0wVnlWakF4VG1WSE5VcGtSa0pRVld4V1UwOVdVWGhqTVc4eVZraFdlVnA2VGsxV01tUnhVV3Q0ZEdGcVRsUk5hMnN5V2tSV2FtUkdVakZqVm5CUFVrUlNjR0pHUm1GbGFscDRXV2x6Y2xFd1VYcGhSRnBZVmtaU2FVNXVSVFZYYlVaVFpXdHdkVmRZVGpaVGEyaDBWMnhDVlU0elZrWlRSRUpIVlVWa2MwNVlhRFZsUkVwelQwWkNSbE5WY0ZGWFNFWXhaVmMxVEZsVE9VeFdhMGt4V1ROS1Rrd3pXazFpYkhCdFVrUldWRlJHVlhaTmJVazBZbFZzUkV3d2N6UldSV2MxVDBWa05tSXpiM2hXVms1V1ZtMDFiRkZUT1hoUFJVcHpUMGRzU2xaSVJrTkxNVTVFWWtaa05WWnViRmRYVjJRd1RXcG5kMVJWUmpCa1JYQkdZVlYwZFZNeU1VVlpWVTVQV25wa1ExZHFVbE5sUjBaRVlWVTFXbVZwY3pSTE1HTTFVbFZGTlZwRll6UlRSMVoxVFcxb05XTnJkRUpWZWxsM1RETmplbUV4WkdGU1JsWm9ZVVpzZEdWR2JFTlVNblJYVkRCNE5HUXlkRXhaTWxKTlYxZDBWRTB5YUZwaFJsazFVMGR3Y0ZGVk9YaGxhekV6VVZRd09VbHVNRDBpTENKMlpYSnphVzl1SWpvaU15SXNJblI1Y0dVaU9pSkVRVlJCWDB0RldTSXNJbVY0Y0dseVlYUnBiMjRpT2pFM01qRTVOVGMzTmpKOQ
```

For more information, see [Amazon ECR public registries](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html#registry_auth_http) in the *Amazon ECR Public*.

## Output

authorizationData -> (structure)

An authorization token data object that corresponds to a public registry.

authorizationToken -> (string)

A base64-encoded string that contains authorization data for a public Amazon ECR registry. When the string is decoded, itâs presented in the format `user:password` for public registry authentication using `docker login` .

expiresAt -> (timestamp)

The Unix time in seconds and milliseconds when the authorization token expires. Authorization tokens are valid for 12 hours.