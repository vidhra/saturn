# gcloud resource-manager folders set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/set-iam-policy)*

**NAME**

: **gcloud resource-manager folders set-iam-policy - set IAM policy for a folder**

**SYNOPSIS**

: **`gcloud resource-manager folders set-iam-policy` `[FOLDER_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/set-iam-policy#FOLDER_ID)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the IAM policy for a folder, given a folder ID and a file encoded in JSON
or YAML that contains the IAM policy.

**EXAMPLES**

: The following command reads an IAM policy defined in a JSON file
`policy.json` and sets it for a folder with the ID
`3589215982`:

```
gcloud resource-manager folders set-iam-policy 3589215982 policy.json
```

**POSITIONAL ARGUMENTS**

: **`FOLDER_ID`**:
ID for the folder whose policy you want to set.

**`POLICY_FILE`**:
JSON or YAML file with the IAM policy.

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

: These variants are also available:

```
gcloud alpha resource-manager folders set-iam-policy
```

```
gcloud beta resource-manager folders set-iam-policy
```