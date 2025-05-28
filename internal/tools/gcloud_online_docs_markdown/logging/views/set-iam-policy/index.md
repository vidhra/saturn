# gcloud logging views set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy)*

**NAME**

: **gcloud logging views set-iam-policy - set IAM policy for a view**

**SYNOPSIS**

: **`gcloud logging views set-iam-policy` `[VIEW_ID](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#VIEW_ID)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#POLICY_FILE)` `[--bucket](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#--bucket)`=`BUCKET` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#--location)`=`LOCATION` [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/views/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Set an IAM policy for a view.

**EXAMPLES**

: To set the IAM policy using a json file 'my_policy.json' for the view
`my-view` in `my-bucket` in the `global`
location, run:

```
gcloud logging views set-iam-policy my-view /path/to/my_policy.json --bucket=my-bucket --location=global
```

**POSITIONAL ARGUMENTS**

: **`VIEW_ID`**:
ID of the view to set IAM policy.

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

**REQUIRED FLAGS**

: **--bucket**:
ID of the bucket that contains the view.

**--location**:
Location of the bucket that contains the view.

**OPTIONAL FLAGS**

: **--billing-account**

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