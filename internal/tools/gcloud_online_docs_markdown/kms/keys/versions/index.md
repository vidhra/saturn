# gcloud kms keys versions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions)*

**NAME**

: **gcloud kms keys versions - create and manage versions**

**SYNOPSIS**

: **`gcloud kms keys versions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A version represents an individual cryptographic key and the associated key
material.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create)`**:
Create a new version.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe)`**:
Get metadata for a given version.

**`[destroy](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/destroy)`**:
Schedule a version to be destroyed.

**`[disable](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/disable)`**:
Disable a given version.

**`[enable](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/enable)`**:
Enable a given version.

**`[get-certificate-chain](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain)`**:
Get a certificate chain for a given version.

**`[get-public-key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key)`**:
Get the public key for a given version.

**`[import](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import)`**:
Import a version into an existing crypto key.

**`[list](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/list)`**:
List the versions within a key.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/restore)`**:
Restore a version scheduled for destruction.

**`[update](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update)`**:
Update a key version.

**NOTES**

: These variants are also available:

```
gcloud alpha kms keys versions
```

```
gcloud beta kms keys versions
```