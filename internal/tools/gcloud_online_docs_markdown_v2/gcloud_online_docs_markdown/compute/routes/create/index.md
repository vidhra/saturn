# gcloud compute routes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routes/create](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create)*

**NAME**

: **gcloud compute routes create - create a new route**

**SYNOPSIS**

: **`gcloud compute routes create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#NAME)` `[--destination-range](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--destination-range)`=`DESTINATION_RANGE` (`[--next-hop-address](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-address)`=`NEXT_HOP_ADDRESS`     | `[--next-hop-gateway](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-gateway)`=`NEXT_HOP_GATEWAY`     | `[--next-hop-ilb](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-ilb)`=`NEXT_HOP_ILB`     | `[--next-hop-instance](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-instance)`=`NEXT_HOP_INSTANCE`     | `[--next-hop-vpn-tunnel](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-vpn-tunnel)`=`NEXT_HOP_VPN_TUNNEL`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--description)`=`DESCRIPTION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--network)`=`NETWORK`; default="default"] [`[--next-hop-ilb-region](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-ilb-region)`=`NEXT_HOP_ILB_REGION`] [`[--next-hop-instance-zone](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-instance-zone)`=`NEXT_HOP_INSTANCE_ZONE`] [`[--next-hop-vpn-tunnel-region](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-vpn-tunnel-region)`=`NEXT_HOP_VPN_TUNNEL_REGION`] [`[--priority](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--priority)`=`PRIORITY`; default=1000] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#TAG)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routes create` is used to create routes. A route is a
rule that specifies how certain packets should be handled by the virtual
network. Routes are associated with virtual machine instances by tag, and the
set of routes for a particular VM is called its routing table. For each packet
leaving a virtual machine, the system searches that machine's routing table for
a single best matching route.
Routes match packets by destination IP address, preferring smaller or more
specific ranges over larger ones (see `--destination-range`). If
there is a tie, the system selects the route with the smallest priority value.
If there is still a tie, it uses the layer 3 and 4 packet headers to select just
one of the remaining matching routes. The packet is then forwarded as specified
by `--next-hop-address`, `--next-hop-instance`,
`--next-hop-vpn-tunnel`, or `--next-hop-gateway` of the
winning route. Packets that do not match any route in the sending virtual
machine routing table will be dropped.
Exactly one of `--next-hop-address`, `--next-hop-gateway`,
`--next-hop-vpn-tunnel`, or `--next-hop-instance` must be
provided with this command.

**EXAMPLES**

: To create a route with the name 'route-name' with destination range '0.0.0.0/0'
and with next hop gateway 'default-internet-gateway', run:

```
gcloud compute routes create route-name --destination-range=0.0.0.0/0 --next-hop-gateway=default-internet-gateway
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the route to create.

**REQUIRED FLAGS**

: **--destination-range**:
The destination range of outgoing packets that the route will apply to. To match
all traffic, use ``0.0.0.0/0´´.

**--next-hop-address**

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the route.

**--network**:
Specifies the network to which the route will be applied.

**--next-hop-ilb-region**:
The region of the next hop forwarding rule. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--next-hop-instance-zone**:
The zone of the next hop instance. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

**--next-hop-vpn-tunnel-region**:
The region of the next hop vpn tunnel. If not specified, you might be prompted
to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--priority**:
Specifies the priority of this route relative to other routes with the same
specificity. The lower the value, the higher the priority.

**--tags**:
Identifies the set of instances that this route will apply to. If no tags are
provided, the route will apply to all instances in the network.

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
gcloud alpha compute routes create
```

```
gcloud beta compute routes create
```