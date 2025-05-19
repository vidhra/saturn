# gcloud alpha bms instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update)*

**NAME**

: **gcloud alpha bms instances update - update a Bare Metal Solution instance**

**SYNOPSIS**

: **`gcloud alpha bms instances update` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--async)`] [`[--[no-]enable-hyperthreading](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--[no-]enable-hyperthreading)`] [`[--kms-crypto-key-version](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--kms-crypto-key-version)`=`KMS_CRYPTO_KEY_VERSION`] [`[--os-image](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--os-image)`=`OS_IMAGE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--remove-labels)`=[`KEY`,…]] [`[--clear-ssh-keys](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--clear-ssh-keys)`     | `[--ssh-keys](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#--ssh-keys)`=[`SSH_KEYS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Bare Metal Solution instance.
This call returns immediately, but the update operation may take several minutes
to complete. To check if the operation is complete, use the
`describe` command for the instance.

**EXAMPLES**

: To update an instance called ``my-instance`` in
region ``us-central1`` with a new label
``key1=value1``, run:

```
gcloud alpha bms instances update my-instance --region=us-central1 --update-labels=key1=value1
```

To clear all labels, run:

```
gcloud alpha bms instances update my-instance --region=us-central1 --clear-labels
```

**POSITIONAL ARGUMENTS**

: **Instance resource - instance. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Region of the resource.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--[no-]enable-hyperthreading**:
Enable hyperthreading for the server. Use `--enable-hyperthreading`
to enable and `--no-enable-hyperthreading` to disable.

**--kms-crypto-key-version**:
Resource ID of a KMS CryptoKeyVersion used to encrypt the initial password.
[https://cloud.google.com/kms/docs/resource-hierarchy#key_versions](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions)

**--os-image**:
OS image to install on the server.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--clear-ssh-keys**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud bms instances update
```