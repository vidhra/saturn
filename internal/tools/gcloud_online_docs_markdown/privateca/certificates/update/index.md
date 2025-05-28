# gcloud privateca certificates update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update)*

**NAME**

: **gcloud privateca certificates update - update an existing certificate**

**SYNOPSIS**

: **`gcloud privateca certificates update` (`[CERTIFICATE](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update#CERTIFICATE)` : `[--issuer-location](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update#--issuer-location)`=`ISSUER_LOCATION` `[--issuer-pool](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update#--issuer-pool)`=`ISSUER_POOL`) [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update labels on a certificate:

```
gcloud privateca certificates update frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1 --update-labels=in_use=true
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE resource - The certificate to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE`**:
ID of the CERTIFICATE or fully qualified identifier for the CERTIFICATE.
To set the `certificate` attribute:

- provide the argument `CERTIFICATE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--issuer-location**:
The location of the CERTIFICATE.
To set the `issuer-location` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- provide the argument `--issuer-location` on the command line;
- set the property `privateca/location`.

**--issuer-pool**:
The parent CA Pool of the CERTIFICATE.
To set the `issuer-pool` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- provide the argument `--issuer-pool` on the command line.**

**FLAGS**

: **--update-labels**:
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