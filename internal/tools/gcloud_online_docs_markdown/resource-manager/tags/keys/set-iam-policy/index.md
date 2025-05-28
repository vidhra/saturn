# gcloud resource-manager tags keys set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/set-iam-policy)*

**NAME**

: **gcloud resource-manager tags keys set-iam-policy - sets IAM policy for a TagKey resource**

**SYNOPSIS**

: **`gcloud resource-manager tags keys set-iam-policy` `[RESOURCE_NAME](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/set-iam-policy#RESOURCE_NAME)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the IAM policy for a TagKey resource given the TagKey's display name and
parent or the TagKey's numeric id and a file encoded in JSON or YAML that
contains the IAM policy.

**EXAMPLES**

: To set the IAM policy for a TagKey with id '123' and IAM policy defined in a
YAML file '/path/to/my_policy.yaml', run:

```
gcloud resource-manager tags keys set-iam-policy tagKeys/123 /path/to/my_policy.yaml
```

To set the IAM policy for a tagKey with the short_name 'env' under
'organization/456' and IAM policy defined in a JSON file
'/path/to/my_policy.json', run:

```
gcloud resource-manager tags keys set-iam-policy 456/env /path/to/my_policy.json
```

**POSITIONAL ARGUMENTS**

: **`RESOURCE_NAME`**:
Resource name or namespaced name. The resource name should be in the form
{resource_type}/{numeric_id}. The namespaced name should be in the form
{org_id}/{short_name} where short_name must be 1-63 characters, beginning and
ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores
( _ ), dots (.), and alphanumerics between.

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy. The
output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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
gcloud alpha resource-manager tags keys set-iam-policy
```

```
gcloud beta resource-manager tags keys set-iam-policy
```