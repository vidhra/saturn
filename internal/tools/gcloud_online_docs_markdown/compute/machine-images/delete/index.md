# gcloud compute machine-images delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/delete](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/delete)*

**NAME**

: **gcloud compute machine-images delete - delete a Compute Engine machine image**

**SYNOPSIS**

: **`gcloud compute machine-images delete` `[IMAGE](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/delete#IMAGE)` [`[IMAGE](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/delete#IMAGE)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Compute Engine machine image.

**EXAMPLES**

: To delete a machine image, run:

```
gcloud compute machine-images delete my-machine-image
```

**POSITIONAL ARGUMENTS**

: **`IMAGE` [`IMAGE` …]**:
Names of the machineImages to delete.

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
gcloud alpha compute machine-images delete
```

```
gcloud beta compute machine-images delete
```