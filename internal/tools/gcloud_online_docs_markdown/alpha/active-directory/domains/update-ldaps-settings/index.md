# gcloud alpha active-directory domains update-ldaps-settings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings)*

**NAME**

: **gcloud alpha active-directory domains update-ldaps-settings - update the LDAPS settings for a domain**

**SYNOPSIS**

: **`gcloud alpha active-directory domains update-ldaps-settings` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings#DOMAIN)` (`[--clear-certificates](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings#--clear-certificates)`     | [`[--certificate-pfx-file](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings#--certificate-pfx-file)`=`PATH_TO_FILE` : `[--certificate-password](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings#--certificate-password)`=`CERTIFICATE_PASSWORD`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Managed Microsoft AD domain's Lightweight
Directory Access Protocol over TLS/SSL (LDAPS) settings. You must be safelisted
for the Managed AD LDAPS Alpha in order to use this feature. Consult the API
documentation for a list of certificate requirements.
This command can fail for the following reasons:

- The certificate is invalid.
- The domain specified does not exist.
- The active account does not have permission to view LDAPS settings for the
domain.

**EXAMPLES**

: To enable LDAPS for the first time or update the certificates being used:

```
gcloud alpha active-directory domains update-ldaps-settings my-domain.com --certificate-pfx-file=certificate-chain-with-private-key.pfx --certificate-password="password"
```

To disable LDAPS:

```
gcloud alpha active-directory domains update-ldaps-settings my-domain.com --clear-certificates
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the managed Managed Microsoft AD domain you want to
update. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
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

: **--clear-certificates**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
allowlist. These variants are also available:

```
gcloud active-directory domains update-ldaps-settings
```

```
gcloud beta active-directory domains update-ldaps-settings
```