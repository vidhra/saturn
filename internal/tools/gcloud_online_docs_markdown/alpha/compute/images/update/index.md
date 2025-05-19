# gcloud alpha compute images update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update)*

**NAME**

: **gcloud alpha compute images update - update a Compute Engine image**

**SYNOPSIS**

: **`gcloud alpha compute images update` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#IMAGE_NAME)` [`[--architecture](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#--architecture)`=`ARCHITECTURE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#--description)`=`DESCRIPTION`] [`[--family](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#--family)`=`FAMILY`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#--remove-labels)`=[`KEY`,…]] [`[--clear-user-licenses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#--clear-user-licenses)`     | `[--update-user-licenses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#--update-user-licenses)`=[`LICENSE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute images update` updates
labels for a Compute Engine image.

**EXAMPLES**

: To update labels ``k0`` and
``k1`` and remove labels with key
``k3``, run:

```
gcloud alpha compute images update example-image --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

```
k0 and k1 will be added as new labels if not already present.
```

Labels can be used to identify the image and to filter them like:

```
gcloud alpha compute images list --filter='labels.k1:value2'
```

To list only the labels when describing a resource, use --format:

```
gcloud alpha compute images describe example-image --format="default(labels)"
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME`**:
Name of the disk image to update.

**FLAGS**

: **--architecture**:
Specifies the architecture or processor type that this image can support. For
available processor types on Compute Engine, see [https://cloud.google.com/compute/docs/cpu-platforms](https://cloud.google.com/compute/docs/cpu-platforms).
`ARCHITECTURE` must be one of: `ARM64`,
`X86_64`.

**--description**:
An optional text description for the image.

**--family**:
Name of the image family to use. If an image family is specified when you create
an instance or disk, the latest non-deprecated image in the family is used.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--clear-user-licenses**

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
gcloud compute images update
```

```
gcloud beta compute images update
```