# gcloud resource-manager tags values get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/get-iam-policy)*

**NAME**

: **gcloud resource-manager tags values get-iam-policy - gets the IAM policy for a TagValue resource**

**SYNOPSIS**

: **`gcloud resource-manager tags values get-iam-policy` `[RESOURCE_NAME](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/get-iam-policy#RESOURCE_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns the IAM policy for a TagValue resource given the TagValue's short name
and parent or the TagValue's numeric id.

**EXAMPLES**

: To get the IAM policy for a TagValue with id '123', run:

```
gcloud resource-manager tags values get-iam-policy tagValues/123
```

To get the IAM policy for a TagValue with the name 'dev' under
'organizations/456' and tagKey parent 'env', run:

```
gcloud resource-manager tags values get-iam-policy 456/env/dev
```

**POSITIONAL ARGUMENTS**

: **`RESOURCE_NAME`**:
Resource name or namespaced name. The resource name should be in the form
{resource_type}/{numeric_id}. The namespaced name should be in the form
{org_id}/{short_name} where short_name must be 1-63 characters, beginning and
ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores
( _ ), dots (.), and alphanumerics between.

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
gcloud alpha resource-manager tags values get-iam-policy
```

```
gcloud beta resource-manager tags values get-iam-policy
```