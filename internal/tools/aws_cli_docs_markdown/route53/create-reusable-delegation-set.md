# create-reusable-delegation-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-reusable-delegation-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-reusable-delegation-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# create-reusable-delegation-set

## Description

Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones that were created by the same Amazon Web Services account.

You can also create a reusable delegation set that uses the four name servers that are associated with an existing hosted zone. Specify the hosted zone ID in the `CreateReusableDelegationSet` request.

### Note

You canât associate a reusable delegation set with a private hosted zone.

For information about using a reusable delegation set to configure white label name servers, see [Configuring White Label Name Servers](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/white-label-name-servers.html) .

The process for migrating existing hosted zones to use a reusable delegation set is comparable to the process for configuring white label name servers. You need to perform the following steps:

- Create a reusable delegation set.
- Recreate hosted zones, and reduce the TTL to 60 seconds or less.
- Recreate resource record sets in the new hosted zones.
- Change the registrarâs name servers to use the name servers for the new hosted zones.
- Monitor traffic for the website or application.
- Change TTLs back to their original values.

If you want to migrate existing hosted zones to use a reusable delegation set, the existing hosted zones canât use any of the name servers that are assigned to the reusable delegation set. If one or more hosted zones do use one or more name servers that are assigned to the reusable delegation set, you can do one of the following:

- For small numbers of hosted zonesâup to a few hundredâitâs relatively easy to create reusable delegation sets until you get one that has four name servers that donât overlap with any of the name servers in your hosted zones.
- For larger numbers of hosted zones, the easiest solution is to use more than one reusable delegation set.
- For larger numbers of hosted zones, you can also migrate hosted zones that have overlapping name servers to hosted zones that donât have overlapping name servers, then migrate the hosted zones again to use the reusable delegation set.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateReusableDelegationSet)

## Synopsis

```
create-reusable-delegation-set
--caller-reference <value>
[--hosted-zone-id <value>]
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

`--caller-reference` (string)

A unique string that identifies the request, and that allows you to retry failed `CreateReusableDelegationSet` requests without the risk of executing the operation twice. You must use a unique `CallerReference` string every time you submit a `CreateReusableDelegationSet` request. `CallerReference` can be any unique string, for example a date/time stamp.

`--hosted-zone-id` (string)

If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone.

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

DelegationSet -> (structure)

A complex type that contains name server information.

Id -> (string)

The ID that Amazon Route 53 assigns to a reusable delegation set.

CallerReference -> (string)

The value that you specified for `CallerReference` when you created the reusable delegation set.

NameServers -> (list)

A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

(string)

Location -> (string)

The unique URL representing the new reusable delegation set.