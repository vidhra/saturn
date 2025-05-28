# gcloud alpha compute images  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images)*

**NAME**

: **gcloud alpha compute images - list, create, and delete Compute Engine images**

**SYNOPSIS**

: **`gcloud alpha compute images` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create and manipulate Compute Engine images.
For more information about images, see the [images documentation](https://cloud.google.com/compute/docs/images).
See also: [Images
API](https://cloud.google.com/compute/docs/reference/rest/v1/images).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[packages](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/packages)`**:
`(ALPHA)` List and diff image packages.

**`[vulnerabilities](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/vulnerabilities)`**:
`(ALPHA)` List and describe image vulnerabilities and related notes.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/add-iam-policy-binding)`**:
`(ALPHA)` Add IAM policy binding to a Compute Engine image.

**`[add-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/add-labels)`**:
`(ALPHA)` Add labels to Google Compute Engine images.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/create)`**:
`(ALPHA)` Create Compute Engine images.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/delete)`**:
`(ALPHA)` Delete Compute Engine images.

**`[deprecate](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate)`**:
`(ALPHA)` Manage deprecation status of Compute Engine images.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/describe)`**:
`(ALPHA)` Describe a Compute Engine image.

**`[describe-from-family](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/describe-from-family)`**:
`(ALPHA)` Describe the latest image from an image family.

**`[export](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/export)`**:
`(ALPHA)` Export a Compute Engine image.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/get-iam-policy)`**:
`(ALPHA)` Get the IAM policy for a Compute Engine image.

**`[import](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import)`**:
`(ALPHA)` `(DEPRECATED)` Import an image into Compute
Engine.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/list)`**:
`(ALPHA)` List Google Compute Engine images.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding)`**:
`(ALPHA)` Remove IAM policy binding from a Compute Engine image.

**`[remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-labels)`**:
`(ALPHA)` Remove labels from Google Compute Engine images.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/set-iam-policy)`**:
`(ALPHA)` Set the IAM policy for a Compute Engine image.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update)`**:
`(ALPHA)` Update a Compute Engine image.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute images
```

```
gcloud beta compute images
```