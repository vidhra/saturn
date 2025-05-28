# gcloud container binauthz attestors public-keys add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add)*

**NAME**

: **gcloud container binauthz attestors public-keys add - add a public key to an Attestor**

**SYNOPSIS**

: **`gcloud container binauthz attestors public-keys add` `[--attestor](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--attestor)`=`ATTESTOR` (`[--pgp-public-key-file](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--pgp-public-key-file)`=`PATH_TO_FILE`     | (`[--keyversion](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--keyversion)`=`KEYVERSION` : `[--keyversion-key](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--keyversion-key)`=`KEYVERSION_KEY` `[--keyversion-keyring](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--keyversion-keyring)`=`KEYVERSION_KEYRING` `[--keyversion-location](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--keyversion-location)`=`KEYVERSION_LOCATION` `[--keyversion-project](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--keyversion-project)`=`KEYVERSION_PROJECT`)     | `[--pkix-public-key-algorithm](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--pkix-public-key-algorithm)`=`PKIX_PUBLIC_KEY_ALGORITHM` `[--pkix-public-key-file](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--pkix-public-key-file)`=`PATH_TO_FILE`) [`[--comment](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--comment)`=`COMMENT`] [`[--public-key-id-override](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#--public-key-id-override)`=`PUBLIC_KEY_ID_OVERRIDE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To add a new KMS public key to an existing Attestor `my_attestor`:

```
gcloud container binauthz attestors public-keys add --attestor=my_attestor --keyversion-project=foo --keyversion-location=us-west1 --keyversion-keyring=aring --keyversion-key=akey --keyversion=1
```

To add a new PGP public key to an existing Attestor `my_attestor`:

```
gcloud container binauthz attestors public-keys add --attestor=my_attestor --pgp-public-key-file=my_key.pub
```

**REQUIRED FLAGS**

: **Attestor resource - The attestor to which the public key should be added. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--attestor` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--attestor**:
ID of the attestor or fully qualified identifier for the attestor.
To set the `name` attribute:

- provide the argument `--attestor` on the command line.**

**--pgp-public-key-file**

**OPTIONAL FLAGS**

: **--comment**:
The comment describing the public key.

**--public-key-id-override**:
If provided, the ID to replace the default API-generated one. All IDs must be
valid URIs as defined by RFC 3986 (https://tools.ietf.org/html/rfc3986).
When creating Attestations to be verified by this key, one must always provide
this custom ID as the public key ID.

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
gcloud alpha container binauthz attestors public-keys add
```

```
gcloud beta container binauthz attestors public-keys add
```