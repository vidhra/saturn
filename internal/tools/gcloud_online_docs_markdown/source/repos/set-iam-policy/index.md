# gcloud source repos set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/source/repos/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/source/repos/set-iam-policy)*

**NAME**

: **gcloud source repos set-iam-policy - set the IAM policy for the named repository**

**SYNOPSIS**

: **`gcloud source repos set-iam-policy` `[REPOSITORY_NAME](https://cloud.google.com/sdk/gcloud/reference/source/repos/set-iam-policy#REPOSITORY_NAME)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/source/repos/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/source/repos/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command sets the IAM policy for the given repository from the policy in the
provided file.

**EXAMPLES**

: To set the IAM policy, issue the following command:

```
gcloud source repos set-iam-policy REPOSITORY_NAME POLICY_FILE
```

**POSITIONAL ARGUMENTS**

: **`REPOSITORY_NAME`**:
Name of the repository.

**`POLICY_FILE`**:
JSON or YAML file with IAM policy. See [https://cloud.google.com/resource-manager/reference/rest/Shared.Types/Policy](https://cloud.google.com/resource-manager/reference/rest/Shared.Types/Policy)

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
gcloud alpha source repos set-iam-policy
```

```
gcloud beta source repos set-iam-policy
```