# gcloud iam workforce-pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/delete](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/delete)*

**NAME**

: **gcloud iam workforce-pools delete - delete a workforce pool**

**SYNOPSIS**

: **`gcloud iam workforce-pools delete` (`[WORKFORCE_POOL](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/delete#WORKFORCE_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a workforce pool.

**EXAMPLES**

: The following command deletes a workforce pool with ID
``my-workforce-pool``:

```
gcloud iam workforce-pools delete my-workforce-pool --location=global
```

**POSITIONAL ARGUMENTS**

: **Workforce pool resource - The workforce pool to delete. The arguments in this
group can be used to specify the attributes of this resource.
This must be specified.

**`WORKFORCE_POOL`**:
ID of the workforce pool or fully qualified identifier for the workforce pool.
To set the `workforce_pool` attribute:

- provide the argument `workforce_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the workforce pool.
To set the `location` attribute:

- provide the argument `workforce_pool` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `iam/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: These variants are also available:

```
gcloud alpha iam workforce-pools delete
```

```
gcloud beta iam workforce-pools delete
```