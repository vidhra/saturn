# gcloud kms keyrings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/describe](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/describe)*

**NAME**

: **gcloud kms keyrings describe - get metadata for a keyring**

**SYNOPSIS**

: **`gcloud kms keyrings describe` (`[KEYRING](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/describe#KEYRING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns metadata for the given keyring.

**EXAMPLES**

: The following command returns the metadata for the keyring `towers`
in the location `us-east1`:

```
gcloud kms keyrings describe towers --location=us-east1
```

**POSITIONAL ARGUMENTS**

: **Keyring resource - The KMS keyring resource. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `keyring` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**`KEYRING`**:
ID of the keyring or fully qualified identifier for the keyring.
To set the `keyring` attribute:

- provide the argument `keyring` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Google Cloud location for the keyring.
To set the `location` attribute:

- provide the argument `keyring` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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
gcloud alpha kms keyrings describe
```

```
gcloud beta kms keyrings describe
```