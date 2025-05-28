# gcloud compute addresses describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/addresses/describe](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/describe)*

**NAME**

: **gcloud compute addresses describe - display detailed information about a reserved static address**

**SYNOPSIS**

: **`gcloud compute addresses describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/describe#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute addresses describe` displays all data associated with
a reserved static address in a project.

**EXAMPLES**

: To get details about a global address, run:

```
gcloud compute addresses describe my-address-name --global
```

To get details about a regional address, run:

```
gcloud compute addresses describe my-address-name --region=us-central1
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

: These variants are also available:

```
gcloud alpha compute addresses describe
```

```
gcloud beta compute addresses describe
```