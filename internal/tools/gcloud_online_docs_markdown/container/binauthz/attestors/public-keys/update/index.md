# gcloud container binauthz attestors public-keys update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/update](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/update)*

**NAME**

: **gcloud container binauthz attestors public-keys update - update a public key on an Attestor**

**SYNOPSIS**

: **`gcloud container binauthz attestors public-keys update` `[PUBLIC_KEY_ID](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/update#PUBLIC_KEY_ID)` `[--attestor](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/update#--attestor)`=`ATTESTOR` [`[--comment](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/update#--comment)`=`COMMENT`] [`[--pgp-public-key-file](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/update#--pgp-public-key-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update a PGP public key on an existing Attestor `my_attestor`:

```
gcloud container binauthz attestors public-keys update 0638AADD940361EA2D7F14C58C124F0E663DA097 --attestor=my_attestor --pgp-public-key-file=my_key.pub
```

**POSITIONAL ARGUMENTS**

: **`PUBLIC_KEY_ID`**:
The ID of the public key to update.

**REQUIRED FLAGS**

: **Attestor resource - The attestor on which the public key should be updated. This
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

**OPTIONAL FLAGS**

: **--comment**:
The comment describing the public key.

**--pgp-public-key-file**:
The path to a file containing the updated ASCII-armored PGP public key. Use a
full or relative path to a local file containing the value of
pgp_public_key_file.

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
gcloud alpha container binauthz attestors public-keys update
```

```
gcloud beta container binauthz attestors public-keys update
```