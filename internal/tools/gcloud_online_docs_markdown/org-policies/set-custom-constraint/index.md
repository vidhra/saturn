# gcloud org-policies set-custom-constraint  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint)*

**NAME**

: **gcloud org-policies set-custom-constraint - set a custom constraint from a JSON or YAML file**

**SYNOPSIS**

: **`gcloud org-policies set-custom-constraint` `[CUSTOM_CONSTRAINT_FILE](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint#CUSTOM_CONSTRAINT_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets a Custom Constraint from a JSON or YAML file. The custom constraint will be
created if it does not exist, or updated if it already exists.

**EXAMPLES**

: To set the custom constraint from the file on the path './sample_path', run:

```
gcloud org-policies set-custom-constraint ./sample_path
```

**POSITIONAL ARGUMENTS**

: **`CUSTOM_CONSTRAINT_FILE`**:
Path to JSON or YAML file that contains the organization policy.

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