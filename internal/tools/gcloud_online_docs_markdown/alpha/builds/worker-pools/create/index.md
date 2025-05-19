# gcloud alpha builds worker-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create)*

**NAME**

: **gcloud alpha builds worker-pools create - create a private pool for use by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds worker-pools create` `[WORKER_POOL](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#WORKER_POOL)` [`[--generation](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--generation)`=`GENERATION`; default=1] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--region)`=`REGION`] [`[--config-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--config-from-file)`=`CONFIG_FROM_FILE`     | `[--disable-public-ip-address](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--disable-public-ip-address)` `[--network-attachment](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--network-attachment)`=`NETWORK_ATTACHMENT` `[--route-all-traffic](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--route-all-traffic)`     | `[--peered-network](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--peered-network)`=`PEERED_NETWORK` `[--peered-network-ip-range](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--peered-network-ip-range)`=`PEERED_NETWORK_IP_RANGE` `[--no-public-egress](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--public-egress)` `[--worker-disk-size](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--worker-disk-size)`=`WORKER_DISK_SIZE` `[--worker-machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#--worker-machine-type)`=`WORKER_MACHINE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a private pool for use by Cloud Build.

**EXAMPLES**

: - Private pools

To create a private pool named `pwp1` in region
`us-central1`, run:

```
gcloud alpha builds worker-pools create pwp1 --region=us-central1
```

To create a private pool in project `p1` in region
`us-central1` where workers are of machine type
`e2-standard-2` and are peered to the VPC network
`projects/123/global/networks/default` within the IP range
`192.168.0.0/28` and have a disk size of 64GB, run:

```
gcloud alpha builds worker-pools create pwp1 --project=p1 --region=us-central1 --peered-network=projects/123/global/networks/default --peered-network-ip-range=192.168.0.0/28 --worker-machine-type=e2-standard-2 --worker-disk-size=64GB
```

To create a private pool in project `p1` in region
`us-central1` where workers are of machine type
`e2-standard-2` and are peered to the network attachment
`projects/p1/regions/us-central1/networkAttachments/na`. The workers
don't have public IP address and all the traffic is routed to the network
attachment.

```
gcloud alpha builds worker-pools create pwp1 --project=p1 --region=us-central1 --network-attachment=projects/p1/regions/us-central1/networkAttachments/na --route-all-traffic --disable-public-ip-address --worker-machine-type=e2-standard-2
```

**POSITIONAL ARGUMENTS**

: **`WORKER_POOL`**:
Unique identifier for the worker pool to create. This value should be 1-63
characters, and valid characters are [a-z][0-9]-

**FLAGS**

: **--generation**:
Generation of the worker pool.

**--region**:
Cloud region where the worker pool is created. See [https://cloud.google.com/build/docs/locations](https://cloud.google.com/build/docs/locations)
for available locations.

**--config-from-file**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud builds worker-pools create
```

```
gcloud beta builds worker-pools create
```