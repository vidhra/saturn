# gcloud alpha builds worker-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update)*

**NAME**

: **gcloud alpha builds worker-pools update - update a private pool used by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds worker-pools update` `[WORKER_POOL](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update#WORKER_POOL)` (`[--config-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update#--config-from-file)`=`CONFIG_FROM_FILE`     | `[--[no-]public-egress](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update#--[no-]public-egress)` `[--worker-disk-size](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update#--worker-disk-size)`=`WORKER_DISK_SIZE` `[--worker-machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update#--worker-machine-type)`=`WORKER_MACHINE_TYPE`) [`[--generation](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update#--generation)`=`GENERATION`; default=1] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a private pool used by Cloud Build.

**EXAMPLES**

: To change the machine type and disk size of workers in a worker pool named wp1,
run:

```
gcloud alpha builds worker-pools update wp1 --region=us-central1 --worker-machine-type=e2-standard-2 --worker-disk-size=64GB
```

**POSITIONAL ARGUMENTS**

: **`WORKER_POOL`**:
Unique identifier for the worker pool to update. This value should be 1-63
characters, and valid characters are [a-z][0-9]-

**REQUIRED FLAGS**

: **--config-from-file**

**OPTIONAL FLAGS**

: **--generation**:
Generation of the worker pool.

**--region**:
Cloud region where the worker pool is updated. See [https://cloud.google.com/build/docs/locations](https://cloud.google.com/build/docs/locations)
for available locations.

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
gcloud builds worker-pools update
```

```
gcloud beta builds worker-pools update
```