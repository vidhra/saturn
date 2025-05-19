# gcloud certificate-manager dns-authorizations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete)*

**NAME**

: **gcloud certificate-manager dns-authorizations delete - delete a DNS Authorization**

**SYNOPSIS**

: **`gcloud certificate-manager dns-authorizations delete` (`[DNS_AUTHORIZATION](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete#DNS_AUTHORIZATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a DNS Authorization.

**EXAMPLES**

: To delete a DNS Authorization called `my-authorization`, run:

```
gcloud certificate-manager dns-authorizations delete my-authorization
```

**POSITIONAL ARGUMENTS**

: **DnsAuthorization resource - The name of the DNS Authorization to delete. The
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

**FLAGS**

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

: This command uses the `certificatemanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/certificate-manager](https://cloud.google.com/certificate-manager)

**NOTES**

: These variants are also available:

```
gcloud alpha certificate-manager dns-authorizations delete
```

```
gcloud beta certificate-manager dns-authorizations delete
```