# gcloud compute ssl-certificates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create)*

**NAME**

: **gcloud compute ssl-certificates create - create a Compute Engine SSL certificate**

**SYNOPSIS**

: **`gcloud compute ssl-certificates create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#NAME)` (`[--domains](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#--domains)`=`DOMAIN`,[`[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#DOMAIN)`,…]     | `[--certificate](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#--certificate)`=`LOCAL_FILE_PATH` `[--private-key](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#--private-key)`=`LOCAL_FILE_PATH`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#--description)`=`DESCRIPTION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute ssl-certificates create` creates SSL certificate
resources, which you can use in a target HTTPS or target SSL proxy. An SSL
certificate resource consists of a certificate and private key. The private key
is encrypted before it is stored.
You can create either a managed or a self-managed SslCertificate resource. A
managed SslCertificate is provisioned and renewed for you. A self-managed
certificate is created by passing the certificate obtained from Certificate
Authority through `--certificate` and `--private-key`
flags.

**EXAMPLES**

: To create a self-managed certificate resource 'my-cert' from a certificate
placed under path 'foo/cert' and a private key placed under path 'foo/pk', run:

```
gcloud compute ssl-certificates create my-cert --certificate=foo/cert --private-key=foo/pk
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the SSL certificate to create.

**REQUIRED FLAGS**

: **--domains**

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the SSL certificate.

**--global**

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
gcloud alpha compute ssl-certificates create
```

```
gcloud beta compute ssl-certificates create
```