# gcloud data-catalog tag-templates add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/add-iam-policy-binding)*

**NAME**

: **gcloud data-catalog tag-templates add-iam-policy-binding - add IAM policy binding to a Data Catalog tag template**

**SYNOPSIS**

: **`gcloud data-catalog tag-templates add-iam-policy-binding` (`[TAG_TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/add-iam-policy-binding#TAG_TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/add-iam-policy-binding#--location)`=`LOCATION`) `[--member](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/add-iam-policy-binding#--role)`=`ROLE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex
aspect-types](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types)` instead.
Add IAM policy binding to a Data Catalog tag template.

**EXAMPLES**

: To add an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' with tag template 'my-tag-template' and location
'us-central1', run:

```
gcloud data-catalog tag-templates add-iam-policy-binding my-tag-template --location='us-central1' --member='user:test-user@gmail.com' --role='roles/editor'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Tag template resource - Tag template for which to add IAM policy binding to. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `tag_template` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TAG_TEMPLATE`**:
ID of the tag template or fully qualified identifier for the tag template.
To set the `tag_template` attribute:

- provide the argument `tag_template` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the tag template.
To set the `location` attribute:

- provide the argument `tag_template` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--member**:
The principal to add the binding for. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.
Some resources also accept the following special values:

- `allUsers` - Special identifier that represents anyone who is on the
internet, with or without a Google account.
- `allAuthenticatedUsers` - Special identifier that represents anyone
who is authenticated with a Google account or a service account.

**--role**:
Role name to assign to the principal. The role name is the complete path of a
predefined role, such as `roles/logging.viewer`, or the role ID for a
custom role, such as
`organizations/{ORGANIZATION_ID}/roles/logging.viewer`.

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

**API REFERENCE**

: This command uses the `datacatalog/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/data-catalog/docs/](https://cloud.google.com/data-catalog/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha data-catalog tag-templates add-iam-policy-binding
```

```
gcloud beta data-catalog tag-templates add-iam-policy-binding
```