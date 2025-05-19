# gcloud compute images describe-from-family  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/images/describe-from-family](https://cloud.google.com/sdk/gcloud/reference/compute/images/describe-from-family)*

**NAME**

: **gcloud compute images describe-from-family - describe the latest image from an image family**

**SYNOPSIS**

: **`gcloud compute images describe-from-family` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/images/describe-from-family#IMAGE_NAME)` [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/images/describe-from-family#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/images/describe-from-family#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute images describe-from-family` looks up the latest
image from an image family and runs a describe on it. If the image is not in the
default project, you need to specify a value for `--project`.

**EXAMPLES**

: To view the description for the latest
``debian-9`` image from the
``debian-cloud`` project, run:

```
gcloud compute images describe-from-family debian-9 --project=debian-cloud
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME`**:
Name of the disk image to describe.

**FLAGS**

: **--zone**:
Zone to query. Returns the latest image available in the image family for the
specified zone. If not specified, returns the latest globally available image.

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
gcloud alpha compute images describe-from-family
```

```
gcloud beta compute images describe-from-family
```