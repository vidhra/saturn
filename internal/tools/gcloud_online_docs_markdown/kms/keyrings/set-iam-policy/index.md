# gcloud kms keyrings set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/set-iam-policy)*

**NAME**

: **gcloud kms keyrings set-iam-policy - set the IAM policy for a keyring**

**SYNOPSIS**

: **`gcloud kms keyrings set-iam-policy` `[KEYRING](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/set-iam-policy#KEYRING)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/set-iam-policy#POLICY_FILE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/set-iam-policy#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the IAM policy for the given keyring as defined in a JSON or YAML file.
See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**EXAMPLES**

: The following command will read am IAM policy defined in a JSON file
'policy.json' and set it for the keyring `fellowship` with location
`global`:

```
gcloud kms keyrings set-iam-policy fellowship policy.json --location=global
```

**POSITIONAL ARGUMENTS**

: **`KEYRING`**:
Name of the key ring whose IAM policy to update.

**`POLICY_FILE`**:
JSON or YAML file with the IAM policy

**FLAGS**

: **--location**:
Location of the keyring.

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
gcloud alpha kms keyrings set-iam-policy
```

```
gcloud beta kms keyrings set-iam-policy
```