# gcloud vmware network-policies external-access-rules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update)*

**NAME**

: **gcloud vmware network-policies external-access-rules update - update a VMware Engine network policy**

**SYNOPSIS**

: **`gcloud vmware network-policies external-access-rules update` (`[EXTERNAL_ACCESS_RULE](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#EXTERNAL_ACCESS_RULE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--location)`=`LOCATION` `[--network-policy](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--network-policy)`=`NETWORK_POLICY`) [`[--action](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--action)`=`ACTION`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--description)`=`DESCRIPTION`] [`[--destination-ports](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--destination-ports)`=`DESTINATION_PORTS`,[…]] [`[--destination-ranges](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--destination-ranges)`=`DESTINATION_IP_RANGES`,[…]] [`[--ip-protocol](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--ip-protocol)`=`IP_PROTOCOL`] [`[--priority](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--priority)`=`PRIORITY`] [`[--source-ports](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--source-ports)`=`SOURCE_PORTS`,[…]] [`[--source-ranges](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#--source-ranges)`=`SOURCE_IP_RANGES`,[…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a VMware Engine external access firewall rule.

**EXAMPLES**

: To update an external access firewall rule named
`my-external-access-rule` so that it denies the traffic for that
rule, run:

```
gcloud vmware network-policies external-access-rules update my-external-access-rule --network-policy=my-network-policy --action=DENY --location=us-west2 --project=my-project
```

Or:

```
gcloud vmware network-policies external-access-rules update my-external-access-rule --network-policy=my-network-policy --action=DENY
```

In the second example, the project and the location are taken from gcloud
properties core/project and compute/regions respectively.

**POSITIONAL ARGUMENTS**

: **VMware Engine External Access Rule resource - external_access_rule. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `external_access_rule` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`EXTERNAL_ACCESS_RULE`**:
ID of the VMware Engine External Access Rule or fully qualified identifier for
the VMware Engine External Access Rule.
To set the `external-access-rule` attribute:

- provide the argument `external_access_rule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The resource name of the location.
To set the `location` attribute:

- provide the argument `external_access_rule` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/region`.

**--network-policy**:
VMware Engine network policy
To set the `network-policy` attribute:

- provide the argument `external_access_rule` on the command line with
a fully specified name;
- provide the argument `--network-policy` on the command line.**

**FLAGS**

: **--action**:
Whether the firewall rule allows or denies traffic based on a successful rule
match. `ACTION` must be one of: `ALLOW`,
`DENY`.

**--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
User-provided description of the external access rule.

**--destination-ports**:
List of allowed destination ports. Each entry must be either an integer or a
range.

**--destination-ranges**:
A list of destination IP addresses that the rule applies to. Each entry in the
list be an ExternalAddress resource name or `0.0.0.0/0`. When the
value is set to `0.0.0.0/0`, all IP addresses are allowed.

**--ip-protocol**:
Internet protocol covered by the rule. Valid values are TCP, UDP, and ICMP.
`IP_PROTOCOL` must be one of: `TCP`,
`UDP`, `ICMP`.

**--priority**:
Priority of this external access rule. Valid values are numbers between 100 and
4096, with 100 being the highest priority. Firewall rules are processed from
highest to lowest priority.

**--source-ports**:
List of allowed source ports. Each entry must be either an integer or a range.

**--source-ranges**:
A list of source IP addresses that the rule applies to. Each entry in the list
can be a CIDR notation or a single IP address. When the value is set to
`0.0.0.0/0`, all IP addresses are allowed.

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