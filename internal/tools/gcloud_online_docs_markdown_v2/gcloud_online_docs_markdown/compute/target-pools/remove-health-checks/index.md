# gcloud compute target-pools remove-health-checks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-health-checks)*

**NAME**

: **gcloud compute target-pools remove-health-checks - remove an HTTP health check from a target pool**

**SYNOPSIS**

: **`gcloud compute target-pools remove-health-checks` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-health-checks#NAME)` `[--http-health-check](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-health-checks#--http-health-check)`=`HTTP_HEALTH_CHECK` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-health-checks#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-health-checks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-pools remove-health-checks` is used to remove
an HTTP health check from a target pool. Health checks are used to determine the
health status of instances in the target pool. For more information on health
checks and load balancing, see [https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/](https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the target pool from which to remove the health check.

**REQUIRED FLAGS**

: **--http-health-check**:
Specifies an HTTP health check object to remove from the target pool.

**OPTIONAL FLAGS**

: **--region**:
Region of the target pool to remove health checks from. If not specified, you
might be prompted to select a region (interactive mode only).
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
gcloud alpha compute target-pools remove-health-checks
```

```
gcloud beta compute target-pools remove-health-checks
```