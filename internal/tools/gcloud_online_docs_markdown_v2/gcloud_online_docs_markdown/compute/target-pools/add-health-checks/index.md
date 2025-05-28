# gcloud compute target-pools add-health-checks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-health-checks)*

**NAME**

: **gcloud compute target-pools add-health-checks - add a legacy HTTP health check to a target pool**

**SYNOPSIS**

: **`gcloud compute target-pools add-health-checks` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-health-checks#NAME)` `[--http-health-check](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-health-checks#--http-health-check)`=`HTTP_HEALTH_CHECK` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-health-checks#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-health-checks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-pools add-health-checks` is used to add a
legacy HTTP health check to a target pool. Legacy health checks are used to
determine the health status of instances in the target pool. Only one health
check can be attached to a target pool, so this command will fail if there as
already a health check attached to the target pool. For more information on
health checks and load balancing, see [https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/](https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the target pool to which to add the health check.

**REQUIRED FLAGS**

: **--http-health-check**:
Specifies an HTTP health check object to add to the target pool.

**OPTIONAL FLAGS**

: **--region**:
Region of the target pool to add health checks to. If not specified, you might
be prompted to select a region (interactive mode only).
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
gcloud alpha compute target-pools add-health-checks
```

```
gcloud beta compute target-pools add-health-checks
```