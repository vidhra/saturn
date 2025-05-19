# gcloud alpha bms instances reimage  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage)*

**NAME**

: **gcloud alpha bms instances reimage - reimage a Bare Metal Solution instance**

**SYNOPSIS**

: **`gcloud alpha bms instances reimage` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage#--region)`=`REGION`) `[--os-image](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage#--os-image)`=`OS_IMAGE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage#--async)`] [`[--kms-crypto-key-version](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage#--kms-crypto-key-version)`=`KMS_CRYPTO_KEY_VERSION`] [`[--ssh-keys](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage#--ssh-keys)`=[`SSH_KEYS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Reimage a Bare Metal Solution instance.
This call returns immediately, but the reimage operation may take several
minutes to complete. To check if the operation is complete, use the
`describe` command for the instance.

**EXAMPLES**

: To reimage an instance called ``my-instance``
in region ``us-central1`` with the OS image
code ``RHEL9x``, run:

```
gcloud alpha bms instances reimage my-instance --region=us-central1 --os-image=RHEL9x
```

To set KMS key and ssh keys in order to connect the instance. Please use
corresponding flags:

```
gcloud alpha bms instances reimage my-instance --region=us-central1 --os-image=RHEL9x --ssh-keys=ssh-key-1,ssh-key-2 --kms-key-version=sample-kms-key-version
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

**REQUIRED FLAGS**

: **--os-image**:
OS image to install on the server.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--kms-crypto-key-version**:
Resource ID of a KMS CryptoKeyVersion used to encrypt the initial password.
[https://cloud.google.com/kms/docs/resource-hierarchy#key_versions](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions)

**SSH key resource - ssh_key. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--ssh-keys` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--ssh-keys` on the command line with a fully
specified name;
- global is the only supported location.

**--ssh-keys**:
IDs of the SSH keys or fully qualified identifiers for the SSH keys.
To set the `ssh_key` attribute:

- provide the argument `--ssh-keys` on the command line.**

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
allowlist.