# gcloud iam workload-identity-pools set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/set-iam-policy)*

**NAME**

: **gcloud iam workload-identity-pools set-iam-policy - set the IAM policy for a workload identity pool**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools set-iam-policy` (`[WORKLOAD_IDENTITY_POOL](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/set-iam-policy#WORKLOAD_IDENTITY_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/set-iam-policy#--location)`=`LOCATION`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Replaces the existing IAM policy for a workload identity pool given a workload
identity pool ID and a file encoded in JSON or YAML that contains the IAM
policy.

**EXAMPLES**

: The following command reads an IAM policy defined in a JSON file
`policy.json` and sets it for the workload identity pool with ID
`my-workload-identity-pool`:

```
gcloud iam workload-identity-pools set-iam-policy my-workload-identity-pool policy.json --location="global"
```

**POSITIONAL ARGUMENTS**

: **Workload identity pool resource - The workload identity pool for which you want
to set IAM policy for. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `workload_identity_pool` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`WORKLOAD_IDENTITY_POOL`**:
ID of the workload identity pool or fully qualified identifier for the workload
identity pool.
To set the `workload_identity_pool` attribute:

- provide the argument `workload_identity_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `workload_identity_pool` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.**

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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