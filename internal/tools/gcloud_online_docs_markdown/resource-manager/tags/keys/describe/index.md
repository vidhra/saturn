# gcloud resource-manager tags keys describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/describe](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/describe)*

**NAME**

: **gcloud resource-manager tags keys describe - describes a TagKey resource**

**SYNOPSIS**

: **`gcloud resource-manager tags keys describe` `[RESOURCE_NAME](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/describe#RESOURCE_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Gets metadata for a TagKey resource given the TagKey's resource name or
namespaced name.

**EXAMPLES**

: To describe a TagKey with id '123', run:

```
gcloud resource-manager tags keys describe tagkeys/123
```

To describe a TagKey with the name 'env' under organizations '456', run:

```
gcloud resource-manager tags keys describe 456/env
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
gcloud alpha resource-manager tags keys describe
```

```
gcloud beta resource-manager tags keys describe
```