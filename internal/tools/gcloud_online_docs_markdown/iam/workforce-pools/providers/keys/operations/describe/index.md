# gcloud iam workforce-pools providers keys operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/operations/describe](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/operations/describe)*

**NAME**

: **gcloud iam workforce-pools providers keys operations describe - describe a workforce pool provider key operation**

**SYNOPSIS**

: **`gcloud iam workforce-pools providers keys operations describe` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/operations/describe#OPERATION)` : `[--key](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/operations/describe#--key)`=`KEY` `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/operations/describe#--location)`=`LOCATION` `[--provider](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/operations/describe#--provider)`=`PROVIDER` `[--workforce-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/operations/describe#--workforce-pool)`=`WORKFORCE_POOL`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a workforce pool provider key operation.

**EXAMPLES**

: To describe the long-running workforce pool provider key operation with the ID
``my-operation``, run:

```
gcloud iam workforce-pools providers keys operations describe my-operation --workforce-pool="my-workforce-pool" --provider="my-provider" --key="my-key" --location="global"
```

**POSITIONAL ARGUMENTS**

: **Workforce pool provider key operation resource - The workforce pool provider key
long-running operation to describe. The arguments in this group can be used to
specify the attributes of this resource.
This must be specified.

**`OPERATION`**:
ID of the workforce pool provider key operation or fully qualified identifier
for the workforce pool provider key operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--key**:
The ID for the key, which becomes the final component of the resource name. This
value must be 4-32 characters, and may contain the characters [a-z0-9-]. The
prefix `gcp-` is reserved for use by Google, and may not be
specified.
To set the `key` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--key` on the command line.

**--location**:
The location for the workforce pool.
To set the `location` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--provider**:
The ID to use for the workforce pool provider, which becomes the final component
of the resource name. This value must be unique within the workforce pool, 4-32
characters in length, and may contain the characters [a-z0-9-]. The prefix
`gcp-` is reserved for use by Google, and may not be specified.
To set the `provider` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--provider` on the command line.

**--workforce-pool**:
The ID to use for the workforce pool, which becomes the final component of the
resource name. This value must be a globally unique string of 6 to 63 lowercase
letters, digits, or hyphens. It must start with a letter, and cannot have a
trailing hyphen. The prefix `gcp-` is reserved for use by Google, and
may not be specified.
To set the `workforce-pool` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--workforce-pool` on the command line.**

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
gcloud alpha iam workforce-pools providers keys operations describe
```

```
gcloud beta iam workforce-pools providers keys operations describe
```