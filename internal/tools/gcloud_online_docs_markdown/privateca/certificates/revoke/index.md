# gcloud privateca certificates revoke  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke)*

**NAME**

: **gcloud privateca certificates revoke - revoke a certificate**

**SYNOPSIS**

: **`gcloud privateca certificates revoke` (`[--certificate](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke#--certificate)`=`CERTIFICATE`     | `[--serial-number](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke#--serial-number)`=`SERIAL_NUMBER`) [`[--reason](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke#--reason)`=`REASON`; default="unspecified"] [`[--issuer-pool](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke#--issuer-pool)`=`ISSUER_POOL` : `[--issuer-location](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke#--issuer-location)`=`ISSUER_LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Revokes the given certificate for the given reason.

**EXAMPLES**

: To revoke the 'frontend-server-tls' certificate due to key compromise:

```
gcloud privateca certificates revoke --certificate=frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1 --reason=key_compromise
```

To revoke the a certificate with the serial number
'7dc1d9186372de2e1f4824abb1c4c9e5e43cbb40' due to a newer one being issued:

```
gcloud privateca certificates revoke --serial-number=7dc1d9186372de2e1f4824abb1c4c9e5e43cbb40 --issuer-pool=my-pool --issuer-location=us-west1 --reason=superseded
```

**REQUIRED FLAGS**

: **The certificate identifier.
Exactly one of these must be specified:

**Certificate resource - The certificate to revoke. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--certificate` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `issuer-location` attribute:

- provide the argument `--certificate` on the command line with a fully
specified name;
- set the property `privateca/location`.

To set the `issuer-pool` attribute:

- provide the argument `--certificate` on the command line with a fully
specified name.

**--certificate**:
ID of the certificate or fully qualified identifier for the certificate.
To set the `certificate` attribute:

- provide the argument `--certificate` on the command line.**

**--serial-number**:
The serial number of the certificate.**

**OPTIONAL FLAGS**

: **--reason**:
Revocation reason to include in the CRL. `REASON` must be
one of: `affiliation-changed`,
`attribute-authority-compromise`,
`certificate-authority-compromise`, `certificate-hold`,
`cessation-of-operation`, `key-compromise`,
`privilege-withdrawn`, `unspecified`,
`superseded`.

**Issuing CA pool resource - The issuing CA pool of the certificate to revoke. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--issuer-pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--issuer-pool**:
ID of the Issuing CA pool or fully qualified identifier for the Issuing CA pool.
To set the `pool` attribute:

- provide the argument `--issuer-pool` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--issuer-location**:
The location of the Issuing CA pool.
To set the `issuer-location` attribute:

- provide the argument `--issuer-pool` on the command line with a fully
specified name;
- provide the argument `--issuer-location` on the command line;
- set the property `privateca/location`.**

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