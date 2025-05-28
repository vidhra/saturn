# gcloud resource-manager tags values update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/update](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/update)*

**NAME**

: **gcloud resource-manager tags values update - updates the specified TagValue resource's description**

**SYNOPSIS**

: **`gcloud resource-manager tags values update` `[RESOURCE_NAME](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/update#RESOURCE_NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/update#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the TagValue's description given the TagValue's namespaced name
<parent_namespace>/<tagkey_short_name>/<short_name> or the
TagValue's numeric id tagValues/<id>

**EXAMPLES**

: To update a TagValue with id ``123``, run:

```
gcloud resource-manager tags values update tagValues/123 --description="foobar"
```

To update a TagValue named ``dev`` with the
tagKey ``env`` under organization
``456``, run:

```
gcloud resource-manager tags values update 465/env/dev --description="foobar"
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

**--description**:
User-assigned description of the TagKey or TagValue. Must not exceed 256
characters.

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
gcloud alpha resource-manager tags values update
```

```
gcloud beta resource-manager tags values update
```