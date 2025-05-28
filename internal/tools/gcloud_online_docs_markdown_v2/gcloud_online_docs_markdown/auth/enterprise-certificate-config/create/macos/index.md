# gcloud auth enterprise-certificate-config create macos  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos)*

**NAME**

: **gcloud auth enterprise-certificate-config create macos - create an enterprise-certificate configuration file for MacOS**

**SYNOPSIS**

: **`gcloud auth enterprise-certificate-config create macos` `[--issuer](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos#--issuer)`=`ISSUER` [`[--ecp](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos#--ecp)`=`ECP`] [`[--ecp-client](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos#--ecp-client)`=`ECP_CLIENT`] [`[--keychain-type](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos#--keychain-type)`=`KEYCHAIN_TYPE`; default="all"] [`[--output-file](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos#--output-file)`=`OUTPUT_FILE`] [`[--tls-offload](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos#--tls-offload)`=`TLS_OFFLOAD`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a configuration file used by gcloud to use the
enterprise-certificate-proxy component for mTLS.

**EXAMPLES**

: To create a credential configuration run:

```
gcloud auth enterprise-certificate-config create macos --issuer=$CERT_ISSUER
```

**REQUIRED FLAGS**

: **--issuer**:
The certificate issuer.

**OPTIONAL FLAGS**

: **--ecp**:
Provide a custom path to the enterprise-certificate-proxy binary. This flag must
be the full path to the binary.

**--ecp-client**:
Provide a custom path to the enterprise-certificate-proxy shared client library.
This flag must be the full path to the shared library.

**--keychain-type**:
Specify the target keychain(s) for certificate lookup.Accepted values are
"login", "system", or "all". If omitted,defaults to "all". Use "all" to include
custom keychains.

**--output-file**:
Override the file path that the enterprise-certificate-proxy configuration is
written to.

**--tls-offload**:
Provide a custom path to the enterprise-certificate-proxy shared tls offload
library. This flag must be the full path to the shared library.

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
gcloud alpha auth enterprise-certificate-config create macos
```

```
gcloud beta auth enterprise-certificate-config create macos
```