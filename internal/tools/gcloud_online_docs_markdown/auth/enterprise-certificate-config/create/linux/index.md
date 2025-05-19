# gcloud auth enterprise-certificate-config create linux  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux)*

**NAME**

: **gcloud auth enterprise-certificate-config create linux - create an enterprise-certificate configuration file for Linux**

**SYNOPSIS**

: **`gcloud auth enterprise-certificate-config create linux` `[--label](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#--label)`=`LABEL` `[--module](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#--module)`=`MODULE` `[--slot](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#--slot)`=`SLOT` [`[--ecp](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#--ecp)`=`ECP`] [`[--ecp-client](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#--ecp-client)`=`ECP_CLIENT`] [`[--output-file](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#--output-file)`=`OUTPUT_FILE`] [`[--tls-offload](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#--tls-offload)`=`TLS_OFFLOAD`] [`[--user-pin](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#--user-pin)`=`USER_PIN`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/linux#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a configuration file used by gcloud to use the
enterprise-certificate-proxy component for mTLS.

**EXAMPLES**

: To create a credential configuration run:

```
gcloud auth enterprise-certificate-config create linux --module=$PATH_TO_PKCS11_MODULE --slot=$PKCS11_SLOT_ID --label=$PKCS11_OBJECT_LABEL --user-pin=$PKCS11_USER_PIN
```

**REQUIRED FLAGS**

: **--label**:
The PKCS #11 label for the target credentials. The certificate, public key, and
private key MUST have the same label. enterprise-certificate-proxy will use all
three objects.

**--module**:
The full file path to the PKCS #11 module.

**--slot**:
The PKCS #11 slot containing the target credentials.

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

**--user-pin**:
The user pin used to login to the PKCS #11 module. If there is no user pin leave
this field empty.

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
gcloud alpha auth enterprise-certificate-config create linux
```

```
gcloud beta auth enterprise-certificate-config create linux
```