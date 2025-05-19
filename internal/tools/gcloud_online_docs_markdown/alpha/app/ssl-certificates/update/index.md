# gcloud alpha app ssl-certificates update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/update](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/update)*

**NAME**

: **gcloud alpha app ssl-certificates update - updates an SSL certificate**

**SYNOPSIS**

: **`gcloud alpha app ssl-certificates update` `[ID](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/update#ID)` [`[--certificate](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/update#--certificate)`=`LOCAL_FILE_PATH`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/update#--display-name)`=`DISPLAY_NAME`] [`[--private-key](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/update#--private-key)`=`LOCAL_FILE_PATH`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Updates an SSL certificate.

**EXAMPLES**

: To update an App Engine SSL certificate, run:

```
gcloud alpha app ssl-certificates update 1234 --display-name='updated name' --certificate='/home/user/me/new_cert.cer' --private-key='/home/user/me/new_key.pfx'
```

**POSITIONAL ARGUMENTS**

: **`ID`**:
The id of the certificate. This identifier is printed upon creation of a new
certificate. Run `[gcloud alpha app
ssl-certificates list](https://cloud.google.com/sdk/gcloud/reference/alpha/app/ssl-certificates/list)` to view existing certificates.

**FLAGS**

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
gcloud app ssl-certificates update
```

```
gcloud beta app ssl-certificates update
```