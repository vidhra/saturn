# gcloud privateca certificates describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe)*

**NAME**

: **gcloud privateca certificates describe - get metadata for a certificate**

**SYNOPSIS**

: **`gcloud privateca certificates describe` (`[CERTIFICATE](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe#CERTIFICATE)` : `[--issuer-location](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe#--issuer-location)`=`ISSUER_LOCATION` `[--issuer-pool](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe#--issuer-pool)`=`ISSUER_POOL`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns metadata for the given certificate.

**EXAMPLES**

: To get metadata for the 'frontend-server-tls' certificate:

```
gcloud privateca certificates describe frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1
```

To download the PEM-encoded certificate for the 'frontend-server-tls'
certificate to a file called 'frontend-server-tls.crt':

```
gcloud privateca certificates describe frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1 --format="value(pemCertificate)" > ./frontend-server-tls.crt
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE resource - The certificate for which to obtain metadata. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `certificate` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE`**:
ID of the CERTIFICATE or fully qualified identifier for the CERTIFICATE.
To set the `certificate` attribute:

- provide the argument `certificate` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--issuer-location**:
The location of the CERTIFICATE.
To set the `issuer-location` attribute:

- provide the argument `certificate` on the command line with a fully
specified name;
- provide the argument `--issuer-location` on the command line;
- set the property `privateca/location`.

**--issuer-pool**:
The ID of the issuing CA Pool.
To set the `issuer-pool` attribute:

- provide the argument `certificate` on the command line with a fully
specified name;
- provide the argument `--issuer-pool` on the command line.**

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

**API REFERENCE**

: This command uses the `privateca/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/](https://cloud.google.com/)