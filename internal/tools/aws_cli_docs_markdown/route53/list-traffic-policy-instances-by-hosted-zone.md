# list-traffic-policy-instances-by-hosted-zoneÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policy-instances-by-hosted-zone.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policy-instances-by-hosted-zone.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# list-traffic-policy-instances-by-hosted-zone

## Description

Gets information about the traffic policy instances that you created in a specified hosted zone.

### Note

After you submit a `CreateTrafficPolicyInstance` or an `UpdateTrafficPolicyInstance` request, thereâs a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the `State` response element.

Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the `MaxItems` parameter to list them in groups of up to 100.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTrafficPolicyInstancesByHostedZone)

## Synopsis

```
list-traffic-policy-instances-by-hosted-zone
--hosted-zone-id <value>
[--traffic-policy-instance-name-marker <value>]
[--traffic-policy-instance-type-marker <value>]
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

`--hosted-zone-id` (string)

The ID of the hosted zone that you want to list traffic policy instances for.

`--traffic-policy-instance-name-marker` (string)

If the value of `IsTruncated` in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another `ListTrafficPolicyInstances` request. For the value of `trafficpolicyinstancename` , specify the value of `TrafficPolicyInstanceNameMarker` from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.

If the value of `IsTruncated` in the previous response was `false` , there are no more traffic policy instances to get.

`--traffic-policy-instance-type-marker` (string)

If the value of `IsTruncated` in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another `ListTrafficPolicyInstances` request. For the value of `trafficpolicyinstancetype` , specify the value of `TrafficPolicyInstanceTypeMarker` from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.

If the value of `IsTruncated` in the previous response was `false` , there are no more traffic policy instances to get.

Possible values:

- `SOA`
- `A`
- `TXT`
- `NS`
- `CNAME`
- `MX`
- `NAPTR`
- `PTR`
- `SRV`
- `SPF`
- `AAAA`
- `CAA`
- `DS`
- `TLSA`
- `SSHFP`
- `SVCB`
- `HTTPS`

`--max-items` (string)

The maximum number of traffic policy instances to be included in the response body for this request. If you have more than `MaxItems` traffic policy instances, the value of the `IsTruncated` element in the response is `true` , and the values of `HostedZoneIdMarker` , `TrafficPolicyInstanceNameMarker` , and `TrafficPolicyInstanceTypeMarker` represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.

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

TrafficPolicyInstances -> (list)

A list that contains one `TrafficPolicyInstance` element for each traffic policy instance that matches the elements in the request.

(structure)

A complex type that contains settings for the new traffic policy instance.

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

TrafficPolicyInstanceNameMarker -> (string)

If `IsTruncated` is `true` , `TrafficPolicyInstanceNameMarker` is the name of the first traffic policy instance in the next group of traffic policy instances.

TrafficPolicyInstanceTypeMarker -> (string)

If `IsTruncated` is true, `TrafficPolicyInstanceTypeMarker` is the DNS type of the resource record sets that are associated with the first traffic policy instance in the next group of traffic policy instances.

IsTruncated -> (boolean)

A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get the next group of traffic policy instances by submitting another `ListTrafficPolicyInstancesByHostedZone` request and specifying the values of `HostedZoneIdMarker` , `TrafficPolicyInstanceNameMarker` , and `TrafficPolicyInstanceTypeMarker` in the corresponding request parameters.

MaxItems -> (string)

The value that you specified for the `MaxItems` parameter in the `ListTrafficPolicyInstancesByHostedZone` request that produced the current response.