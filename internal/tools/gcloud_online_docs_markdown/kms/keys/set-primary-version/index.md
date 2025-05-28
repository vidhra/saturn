# gcloud kms keys set-primary-version  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-primary-version](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-primary-version)*

**NAME**

: **gcloud kms keys set-primary-version - set the primary version of a key**

**SYNOPSIS**

: **`gcloud kms keys set-primary-version` (`[KEY](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-primary-version#KEY)` : `[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-primary-version#--keyring)`=`KEYRING` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-primary-version#--location)`=`LOCATION`) `[--version](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-primary-version#--version)`=`VERSION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-primary-version#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the specified version as the primary version of the given key. The version
is specified by its version number assigned on creation.

**EXAMPLES**

: The following command sets version 9 as the primary version of the key
`samwise` within keyring `fellowship` and location
`global`:

```
gcloud kms keys set-primary-version samwise --version=9 --keyring=fellowship --location=global
```

**POSITIONAL ARGUMENTS**

: **Key resource - The KMS key resource. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- set the property `core/project`.

This must be specified.

**`KEY`**:
ID of the key or fully qualified identifier for the key.
To set the `key` attribute:

- provide the argument `key` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--keyring**:
The KMS keyring of the key.
To set the `keyring` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--keyring` on the command line.

**--location**:
The Google Cloud location for the key.
To set the `location` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--version**:
Version to make primary.

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
gcloud alpha kms keys set-primary-version
```

```
gcloud beta kms keys set-primary-version
```