# gcloud alpha compute diagnose  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/diagnose](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/diagnose)*

**NAME**

: **gcloud alpha compute diagnose - debugging tools for Compute Engine virtual machine instances**

**SYNOPSIS**

: **`gcloud alpha compute diagnose` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/diagnose#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/diagnose#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Debugging tools for Compute Engine virtual machine
instances.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[export-logs](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/diagnose/export-logs)`**:
`(ALPHA)` Triggers instance to gather logs and upload them to a Cloud
Storage Bucket.

**`[routes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/diagnose/routes)`**:
`(ALPHA)` Routes to/from Compute Engine virtual machine instances.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute diagnose
```

```
gcloud beta compute diagnose
```