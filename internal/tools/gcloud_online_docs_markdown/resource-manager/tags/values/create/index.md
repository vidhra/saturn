# gcloud resource-manager tags values create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create)*

**NAME**

: **gcloud resource-manager tags values create - creates a TagValue resource**

**SYNOPSIS**

: **`gcloud resource-manager tags values create` (`[SHORT_NAME](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create#SHORT_NAME)` `[--parent](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create#--parent)`=`PARENT`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a TagValue resource given the short_name and description (optional) as
well as the parent, the of the TagValue. The parent of the TagValue is always a
TagKey and the TagKey's details can be passed as a numeric id or the namespaced
name.

**EXAMPLES**

: To create a TagValue with the short name 'test' and the description
'description' under a TagKey with a short name 'env' under 'organizations/123',
run:

```
gcloud resource-manager tags values create test --parent=123/env --description=description
```

To create a TagValue with the short name 'test' under TagKey with id '456', run:

```
gcloud resource-manager tags values create test --parent=tagKeys/456 --description=description
```

**POSITIONAL ARGUMENTS**

: **TagValue.
This must be specified.

**`SHORT_NAME`**:
User specified, friendly name of the TagKey or TagValue. The field must be 1-63
characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z])
with dashes (-), underscores ( _ ), dots (.), and alphanumerics between.
This positional argument must be specified if any of the other arguments in this
group are specified.

**--parent**:
Parent of the TagValue in either in the form of tagKeys/{id} or
{org_id}/{tagkey_short_name}
This flag argument must be specified if any of the other arguments in this group
are specified.**

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
gcloud alpha resource-manager tags values create
```

```
gcloud beta resource-manager tags values create
```