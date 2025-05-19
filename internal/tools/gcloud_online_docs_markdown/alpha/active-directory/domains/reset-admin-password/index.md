# gcloud alpha active-directory domains reset-admin-password  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/reset-admin-password](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/reset-admin-password)*

**NAME**

: **gcloud alpha active-directory domains reset-admin-password - reset the admin password for a Managed Microsoft AD domain**

**SYNOPSIS**

: **`gcloud alpha active-directory domains reset-admin-password` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/reset-admin-password#DOMAIN)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/reset-admin-password#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Reset the delegated admin password for a Managed Microsoft
AD domain given a valid AD domain fully-qualified domain name.
This command can fail for the following reasons:

- The AD domain specified does not exist.
- The active account does not have permission to access the given AD domain.

**EXAMPLES**

: The following command resets the admin password for an AD domain with the name
`my-domain.com`.

```
gcloud alpha active-directory domains reset-admin-password my-domain.com
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the Managed Microsoft AD domain you want to reset the
password for. This represents a Cloud resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `domain` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DOMAIN`**:
ID of the domain or fully qualified identifier for the domain.
To set the `domain` attribute:

- provide the argument `domain` on the command line.**

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

: This command uses the `managedidentities/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud active-directory domains reset-admin-password
```

```
gcloud beta active-directory domains reset-admin-password
```