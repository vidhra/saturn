# gcloud storage managed-folders set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy)*

**NAME**

: **gcloud storage managed-folders set-iam-policy - set the IAM policy for a managed folder**

**SYNOPSIS**

: **`gcloud storage managed-folders set-iam-policy` `[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#URLS)` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#URLS)` …] `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#POLICY_FILE)` [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#-c)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#--etag)`=`ETAG`, `[-e](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#-e)` `[ETAG](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#ETAG)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Set the IAM policy for a managed folder. For more information, see [Cloud Identity
and Access Management](https://cloud.google.com/storage/docs/access-control/iam).

**EXAMPLES**

: To set the IAM policy in POLICY-FILE on a managed folder
`managed-folder` in a bucket `bucket`:

```
gcloud storage managed-folders set-iam-policy gs://bucket/managed-folder POLICY-FILE
```

**POSITIONAL ARGUMENTS**

: **`URLS` [`URLS` …]**:
URLs for managed folders to apply the IAM policy to.

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

**FLAGS**

: **--continue-on-error**:
If any operations are unsuccessful, the command will exit with a non-zero exit
status after completing the remaining operations. This flag takes effect only in
sequential execution mode (i.e. processor and thread count are set to 1).
Parallelism is default.

**--etag**:
Custom etag to set on IAM policy. API will reject etags that do not match this
value, making it useful as a precondition during concurrent operations.

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

: This variant is also available:

```
gcloud alpha storage managed-folders set-iam-policy
```