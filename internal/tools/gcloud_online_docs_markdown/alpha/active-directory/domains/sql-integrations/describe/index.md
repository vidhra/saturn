# gcloud alpha active-directory domains sql-integrations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/sql-integrations/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/sql-integrations/describe)*

**NAME**

: **gcloud alpha active-directory domains sql-integrations describe - describe a Cloud SQL integration against a Managed Microsoft AD domain**

**SYNOPSIS**

: **`gcloud alpha active-directory domains sql-integrations describe` (`[SQL_INTEGRATION](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/sql-integrations/describe#SQL_INTEGRATION)` : `[--domain](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/sql-integrations/describe#--domain)`=`DOMAIN`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/sql-integrations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a Cloud SQL integration against a Managed
Microsoft AD domain.
Displays all details of a Cloud SQL integration given a valid integration ID.

**EXAMPLES**

: To describe a Cloud SQL integration with the ID `my-integration`
under the managed AD domain `my-domain`, run:

```
gcloud alpha active-directory domains sql-integrations describe my-integration --domain=my-domain --project=my-project
```

**POSITIONAL ARGUMENTS**

: **SQL integration resource - Arguments and flags that specify the SQL integration
you want to describe. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `sql_integration` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SQL_INTEGRATION`**:
ID of the SQL integration or fully qualified identifier for the SQL integration.
To set the `sql_integration` attribute:

- provide the argument `sql_integration` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--domain**:
The fully-qualified domain name of the Microsoft Active Directory domain.
To set the `domain` attribute:

- provide the argument `sql_integration` on the command line with a
fully specified name;
- provide the argument `--domain` on the command line.**

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

: This command uses the `managedidentities/v1alpha1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta active-directory domains sql-integrations describe
```