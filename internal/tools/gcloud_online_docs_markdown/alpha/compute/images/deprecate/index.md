# gcloud alpha compute images deprecate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate)*

**NAME**

: **gcloud alpha compute images deprecate - manage deprecation status of Compute Engine images**

**SYNOPSIS**

: **`gcloud alpha compute images deprecate` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#IMAGE_NAME)` `[--state](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#--state)`=`STATE` [`[--replacement](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#--replacement)`=`REPLACEMENT`] [`[--delete-in](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#--delete-in)`=`DELETE_IN`     | `[--delete-on](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#--delete-on)`=`DELETE_ON`] [`[--deprecate-in](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#--deprecate-in)`=`DEPRECATE_IN`     | `[--deprecate-on](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#--deprecate-on)`=`DEPRECATE_ON`] [`[--obsolete-in](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#--obsolete-in)`=`OBSOLETE_IN`     | `[--obsolete-on](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#--obsolete-on)`=`OBSOLETE_ON`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute images deprecate` is used
to deprecate images.

**EXAMPLES**

: To deprecate an image called 'IMAGE' immediately, mark it as obsolete in one
day, and mark it as deleted in two days, use:

```
gcloud alpha compute images deprecate IMAGE --state=DEPRECATED --obsolete-in=1d --delete-in=2d
```

To un-deprecate an image called 'IMAGE' and clear times for deprecated,
obsoleted, and deleted, use:

```
gcloud alpha compute images deprecate IMAGE --state=ACTIVE
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME`**:
Name of the disk image to operate on.

**REQUIRED FLAGS**

: **--state**:
The deprecation state to set on the image. `STATE` must be
one of:

**`ACTIVE`**:
The image is currently supported.

**`DELETED`**:
New uses result in an error. Setting this state will not automatically delete
the image. You must still make a request to delete the image to remove it from
the image list.

**`DEPRECATED`**:
Operations which create a new `DEPRECATED` resource return
successfully, but with a warning indicating that the image is deprecated and
recommending its replacement.

**`OBSOLETE`**:
New uses result in an error.

**OPTIONAL FLAGS**

: **--replacement**:
Specifies a Compute Engine image as a replacement for the image being phased
out. Users of the deprecated image will be advised to switch to this
replacement. For example, `--replacement example-image` or
`--replacement projects/google/global/images/example-image`.
This flag value is purely informational and is not validated in any way.

**--delete-in**

**--deprecate-in**

**--obsolete-in**

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
gcloud compute images deprecate
```

```
gcloud beta compute images deprecate
```