# gcloud organizations set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/organizations/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/organizations/set-iam-policy)*

**NAME**

: **gcloud organizations set-iam-policy - set IAM policy for an organization**

**SYNOPSIS**

: **`gcloud organizations set-iam-policy` `[ORGANIZATION_ID](https://cloud.google.com/sdk/gcloud/reference/organizations/set-iam-policy#ORGANIZATION_ID)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/organizations/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/organizations/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Given an organization ID and a file encoded in JSON or YAML that contains the
IAM policy, this command will set the IAM policy for that organization.

**EXAMPLES**

: The following command reads an IAM policy defined in a JSON file
`policy.json` and sets it for an organization with the ID
`123456789`:

```
gcloud organizations set-iam-policy 123456789 policy.json
```

The following command reads an IAM policy defined in a JSON file
`policy.json` and sets it for the organization associated with the
domain `example.com`:

```
gcloud organizations set-iam-policy example.com policy.json
```

**POSITIONAL ARGUMENTS**

: **`ORGANIZATION_ID`**:
ID or domain for the organization whose IAM policy you want to set.

**`POLICY_FILE`**:
JSON or YAML file containing the IAM policy.

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
gcloud alpha organizations set-iam-policy
```

```
gcloud beta organizations set-iam-policy
```