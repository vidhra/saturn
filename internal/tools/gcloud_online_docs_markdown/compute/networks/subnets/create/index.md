# gcloud compute networks subnets create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create)*

**NAME**

: **gcloud compute networks subnets create - define a subnet for a network in custom subnet mode**

**SYNOPSIS**

: **`gcloud compute networks subnets create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#NAME)` `[--network](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--network)`=`NETWORK` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--description)`=`DESCRIPTION`] [`[--enable-flow-logs](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--enable-flow-logs)`] [`[--enable-private-ip-google-access](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--enable-private-ip-google-access)`] [`[--external-ipv6-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--external-ipv6-prefix)`=`EXTERNAL_IPV6_PREFIX`] [`[--ip-collection](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--ip-collection)`=`IP_COLLECTION`] [`[--ipv6-access-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--ipv6-access-type)`=`IPV6_ACCESS_TYPE`] [`[--logging-aggregation-interval](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--logging-aggregation-interval)`=`LOGGING_AGGREGATION_INTERVAL`] [`[--logging-filter-expr](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--logging-filter-expr)`=`LOGGING_FILTER_EXPR`] [`[--logging-flow-sampling](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--logging-flow-sampling)`=`LOGGING_FLOW_SAMPLING`] [`[--logging-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--logging-metadata)`=`LOGGING_METADATA`] [`[--logging-metadata-fields](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--logging-metadata-fields)`=[`METADATA_FIELD`,…]] [`[--private-ipv6-google-access-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--private-ipv6-google-access-type)`=`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE`] [`[--purpose](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--purpose)`=`PURPOSE`] [`[--range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--range)`=`RANGE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--region)`=`REGION`] [`[--reserved-internal-range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--reserved-internal-range)`=`RESERVED_INTERNAL_RANGE`] [`[--role](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--role)`=`ROLE`] [`[--secondary-range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--secondary-range)`=`PROPERTY`=`VALUE`,[…]] [`[--secondary-range-with-reserved-internal-range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--secondary-range-with-reserved-internal-range)`=`RANGE_NAME`=`INTERNAL_RANGE_URL`,[…]] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--stack-type)`=`STACK_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks subnets create` define a subnetwork for a
network in custom subnet mode. Subnets must be uniquely named per region.

**EXAMPLES**

: To create the subnetwork ``subnet-1`` with
address range ``10.10.0.0/24`` in the network
``network-0``, run:

```
gcloud compute networks subnets create subnet-1 --network=network-0 --range=10.10.0.0/24 --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the subnetwork to create.

**REQUIRED FLAGS**

: **--network**:
The network to which the subnetwork belongs.

**OPTIONAL FLAGS**

: **--description**:
An optional description of this subnetwork.

**--enable-flow-logs**:
Enable/disable VPC Flow Logs for this subnet. More information for VPC Flow Logs
can be found at [https://cloud.google.com/vpc/docs/using-flow-logs](https://cloud.google.com/vpc/docs/using-flow-logs).

**--enable-private-ip-google-access**:
Enable/disable access to Google Cloud APIs from this subnet for instances
without a public ip address.

**--external-ipv6-prefix**:
The /64 external IPv6 CIDR range to assign to this subnet. The range must be
associated with an IPv6 BYOIP sub-prefix that is defined by the --ip-collection
flag. If you specify --ip-collection but not --external-ipv6-prefix, a random
/64 range is allocated from the sub-prefix.
For example, `--external-ipv6-prefix=2600:1901:0:0:0:0:0:0/64`

**--ip-collection**:
Resource reference to a public delegated prefix. The PublicDelegatedPrefix must
be a sub-prefix in EXTERNAL_IPV6_SUBNETWORK_CREATION mode.

**--ipv6-access-type**:
IPv6 access type can be specified only when the subnet is created, or when the
subnet is first updated to have a stack type of IPV4_IPV6. Once set, the access
type is immutable. `IPV6_ACCESS_TYPE` must be one of:

**`EXTERNAL`**:
VMs in this subnet can have external IPv6.

**`INTERNAL`**:
VMs in this subnet can have internal IPv6.

**--logging-aggregation-interval**:
Can only be specified if VPC Flow Logs for this subnetwork is enabled. Toggles
the aggregation interval for collecting flow logs. Increasing the interval time
will reduce the amount of generated flow logs for long lasting connections.
Default is an interval of 5 seconds per connection.
`LOGGING_AGGREGATION_INTERVAL` must be one of:
`interval-10-min`, `interval-15-min`,
`interval-1-min`, `interval-30-sec`,
`interval-5-min`, `interval-5-sec`.

**--logging-filter-expr**:
Can only be specified if VPC Flow Logs for this subnetwork is enabled. Export
filter used to define which logs should be generated.

**--logging-flow-sampling**:
Can only be specified if VPC Flow Logs for this subnetwork is enabled. The value
of the field must be in [0, 1]. Set the sampling rate of VPC flow logs within
the subnetwork where 1.0 means all collected logs are reported and 0.0 means no
logs are reported. Default is 0.5 which means half of all collected logs are
reported.

**--logging-metadata**:
Can only be specified if VPC Flow Logs for this subnetwork is enabled.
Configures whether metadata fields should be added to the reported logs. Default
is to exclude all metadata. `LOGGING_METADATA` must be one
of: `custom`, `exclude-all`, `include-all`.

**--logging-metadata-fields**:
Can only be specified if VPC Flow Logs for this subnetwork is enabled and
"metadata" is set to CUSTOM_METADATA. The comma-separated list of metadata
fields that should be added to reported logs.

**--private-ipv6-google-access-type**:
The private IPv6 google access type for the VMs in this subnet.
`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE` must be one of:
`disable`, `enable-bidirectional-access`,
`enable-outbound-vm-access`.

**--purpose**:
The purpose of this subnetwork. `PURPOSE` must be one of:

**`GLOBAL_MANAGED_PROXY`**:
Reserved for Global Envoy-based Load Balancing.

**`INTERNAL_HTTPS_LOAD_BALANCER`**:
Reserved for Internal HTTP(S) Load Balancing.

**`PEER_MIGRATION`**:
Reserved for subnet migration between peered VPCs.

**`PRIVATE`**:
Regular user created or automatically created subnet.

**`PRIVATE_NAT`**:
Reserved for use as source range for Private NAT.

**`PRIVATE_SERVICE_CONNECT`**:
Reserved for Private Service Connect Internal Load Balancing.

**`REGIONAL_MANAGED_PROXY`**:
Reserved for Regional Envoy-based Load Balancing.

**--range**:
The IP space allocated to this subnetwork in CIDR format.

**--region**:
Region of the subnetwork to create. If not specified, you might be prompted to
select a region (interactive mode only).
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

**--reserved-internal-range**:
If set, the primary IP range of the subnetwork will be associated with the given
internal range resource. If --range is set, the subnetwork will only use the
given IP range, which must be contained by the IP range defined by the internal
range resource. For example, --range=10.0.0.0/24 --reserved-internal-range
//networkconnectivity.googleapis.com/projects/PROJECT/locations/global/internalRanges/RANGE
If --range is not set, the subnetwork will use the entire IP range defined by
the internal range resource. For example, `--reserved-internal-range
//networkconnectivity.googleapis.com/projects/PROJECT/locations/global/internalRanges/RANGE`

**--role**:
The role of subnetwork. This field is required when the purpose is set to
GLOBAL_MANAGED_PROXY, REGIONAL_MANAGED_PROXY or INTERNAL_HTTPS_LOAD_BALANCER.
`ROLE` must be one of:

**`ACTIVE`**:
The ACTIVE subnet that is currently used.

**`BACKUP`**:
The BACKUP subnet that could be promoted to ACTIVE.

**--secondary-range**:
Adds a secondary IP range to the subnetwork for use in IP aliasing.
For example, `--secondary-range range1=192.168.64.0/24` adds a
secondary range 192.168.64.0/24 with name range1.

- `RANGE_NAME` - Name of the secondary range.
- `RANGE` - `IP range in CIDR format.`

**--secondary-range-with-reserved-internal-range**:
Adds secondary IP ranges that are associated with internal range resources. For
example, `--secondary-range-with-reserved-internal-range
range1=//networkconnectivity.googleapis.com/projects/PROJECT/locations/global/internalRanges/RANGE`
adds a secondary range with the reserved internal range resource.

- `RANGE_NAME` - Name of the secondary range.
- `INTERNAL_RANGE_URL` - `URL of an internal range
resource.`

**--stack-type**:
The stack type for this subnet. Determines if IPv6 is enabled on the subnet. If
not specified IPV4_ONLY will be used. `STACK_TYPE` must be
one of:

**`IPV4_IPV6`**:
New VMs in this subnet can have both IPv4 and IPv6 addresses

**`IPV4_ONLY`**:
New VMs in this subnet will only be assigned IPv4 addresses

**`IPV6_ONLY`**:
New VMs in this subnet will only be assigned IPv6 addresses

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
gcloud alpha compute networks subnets create
```

```
gcloud beta compute networks subnets create
```