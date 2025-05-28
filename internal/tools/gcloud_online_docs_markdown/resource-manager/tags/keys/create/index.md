# gcloud resource-manager tags keys create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create)*

**NAME**

: **gcloud resource-manager tags keys create - creates a TagKey resource under the specified tag parent**

**SYNOPSIS**

: **`gcloud resource-manager tags keys create` (`[SHORT_NAME](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create#SHORT_NAME)` `[--parent](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create#--parent)`=`PARENT`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create#--description)`=`DESCRIPTION`] [`[--purpose](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create#--purpose)`=`PURPOSE`] [`[--purpose-data](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create#--purpose-data)`=[`network`=`NETWORK`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a TagKey with the name env under 'organizations/123' with description
'description', run:

```
gcloud resource-manager tags keys create env --parent=organizations/123 --description=description
```

**POSITIONAL ARGUMENTS**

: **TagKey.
This must be specified.

**`SHORT_NAME`**:
User specified, friendly name of the TagKey or TagValue. The field must be 1-63
characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z])
with dashes (-), underscores ( _ ), dots (.), and alphanumerics between.
This positional argument must be specified if any of the other arguments in this
group are specified.

**--parent**:
Parent of the TagKey in the form of organizations/{org_id}.
This flag argument must be specified if any of the other arguments in this group
are specified.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
User-assigned description of the TagKey or TagValue. Must not exceed 256
characters.

**--purpose**:
Purpose specifier of the TagKey that can only be set on creation. Specifying
this field adds additional validation from the policy system that corresponds to
the purpose. `PURPOSE` must be one of:
`GCE_FIREWALL`, `DATA_GOVERNANCE`.

**--purpose-data**:
Purpose data of the TagKey that can only be set on creation. This data is
validated by the policy system that corresponds to the purpose.

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
gcloud alpha resource-manager tags keys create
```

```
gcloud beta resource-manager tags keys create
```