# gcloud builds worker-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create)*

**NAME**

: **gcloud builds worker-pools create - create a worker pool for use by Google Cloud Build**

**SYNOPSIS**

: **`gcloud builds worker-pools create` `[WORKER_POOL](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#WORKER_POOL)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#--region)`=`REGION`] [`[--config-from-file](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#--config-from-file)`=`CONFIG_FROM_FILE`     | `[--worker-disk-size](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#--worker-disk-size)`=`WORKER_DISK_SIZE` `[--worker-machine-type](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#--worker-machine-type)`=`WORKER_MACHINE_TYPE` `[--peered-network](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#--peered-network)`=`PEERED_NETWORK` `[--peered-network-ip-range](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#--peered-network-ip-range)`=`PEERED_NETWORK_IP_RANGE` `[--no-public-egress](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#--public-egress)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a worker pool for use by Google Cloud Build.

**EXAMPLES**

: To create a worker pool named `wp1` in region
`us-central1`, run:

```
gcloud builds worker-pools create wp1 --region=us-central1
```

To create a worker pool in project `p1` in region
`us-central1` where workers are of machine type
`e2-standard-2` and are peered to the VPC network
`projects/123/global/networks/default` within the IP range
`192.168.0.0/28` and have a disk size of 64GB, run:

```
gcloud builds worker-pools create wp1 --project=p1 --region=us-central1 --peered-network=projects/123/global/networks/default --peered-network-ip-range=192.168.0.0/28 --worker-machine-type=e2-standard-2 --worker-disk-size=64GB
```

**POSITIONAL ARGUMENTS**

: **`WORKER_POOL`**:
Unique identifier for the worker pool to create. This value should be 1-63
characters, and valid characters are [a-z][0-9]-

**FLAGS**

: **--region**:
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

: These variants are also available:

```
gcloud alpha builds worker-pools create
```

```
gcloud beta builds worker-pools create
```