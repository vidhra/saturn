# gcloud iam workload-identity-pools managed-identities remove-attestation-rule  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule)*

**NAME**

: **gcloud iam workload-identity-pools managed-identities remove-attestation-rule - remove an attestation rule on a workload identity pool managed identity**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools managed-identities remove-attestation-rule` (`[MANAGED_IDENTITY](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule#MANAGED_IDENTITY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule#--location)`=`LOCATION` `[--namespace](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule#--namespace)`=`NAMESPACE` `[--workload-identity-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule#--workload-identity-pool)`=`WORKLOAD_IDENTITY_POOL`) `[--google-cloud-resource](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule#--google-cloud-resource)`=`GOOGLE_CLOUD_RESOURCE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/remove-attestation-rule#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove an attestation rule on a workload identity pool managed identity.

**EXAMPLES**

: The following command removes an attestation rule with a Google Cloud resource
on a workload identity pool managed identity `my-managed-identity`.

```
gcloud iam workload-identity-pools managed-identities remove-attestation-rule my-managed-identity --namespace="my-namespace" --workload-identity-pool="my-workload-identity-pool" --location="global" --google-cloud-resource="//compute.googleapis.com/projects/123/type/Instance/attached_service_account.uid/12345"
```

**POSITIONAL ARGUMENTS**

: **Workload identity pool managed identity resource - The workload identity pool
managed identity to remove attestation rule on. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `managed_identity` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MANAGED_IDENTITY`**:
ID of the workload identity pool managed identity or fully qualified identifier
for the workload identity pool managed identity.
To set the `managed_identity` attribute:

- provide the argument `managed_identity` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `managed_identity` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.

**--namespace**:
The ID to use for the namespace. This value must be 2-63 characters, and may
contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for
use by Google, and may not be specified.
To set the `namespace` attribute:

- provide the argument `managed_identity` on the command line with a
fully specified name;
- provide the argument `--namespace` on the command line.

**--workload-identity-pool**:
The ID to use for the pool, which becomes the final component of the resource
name. This value should be 4-32 characters, and may contain the characters
[a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may
not be specified.
To set the `workload-identity-pool` attribute:

- provide the argument `managed_identity` on the command line with a
fully specified name;
- provide the argument `--workload-identity-pool` on the command line.**

**REQUIRED FLAGS**

: **--google-cloud-resource**:
A single workload operating on Google Cloud. This will be set in the attestation
rule to be added.

**OPTIONAL FLAGS**

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