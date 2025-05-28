# gcloud dns response-policies rules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update)*

**NAME**

: **gcloud dns response-policies rules update - updates a new Cloud DNS response policy rule**

**SYNOPSIS**

: **`gcloud dns response-policies rules update` (`[RESPONSE_POLICY_RULE](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update#RESPONSE_POLICY_RULE)` : `[--response-policy](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update#--response-policy)`=`RESPONSE_POLICY`) [`[--behavior](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update#--behavior)`=`BEHAVIOR`] [`[--dns-name](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update#--dns-name)`=`DNS_NAME`] [`[--local-data](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update#--local-data)`=[`LOCAL_DATA`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates a new Cloud DNS response policy rule.

**EXAMPLES**

: To update a new response policy rule with DNS name, run:

```
gcloud dns response-policies rules update myresponsepolicyrule --response-policy="myresponsepolicy" --dns-name="www.newzone.com." # pylint: disable=line-too-long
```

To update a new response policy rule with local data rrsets, run:

```
gcloud dns response-policies rules update myresponsepolicyrule --response-policy="myresponsepolicy" --local-data=name=www.zone.com.,type=A,ttl=21600,rrdatas=1.2.3.4
```

To update a new response policy rule with behavior, run:

```
gcloud dns response-policies rules update myresponsepolicyrule --response-policy="myresponsepolicy" --behavior=bypassResponsePolicy
```

**POSITIONAL ARGUMENTS**

: **Response policy rule resource - The response policy rule to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `response_policy_rule` on the command line with
a fully specified name;
- set the property `core/project`.

This must be specified.

**`RESPONSE_POLICY_RULE`**:
ID of the response_policy_rule or fully qualified identifier for the
response_policy_rule.
To set the `response-policy-rule` attribute:

- provide the argument `response_policy_rule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--response-policy**:
The Cloud DNS response policy name response_policy_rule.
To set the `response-policy` attribute:

- provide the argument `response_policy_rule` on the command line with
a fully specified name;
- provide the argument `--response-policy` on the command line.**

**FLAGS**

: **--behavior**:
The response policy rule query behavior. `BEHAVIOR` must
be one of: `behaviorUnspecified`, `bypassResponsePolicy`.

**--dns-name**:
DNS name (wildcard or exact) to apply this rule to.

**--local-data**:
All resource record sets for this selector, one per resource record type. The
name must match the dns_name.
This is a repeated argument that can be specified multiple times to specify
multiple local data rrsets. (e.g.
--local-data=name="zone.com.",type="A",ttl=21600,rrdata="1.2.3.4 "
--local-data=name="www.zone.com.",type="CNAME",ttl=21600,rrdata="1.2.3.4|5.6.7.8")

**`name`**:
The DnsName of a resource record set.

**`type`**:
Type of all resource records in this set. For example, A, AAAA, SOA, MX, NS, TXT
…

**`ttl`**:
Number of seconds that this ResourceRecordSet can be cached by resolvers.

**`rrdatas`**:
The list of datas for this record, split by "|".

**--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha dns response-policies rules update
```

```
gcloud beta dns response-policies rules update
```