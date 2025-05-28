# gcloud resource-manager tags bindings create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create)*

**NAME**

: **gcloud resource-manager tags bindings create - creates a TagBinding resource**

**SYNOPSIS**

: **`gcloud resource-manager tags bindings create` `[--parent](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create#--parent)`=`PARENT` `[--tag-value](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create#--tag-value)`=`TAG_VALUE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create#--async)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a TagBinding given the TagValue and the parent cloud resource the
TagValue will be attached to. The TagValue can be represented with its numeric
id or its namespaced name of
{parent_namespace}/{tag_key_short_name}/{tag_value_short_name}. The parent
resource should be represented with its full resource name. See: [https://cloud.google.com/apis/design/resource_names#full_resource_name](https://cloud.google.com/apis/design/resource_names#full_resource_name).

**EXAMPLES**

: To create a TagBinding between tagValues/123 and Project with name
``//cloudresourcemanager.googleapis.com/projects/1234``
run:

```
gcloud resource-manager tags bindings create --tag-value=tagValues/123 --parent=//cloudresourcemanager.googleapis.com/projects/1234
```

To create a TagBinding between TagValue
``test`` under TagKey
``env`` and Project with name
``//cloudresourcemanager.googleapis.com/projects/1234``
run:

```
gcloud resource-manager tags bindings create --tag-value=789/env/test --parent=//cloudresourcemanager.googleapis.com/projects/1234
```

**REQUIRED FLAGS**

: **--parent**:
Full resource name of the resource to attach to the tagValue.

**--tag-value**:
Tag value name or namespaced name. The name should be in the form
tagValues/{numeric_id}. The namespaced name should be in the form
{org_id}/{tag_key_short_name}/{short_name} where short_name must be 1-63
characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z])
with dashes (-), underscores (`), dots (.), and alphanumerics between.`

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--location**:
Region or zone of the resource to bind to the TagValue. This field is not
required if the resource is a global resource like projects, folders and
organizations.

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
gcloud alpha resource-manager tags bindings create
```

```
gcloud beta resource-manager tags bindings create
```