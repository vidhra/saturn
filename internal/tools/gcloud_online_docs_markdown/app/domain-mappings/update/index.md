# gcloud app domain-mappings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/update](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/update)*

**NAME**

: **gcloud app domain-mappings update - updates a domain mapping**

**SYNOPSIS**

: **`gcloud app domain-mappings update` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/update#DOMAIN)` [`[--certificate-management](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/update#--certificate-management)`=`CERTIFICATE_MANAGEMENT`] [`[--certificate-id](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/update#--certificate-id)`=`CERTIFICATE_ID`     | `[--no-certificate-id](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/update#--certificate-id)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a domain mapping.

**EXAMPLES**

: To update an App Engine domain mapping, run:

```
gcloud app domain-mappings update '*.example.com' --certificate-id=1234
```

To remove a certificate from a domain:

```
gcloud app domain-mappings update '*.example.com' --no-certificate-id
```

**POSITIONAL ARGUMENTS**

: **`DOMAIN`**:
A valid domain which may begin with a wildcard, such as:
`example.com` or `*.example.com`

**FLAGS**

: **--certificate-management**:
Type of certificate management. 'automatic' will provision an SSL certificate
automatically while 'manual' requires the user to provide a certificate id to
provision. `CERTIFICATE_MANAGEMENT` must be one of:
`automatic`, `manual`.

**--certificate-id**

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
gcloud alpha app domain-mappings update
```

```
gcloud beta app domain-mappings update
```