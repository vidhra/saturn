# gcloud compute firewall-rules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update)*

**NAME**

: **gcloud compute firewall-rules update - update a firewall rule**

**SYNOPSIS**

: **`gcloud compute firewall-rules update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#NAME)` [`[--allow](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--allow)`=[`PROTOCOL`[:`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#PORT)`[-`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#PORT)`]],…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--description)`=`DESCRIPTION`] [`[--destination-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--destination-ranges)`=[`CIDR_RANGE`,…]] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--disabled)`] [`[--[no-]enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--[no-]enable-logging)`] [`[--logging-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--logging-metadata)`=`LOGGING_METADATA`] [`[--priority](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--priority)`=`PRIORITY`] [`[--rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--rules)`=[`PROTOCOL`[:`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#PORT)`[-`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#PORT)`]],…]] [`[--source-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--source-ranges)`=[`CIDR_RANGE`,…]] [`[--source-service-accounts](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--source-service-accounts)`=[`EMAIL`,…]] [`[--source-tags](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--source-tags)`=[`TAG`,…]] [`[--target-service-accounts](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--target-service-accounts)`=[`EMAIL`,…]] [`[--target-tags](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#--target-tags)`=[`TAG`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute firewall-rules update` is used to update firewall
rules that allow/deny incoming/outgoing traffic. The firewall rule will only be
updated for arguments that are specifically passed. Other attributes will remain
unaffected. The `action` flag (whether to allow or deny matching
traffic) cannot be defined when updating a firewall rule; use `[gcloud compute
firewall-rules delete](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/delete)` to remove the rule instead.

**EXAMPLES**

: To update the firewall rule ``RULE`` to enable
logging, run:

```
gcloud compute firewall-rules update RULE --enable-logging
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the firewall rule to update.

**FLAGS**

: **--allow**:
A list of protocols and ports whose traffic will be allowed.
The protocols allowed over this connection. This can be the (case-sensitive)
string values `tcp`, `udp`, `icmp`,
`esp`, `ah`, `sctp`, or any IP protocol number.
An IP-based protocol must be specified for each rule. The rule applies only to
specified protocol.
For port-based protocols - `tcp`, `udp`, and
`sctp` - a list of destination ports or port ranges to which the rule
applies may optionally be specified. If no port or port range is specified, the
rule applies to all destination ports.
The ICMP protocol is supported, but there is no support for configuring ICMP
packet filtering by ICMP code.
For example, to create a rule that allows TCP traffic through port 80 and ICMP
traffic:

```
gcloud compute firewall-rules update MY-RULE --allow tcp:80,icmp
```

To create a rule that allows TCP traffic from port 20000 to 25000:

```
gcloud compute firewall-rules update MY-RULE --allow tcp:20000-25000
```

To create a rule that allows all TCP traffic:

```
gcloud compute firewall-rules update MY-RULE --allow tcp
```

Setting this will override the current values.

**--description**:
A textual description for the firewall rule. Set to an empty string to clear
existing.

**--destination-ranges**:
The firewall rule will apply to traffic that has destination IP address in these
IP address block list. The IP address blocks must be specified in CIDR format:
[http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
Setting this will override the existing destination ranges for the firewall. The
following will clear the existing destination ranges:

```
gcloud compute firewall-rules update MY-RULE --destination-ranges
```

**--disabled**:
Disable a firewall rule and stop it from being enforced in the network. If a
firewall rule is disabled, the associated network behaves as if the rule did not
exist. To enable a disabled rule, use:

```
gcloud compute firewall-rules update MY-RULE --no-disabled
```

**--[no-]enable-logging**:
Enable logging for the firewall rule. Logs will be exported to StackDriver.
Firewall logging is disabled by default. To enable logging for an existing rule,
run:

```
gcloud compute firewall-rules update MY-RULE --enable-logging
```

To disable logging on an existing rule, run:

```
gcloud compute firewall-rules update MY-RULE --no-enable-logging
```

Use `--enable-logging` to enable and `--no-enable-logging`
to disable.

**--logging-metadata**:
Adds or removes metadata fields to or from the reported firewall logs. Can only
be specified if --enable-logging is true.
`LOGGING_METADATA` must be one of:
`exclude-all`, `include-all`.

**--priority**:
This is an integer between 0 and 65535, both inclusive. When NOT specified, the
value assumed is 1000. Relative priority determines precedence of conflicting
rules: lower priority values imply higher precedence. DENY rules take precedence
over ALLOW rules having equal priority.

**--rules**:
A list of protocols and ports to which the firewall rule will apply.
PROTOCOL is the IP protocol whose traffic will be checked. PROTOCOL can be
either the name of a well-known protocol (e.g., tcp or icmp) or the IP protocol
number. A list of IP protocols can be found at [http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)
A port or port range can be specified after PROTOCOL to which the firewall rule
apply on traffic through specific ports. If no port or port range is specified,
connections through all ranges are applied. TCP and UDP rules must include a
port or port range.
Setting this will override the current values.

**--source-ranges**:
A list of IP address blocks that are allowed to make inbound connections that
match the firewall rule to the instances on the network. The IP address blocks
must be specified in CIDR format: [http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
If neither --source-ranges nor --source-tags are specified, --source-ranges
defaults to `0.0.0.0/0`, which means that the rule applies to all
incoming IPv4 connections from inside or outside the network. If both
--source-ranges and --source-tags are specified, the rule matches if either the
range of the source matches --source-ranges or the tag of the source matches
--source-tags.
Setting this will override the existing source ranges for the firewall. The
following will clear the existing source ranges:

```
gcloud compute firewall-rules update MY-RULE --source-ranges
```

**--source-service-accounts**:
The email of a service account indicating the set of instances on the network
which match a traffic source in the firewall rule.
If a source service account is specified then neither source tags nor target
tags can also be specified.
Setting this will override the existing source service accounts for the
firewall. The following will clear the existing source service accounts:

```
gcloud compute firewall-rules update MY-RULE --source-service-accounts
```

**--source-tags**:
A list of instance tags indicating the set of instances on the network to which
the rule applies if all other fields match. If neither --source-ranges nor
--source-tags are specified, --source-ranges defaults to `0.0.0.0/0`,
which means that the rule applies to all incoming IPv4 connections from inside
or outside the network.
If both --source-ranges and --source-tags are specified, an inbound connection
is allowed if either the range of the source matches --source-ranges or the tag
of the source matches --source-tags.
Tags can be assigned to instances during instance creation.
If source tags are specified then neither a source nor target service account
can also be specified.
Setting this will override the existing source tags for the firewall. The
following will clear the existing source tags:

```
gcloud compute firewall-rules update MY-RULE --source-tags
```

**--target-service-accounts**:
The email of a service account indicating the set of instances to which firewall
rules apply. If both target tags and target service account are omitted, the
firewall rule is applied to all instances on the network.
If a target service account is specified then neither source tag nor target tags
can also be specified.
Setting this will override the existing target service accounts for the
firewall. The following will clear the existing target service accounts:

```
gcloud compute firewall-rules update MY-RULE --target-service-accounts
```

**--target-tags**:
List of instance tags indicating the set of instances on the network which may
accept connections that match the firewall rule. Note that tags can be assigned
to instances during instance creation.
If target tags are specified, then neither a source nor target service account
can also be specified.
If both target tags and target service account are omitted, all instances on the
network can receive connections that match the rule.
Setting this will override the existing target tags for the firewall. The
following will clear the existing target tags:

```
gcloud compute firewall-rules update MY-RULE --target-tags
```

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
gcloud alpha compute firewall-rules update
```

```
gcloud beta compute firewall-rules update
```