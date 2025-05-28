# gcloud kms ekm-config set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/set-iam-policy)*

**NAME**

: **gcloud kms ekm-config set-iam-policy - set the IAM policy for an EkmConfig**

**SYNOPSIS**

: **`gcloud kms ekm-config set-iam-policy` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/set-iam-policy#POLICY_FILE)` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/set-iam-policy#--location)`=`LOCATION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the IAM policy for the EkmConfig in a location as defined in a JSON or YAML
file.
See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**EXAMPLES**

: The following command will read am IAM policy defined in a JSON file
'policy.json' and set it for the EkmConfig with location
`us-central1`:

```
gcloud kms ekm-config set-iam-policy policy.json --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **`POLICY_FILE`**:
JSON or YAML file with the IAM policy

**REQUIRED FLAGS**

: **Location resource - The KMS location resource. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

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
gcloud alpha kms ekm-config set-iam-policy
```

```
gcloud beta kms ekm-config set-iam-policy
```