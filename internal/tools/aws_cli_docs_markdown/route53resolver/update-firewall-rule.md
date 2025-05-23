# update-firewall-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html#cli-aws-route53resolver) ]

# update-firewall-rule

## Description

Updates the specified firewall rule.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53resolver-2018-04-01/UpdateFirewallRule)

## Synopsis

```
update-firewall-rule
--firewall-rule-group-id <value>
[--firewall-domain-list-id <value>]
[--firewall-threat-protection-id <value>]
[--priority <value>]
[--action <value>]
[--block-response <value>]
[--block-override-domain <value>]
[--block-override-dns-type <value>]
[--block-override-ttl <value>]
[--name <value>]
[--firewall-domain-redirection-action <value>]
[--qtype <value>]
[--dns-threat-protection <value>]
[--confidence-threshold <value>]
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

`--firewall-rule-group-id` (string)

The unique identifier of the firewall rule group for the rule.

`--firewall-domain-list-id` (string)

The ID of the domain list to use in the rule.

`--firewall-threat-protection-id` (string)

The DNS Firewall Advanced rule ID.

`--priority` (integer)

The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.

You must specify a unique priority for each rule in a rule group. To make it easier to insert rules later, leave space between the numbers, for example, use 100, 200, and so on. You can change the priority setting for the rules in a rule group at any time.

`--action` (string)

The action that DNS Firewall should take on a DNS query when it matches one of the domains in the ruleâs domain list, or a threat in a DNS Firewall Advanced rule:

- `ALLOW` - Permit the request to go through. Not available for DNS Firewall Advanced rules.
- `ALERT` - Permit the request to go through but send an alert to the logs.
- `BLOCK` - Disallow the request. This option requires additional details in the ruleâs `BlockResponse` .

Possible values:

- `ALLOW`
- `BLOCK`
- `ALERT`

`--block-response` (string)

The way that you want DNS Firewall to block the request. Used for the rule action setting `BLOCK` .

- `NODATA` - Respond indicating that the query was successful, but no response is available for it.
- `NXDOMAIN` - Respond indicating that the domain name thatâs in the query doesnât exist.
- `OVERRIDE` - Provide a custom override in the response. This option requires custom handling details in the ruleâs `BlockOverride*` settings.

Possible values:

- `NODATA`
- `NXDOMAIN`
- `OVERRIDE`

`--block-override-domain` (string)

The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE` .

`--block-override-dns-type` (string)

The DNS recordâs type. This determines the format of the record value that you provided in `BlockOverrideDomain` . Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE` .

Possible values:

- `CNAME`

`--block-override-ttl` (integer)

The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE` .

`--name` (string)

The name of the rule.

`--firewall-domain-redirection-action` (string)

How you want the the rule to evaluate DNS redirection in the DNS redirection chain, such as CNAME or DNAME.

`INSPECT_REDIRECTION_DOMAIN` : (Default) inspects all domains in the redirection chain. The individual domains in the redirection chain must be added to the domain list.

`TRUST_REDIRECTION_DOMAIN` : Inspects only the first domain in the redirection chain. You donât need to add the subsequent domains in the domain in the redirection list to the domain list.

Possible values:

- `INSPECT_REDIRECTION_DOMAIN`
- `TRUST_REDIRECTION_DOMAIN`

`--qtype` (string)

The DNS query type you want the rule to evaluate. Allowed values are;

- A: Returns an IPv4 address.
- AAAA: Returns an Ipv6 address.
- CAA: Restricts CAs that can create SSL/TLS certifications for the domain.
- CNAME: Returns another domain name.
- DS: Record that identifies the DNSSEC signing key of a delegated zone.
- MX: Specifies mail servers.
- NAPTR: Regular-expression-based rewriting of domain names.
- NS: Authoritative name servers.
- PTR: Maps an IP address to a domain name.
- SOA: Start of authority record for the zone.
- SPF: Lists the servers authorized to send emails from a domain.
- SRV: Application specific values that identify servers.
- TXT: Verifies email senders and application-specific values.
- A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65334, for example, TYPE28. For more information, see [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types) .

### Note

If you set up a firewall BLOCK rule with action NXDOMAIN on query type equals AAAA, this action will not be applied to synthetic IPv6 addresses generated when DNS64 is enabled.

`--dns-threat-protection` (string)

The type of the DNS Firewall Advanced rule. Valid values are:

- `DGA` : Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to to launch malware attacks.
- `DNS_TUNNELING` : DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.

Possible values:

- `DGA`
- `DNS_TUNNELING`

`--confidence-threshold` (string)

The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule. The confidence level values mean:

- `LOW` : Provides the highest detection rate for threats, but also increases false positives.
- `MEDIUM` : Provides a balance between detecting threats and false positives.
- `HIGH` : Detects only the most well corroborated threats with a low rate of false positives.

Possible values:

- `LOW`
- `MEDIUM`
- `HIGH`

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

**To update a firewall rule**

The following `update-firewall-rule` example updates a firewall rule with the parameters you specify.

```
aws route53resolver update-firewall-rule \
    --firewall-rule-group-id rslvr-frg-47f93271fexample \
    --firewall-domain-list-id rslvr-fdl-9e956e9ffexample \
    --priority 102
```

Output:

```
{
    "FirewallRule": {
        "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
        "FirewallDomainListId": "rslvr-fdl-9e956e9ffexample",
        "Name": "allow-rule",
        "Priority": 102,
        "Action": "ALLOW",
        "CreatorRequestId": "d81e3fb7-020b-415e-939f-EXAMPLE11111",
        "CreationTime": "2021-05-25T21:44:00.346093Z",
        "ModificationTime": "2021-05-25T21:45:59.611600Z"
    }
}
```

For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html) in the *Amazon Route 53 Developer Guide*.

## Output

FirewallRule -> (structure)

The firewall rule that you just updated.

FirewallRuleGroupId -> (string)

The unique identifier of the Firewall rule group of the rule.

FirewallDomainListId -> (string)

The ID of the domain list thatâs used in the rule.

FirewallThreatProtectionId -> (string)

ID of the DNS Firewall Advanced rule.

Name -> (string)

The name of the rule.

Priority -> (integer)

The priority of the rule in the rule group. This value must be unique within the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.

Action -> (string)

The action that DNS Firewall should take on a DNS query when it matches one of the domains in the ruleâs domain list, or a threat in a DNS Firewall Advanced rule:

- `ALLOW` - Permit the request to go through. Not available for DNS Firewall Advanced rules.
- `ALERT` - Permit the request to go through but send an alert to the logs.
- `BLOCK` - Disallow the request. If this is specified, additional handling details are provided in the ruleâs `BlockResponse` setting.

BlockResponse -> (string)

The way that you want DNS Firewall to block the request. Used for the rule action setting `BLOCK` .

- `NODATA` - Respond indicating that the query was successful, but no response is available for it.
- `NXDOMAIN` - Respond indicating that the domain name thatâs in the query doesnât exist.
- `OVERRIDE` - Provide a custom override in the response. This option requires custom handling details in the ruleâs `BlockOverride*` settings.

BlockOverrideDomain -> (string)

The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE` .

BlockOverrideDnsType -> (string)

The DNS recordâs type. This determines the format of the record value that you provided in `BlockOverrideDomain` . Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE` .

BlockOverrideTtl -> (integer)

The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE` .

CreatorRequestId -> (string)

A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of executing the operation twice. This can be any unique string, for example, a timestamp.

CreationTime -> (string)

The date and time that the rule was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime -> (string)

The date and time that the rule was last modified, in Unix time format and Coordinated Universal Time (UTC).

FirewallDomainRedirectionAction -> (string)

How you want the the rule to evaluate DNS redirection in the DNS redirection chain, such as CNAME or DNAME.

`INSPECT_REDIRECTION_DOMAIN` : (Default) inspects all domains in the redirection chain. The individual domains in the redirection chain must be added to the domain list.

`TRUST_REDIRECTION_DOMAIN` : Inspects only the first domain in the redirection chain. You donât need to add the subsequent domains in the domain in the redirection list to the domain list.

Qtype -> (string)

The DNS query type you want the rule to evaluate. Allowed values are;

- A: Returns an IPv4 address.
- AAAA: Returns an Ipv6 address.
- CAA: Restricts CAs that can create SSL/TLS certifications for the domain.
- CNAME: Returns another domain name.
- DS: Record that identifies the DNSSEC signing key of a delegated zone.
- MX: Specifies mail servers.
- NAPTR: Regular-expression-based rewriting of domain names.
- NS: Authoritative name servers.
- PTR: Maps an IP address to a domain name.
- SOA: Start of authority record for the zone.
- SPF: Lists the servers authorized to send emails from a domain.
- SRV: Application specific values that identify servers.
- TXT: Verifies email senders and application-specific values.
- A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65334, for example, TYPE28. For more information, see [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types) .

DnsThreatProtection -> (string)

The type of the DNS Firewall Advanced rule. Valid values are:

- `DGA` : Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to to launch malware attacks.
- `DNS_TUNNELING` : DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.

ConfidenceThreshold -> (string)

The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule. The confidence level values mean:

- `LOW` : Provides the highest detection rate for threats, but also increases false positives.
- `MEDIUM` : Provides a balance between detecting threats and false positives.
- `HIGH` : Detects only the most well corroborated threats with a low rate of false positives.