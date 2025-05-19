# gcloud alpha compute images delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/delete)*

**NAME**

: **gcloud alpha compute images delete - delete Compute Engine images**

**SYNOPSIS**

: **`gcloud alpha compute images delete` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/delete#IMAGE_NAME)` [`[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/delete#IMAGE_NAME)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute images delete` deletes one
or more Compute Engine images.

**EXAMPLES**

: To delete images 'my-image1' and 'my-image2', run:

```
gcloud alpha compute images delete my-image1 my-image2
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME` [`IMAGE_NAME` …]**:
Names of the disk images to delete.

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
gcloud compute images delete
```

```
gcloud beta compute images delete
```