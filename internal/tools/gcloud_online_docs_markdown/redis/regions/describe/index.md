# gcloud redis regions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/regions/describe](https://cloud.google.com/sdk/gcloud/reference/redis/regions/describe)*

**NAME**

: **gcloud redis regions describe - show metadata for a Memorystore Redis region**

**SYNOPSIS**

: **`gcloud redis regions describe` `[REGION](https://cloud.google.com/sdk/gcloud/reference/redis/regions/describe#REGION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/regions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display all metadata associated with a Redis region given a valid region name.
This command can fail for the following reasons:

- The region specified does not exist.
- The active account does not have permission to access the given region.

**EXAMPLES**

: To display the metadata for the region `us-central1`, run:

```
gcloud redis regions describe us-central1
```

**POSITIONAL ARGUMENTS**

: **Region resource - Arguments and flags that specify the Memorystore Redis region
you want to describe. This represents a Cloud resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `region` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REGION`**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `region` on the command line.**

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

**API REFERENCE**

: This command uses the `redis/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/memorystore/docs/redis/](https://cloud.google.com/memorystore/docs/redis/)

**NOTES**

: These variants are also available:

```
gcloud alpha redis regions describe
```

```
gcloud beta redis regions describe
```