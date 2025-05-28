# gcloud privateca subordinates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create)*

**NAME**

: **gcloud privateca subordinates create - create a new subordinate certificate authority**

**SYNOPSIS**

: **`gcloud privateca subordinates create` (`[CERTIFICATE_AUTHORITY](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#CERTIFICATE_AUTHORITY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--location)`=`LOCATION` `[--pool](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--pool)`=`POOL`) (`[--create-csr](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--create-csr)` `[--csr-output-file](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--csr-output-file)`=`CSR_OUTPUT_FILE`     | [`[--issuer-pool](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--issuer-pool)`=`ISSUER_POOL` : `[--issuer-location](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--issuer-location)`=`ISSUER_LOCATION`]) [`[--auto-enable](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--auto-enable)`] [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--bucket)`=`BUCKET`] [`[--custom-aia-urls](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--custom-aia-urls)`=[`CUSTOM_AIA_URLS`,…]] [`[--custom-cdp-urls](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--custom-cdp-urls)`=[`CUSTOM_CDP_URLS`,…]] [`[--dns-san](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--dns-san)`=[`DNS_SAN`,…]] [`[--email-san](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--email-san)`=[`EMAIL_SAN`,…]] [`[--from-ca](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--from-ca)`=`FROM_CA`] [`[--ip-san](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--ip-san)`=[`IP_SAN`,…]] [`[--issuer-ca](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--issuer-ca)`=`ISSUER_CA`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--subject](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--subject)`=[`SUBJECT`,…]] [`[--subject-key-id](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--subject-key-id)`=`SUBJECT_KEY_ID`] [`[--uri-san](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--uri-san)`=[`URI_SAN`,…]] [`[--validity](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--validity)`=`VALIDITY`; default="P3Y"] [`[--key-algorithm](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--key-algorithm)`=`KEY_ALGORITHM`; default="rsa-pkcs1-2048-sha256"     | [`[--kms-key-version](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--kms-key-version)`=`KMS_KEY_VERSION` : `[--kms-key](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--kms-key)`=`KMS_KEY` `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--kms-project)`=`KMS_PROJECT`]] [`[--use-preset-profile](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--use-preset-profile)`=`USE_PRESET_PROFILE`     | `[--extended-key-usages](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--extended-key-usages)`=[`EXTENDED_KEY_USAGES`,…] `[--key-usages](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--key-usages)`=[`KEY_USAGES`,…] `[--max-chain-length](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--max-chain-length)`=`MAX_CHAIN_LENGTH`     | `[--unconstrained-chain-length](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--unconstrained-chain-length)` `[--no-name-constraints-critical](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-constraints-critical)` `[--name-excluded-dns](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-excluded-dns)`=[`NAME_EXCLUDED_DNS`,…] `[--name-excluded-email](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-excluded-email)`=[`NAME_EXCLUDED_EMAIL`,…] `[--name-excluded-ip](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-excluded-ip)`=[`NAME_EXCLUDED_IP`,…] `[--name-excluded-uri](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-excluded-uri)`=[`NAME_EXCLUDED_URI`,…] `[--name-permitted-dns](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-permitted-dns)`=[`NAME_PERMITTED_DNS`,…] `[--name-permitted-email](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-permitted-email)`=[`NAME_PERMITTED_EMAIL`,…] `[--name-permitted-ip](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-permitted-ip)`=[`NAME_PERMITTED_IP`,…] `[--name-permitted-uri](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#--name-permitted-uri)`=[`NAME_PERMITTED_URI`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a subordinate CA named 'server-tls-1' whose issuer is on Private CA:

```
gcloud privateca subordinates create server-tls-1 --location=us-west1 --pool=my-pool --subject="CN=Example TLS CA, O=Google" --issuer-pool=other-pool --issuer-location=us-west1 --kms-key-version="projects/my-project-pki/locations/us-west1/keyRings/kr1/cryptoKeys/key2/cryptoKeyVersions/1"
```

To create a subordinate CA named 'server-tls-1' whose issuer is located
elsewhere:

```
gcloud privateca subordinates create server-tls-1 --location=us-west1 --pool=my-pool --subject="CN=Example TLS CA, O=Google" --create-csr --csr-output-file=./csr.pem --kms-key-version="projects/my-project-pki/locations/us-west1/keyRings/kr1/cryptoKeys/key2/cryptoKeyVersions/1"
```

To create a subordinate CA named 'server-tls-1' chaining up to a root CA named
'prod-root' based on an existing CA:

```
gcloud privateca subordinates create server-tls-1 --location=us-west1 --pool=my-pool --issuer-pool=other-pool --issuer-location=us-west1 --from-ca=source-ca --kms-key-version="projects/my-project-pki/locations/us-west1/keyRings/kr1/cryptoKeys/key2/cryptoKeyVersions/1"
```

**POSITIONAL ARGUMENTS**

: **Certificate Authority resource - The name of the subordinate CA to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE_AUTHORITY`**:
ID of the Certificate Authority or fully qualified identifier for the
Certificate Authority.
To set the `certificate_authority` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Certificate Authority.
To set the `location` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.

**--pool**:
The parent CA Pool of the Certificate Authority.
To set the `pool` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--pool` on the command line.**

**REQUIRED FLAGS**

: **--create-csr**

**OPTIONAL FLAGS**

: **--auto-enable**:
If this flag is set, the Certificate Authority will be automatically enabled
upon creation.

**--bucket**:
The name of an existing storage bucket to use for storing the CA certificates
and CRLs for CAs in this pool. If omitted, a new bucket will be created and
managed by the service on your behalf.

**--custom-aia-urls**:
One or more comma-separated URLs that will be added to the Authority Information
Access extension in the issued certificate. These URLs are where the issuer CA
certificate is located.

**--custom-cdp-urls**:
One or more comma-separated URLs that will be added to the CRL Distribution
Points (CDP) extension in the issued certificate. These URLs are where CRL
information is located.

**--dns-san**:
One or more comma-separated DNS Subject Alternative Names.

**--email-san**:
One or more comma-separated email Subject Alternative Names.

**Source CA resource - An existing CA from which to copy configuration values for
the new CA. You can still override any of those values by explicitly providing
the appropriate flags. The specified existing CA must be part of the same pool
as the one being created. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--from-ca` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--from-ca` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.

To set the `pool` attribute:

- provide the argument `--from-ca` on the command line with a fully
specified name;
- provide the argument `--pool` on the command line.

**--from-ca**:
ID of the source CA or fully qualified identifier for the source CA.
To set the `certificate_authority` attribute:

- provide the argument `--from-ca` on the command line.**

**--ip-san**:
One or more comma-separated IP Subject Alternative Names.

**--issuer-ca**:
The Certificate Authority ID of the CA to issue the subordinate CA certificate
from. This ID is optional. If ommitted, any available ENABLED CA in the issuing
CA pool will be chosen.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--subject**:
X.501 name of the certificate subject. Example: --subject
"C=US,ST=California,L=Mountain View,O=Google LLC,CN=google.com"

**--subject-key-id**:
Optional field to specify subject key ID for certificate. DO NOT USE except to
maintain a previously established identifier for a public key, whose SKI was not
generated using method (1) described in RFC 5280 section 4.2.1.2.

**--uri-san**:
One or more comma-separated URI Subject Alternative Names.

**--validity**:
The validity of this CA, as an ISO8601 duration. Defaults to 3 years.

**--key-algorithm**

**--use-preset-profile**

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