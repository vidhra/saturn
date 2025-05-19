# gcloud compute firewall-rules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)*

**NAME**

: **gcloud compute firewall-rules create - create a Compute Engine firewall rule**

**SYNOPSIS**

: **`gcloud compute firewall-rules create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#NAME)` (`[--action](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--action)`=`ACTION`     | `[--allow](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--allow)`=`PROTOCOL`[:`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#PORT)`[-`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#PORT)`]],[…]) [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--description)`=`DESCRIPTION`] [`[--destination-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--destination-ranges)`=`CIDR_RANGE`,[`[CIDR_RANGE](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#CIDR_RANGE)`,…]] [`[--direction](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--direction)`=`DIRECTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--disabled)`] [`[--[no-]enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--[no-]enable-logging)`] [`[--logging-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--logging-metadata)`=`LOGGING_METADATA`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--network)`=`NETWORK`; default="default"] [`[--priority](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--priority)`=`PRIORITY`] [`[--rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--rules)`=`PROTOCOL`[:`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#PORT)`[-`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#PORT)`]],[…]] [`[--source-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--source-ranges)`=`CIDR_RANGE`,[`[CIDR_RANGE](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#CIDR_RANGE)`,…]] [`[--source-service-accounts](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--source-service-accounts)`=`EMAIL`,[`[EMAIL](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#EMAIL)`,…]] [`[--source-tags](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--source-tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#TAG)`,…]] [`[--target-service-accounts](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--target-service-accounts)`=`EMAIL`,[`[EMAIL](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#EMAIL)`,…]] [`[--target-tags](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--target-tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#TAG)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute firewall-rules create` is used to create firewall
rules to allow/deny incoming/outgoing traffic.

**EXAMPLES**

: To create a firewall rule allowing incoming TCP traffic on port 8080, run:

```
gcloud compute firewall-rules create example-service --allow=tcp:8080 --description="Allow incoming traffic on TCP port 8080" --direction=INGRESS
```

To create a firewall rule that allows TCP traffic through port 80 and determines
a list of specific IP address blocks that are allowed to make inbound
connections, run:

```
gcloud compute firewall-rules create tcp-rule --allow=tcp:80 --source-ranges="10.0.0.0/22,10.0.0.0/14" --description="Narrowing TCP traffic"
```

To list existing firewall rules, run:

```
gcloud compute firewall-rules list
```

For more detailed examples see [https://cloud.google.com/vpc/docs/using-firewalls](https://cloud.google.com/vpc/docs/using-firewalls)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the firewall rule to create.

**REQUIRED FLAGS**

: **--action**

**OPTIONAL FLAGS**

: **--description**:
A textual description for the firewall rule.

**--destination-ranges**:
The firewall rule will apply to traffic that has destination IP address in these
IP address block list. The IP address blocks must be specified in CIDR format:
[http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
If --destination-ranges is NOT provided, then this flag will default to
0.0.0.0/0, allowing all IPv4 destinations. Multiple IP address blocks can be
specified if they are separated by commas.

**--direction**:
If direction is NOT specified, then default is to apply on incoming traffic. For
outbound traffic, it is NOT supported to specify source-tags.
For convenience, 'IN' can be used to represent ingress direction and 'OUT' can
be used to represent egress direction.
`DIRECTION` must be one of: `INGRESS`,
`EGRESS`, `IN`, `OUT`.

**--disabled**:
Disable a firewall rule and stop it from being enforced in the network. If a
firewall rule is disabled, the associated network behaves as if the rule did not
exist. To enable a disabled rule, use:

```
gcloud compute firewall-rules update MY-RULE --no-disabled
```

Firewall rules are enabled by default.

**--[no-]enable-logging**:
Enable logging for the firewall rule. Logs will be exported to StackDriver.
Firewall logging is disabled by default. To enable logging for an existing rule,
run:

```
gcloud compute firewall-rules create MY-RULE --enable-logging
```

To disable logging on an existing rule, run:

```
gcloud compute firewall-rules create MY-RULE --no-enable-logging
```

Use `--enable-logging` to enable and `--no-enable-logging`
to disable.

**--logging-metadata**:
Adds or removes metadata fields to or from the reported firewall logs. Can only
be specified if --enable-logging is true.
`LOGGING_METADATA` must be one of:
`exclude-all`, `include-all`.

**--network**:
The network to which this rule is attached. If omitted, the rule is attached to
the ``default`` network.

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
If specified, the flag --action must also be specified.
For example, the following will create a rule that blocks TCP traffic through
port 80 and ICMP traffic:

```
gcloud compute firewall-rules create MY-RULE --action deny --rules tcp:80,icmp
```

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
Multiple IP address blocks can be specified if they are separated by commas.

**--source-service-accounts**:
The email of a service account indicating the set of instances on the network
which match a traffic source in the firewall rule.
If a source service account is specified then neither source tags nor target
tags can also be specified.

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

**--target-service-accounts**:
The email of a service account indicating the set of instances to which firewall
rules apply. If both target tags and target service account are omitted, the
firewall rule is applied to all instances on the network.
If a target service account is specified then neither source tag nor target tags
can also be specified.

**--target-tags**:
List of instance tags indicating the set of instances on the network which may
accept connections that match the firewall rule. Note that tags can be assigned
to instances during instance creation.
If target tags are specified, then neither a source nor target service account
can also be specified.
If both target tags and target service account are omitted, all instances on the
network can receive connections that match the rule.

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
gcloud alpha compute firewall-rules create
```

```
gcloud beta compute firewall-rules create
```