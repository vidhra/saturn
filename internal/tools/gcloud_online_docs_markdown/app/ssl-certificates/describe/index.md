# gcloud app ssl-certificates describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/ssl-certificates/describe](https://cloud.google.com/sdk/gcloud/reference/app/ssl-certificates/describe)*

**NAME**

: **gcloud app ssl-certificates describe - describes a specified SSL certificate**

**SYNOPSIS**

: **`gcloud app ssl-certificates describe` `[ID](https://cloud.google.com/sdk/gcloud/reference/app/ssl-certificates/describe#ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/ssl-certificates/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describes a specified SSL certificate.

**EXAMPLES**

: To describe an App Engine SSL certificate, run:

```
gcloud app ssl-certificates describe 1234
```

**POSITIONAL ARGUMENTS**

: **`ID`**:
The id of the certificate. This identifier is printed upon creation of a new
certificate. Run `[gcloud app
ssl-certificates list](https://cloud.google.com/sdk/gcloud/reference/app/ssl-certificates/list)` to view existing certificates.

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
gcloud alpha app ssl-certificates describe
```

```
gcloud beta app ssl-certificates describe
```