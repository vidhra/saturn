# gcloud alpha compute forwarding-rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules)*

**NAME**

: **gcloud alpha compute forwarding-rules - read and manipulate traffic forwarding rules to network load balancers**

**SYNOPSIS**

: **`gcloud alpha compute forwarding-rules` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate traffic forwarding rules for load
balancers, protocol forwarding, or Classic Cloud VPN.
For more information about forwarding rules, see the [forwarding
rules documentation](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts).
See also: [Region
forwarding rules API](https://cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) and [Global
forwarding rules API](https://cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/config)`**:
`(ALPHA)` Manage traffic forwarding rule configurations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/create)`**:
`(ALPHA)` Create a forwarding rule to direct network traffic to a
load balancer.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/delete)`**:
`(ALPHA)` Delete forwarding rules.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/describe)`**:
`(ALPHA)` Display detailed information about a forwarding rule.

**`[export](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/export)`**:
`(ALPHA)` Export a forwarding rule.

**`[import](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/import)`**:
`(ALPHA)` Import a forwarding rule.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/list)`**:
`(ALPHA)` List Google Compute Engine forwarding rules.

**`[set-target](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/set-target)`**:
`(ALPHA)` Modify a forwarding rule to direct network traffic to a new
target.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/update)`**:
`(ALPHA)` Update a Compute Engine forwarding rule.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute forwarding-rules
```

```
gcloud beta compute forwarding-rules
```