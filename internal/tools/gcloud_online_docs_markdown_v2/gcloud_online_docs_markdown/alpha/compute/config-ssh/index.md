# gcloud alpha compute config-ssh  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh)*

**NAME**

: **gcloud alpha compute config-ssh - populate SSH config files with Host entries from each instance**

**SYNOPSIS**

: **`gcloud alpha compute config-ssh` [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh#--dry-run)`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh#--force-key-file-overwrite)`] [`[--remove](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh#--remove)`] [`[--ssh-config-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh#--ssh-config-file)`=`SSH_CONFIG_FILE`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh#--ssh-key-file)`=`SSH_KEY_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute config-ssh` makes SSHing
to virtual machine instances easier by adding an alias for each instance to the
user SSH configuration (`~/.ssh/config`) file.
In most cases, it is sufficient to run:

```
gcloud alpha compute config-ssh
```

Each instance will be given an alias of the form `NAME.ZONE.PROJECT`.
For example, if `example-instance` resides in
`us-central1-a`, you can SSH to it by running:

```
ssh example-instance.us-central1-a.MY-PROJECT
```

On some platforms, the host alias can be tab-completed, making the long alias
less daunting to type.
The aliases created interface with SSH-based programs like `scp(1)`,
so it is possible to use the aliases elsewhere:

```
scp ~/MY-FILE example-instance.us-central1-a.MY-PROJECT:~
```

Whenever instances are added, removed, or their external IP addresses are
changed, the remove command must be run to clear the existing configuration and
then the command can set executed to set the configuration to the current state.
This command ensures that the user's public SSH key is present in the project's
metadata. If the user does not have a public SSH key, one is generated using
`ssh-keygen(1)` (if the `--quiet` flag is given, the
generated key will have an empty passphrase).

**EXAMPLES**

: To populate SSH config file with Host entries from each running instance, run:

```
gcloud alpha compute config-ssh
```

To remove the change to the SSH config file by this command, run:

```
gcloud alpha compute config-ssh --remove
```

**FLAGS**

: **--dry-run**:
If provided, the proposed changes to the SSH config file are printed to standard
output and no actual changes are made.

**--force-key-file-overwrite**:
If enabled, the gcloud command-line tool will regenerate and overwrite the files
associated with a broken SSH key without asking for confirmation in both
interactive and non-interactive environments.
If disabled, the files associated with a broken SSH key will not be regenerated
and will fail in both interactive and non-interactive environments.

**--remove**:
If provided, any changes made to the SSH config file by this tool are reverted.

**--ssh-config-file**:
Specifies an alternative per-user SSH configuration file. By default, this is
``~/.ssh/config``.

**--ssh-key-file**:
The path to the SSH key file. By default, this is
``~/.ssh/google_compute_engine``.

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
allowlist. These variants are also available:

```
gcloud compute config-ssh
```

```
gcloud beta compute config-ssh
```