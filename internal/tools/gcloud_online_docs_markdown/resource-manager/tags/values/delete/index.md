# gcloud resource-manager tags values delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/delete](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/delete)*

**NAME**

: **gcloud resource-manager tags values delete - deletes the specified TagValue resource**

**SYNOPSIS**

: **`gcloud resource-manager tags values delete` `[RESOURCE_NAME](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/delete#RESOURCE_NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes the TagValue resource given the TagValue's parent and short name or the
TagValue's numeric id.

**EXAMPLES**

: To delete a TagValue with id ``123``, run:

```
gcloud resource-manager tags values delete tagValues/123
```

To delete a TagValue named ``dev`` with tagKey
``env`` under organization
``456``, run:

```
gcloud resource-manager tags values delete 456/env/dev
```

**POSITIONAL ARGUMENTS**

: **`RESOURCE_NAME`**:
Resource name or namespaced name. The resource name should be in the form
{resource_type}/{numeric_id}. The namespaced name should be in the form
{org_id}/{short_name} where short_name must be 1-63 characters, beginning and
ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores
( _ ), dots (.), and alphanumerics between.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha resource-manager tags values delete
```

```
gcloud beta resource-manager tags values delete
```