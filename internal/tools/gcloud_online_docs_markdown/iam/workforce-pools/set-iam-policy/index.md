# gcloud iam workforce-pools set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/set-iam-policy)*

**NAME**

: **gcloud iam workforce-pools set-iam-policy - set the IAM policy for a workforce pool**

**SYNOPSIS**

: **`gcloud iam workforce-pools set-iam-policy` (`[WORKFORCE_POOL](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/set-iam-policy#WORKFORCE_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/set-iam-policy#--location)`=`LOCATION`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Set the IAM policy for a workforce pool.

**EXAMPLES**

: The following command reads an IAM policy defined in a JSON file
``policy.json`` and sets it for the workforce
pool with ID ``my-workforce-pool``:

```
gcloud iam workforce-pools set-iam-policy my-workforce-pool policy.json --location=global
```

**POSITIONAL ARGUMENTS**

: **Workforce pool resource - The workforce pool for which to display the IAM
policy. The arguments in this group can be used to specify the attributes of
this resource.
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