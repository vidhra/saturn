# gcloud alpha cloud-shell  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell)*

**NAME**

: **gcloud alpha cloud-shell - manage Google Cloud Shell**

**SYNOPSIS**

: **`gcloud alpha cloud-shell` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Interact with and connect to your Cloud Shell environment.
More information on Cloud Shell can be found at [https://cloud.google.com/shell/docs/](https://cloud.google.com/shell/docs/).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[get-mount-command](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/get-mount-command)`**:
`(ALPHA)` Prints a command to mount the Cloud Shell home directory
via sshfs.

**`[scp](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp)`**:
`(ALPHA)` Copies files between Cloud Shell and the local machine.

**`[ssh](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh)`**:
`(ALPHA)` Allows you to establish an interactive SSH session with
Cloud Shell.

**NOTES**

: The previous `gcloud alpha shell` command to launch an interactive
shell was renamed to `[gcloud alpha
interactive](https://cloud.google.com/sdk/gcloud/reference/alpha/interactive)`.
This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud cloud-shell
```

```
gcloud beta cloud-shell
```