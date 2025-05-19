# gcloud alpha app ssl-certificates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/create](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/create)*

**NAME**

: **gcloud alpha app ssl-certificates create - uploads a new SSL certificate**

**SYNOPSIS**

: **`gcloud alpha app ssl-certificates create` `[--certificate](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/create#--certificate)`=`LOCAL_FILE_PATH` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/create#--display-name)`=`DISPLAY_NAME` `[--private-key](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/create#--private-key)`=`LOCAL_FILE_PATH` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The user must be the verified owner of the certificate
domain(s). Use the gcloud domains command group to manage domain ownership and
verification.

**EXAMPLES**

: To add a new SSL certificate to App Engine, run:

```
gcloud alpha app ssl-certificates create --display-name='example cert' --certificate='/home/user/me/my_cert.cer' --private-key='/home/user/me/my_key.pfx'
```

**REQUIRED FLAGS**

: **--certificate**:
The file path for the new certificate to upload. Must be in PEM x.509 format
including the header and footer.

**--display-name**:
A display name for this certificate.

**--private-key**:
The file path to a local RSA private key file. The private key must be PEM
encoded with header and footer and must be 2048 bits or fewer.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud app ssl-certificates create
```

```
gcloud beta app ssl-certificates create
```