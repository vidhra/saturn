# gcloud alpha compute addresses describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/describe)*

**NAME**

: **gcloud alpha compute addresses describe - display detailed information about a reserved static address**

**SYNOPSIS**

: **`gcloud alpha compute addresses describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/describe#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute addresses describe`
displays all data associated with a reserved static address in a project.

**EXAMPLES**

: To get details about a global address, run:

```
gcloud alpha compute addresses describe my-address-name --global
```

To get details about a regional address, run:

```
gcloud alpha compute addresses describe my-address-name --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the address to describe.

**FLAGS**

: **--global**

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
gcloud compute addresses describe
```

```
gcloud beta compute addresses describe
```