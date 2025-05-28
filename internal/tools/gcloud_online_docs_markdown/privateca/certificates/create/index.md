# gcloud privateca certificates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create)*

**NAME**

: **gcloud privateca certificates create - create a new certificate**

**SYNOPSIS**

: **`gcloud privateca certificates create` [[`[CERTIFICATE](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#CERTIFICATE)`] `[--issuer-location](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--issuer-location)`=`ISSUER_LOCATION` `[--issuer-pool](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--issuer-pool)`=`ISSUER_POOL`] (`[--cert-output-file](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--cert-output-file)`=`CERT_OUTPUT_FILE`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--validate-only)`) (`[--csr](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--csr)`=`CSR`     | [(`[--dns-san](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--dns-san)`=[`DNS_SAN`,…] `[--email-san](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--email-san)`=[`EMAIL_SAN`,…] `[--ip-san](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--ip-san)`=[`IP_SAN`,…] `[--subject](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--subject)`=[`SUBJECT`,…] `[--uri-san](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--uri-san)`=[`URI_SAN`,…]) (`[--generate-key](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--generate-key)` `[--key-output-file](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--key-output-file)`=`KEY_OUTPUT_FILE` | [`[--kms-key-version](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--kms-key-version)`=`KMS_KEY_VERSION` : `[--kms-key](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--kms-key)`=`KMS_KEY` `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--kms-project)`=`KMS_PROJECT`]) : `[--use-preset-profile](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--use-preset-profile)`=`USE_PRESET_PROFILE` | `[--extended-key-usages](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--extended-key-usages)`=[`EXTENDED_KEY_USAGES`,…] `[--is-ca-cert](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--is-ca-cert)` `[--key-usages](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--key-usages)`=[`KEY_USAGES`,…] `[--max-chain-length](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--max-chain-length)`=`MAX_CHAIN_LENGTH` | `[--unconstrained-chain-length](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--unconstrained-chain-length)` `[--no-name-constraints-critical](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-constraints-critical)` `[--name-excluded-dns](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-excluded-dns)`=[`NAME_EXCLUDED_DNS`,…] `[--name-excluded-email](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-excluded-email)`=[`NAME_EXCLUDED_EMAIL`,…] `[--name-excluded-ip](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-excluded-ip)`=[`NAME_EXCLUDED_IP`,…] `[--name-excluded-uri](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-excluded-uri)`=[`NAME_EXCLUDED_URI`,…] `[--name-permitted-dns](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-permitted-dns)`=[`NAME_PERMITTED_DNS`,…] `[--name-permitted-email](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-permitted-email)`=[`NAME_PERMITTED_EMAIL`,…] `[--name-permitted-ip](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-permitted-ip)`=[`NAME_PERMITTED_IP`,…] `[--name-permitted-uri](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--name-permitted-uri)`=[`NAME_PERMITTED_URI`,…]]) [`[--ca](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--ca)`=`CA`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--subject-key-id](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--subject-key-id)`=`SUBJECT_KEY_ID`] [`[--validity](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--validity)`=`VALIDITY`; default="P30D"] [`[--template](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--template)`=`TEMPLATE` : `[--template-location](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#--template-location)`=`TEMPLATE_LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a certificate using a CSR:

```
gcloud privateca certificates create frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1 --csr=./csr.pem --cert-output-file=./cert.pem --validity=P30D
```

To create a certificate using a client-generated key:

```
gcloud privateca certificates create frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1 --generate-key --key-output-file=./key --cert-output-file=./cert.pem --dns-san=www.example.com --use-preset-profile=leaf_server_tls
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE resource - The name of the certificate to issue. If the certificate
ID is omitted, a random identifier will be generated according to the following
format: {YYYYMMDD}-{3 random alphanumeric characters}-{3 random alphanumeric
characters}. The certificate ID is not required when the issuing CA pool is in
the DevOps tier. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- certificate id will default to an automatically generated id with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`CERTIFICATE`]**:
ID of the CERTIFICATE or fully qualified identifier for the CERTIFICATE.
To set the `certificate` attribute:

- provide the argument `CERTIFICATE` on the command line;
- certificate id will default to an automatically generated id.

**--issuer-location**:
The location of the CERTIFICATE.
To set the `issuer-location` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- certificate id will default to an automatically generated id with a fully
specified name;
- provide the argument `--issuer-location` on the command line;
- set the property `privateca/location`.

**--issuer-pool**:
The parent CA Pool of the CERTIFICATE.
To set the `issuer-pool` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- certificate id will default to an automatically generated id with a fully
specified name;
- provide the argument `--issuer-pool` on the command line.**

**REQUIRED FLAGS**

: **--cert-output-file**

**--csr**

**OPTIONAL FLAGS**

: **--ca**:
The name of an existing certificate authority to use for issuing the
certificate. If omitted, a certificate authority will be will be chosen from the
CA pool by the service on your behalf.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--subject-key-id**:
Optional field to specify subject key ID for certificate. DO NOT USE except to
maintain a previously established identifier for a public key, whose SKI was not
generated using method (1) described in RFC 5280 section 4.2.1.2.

**--validity**:
The validity of this certificate, as an ISO8601 duration. Defaults to 30 days.

**Certificate template resource - The name of a certificate template to use for
issuing this certificate, if desired. A template may overwrite parts of the
certificate request, and the use of certificate templates may be required and/or
regulated by the issuing CA Pool's CA Manager. The specified template must be in
the same location as the issuing CA Pool. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--template` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--template**:
ID of the certificate_template or fully qualified identifier for the
certificate_template.
To set the `certificate template` attribute:

- provide the argument `--template` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--template-location**:
The location of the certificate_template.
To set the `location` attribute:

- provide the argument `--template` on the command line with a fully
specified name;
- provide the argument `--template-location` on the command line;
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