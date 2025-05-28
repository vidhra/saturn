# gcloud kms keys  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys](https://cloud.google.com/sdk/gcloud/reference/kms/keys)*

**NAME**

: **gcloud kms keys - create and manage keys**

**SYNOPSIS**

: **`gcloud kms keys` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/kms/keys#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/kms/keys#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A key represents a logical key that can be used for cryptographic operations.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[versions](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions)`**:
Create and manage versions.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding)`**:
Add IAM policy binding for a kms key.

**`[create](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create)`**:
Create a new key.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/kms/keys/describe)`**:
Get metadata for a given key.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy)`**:
Get the IAM policy for a key.

**`[list](https://cloud.google.com/sdk/gcloud/reference/kms/keys/list)`**:
List the keys within a keyring.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/kms/keys/remove-iam-policy-binding)`**:
Remove IAM policy binding for a kms key.

**`[remove-rotation-schedule](https://cloud.google.com/sdk/gcloud/reference/kms/keys/remove-rotation-schedule)`**:
Remove the rotation schedule for a key.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-iam-policy)`**:
Set the IAM policy for a key.

**`[set-primary-version](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-primary-version)`**:
Set the primary version of a key.

**`[set-rotation-schedule](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule)`**:
Update the rotation schedule for a key.

**`[update](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update)`**:
Update a key.

**NOTES**

: These variants are also available:

```
gcloud alpha kms keys
```

```
gcloud beta kms keys
```