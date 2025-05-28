# gcloud iam workload-identity-pools managed-identities set-attestation-rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules)*

**NAME**

: **gcloud iam workload-identity-pools managed-identities set-attestation-rules - set attestation rules on a workload identity pool managed identity**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools managed-identities set-attestation-rules` (`[MANAGED_IDENTITY](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules#MANAGED_IDENTITY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules#--location)`=`LOCATION` `[--namespace](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules#--namespace)`=`NAMESPACE` `[--workload-identity-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules#--workload-identity-pool)`=`WORKLOAD_IDENTITY_POOL`) `[--policy-file](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules#--policy-file)`=`POLICY_FILE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/set-attestation-rules#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Set attestation rules on a workload identity pool managed identity.

**EXAMPLES**

: The following command sets attestation rules on a workload identity pool managed
identity `my-managed-identity` using a policy file.

```
gcloud iam workload-identity-pools managed-identities set-attestation-rules my-managed-identity --namespace="my-namespace" --workload-identity-pool="my-workload-identity-pool" --location="global" --policy-file="policy.json"
```

**POSITIONAL ARGUMENTS**

: **Workload identity pool managed identity resource - The workload identity pool
managed identity to set attestation rules on. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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

: **--policy-file**:
Path to a local JSON-formatted or YAML-formatted file containing an attestation
policy, structured as a [list
of attestation rules](https://cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/setAttestationRules#request-body).

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