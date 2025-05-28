# gcloud dns policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/policies/update](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update)*

**NAME**

: **gcloud dns policies update - update an existing Cloud DNS policy**

**SYNOPSIS**

: **`gcloud dns policies update` `[POLICY](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update#POLICY)` [`[--alternative-name-servers](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update#--alternative-name-servers)`=[`NAME_SERVERS`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update#--description)`=`DESCRIPTION`] [`[--enable-inbound-forwarding](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update#--enable-inbound-forwarding)`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update#--enable-logging)`] [`[--networks](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update#--networks)`=[`NETWORKS`,…]] [`[--private-alternative-name-servers](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update#--private-alternative-name-servers)`=[`NAME_SERVERS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing Cloud DNS policy.

**EXAMPLES**

: To change the description of a policy, run:

```
gcloud dns policies update mypolicy --description="Hello, world!"
```

**POSITIONAL ARGUMENTS**

: **Policy resource - The policy to update. This represents a Cloud resource. (NOTE)
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

**FLAGS**

: **--alternative-name-servers**:
List of alternative name servers to forward to. Non-RFC1918 addresses will
forward to the target through the Internet.RFC1918 addresses will forward
through the VPC.

**--description**:
A description of the policy.

**--enable-inbound-forwarding**:
Specifies whether to allow networks bound to this policy to receive DNS queries
sent by VMs or applications over VPN connections. Defaults to False.

**--enable-logging**:
Specifies whether to enable query logging. Defaults to False.

**--networks**:
The comma separated list of network names to associate with the policy.

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
gcloud alpha dns policies update
```

```
gcloud beta dns policies update
```