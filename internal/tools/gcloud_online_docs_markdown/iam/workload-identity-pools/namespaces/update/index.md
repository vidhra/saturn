# gcloud iam workload-identity-pools namespaces update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update)*

**NAME**

: **gcloud iam workload-identity-pools namespaces update - update workload identity pool namespace**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools namespaces update` (`[NAMESPACE](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update#NAMESPACE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update#--location)`=`LOCATION` `[--workload-identity-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update#--workload-identity-pool)`=`WORKLOAD_IDENTITY_POOL`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update#--description)`=`DESCRIPTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update#--disabled)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update workload identity pool namespace.

**EXAMPLES**

: The following command updates the workload identity pool namespace with the ID
my-namespace:

```
gcloud iam workload-identity-pools namespaces update my-namespace --location="global" --workload-identity-pool="my-workload-identity-pool" --description="My namespace description" --disabled
```

**POSITIONAL ARGUMENTS**

: **Workload identity pool namespace resource - The workload identity pool namespace
to update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `namespace` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAMESPACE`**:
ID of the workload identity pool namespace or fully qualified identifier for the
workload identity pool namespace.
To set the `namespace` attribute:

- provide the argument `namespace` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `namespace` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--workload-identity-pool**:
The ID to use for the pool, which becomes the final component of the resource
name. This value should be 4-32 characters, and may contain the characters
[a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may
not be specified.
To set the `workload-identity-pool` attribute:

- provide the argument `namespace` on the command line with a fully
specified name;
- provide the argument `--workload-identity-pool` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description of the namespace.

**--disabled**:
Whether the namespace is disabled. If disabled, credentials may no longer be
issued for identities in this namespace. Existing credentials may continue to be
accepted until they expire.

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