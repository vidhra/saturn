# gcloud iam roles describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/roles/describe](https://cloud.google.com/sdk/gcloud/reference/iam/roles/describe)*

**NAME**

: **gcloud iam roles describe - show metadata for a role**

**SYNOPSIS**

: **`gcloud iam roles describe` `[ROLE_ID](https://cloud.google.com/sdk/gcloud/reference/iam/roles/describe#ROLE_ID)` [`[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/roles/describe#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/iam/roles/describe#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/roles/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command shows metadata for a role.
This command can fail for the following reasons:

- The role specified does not exist.
- The active user does not have permission to access the given role.

**EXAMPLES**

: To print metadata for the role
``spanner.databaseAdmin`` of the organization
``1234567``, run:

```
gcloud iam roles describe roles/spanner.databaseAdmin --organization=1234567
```

To print metadata for the role
``spanner.databaseAdmin`` of the project
``myproject``, run:

```
gcloud iam roles describe roles/spanner.databaseAdmin --project=myproject
```

To print metadata for a predefined role,
``spanner.databaseAdmin``, run:

```
gcloud iam roles describe roles/spanner.databaseAdmin
```

**POSITIONAL ARGUMENTS**

: **`ROLE_ID`**:
ID of the role to describe. Curated roles example: roles/viewer. Custom roles
example: CustomRole. For custom roles, you must also specify the
`--organization` or `--project` flag.

**FLAGS**

: **--organization**

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
gcloud alpha iam roles describe
```

```
gcloud beta iam roles describe
```