# gcloud compute operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/operations/describe](https://cloud.google.com/sdk/gcloud/reference/compute/operations/describe)*

**NAME**

: **gcloud compute operations describe - describe a Compute Engine operation**

**SYNOPSIS**

: **`gcloud compute operations describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/operations/describe#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/operations/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/operations/describe#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/operations/describe#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute operations describe` displays all data associated
with a Compute Engine operation in a project.

**EXAMPLES**

: To get details about a global operation (e.g. operation-111-222-333-444), run:

```
gcloud compute operations describe operation-111-222-333-444 --global
```

To get details about a regional operation, run:

```
gcloud compute operations describe operation-111-222-333-444 --region=us-central1
```

To get details about a zonal operation, run:

```
gcloud compute operations describe operation-111-222-333-444 --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the operation returned by an asynchronous command. Use `[gcloud compute operations
list](https://cloud.google.com/sdk/gcloud/reference/compute/operations/list)` to display recent operations.

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
gcloud alpha compute operations describe
```

```
gcloud beta compute operations describe
```