# gcloud resource-manager org-policies set-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy)*

**NAME**

: **gcloud resource-manager org-policies set-policy - set Organization Policy**

**SYNOPSIS**

: **`gcloud resource-manager org-policies set-policy` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy#POLICY_FILE)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets an Organization Policy associated with the specified resource from a file
that contains the JSON or YAML encoded Organization Policy.

**EXAMPLES**

: Organization policy list constraint YAML file example:

```
constraint: constraints/CONSTRAINT_NAME
listPolicy:
  deniedValues:
  - VALUE_A
```

Organization policy list constraint JSON file example:

```
{
  "constraint": "constraints/CONSTRAINT_NAME",
  "listPolicy": {
    "deniedValues": ["VALUE_A"]
  }
}
```

The following command sets an Organization Policy for a constraint on project
`foo-project` from file `/tmp/policy.yaml`:

```
gcloud resource-manager org-policies set-policy --project=foo-project /tmp/policy.yaml
```

**POSITIONAL ARGUMENTS**

: **`POLICY_FILE`**:
JSON or YAML file with the Organization Policy.

**REQUIRED FLAGS**

: **--folder**

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
gcloud alpha resource-manager org-policies set-policy
```

```
gcloud beta resource-manager org-policies set-policy
```