# get-protection-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-protection-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-protection-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/index.html#cli-aws-fms) ]

# get-protection-status

## Description

If you created a Shield Advanced policy, returns policy-level attack summary information in the event of a potential DDoS attack. Other policy types are currently unsupported.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetProtectionStatus)

## Synopsis

```
get-protection-status
--policy-id <value>
[--member-account-id <value>]
[--start-time <value>]
[--end-time <value>]
[--next-token <value>]
[--max-results <value>]
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

`--policy-id` (string)

The ID of the policy for which you want to get the attack information.

`--member-account-id` (string)

The Amazon Web Services account that is in scope of the policy that you want to get the details for.

`--start-time` (timestamp)

The start of the time period to query for the attacks. This is a `timestamp` type. The request syntax listing indicates a `number` type because the default used by Firewall Manager is Unix time in seconds. However, any valid `timestamp` format is allowed.

`--end-time` (timestamp)

The end of the time period to query for the attacks. This is a `timestamp` type. The request syntax listing indicates a `number` type because the default used by Firewall Manager is Unix time in seconds. However, any valid `timestamp` format is allowed.

`--next-token` (string)

If you specify a value for `MaxResults` and you have more objects than the number that you specify for `MaxResults` , Firewall Manager returns a `NextToken` value in the response, which you can use to retrieve another group of objects. For the second and subsequent `GetProtectionStatus` requests, specify the value of `NextToken` from the previous response to get information about another batch of objects.

`--max-results` (integer)

Specifies the number of objects that you want Firewall Manager to return for this request. If you have more objects than the number that you specify for `MaxResults` , the response includes a `NextToken` value that you can use to get another batch of objects.

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

AdminAccountId -> (string)

The ID of the Firewall Manager administrator account for this policy.

ServiceType -> (string)

The service type that is protected by the policy. Currently, this is always `SHIELD_ADVANCED` .

Data -> (string)

Details about the attack, including the following:

- Attack type
- Account ID
- ARN of the resource attacked
- Start time of the attack
- End time of the attack (ongoing attacks will not have an end time)

The details are in JSON format.

NextToken -> (string)

If you have more objects than the number that you specified for `MaxResults` in the request, the response includes a `NextToken` value. To list more objects, submit another `GetProtectionStatus` request, and specify the `NextToken` value from the response in the `NextToken` value in the next request.

Amazon Web Services SDKs provide auto-pagination that identify `NextToken` in a response and make subsequent request calls automatically on your behalf. However, this feature is not supported by `GetProtectionStatus` . You must submit subsequent requests with `NextToken` using your own processes.