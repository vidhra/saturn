# gcloud compute networks subnets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update)*

**NAME**

: **gcloud compute networks subnets update - updates properties of an existing Compute Engine subnetwork**

**SYNOPSIS**

: **`gcloud compute networks subnets update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#NAME)` [`[--add-secondary-ranges-with-reserved-internal-range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--add-secondary-ranges-with-reserved-internal-range)`=`RANGE_NAME`=`INTERNAL_RANGE_URL`,[…]] [`[--drain-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--drain-timeout)`=`DRAIN_TIMEOUT`; default="0s"] [`[--external-ipv6-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--external-ipv6-prefix)`=`EXTERNAL_IPV6_PREFIX`] [`[--ip-collection](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--ip-collection)`=`IP_COLLECTION`] [`[--ipv6-access-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--ipv6-access-type)`=`IPV6_ACCESS_TYPE`] [`[--logging-aggregation-interval](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--logging-aggregation-interval)`=`LOGGING_AGGREGATION_INTERVAL`] [`[--logging-filter-expr](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--logging-filter-expr)`=`LOGGING_FILTER_EXPR`] [`[--logging-flow-sampling](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--logging-flow-sampling)`=`LOGGING_FLOW_SAMPLING`] [`[--logging-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--logging-metadata)`=`LOGGING_METADATA`] [`[--logging-metadata-fields](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--logging-metadata-fields)`=[`METADATA_FIELD`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--region)`=`REGION`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--stack-type)`=`STACK_TYPE`] [`[--add-secondary-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--add-secondary-ranges)`=`PROPERTY`=`VALUE`,[…]     | `[--[no-]enable-flow-logs](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--[no-]enable-flow-logs)`     | `[--[no-]enable-private-ip-google-access](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--[no-]enable-private-ip-google-access)`     | `[--private-ipv6-google-access-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--private-ipv6-google-access-type)`=`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE`     | `[--purpose](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--purpose)`=`PURPOSE`     | `[--remove-secondary-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--remove-secondary-ranges)`=`PROPERTY`=`VALUE`,[…]     | `[--role](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#--role)`=`ROLE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks subnets update` is used to update properties
of an existing Compute Engine subnetwork.

**EXAMPLES**

: To enable external IPv6 addresses on the subnetwork example-subnet-1 in
network-1, run

```
gcloud compute networks subnets update example-subnet-1 --stack-type=IPV4_IPV6 --ipv6-access-type=EXTERNAL --region=REGION
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the subnetwork to update.

**FLAGS**

: **--add-secondary-ranges-with-reserved-internal-range**:
Adds secondary IP ranges that are associated with internal range resources.
For example, `--add-secondary-ranges-with-reserved-internal-range
range1=//networkconnectivity.googleapis.com/projects/PROJECT/locations/global/internalRanges/RANGE`
adds a secondary range with the reserved internal range resource.

- `RANGE_NAME` - Name of the secondary range.
- `INTERNAL_RANGE_URL` - `URL of an internal range
resource.`

**--drain-timeout**:
The time period for draining traffic from Internal HTTP(S) Load Balancer proxies
that are assigned addresses in the current ACTIVE subnetwork. For example,
``1h``,
``60m`` and
``3600s`` each specify a duration of 1 hour for
draining the traffic. Longer times reduce the number of proxies that are
draining traffic at any one time, and so improve the availability of proxies for
load balancing. The drain timeout is only applicable when the [--role=ACTIVE]
flag is being used.

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
Can only be specified if VPC Flow logs for this subnetwork is enabled. The value
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

**--region**:
Region of the subnetwork to update. If not specified, you might be prompted to
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

**--stack-type**:
The stack type for this subnet. Determines if IPv6 is enabled on the subnet.
`STACK_TYPE` must be one of:

**`IPV4_IPV6`**:
New VMs in this subnet can have both IPv4 and IPv6 addresses

**`IPV4_ONLY`**:
New VMs in this subnet will only be assigned IPv4 addresses

**--add-secondary-ranges**

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
gcloud alpha compute networks subnets update
```

```
gcloud beta compute networks subnets update
```