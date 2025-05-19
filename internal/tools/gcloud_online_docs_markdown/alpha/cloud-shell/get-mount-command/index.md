# gcloud alpha cloud-shell get-mount-command  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/get-mount-command](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/get-mount-command)*

**NAME**

: **gcloud alpha cloud-shell get-mount-command - prints a command to mount the Cloud Shell home directory via sshfs**

**SYNOPSIS**

: **`gcloud alpha cloud-shell get-mount-command` `[MOUNT_DIR](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/get-mount-command#MOUNT_DIR)` [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/get-mount-command#--force-key-file-overwrite)`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/get-mount-command#--ssh-key-file)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/get-mount-command#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha cloud-shell get-mount-command`
starts your Cloud Shell if it is not already running, then prints out a command
that allows you to mount the Cloud Shell home directory onto your local file
system using `sshfs`. You must install and run sshfs yourself.
After mounting the Cloud Shell home directory, any changes you make under the
mount point on your local file system will be reflected in Cloud Shell and
vice-versa.

**EXAMPLES**

: To print a command that mounts a remote directory onto your local file system,
run:

```
gcloud alpha cloud-shell get-mount-command REMOTE-DIR
```

**POSITIONAL ARGUMENTS**

: **`MOUNT_DIR`**:
Local directory onto which the Cloud Shell home directory should be mounted.

**FLAGS**

: **--force-key-file-overwrite**:
If enabled gcloud will regenerate and overwrite the files associated with a
broken SSH key without asking for confirmation in both interactive and
non-interactive environment.
If disabled gcloud will not attempt to regenerate the files associated with a
broken SSH key and fail in both interactive and non-interactive environment.

**--ssh-key-file**:
The path to the SSH key file. By default, this is
`~/.ssh/google_compute_engine`.

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
gcloud cloud-shell get-mount-command
```

```
gcloud beta cloud-shell get-mount-command
```