# gcloud compute networks subnets expand-ip-range  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range)*

**NAME**

: **gcloud compute networks subnets expand-ip-range - expand the IP range of a Compute Engine subnetwork**

**SYNOPSIS**

: **`gcloud compute networks subnets expand-ip-range` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range#NAME)` `[--prefix-length](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range#--prefix-length)`=`PREFIX_LENGTH` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks subnets expand-ip-range` expands the IP
range of a VPC subnetwork.
For more information about expanding a subnet, see [Expanding a
primary IP range](https://cloud.google.com/vpc/docs/using-vpc#expand-subnet).
This command doesn't work for secondary subnets or for subnets that are used
exclusively for load balancer proxies. For more information, see [Proxy-only
subnets for load balancers](https://cloud.google.com/load-balancing/docs/l7-internal/proxy-only-subnets).

**EXAMPLES**

: To expand the IP range of ``SUBNET`` to /16,
run:

```
gcloud compute networks subnets expand-ip-range SUBNET --region=us-central1 --prefix-length=16
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the subnetwork to operate on.

**REQUIRED FLAGS**

: **--prefix-length**:
The new prefix length of the subnet. It must be smaller than the original and in
the private address space 10.0.0.0/8, 172.16.0.0/12 or 192.168.0.0/16 defined in
RFC 1918.

**OPTIONAL FLAGS**

: **--region**:
Region of the subnetwork to operate on. If not specified, you might be prompted
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
gcloud alpha compute networks subnets expand-ip-range
```

```
gcloud beta compute networks subnets expand-ip-range
```