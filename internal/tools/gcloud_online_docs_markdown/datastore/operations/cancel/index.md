# gcloud datastore operations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastore/operations/cancel](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/cancel)*

**NAME**

: **gcloud datastore operations cancel - cancel a currently-running Cloud Datastore admin operation**

**SYNOPSIS**

: **`gcloud datastore operations cancel` `[NAME](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/cancel#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancel a currently-running Cloud Datastore admin operation.

**EXAMPLES**

: To cancel the currently-running operation with id `exampleId`, run:

```
gcloud datastore operations cancel exampleId
```

or

```
gcloud datastore operations cancel projects/your-project-id/operations/exampleId
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The unique name of the Operation to cancel, formatted as either the full or
relative resource path:

```
projects/my-app-id/operations/foo
```

or:

```
foo
```

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
gcloud alpha datastore operations cancel
```

```
gcloud beta datastore operations cancel
```