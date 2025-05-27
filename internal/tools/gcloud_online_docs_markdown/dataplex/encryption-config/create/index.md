# gcloud dataplex encryption-config create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/create)*

**NAME**

: **gcloud dataplex encryption-config create - create a Dataplex encryption config resource**

**SYNOPSIS**

: **`gcloud dataplex encryption-config create` (`[ENCRYPTION_CONFIG](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/create#ENCRYPTION_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/create#--organization)`=`ORGANIZATION`) [`[--key](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/create#--key)`=`KEY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: An EncryptionConfig is created only for CMEK opted in organizations.

**EXAMPLES**

: To create an EncryptionConfig `default` in organization
`test-org-id` at location `us-central1` with key
`test-key`, run:
```
gcloud dataplex encryption-config create default --location=us-central1 --organization=test-org-id --key='test-key'
```

**POSITIONAL ARGUMENTS**

: **Encryption config resource - Arguments and flags that define the Dataplex
EncryptionConfig you want to create. The arguments in this group can be used to
specify the attributes of this resource.
This must be specified.

**`ENCRYPTION_CONFIG`**:
ID of the encryption config or fully qualified identifier for the encryption
config.
To set the `encryption_config` attribute:

- provide the argument `encryption_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `encryption_config` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.

**--organization**:
The name of encryption config to use.
To set the `organization` attribute:

- provide the argument `encryption_config` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line.**

**FLAGS**

: **--key**:
The KMS key to use for encryption.

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

: This variant is also available:

```
gcloud alpha dataplex encryption-config create
```