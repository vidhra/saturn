# gcloud active-directory domains trusts create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create)*

**NAME**

: **gcloud active-directory domains trusts create - create a Microsoft Active Directory Trust between a Managed Microsoft AD domain and another domain**

**SYNOPSIS**

: **`gcloud active-directory domains trusts create` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#DOMAIN)` `[--target-dns-ip-addresses](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#--target-dns-ip-addresses)`=[`TARGET_DNS_IP_ADDRESSES`,…] `[--target-domain-name](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#--target-domain-name)`=`TARGET_DOMAIN_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#--async)`] [`[--direction](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#--direction)`=`DIRECTION`; default="BIDIRECTIONAL"] [`[--handshake-secret](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#--handshake-secret)`=`HANDSHAKE_SECRET`] [`[--selective-authentication](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#--selective-authentication)`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#--type)`=`TYPE`; default="FOREST"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Microsoft Active Directory Trust between a Managed Microsoft AD domain
and another domain.
This command can fail for the following reasons:

- The domain specified does not exist.
- The active account does not have permission to access the given domain.
- A trust already exists with the same target domain name.
- The active account does not have permission to create AD trusts.

**EXAMPLES**

: The following command creates an external, bidirectional AD trust between
`my-domain.com` and `target-domain.com`.

```
gcloud active-directory domains trusts create my-domain.com --target-domain-name=target-domain.com --target-dns-ip-addresses=10.177.0.2 --type=EXTERNAL --direction=BIDIRECTIONAL --selective-authentication=false --async
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the Managed Microsoft AD domain you want to create an
AD trust from. This represents a Cloud resource. (NOTE) Some attributes are not
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

**REQUIRED FLAGS**

: **--target-dns-ip-addresses**:
Target DNS server IP addresses that can resolve the target domain.
Only IPv4 is supported.

**--target-domain-name**:
Target domain name for the Managed Microsoft AD Trust.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--direction**:
Direction of the trust.
Must be one of: INBOUND, OUTBOUND, BIDIRECTIONAL. Default is BIDIRECTIONAL.
`DIRECTION` must be one of: `bidirectional`,
`inbound`, `outbound`,
`trust-direction-unspecified`.

**--handshake-secret**:
Trust handshake secret with target domain. The secret will not be stored. If not
specified, command will prompt user for secret.

**--selective-authentication**:
If specified, trusted side will only have selective access to approved set of
resources.
Otherwise, the trusted side has forest/domain wide access. Default is false.

**--type**:
Type of the trust. Must be FOREST or EXTERNAL. Default is FOREST.
`TYPE` must be one of: `external`,
`forest`, `trust-type-unspecified`.

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

: These variants are also available:

```
gcloud alpha active-directory domains trusts create
```

```
gcloud beta active-directory domains trusts create
```