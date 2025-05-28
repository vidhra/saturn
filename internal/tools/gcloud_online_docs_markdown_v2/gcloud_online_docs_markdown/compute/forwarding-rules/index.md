# gcloud compute forwarding-rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules)*

**NAME**

: **gcloud compute forwarding-rules - read and manipulate traffic forwarding rules to network load balancers**

**SYNOPSIS**

: **`gcloud compute forwarding-rules` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate traffic forwarding rules for load balancers, protocol
forwarding, or Classic Cloud VPN.
For more information about forwarding rules, see the [forwarding
rules documentation](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts).
See also: [Region
forwarding rules API](https://cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) and [Global
forwarding rules API](https://cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create)`**:
Create a forwarding rule to direct network traffic to a load balancer.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/delete)`**:
Delete forwarding rules.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe)`**:
Display detailed information about a forwarding rule.

**`[export](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/export)`**:
Export a forwarding rule.

**`[import](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/import)`**:
Import a forwarding rule.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/list)`**:
List Google Compute Engine forwarding rules.

**`[set-target](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target)`**:
Modify a forwarding rule to direct network traffic to a new target.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update)`**:
Update a Compute Engine forwarding rule.

**NOTES**

: These variants are also available:

```
gcloud alpha compute forwarding-rules
```

```
gcloud beta compute forwarding-rules
```