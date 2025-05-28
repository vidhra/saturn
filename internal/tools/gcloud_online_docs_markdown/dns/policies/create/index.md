# gcloud dns policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/policies/create](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create)*

**NAME**

: **gcloud dns policies create - creates a new Cloud DNS policy**

**SYNOPSIS**

: **`gcloud dns policies create` `[POLICY](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create#POLICY)` `[--description](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create#--description)`=`DESCRIPTION` `[--networks](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create#--networks)`=[`NETWORKS`,…] [`[--alternative-name-servers](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create#--alternative-name-servers)`=[`NAME_SERVERS`,…]] [`[--enable-inbound-forwarding](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create#--enable-inbound-forwarding)`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create#--enable-logging)`] [`[--private-alternative-name-servers](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create#--private-alternative-name-servers)`=[`NAME_SERVERS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a new Cloud DNS policy.

**EXAMPLES**

: To create a new policy with minimal arguments, run:

```
gcloud dns policies create mypolicy --description='My new policy test policy 5' --networks=''
```

To create a new policy with all optional arguments, run:

```
gcloud dns policies create mypolicy --description='My new policy test policy 5' --networks=network1,network2 --alternative-name-servers=192.168.1.1,192.168.1.2 --enable-inbound-forwarding --enable-logging
```

**POSITIONAL ARGUMENTS**

: **Policy resource - The policy to create. This represents a Cloud resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `policy` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**`POLICY`**:
ID of the policy or fully qualified identifier for the policy.
To set the `policy` attribute:

- provide the argument `policy` on the command line.**

**REQUIRED FLAGS**

: **--description**:
A description of the policy.

**--networks**:
The comma separated list of network names to associate with the policy.

**OPTIONAL FLAGS**

: **--alternative-name-servers**:
List of alternative name servers to forward to. Non-RFC1918 addresses will
forward to the target through the Internet.RFC1918 addresses will forward
through the VPC.

**--enable-inbound-forwarding**:
Specifies whether to allow networks bound to this policy to receive DNS queries
sent by VMs or applications over VPN connections. Defaults to False.

**--enable-logging**:
Specifies whether to enable query logging. Defaults to False.

**--private-alternative-name-servers**:
List of alternative name servers to forward to. All addresses specified for this
parameter will be reached through the VPC.

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
gcloud alpha dns policies create
```

```
gcloud beta dns policies create
```