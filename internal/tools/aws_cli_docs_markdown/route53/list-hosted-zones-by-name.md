# list-hosted-zones-by-nameÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-name.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-name.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# list-hosted-zones-by-name

## Description

Retrieves a list of your hosted zones in lexicographic order. The response includes a `HostedZones` child element for each hosted zone created by the current Amazon Web Services account.

`ListHostedZonesByName` sorts hosted zones by name with the labels reversed. For example:

`com.example.www.`

Note the trailing dot, which can change the sort order in some circumstances.

If the domain name includes escape characters or Punycode, `ListHostedZonesByName` alphabetizes the domain name using the escaped or Punycoded value, which is the format that Amazon Route 53 saves in its database. For example, to create a hosted zone for exÃ¤mple.com, you specify ex344mple.com for the domain name. `ListHostedZonesByName` alphabetizes it as:

`com.ex\344mple.`

The labels are reversed and alphabetized using the escaped value. For more information about valid domain name formats, including internationalized domain names, see [DNS Domain Name Format](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html) in the *Amazon Route 53 Developer Guide* .

Route 53 returns up to 100 items in each response. If you have a lot of hosted zones, use the `MaxItems` parameter to list them in groups of up to 100. The response includes values that help navigate from one group of `MaxItems` hosted zones to the next:

- The `DNSName` and `HostedZoneId` elements in the response contain the values, if any, specified for the `dnsname` and `hostedzoneid` parameters in the request that produced the current response.
- The `MaxItems` element in the response contains the value, if any, that you specified for the `maxitems` parameter in the request that produced the current response.
- If the value of `IsTruncated` in the response is true, there are more hosted zones associated with the current Amazon Web Services account.  If `IsTruncated` is false, this response includes the last hosted zone that is associated with the current account. The `NextDNSName` element and `NextHostedZoneId` elements are omitted from the response.
- The `NextDNSName` and `NextHostedZoneId` elements in the response contain the domain name and the hosted zone ID of the next hosted zone that is associated with the current Amazon Web Services account. If you want to list more hosted zones, make another call to `ListHostedZonesByName` , and specify the value of `NextDNSName` and `NextHostedZoneId` in the `dnsname` and `hostedzoneid` parameters, respectively.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHostedZonesByName)

## Synopsis

```
list-hosted-zones-by-name
[--dns-name <value>]
[--hosted-zone-id <value>]
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

`--dns-name` (string)

(Optional) For your first request to `ListHostedZonesByName` , include the `dnsname` parameter only if you want to specify the name of the first hosted zone in the response. If you donât include the `dnsname` parameter, Amazon Route 53 returns all of the hosted zones that were created by the current Amazon Web Services account, in ASCII order. For subsequent requests, include both `dnsname` and `hostedzoneid` parameters. For `dnsname` , specify the value of `NextDNSName` from the previous response.

`--hosted-zone-id` (string)

(Optional) For your first request to `ListHostedZonesByName` , do not include the `hostedzoneid` parameter.

If you have more hosted zones than the value of `maxitems` , `ListHostedZonesByName` returns only the first `maxitems` hosted zones. To get the next group of `maxitems` hosted zones, submit another request to `ListHostedZonesByName` and include both `dnsname` and `hostedzoneid` parameters. For the value of `hostedzoneid` , specify the value of the `NextHostedZoneId` element from the previous response.

`--max-items` (string)

The maximum number of hosted zones to be included in the response body for this request. If you have more than `maxitems` hosted zones, then the value of the `IsTruncated` element in the response is true, and the values of `NextDNSName` and `NextHostedZoneId` specify the first hosted zone in the next group of `maxitems` hosted zones.

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

The following command lists up to 100 hosted zones ordered by domain name:

```
aws route53 list-hosted-zones-by-name
```

Output:

```
{
  "HostedZones": [
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "test20150527-2",
          "Config": {
              "Comment": "test2",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z119WBBTVP5WFX",
          "Name": "2.example.com."
      },
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "test20150527-1",
          "Config": {
              "Comment": "test",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z3P5QSUBK4POTI",
          "Name": "www.example.com."
      }
  ],
  "IsTruncated": false,
  "MaxItems": "100"
}
```

The following command lists hosted zones ordered by name, beginning with `www.example.com`:

```
aws route53 list-hosted-zones-by-name --dns-name www.example.com
```

Output:

```
{
  "HostedZones": [
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "mwunderl20150527-1",
          "Config": {
              "Comment": "test",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z3P5QSUBK4POTI",
          "Name": "www.example.com."
      }
  ],
  "DNSName": "www.example.com",
  "IsTruncated": false,
  "MaxItems": "100"
}
```

## Output

HostedZones -> (list)

A complex type that contains general information about the hosted zone.

(structure)

A complex type that contains general information about the hosted zone.

Id -> (string)

The ID that Amazon Route 53 assigned to the hosted zone when you created it.

Name -> (string)

The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.

For information about how to specify characters other than `a-z` , `0-9` , and `-` (hyphen) and how to specify internationalized domain names, see [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html) .

CallerReference -> (string)

The value that you specified for `CallerReference` when you created the hosted zone.

Config -> (structure)

A complex type that includes the `Comment` and `PrivateZone` elements. If you omitted the `HostedZoneConfig` and `Comment` elements from the request, the `Config` and `Comment` elements donât appear in the response.

Comment -> (string)

Any comments that you want to include about the hosted zone.

PrivateZone -> (boolean)

A value that indicates whether this is a private hosted zone.

ResourceRecordSetCount -> (long)

The number of resource record sets in the hosted zone.

LinkedService -> (structure)

If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you canât edit or delete it using Route 53.

ServicePrincipal -> (string)

If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you canât edit or delete it using Amazon Route 53.

Description -> (string)

If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you canât edit or delete it using Amazon Route 53.

DNSName -> (string)

For the second and subsequent calls to `ListHostedZonesByName` , `DNSName` is the value that you specified for the `dnsname` parameter in the request that produced the current response.

HostedZoneId -> (string)

The ID that Amazon Route 53 assigned to the hosted zone when you created it.

IsTruncated -> (boolean)

A flag that indicates whether there are more hosted zones to be listed. If the response was truncated, you can get the next group of `maxitems` hosted zones by calling `ListHostedZonesByName` again and specifying the values of `NextDNSName` and `NextHostedZoneId` elements in the `dnsname` and `hostedzoneid` parameters.

NextDNSName -> (string)

If `IsTruncated` is true, the value of `NextDNSName` is the name of the first hosted zone in the next group of `maxitems` hosted zones. Call `ListHostedZonesByName` again and specify the value of `NextDNSName` and `NextHostedZoneId` in the `dnsname` and `hostedzoneid` parameters, respectively.

This element is present only if `IsTruncated` is `true` .

NextHostedZoneId -> (string)

If `IsTruncated` is `true` , the value of `NextHostedZoneId` identifies the first hosted zone in the next group of `maxitems` hosted zones. Call `ListHostedZonesByName` again and specify the value of `NextDNSName` and `NextHostedZoneId` in the `dnsname` and `hostedzoneid` parameters, respectively.

This element is present only if `IsTruncated` is `true` .

MaxItems -> (string)

The value that you specified for the `maxitems` parameter in the call to `ListHostedZonesByName` that produced the current response.