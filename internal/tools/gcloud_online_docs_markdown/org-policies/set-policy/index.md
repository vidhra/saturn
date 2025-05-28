# gcloud org-policies set-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/org-policies/set-policy](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-policy)*

**NAME**

: **gcloud org-policies set-policy - set an organization policy from a JSON or YAML file**

**SYNOPSIS**

: **`gcloud org-policies set-policy` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-policy#POLICY_FILE)` [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-policy#--update-mask)`=`UPDATE_MASK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets an organization policy from a JSON or YAML file. The policy will be created
if it does not exist, or updated if it already exists.

**EXAMPLES**

: Organization policy list constraint YAML file example:

```
name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
spec:
  rules:
  - values:
    denied_values:
    - VALUE_A
```

Organization policy list constraint JSON file example:

```
{
  "name": "projects/PROJECT_ID/policies/CONSTRAINT_NAME",
  "spec": {
    "rules": [
      {
        "values": {
            "deniedValues": ["VALUE_A"]
        }
      }
    ]
  }
}
```

To set the policy from the file on the path './sample_path', run:

```
gcloud org-policies set-policy ./sample_path
```

**POSITIONAL ARGUMENTS**

: **`POLICY_FILE`**:
Path to JSON or YAML file that contains the organization policy.

**FLAGS**

: **--update-mask**:
Field mask used to specify the fields to be overwritten in the policy by the
set. The fields specified in the update_mask are relative to the policy, not the
full request. The update-mask flag can be empty, or have values
`policy.spec`, `policy.dry_run_spec` or `*`. If
the policy does not contain the dry_run_spec and update-mask flag is not
provided, then it defaults to `policy.spec`.

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