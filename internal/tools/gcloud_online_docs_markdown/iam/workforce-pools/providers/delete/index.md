# gcloud iam workforce-pools providers delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/delete](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/delete)*

**NAME**

: **gcloud iam workforce-pools providers delete - delete a workforce pool provider**

**SYNOPSIS**

: **`gcloud iam workforce-pools providers delete` (`[PROVIDER](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/delete#PROVIDER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/delete#--location)`=`LOCATION` `[--workforce-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/delete#--workforce-pool)`=`WORKFORCE_POOL`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a workforce pool provider.

**EXAMPLES**

: The following command deletes a workforce pool provider with the ID
`my-workforce-pool-provider`:

```
gcloud iam workforce-pools providers delete my-workforce-pool-provider --workforce-pool="my-workforce-pool" --location="global"
```

**POSITIONAL ARGUMENTS**

: **Workforce pool provider resource - The workforce pool provider to delete. The
arguments in this group can be used to specify the attributes of this resource.
This must be specified.

**`PROVIDER`**:
ID of the workforce pool provider or fully qualified identifier for the
workforce pool provider.
To set the `provider` attribute:

- provide the argument `provider` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the workforce pool.
To set the `location` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--workforce-pool**:
The ID to use for the workforce pool, which becomes the final component of the
resource name. This value must be a globally unique string of 6 to 63 lowercase
letters, digits, or hyphens. It must start with a letter, and cannot have a
trailing hyphen. The prefix `gcp-` is reserved for use by Google, and
may not be specified.
To set the `workforce-pool` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--workforce-pool` on the command line.**

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
gcloud alpha iam workforce-pools providers delete
```

```
gcloud beta iam workforce-pools providers delete
```