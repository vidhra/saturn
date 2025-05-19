# gcloud beta active-directory domains trusts update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/trusts/update](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/trusts/update)*

**NAME**

: **gcloud beta active-directory domains trusts update - update target DNS IP addresses for a Managed Microsoft AD trust**

**SYNOPSIS**

: **`gcloud beta active-directory domains trusts update` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/trusts/update#DOMAIN)` `[--target-dns-ip-addresses](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/trusts/update#--target-dns-ip-addresses)`=[`TARGET_DNS_IP_ADDRESSES`,…] `[--target-domain-name](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/trusts/update#--target-domain-name)`=`TARGET_DOMAIN_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/trusts/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/trusts/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Update target DNS IP addresses for a Managed Microsoft AD
trust between the managed domain and the target domain.

```
This command can fail for the following reasons:
  * The domain specified does not exist.
  * The active account does not have permission to access the given
    domain.
  * The AD trust specified does not exist.
  * The active account does not have permission to access the given
    AD trust.
```

**EXAMPLES**

: The following command updates the target DNS IP address for the AD trust between
`my-domain.com` and `my-target-domain.com` to
`10.177.0.3`.

```
gcloud beta active-directory domains trusts update my-domain.com --target-domain-name=my-target-domain.com --target-dns-ip-addresses=10.177.0.3
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the Managed Microsoft AD trust for which you want to
update target DNS IP Addresses. This represents a Cloud resource. (NOTE) Some
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

: **--target-dns-ip-addresses**:
DNS server IP addresses that can resolve the target domain.
Only IPv4 is supported.

**--target-domain-name**:
Target domain name for the Managed Microsoft AD trust you want to update.

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

: This command uses the `managedidentities/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud active-directory domains trusts update
```

```
gcloud alpha active-directory domains trusts update
```