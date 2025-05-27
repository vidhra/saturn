# gcloud dataplex encryption-config describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/describe](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/describe)*

**NAME**

: **gcloud dataplex encryption-config describe - describe an EncryptionConfig**

**SYNOPSIS**

: **`gcloud dataplex encryption-config describe` (`[ENCRYPTION_CONFIG](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/describe#ENCRYPTION_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/describe#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an EncryptionConfig. Displays all the details of an EncryptionConfig
used for CMEK with valid organization and location.

**EXAMPLES**

: To describe an EncryptionConfig:
```
gcloud dataplex encryption-config describe default --location=us-central1 --organization=test-org
```

**POSITIONAL ARGUMENTS**

: **Encryption config resource - encryption_config you want to Describe The
arguments in this group can be used to specify the attributes of this resource.
This must be specified.

**`ENCRYPTION_CONFIG`**:
ID of the encryption config or fully qualified identifier for the encryption
config.
To set the `encryption_config` attribute:

- provide the argument `encryption_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `encryption_config` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.

**--organization**:
Name of the Cloud organization to use.
To set the `organization` attribute:

- provide the argument `encryption_config` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line.**

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

: This command uses the `dataplex/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataplex/docs](https://cloud.google.com/dataplex/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex encryption-config describe
```