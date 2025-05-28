# gcloud alpha certificate-manager dns-authorizations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create)*

**NAME**

: **gcloud alpha certificate-manager dns-authorizations create - create a DNS Authorization**

**SYNOPSIS**

: **`gcloud alpha certificate-manager dns-authorizations create` (`[DNS_AUTHORIZATION](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create#DNS_AUTHORIZATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create#--location)`=`LOCATION`) `[--domain](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create#--domain)`=`DOMAIN` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--type](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create#--type)`=`TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new DNS Authorization.

**EXAMPLES**

: To create a DNS authorization called `my-authorization`, run:

```
gcloud alpha certificate-manager dns-authorizations create my-authorization --domain=host.example.com
```

**POSITIONAL ARGUMENTS**

: **DnsAuthorization resource - The name of the DNS Authorization to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `dns_authorization` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DNS_AUTHORIZATION`**:
ID of the dnsAuthorization or fully qualified identifier for the
dnsAuthorization.
To set the `dns_authorization` attribute:

- provide the argument `dns_authorization` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Certificate Manager location.
To set the `location` attribute:

- provide the argument `dns_authorization` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- default value of location is [global].**

**REQUIRED FLAGS**

: **--domain**:
Public domain name to create an authorization for.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Human-readable description of the resource.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--type**:
Type of the DNS authorization. `TYPE` must be one of:
`fixed-record`, `per-project-record`,
`type-unspecified`.

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

: This command uses the `certificatemanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/certificate-manager](https://cloud.google.com/certificate-manager)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud certificate-manager dns-authorizations create
```

```
gcloud beta certificate-manager dns-authorizations create
```