# gcloud compute packet-mirrorings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update)*

**NAME**

: **gcloud compute packet-mirrorings update - update a Compute Engine packet mirroring policy**

**SYNOPSIS**

: **`gcloud compute packet-mirrorings update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--async)`] [`[--collector-ilb](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--collector-ilb)`=`COLLECTOR_ILB`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--description)`=`DESCRIPTION`] [`[--enable](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--enable)`] [`[--filter-direction](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--filter-direction)`=`DIRECTION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--region)`=`REGION`] [`[--add-filter-cidr-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--add-filter-cidr-ranges)`=[`CIDR_RANGE`,…]     | `[--clear-filter-cidr-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--clear-filter-cidr-ranges)`     | `[--remove-filter-cidr-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--remove-filter-cidr-ranges)`=[`CIDR_RANGE`,…]     | `[--set-filter-cidr-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--set-filter-cidr-ranges)`=[`CIDR_RANGE`,…]] [`[--add-filter-protocols](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--add-filter-protocols)`=[`PROTOCOL`,…]     | `[--clear-filter-protocols](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--clear-filter-protocols)`     | `[--remove-filter-protocols](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--remove-filter-protocols)`=[`PROTOCOL`,…]     | `[--set-filter-protocols](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--set-filter-protocols)`=[`PROTOCOL`,…]] [`[--add-mirrored-instances](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--add-mirrored-instances)`=[`INSTANCE`,…]     | `[--clear-mirrored-instances](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--clear-mirrored-instances)`     | `[--remove-mirrored-instances](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--remove-mirrored-instances)`=[`INSTANCE`,…]     | `[--set-mirrored-instances](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--set-mirrored-instances)`=[`INSTANCE`,…]] [`[--add-mirrored-subnets](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--add-mirrored-subnets)`=[`SUBNET`,…]     | `[--clear-mirrored-subnets](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--clear-mirrored-subnets)`     | `[--remove-mirrored-subnets](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--remove-mirrored-subnets)`=[`SUBNET`,…]     | `[--set-mirrored-subnets](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--set-mirrored-subnets)`=[`SUBNET`,…]] [`[--add-mirrored-tags](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--add-mirrored-tags)`=[`TAG`,…]     | `[--clear-mirrored-tags](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--clear-mirrored-tags)`     | `[--remove-mirrored-tags](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--remove-mirrored-tags)`=[`TAG`,…]     | `[--set-mirrored-tags](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#--set-mirrored-tags)`=[`TAG`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Compute Engine packet mirroring policy.

**EXAMPLES**

: Stop mirroring by tags, add subnet-1 as a mirrored subnet.

```
gcloud compute packet-mirrorings update my-pm --region us-central1 --clear-mirrored-tags --add-mirrored-subnets subnet-1
```

Change the load-balancer to send mirrored traffic to.

```
gcloud compute packet-mirrorings update my-pm --region us-central1 --collector-ilb new-forwarding-rule
```

Disable a Packet Mirroring policy.

```
gcloud compute packet-mirrorings update my-pm --region us-central1 --no-enable
```

Re-enable a disabled Packet Mirroring policy.

```
gcloud compute packet-mirrorings update my-pm --region us-central1 --enable
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the packet mirroring to update.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--collector-ilb**:
Forwarding rule configured as collector. This must be a regional forwarding rule
(in the same region) with load balancing scheme INTERNAL and
isMirroringCollector set to true.
You can provide this as the full URL to the forwarding rule, partial URL, or
name. For example, the following are valid values:

- [https://compute.googleapis.com/compute/v1/projects/myproject/](https://compute.googleapis.com/compute/v1/projects/myproject/)
regions/us-central1/forwardingRules/fr-1
- projects/myproject/regions/us-central1/forwardingRules/fr-1
- fr-1

**--description**:
Optional, textual description for the packet mirroring.

**--enable**:
Enable or disable the packet-mirroring.

**--filter-direction**:
- For `ingress`, only ingress traffic is mirrored.
- For `egress`, only egress traffic is mirrored.
- For `both` (default), both directions are mirrored.
`DIRECTION` must be one of: `both`,
`egress`, `ingress`.

**--region**:
Region of the packet mirroring to update. Overrides the default
`compute/region` property value for this command invocation.

**--add-filter-cidr-ranges**

**--add-filter-protocols**

**--add-mirrored-instances**

**--add-mirrored-subnets**

**--add-mirrored-tags**

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
gcloud alpha compute packet-mirrorings update
```

```
gcloud beta compute packet-mirrorings update
```