# gcloud certificate-manager certificates update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update)*

**NAME**

: **gcloud certificate-manager certificates update - update a certificate**

**SYNOPSIS**

: **`gcloud certificate-manager certificates update` (`[CERTIFICATE](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#CERTIFICATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#--description)`=`DESCRIPTION`] [`[--certificate-file](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#--certificate-file)`=`PATH_TO_FILE` `[--private-key-file](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#--private-key-file)`=`PATH_TO_FILE`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates existing certificate.

**EXAMPLES**

: To update a certificate with name simple-cert, run:

```
gcloud certificate-manager certificates update simple-cert --description="desc" --update-labels="key=value" --certificate-file=cert.pem --private-key-file=key.pem
```

**POSITIONAL ARGUMENTS**

: **Certificate resource - The certificate to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `certificate` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE`**:
ID of the certificate or fully qualified identifier for the certificate.
To set the `certificate` attribute:

- provide the argument `certificate` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the certificate.
To set the `location` attribute:

- provide the argument `certificate` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- default value of location is [global].**

**COMMONLY USED FLAGS**

: **--description**:
Text description of a certificate.

**--certificate-file**

**OTHER FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud alpha certificate-manager certificates update
```

```
gcloud beta certificate-manager certificates update
```