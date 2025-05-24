# update-traffic-policy-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-traffic-policy-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-traffic-policy-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# update-traffic-policy-instance

## Description

### Note

After you submit a `UpdateTrafficPolicyInstance` request, thereâs a brief delay while Route 53 creates the resource record sets that are specified in the traffic policy definition. Use `GetTrafficPolicyInstance` with the `id` of updated traffic policy instance confirm that the `UpdateTrafficPolicyInstance` request completed successfully. For more information, see the `State` response element.

Updates the resource record sets in a specified hosted zone that were created based on the settings in a specified traffic policy version.

When you update a traffic policy instance, Amazon Route 53 continues to respond to DNS queries for the root resource record set name (such as example.com) while it replaces one group of resource record sets with another. Route 53 performs the following operations:

- Route 53 creates a new group of resource record sets based on the specified traffic policy. This is true regardless of how significant the differences are between the existing resource record sets and the new resource record sets.
- When all of the new resource record sets have been created, Route 53 starts to respond to DNS queries for the root resource record set name (such as example.com) by using the new resource record sets.
- Route 53 deletes the old group of resource record sets that are associated with the root resource record set name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/UpdateTrafficPolicyInstance)

## Synopsis

```
update-traffic-policy-instance
--id <value>
--ttl <value>
--traffic-policy-id <value>
--traffic-policy-version <value>
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

`--id` (string)

The ID of the traffic policy instance that you want to update.

`--ttl` (long)

The TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.

`--traffic-policy-id` (string)

The ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.

`--traffic-policy-version` (integer)

The version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.

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

TrafficPolicyInstance -> (structure)

A complex type that contains settings for the updated traffic policy instance.

Id -> (string)

The ID that Amazon Route 53 assigned to the new traffic policy instance.

HostedZoneId -> (string)

The ID of the hosted zone that Amazon Route 53 created resource record sets in.

Name -> (string)

The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.

TTL -> (long)

The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

State -> (string)

The value of `State` is one of the following values:

Applied

Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.

Creating

Route 53 is creating the resource record sets. Use `GetTrafficPolicyInstance` to confirm that the `CreateTrafficPolicyInstance` request completed successfully.

Failed

Route 53 wasnât able to create or update the resource record sets. When the value of `State` is `Failed` , see `Message` for an explanation of what caused the request to fail.

Message -> (string)

If `State` is `Failed` , an explanation of the reason for the failure. If `State` is another value, `Message` is empty.

TrafficPolicyId -> (string)

The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyVersion -> (integer)

The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyType -> (string)

The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.