# gcloud alpha compute images remove-labels  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-labels)*

**NAME**

: **gcloud alpha compute images remove-labels - remove labels from Google Compute Engine images**

**SYNOPSIS**

: **`gcloud alpha compute images remove-labels` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-labels#IMAGE_NAME)` (`[--all](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-labels#--all)`     | `[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-labels#--labels)`=`KEY`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-labels#KEY)`,…]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-labels#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute images remove-labels`
removes labels from a Google Compute Engine image.

**EXAMPLES**

: To remove existing labels with key ``k0`` and
``k1`` from 'example-image'

```
gcloud alpha compute images remove-labels example-image --labels=k0,k1
```

Labels can be used to identify the image and to filter them. To find a image
labeled with key-value pair ``k1``,
``v2``

```
gcloud alpha compute images list --filter='labels.k1:v2'
```

To list only the labels when describing a resource, use --format

```
gcloud alpha compute images describe example-image --format='default(labels)'
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME`**:
Name of the disk image to operate on.

**REQUIRED FLAGS**

: **--all**

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
gcloud compute images remove-labels
```

```
gcloud beta compute images remove-labels
```