# gcloud vmware network-policies external-access-rules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create)*

**NAME**

: **gcloud vmware network-policies external-access-rules create - create a VMware Engine external access firewall rule**

**SYNOPSIS**

: **`gcloud vmware network-policies external-access-rules create` (`[EXTERNAL_ACCESS_RULE](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#EXTERNAL_ACCESS_RULE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--location)`=`LOCATION` `[--network-policy](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--network-policy)`=`NETWORK_POLICY`) `[--destination-ranges](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--destination-ranges)`=`DESTINATION_IP_RANGES`,[…] `[--ip-protocol](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--ip-protocol)`=`IP_PROTOCOL` `[--priority](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--priority)`=`PRIORITY` `[--source-ranges](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--source-ranges)`=`SOURCE_IP_RANGES`,[…] [`[--action](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--action)`=`ACTION`; default="ALLOW"] [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--description)`=`DESCRIPTION`] [`[--destination-ports](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--destination-ports)`=`DESTINATION_PORTS`,[…]] [`[--source-ports](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#--source-ports)`=`SOURCE_PORTS`,[…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a VMware Engine external access firewall rule. Check the progress of a
VMware Engine external access firewall rule creation using `[gcloud
vmware network-policies external-access-rules list](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list)`.

**EXAMPLES**

: To create an external access firewall rule called
`my-external-access-rule` associated with the network policy
`my-network-policy` in the `us-west2` region, run:

```
gcloud vmware network-policies external-access-rules create my-external-access-rule --network-policy=my-network-policy --priority=1000 --ip-protocol=TCP --source-ranges=34.148.30.114/32 --destination-ranges=projects/sample-project/locations/us-west2-a/privateClouds/my-private-cloud/externalAddresses/my-external-address --source-ports=22,10000-11000 --destination-ports=22 --action=ALLOW --location=us-west2 --project=sample-project
```

Or:

```
gcloud vmware network-policies external-access-rules create my-external-access-rule --network-policy=my-network-policy --priority=1000 --ip-protocol=TCP --source-ranges=34.148.30.114/32 --destination-ranges=projects/sample-project/locations/us-west2-a/privateClouds/my-private-cloud/externalAddresses/my-external-address --source-ports=22,10000-11000 --destination-ports=22
```

In the second example, the project and the location are taken from gcloud
properties core/project and compute/region respectively. The
`--action` field also isn't specified, so its value defaults to
`ALLOW`.

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

**REQUIRED FLAGS**

: **--destination-ranges**:
A list of destination IP addresses that the rule applies to. Each entry in the
list can be an ExternalAddress resource name or `0.0.0.0/0`. When the
value is set to `0.0.0.0/0`, all IP addresses are allowed.

**--ip-protocol**:
Internet protocol covered by the rule. Valid values are TCP, UDP, and ICMP.
`IP_PROTOCOL` must be one of: `TCP`,
`UDP`, `ICMP`.

**--priority**:
Priority of this external access rule. Valid values are numbers between 100 and
4096, with 100 being the highest priority. Firewall rules are processed from
highest to lowest priority.

**--source-ranges**:
A list of source IP addresses that the rule applies to. Each entry in the list
can be a CIDR notation or a single IP address. When the value is set to
`0.0.0.0/0`, all IP addresses are allowed.

**OPTIONAL FLAGS**

: **--action**:
Whether the firewall rule allows or denies traffic based on a successful rule
match. By default, the action is ALLOW. `ACTION` must be
one of: `ALLOW`, `DENY`.

**--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
User-provided description of the external access rule.

**--destination-ports**:
List of allowed destination ports. Each entry must be either an integer or a
range.

**--source-ports**:
List of allowed source ports. Each entry must be either an integer or a range.

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