# gcloud iam workload-identity-pools providers operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/operations/describe](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/operations/describe)*

**NAME**

: **gcloud iam workload-identity-pools providers operations describe - describe a workload identity pool provider operation**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools providers operations describe` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/operations/describe#OPERATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/operations/describe#--location)`=`LOCATION` `[--provider](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/operations/describe#--provider)`=`PROVIDER` `[--workload-identity-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/operations/describe#--workload-identity-pool)`=`WORKLOAD_IDENTITY_POOL`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a workload identity pool provider operation.

**EXAMPLES**

: The following command describes the long running workload identity pool provider
operation with the ID ``my-operation``:

```
gcloud iam workload-identity-pools providers operations describe my-operation --workload-identity-pool="my-workload-identity-pool" --provider="my-provider" --location="global"
```

**POSITIONAL ARGUMENTS**

: **Workload identity pool provider operation resource - The workload identity pool
provider long running operation to describe. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OPERATION`**:
ID of the workload identity pool provider operation or fully qualified
identifier for the workload identity pool provider operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--provider**:
The ID for the provider, which becomes the final component of the resource name.
This value must be 4-32 characters, and may contain the characters [a-z0-9-].
The prefix `gcp-` is reserved for use by Google, and may not be
specified.
To set the `provider` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--provider` on the command line.

**--workload-identity-pool**:
The ID to use for the pool, which becomes the final component of the resource
name. This value should be 4-32 characters, and may contain the characters
[a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may
not be specified.
To set the `workload-identity-pool` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--workload-identity-pool` on the command line.**

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
gcloud alpha iam workload-identity-pools providers operations describe
```

```
gcloud beta iam workload-identity-pools providers operations describe
```