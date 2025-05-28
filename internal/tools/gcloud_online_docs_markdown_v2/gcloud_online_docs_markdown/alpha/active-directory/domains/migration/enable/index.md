# gcloud alpha active-directory domains migration enable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable)*

**NAME**

: **gcloud alpha active-directory domains migration enable - enable domain migration permissions on a Managed Microsoft AD domain**

**SYNOPSIS**

: **`gcloud alpha active-directory domains migration enable` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable#DOMAIN)` `[--onprem-domains](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable#--onprem-domains)`=[`ONPREM_DOMAINS`,…] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable#--async)`] [`[--disable-sid-filtering-domains](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable#--disable-sid-filtering-domains)`=[`DISABLE_SID_FILTERING_DOMAINS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Enable domain migration permissions on a Managed Microsoft
AD domain.
This command can fail for the following reasons:

- The specified domain doesn't exist.
- The specified domain is either being created or updated.
- The active account doesn't have permission to enable migration permissions on
the specified domain.

**EXAMPLES**

: The following command enables migration permissions on the domain
`my-domain.com` in project `my-project` for two
on-premises domains `onprem-domain-1.com` and
`onprem-domain-2.com`, with SID Filtering disabled for
`onprem-domain-1.com`.

```
gcloud alpha active-directory domains migration enable my-domain.com --onprem-domains=onprem-domain-1.com,onprem-domain-2.com --disable-sid-filtering-domains=onprem-domain-1.com --project=my-project --async
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the Managed Microsoft AD domain on which you want to
enable migration permissions. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--onprem-domains**:
List of trusted domains that are being migrated.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--disable-sid-filtering-domains**:
List of migrating domains on which SID Filtering must be disabled. The list is
empty by default.

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
gcloud beta active-directory domains migration enable
```