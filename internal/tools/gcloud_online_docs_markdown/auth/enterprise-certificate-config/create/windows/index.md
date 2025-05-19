# gcloud auth enterprise-certificate-config create windows  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows)*

**NAME**

: **gcloud auth enterprise-certificate-config create windows - create an enterprise-certificate configuration file for Windows**

**SYNOPSIS**

: **`gcloud auth enterprise-certificate-config create windows` `[--issuer](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows#--issuer)`=`ISSUER` `[--provider](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows#--provider)`=`PROVIDER` `[--store](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows#--store)`=`STORE` [`[--ecp](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows#--ecp)`=`ECP`] [`[--ecp-client](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows#--ecp-client)`=`ECP_CLIENT`] [`[--output-file](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows#--output-file)`=`OUTPUT_FILE`] [`[--tls-offload](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows#--tls-offload)`=`TLS_OFFLOAD`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a configuration file used by gcloud to use the
enterprise-certificate-proxy component for mTLS.

**EXAMPLES**

: To create a credential configuration run:

```
gcloud auth enterprise-certificate-config create windows --issuer=$CERT_ISSUER --store=$STORE --provider=$PROVIDER
```

**REQUIRED FLAGS**

: **--issuer**:
The certificate issuer.

**--provider**:
The Windows secure store provider.

**--store**:
The Windows secure store.

**OPTIONAL FLAGS**

: **--ecp**:
Provide a custom path to the enterprise-certificate-proxy binary. This flag must
be the full path to the binary.

**--ecp-client**:
Provide a custom path to the enterprise-certificate-proxy shared client library.
This flag must be the full path to the shared library.

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
gcloud alpha auth enterprise-certificate-config create windows
```

```
gcloud beta auth enterprise-certificate-config create windows
```