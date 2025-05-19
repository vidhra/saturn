# gcloud container binauthz attestors set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/set-iam-policy)*

**NAME**

: **gcloud container binauthz attestors set-iam-policy - set the IAM policy for an attestor**

**SYNOPSIS**

: **`gcloud container binauthz attestors set-iam-policy` `[ATTESTOR_NAME](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/set-iam-policy#ATTESTOR_NAME)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**EXAMPLES**

: The following command will read an IAM policy defined in a JSON file
'iam_policy.json' and set it for the attestor `my_attestor`:

```
gcloud container binauthz attestors set-iam-policy my_attestor iam_policy.json
```

**POSITIONAL ARGUMENTS**

: **`ATTESTOR_NAME`**:
The name of the attestor whose IAM policy will be updated.

**`POLICY_FILE`**:
The JSON or YAML file containing the IAM policy.

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
gcloud alpha container binauthz attestors set-iam-policy
```

```
gcloud beta container binauthz attestors set-iam-policy
```