# gcloud datastore indexes describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/describe](https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/describe)*

**NAME**

: **gcloud datastore indexes describe - show details about an Cloud Datastore index**

**SYNOPSIS**

: **`gcloud datastore indexes describe` `[INDEX](https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/describe#INDEX)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details about an Cloud Datastore index.

**EXAMPLES**

: To describe the index with id `exampleIndexId`, run:

```
gcloud datastore indexes describe exampleIndexId
```

**POSITIONAL ARGUMENTS**

: **Index resource - The index you want to get the details of. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `index` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INDEX`**:
ID of the index or fully qualified identifier for the index.
To set the `index` attribute:

- provide the argument `index` on the command line.**

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

: This command uses the `datastore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/datastore/](https://cloud.google.com/datastore/)

**NOTES**

: These variants are also available:

```
gcloud alpha datastore indexes describe
```

```
gcloud beta datastore indexes describe
```