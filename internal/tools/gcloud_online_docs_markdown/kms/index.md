# gcloud kms  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms](https://cloud.google.com/sdk/gcloud/reference/kms)*

**NAME**

: **gcloud kms - manage cryptographic keys in the cloud**

**SYNOPSIS**

: **`gcloud kms` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/kms#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/kms#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud kms command group lets you generate, use, rotate and destroy Google
Cloud KMS keys.
Cloud KMS is a cloud-hosted key management service that lets you manage
encryption for your cloud services the same way you do on-premises. You can
generate, use, rotate and destroy AES256 encryption keys. Cloud KMS is
integrated with IAM and Cloud Audit Logging so that you can manage permissions
on individual keys, and monitor how these are used. Use Cloud KMS to protect
secrets and other sensitive data which you need to store in Google Cloud
Platform.
More information on Cloud KMS can be found here: [https://cloud.google.com/kms/](https://cloud.google.com/kms/) and
detailed documentation can be found here: [https://cloud.google.com/kms/docs/](https://cloud.google.com/kms/docs/)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[autokey-config](https://cloud.google.com/sdk/gcloud/reference/kms/autokey-config)`**:
Update and retrieve the AutokeyConfig.

**`[ekm-config](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config)`**:
Update and retrieve the EkmConfig.

**`[ekm-connections](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections)`**:
Create and manage ekm connections.

**`[import-jobs](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs)`**:
Create and manage import jobs.

**`[inventory](https://cloud.google.com/sdk/gcloud/reference/kms/inventory)`**:
Manages the KMS Inventory and Key Tracking commands.

**`[key-handles](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles)`**:
Create and manage KeyHandle resources.

**`[keyrings](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings)`**:
Create and manage keyrings.

**`[keys](https://cloud.google.com/sdk/gcloud/reference/kms/keys)`**:
Create and manage keys.

**`[locations](https://cloud.google.com/sdk/gcloud/reference/kms/locations)`**:
View locations available for a project.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[asymmetric-decrypt](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt)`**:
Decrypt an input file using an asymmetric-encryption key version.

**`[asymmetric-sign](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign)`**:
Sign a user input file using an asymmetric-signing key version.

**`[decrypt](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt)`**:
Decrypt a ciphertext file using a Cloud KMS key.

**`[encrypt](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt)`**:
Encrypt a plaintext file using a key.

**`[mac-sign](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign)`**:
Sign a user input file using a MAC key version.

**`[mac-verify](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify)`**:
Verify a user signature file using a MAC key version.

**`[raw-decrypt](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt)`**:
Decrypt a ciphertext file using a raw key.

**`[raw-encrypt](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt)`**:
Encrypt a plaintext file using a raw key.

**NOTES**

: These variants are also available:

```
gcloud alpha kms
```

```
gcloud beta kms
```