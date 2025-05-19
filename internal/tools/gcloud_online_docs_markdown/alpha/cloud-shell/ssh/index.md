# gcloud alpha cloud-shell ssh  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh)*

**NAME**

: **gcloud alpha cloud-shell ssh - allows you to establish an interactive SSH session with Cloud Shell**

**SYNOPSIS**

: **`gcloud alpha cloud-shell ssh` [`[--authorize-session](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh#--authorize-session)`] [`[--command](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh#--command)`=`COMMAND`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh#--dry-run)`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh#--force-key-file-overwrite)`] [`[--ssh-flag](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh#--ssh-flag)`=`SSH_FLAG`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh#--ssh-key-file)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh#GCLOUD-WIDE-FLAGS) …`] [-- `[SSH_ARGS](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh#SSH_ARGS)` …]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha cloud-shell ssh` lets you remotely
log in to Cloud Shell. If your Cloud Shell is not currently running, this will
cause it to be started before establishing the SSH session.

**EXAMPLES**

: To SSH into your Cloud Shell, run:

```
gcloud alpha cloud-shell ssh
```

To run a remote command in your Cloud Shell, run:

```
gcloud alpha cloud-shell ssh --command=ls
```

**POSITIONAL ARGUMENTS**

: **[-- `SSH_ARGS` …]**:
Flags and positionals passed to the underlying ssh implementation.
The '--' argument must be specified between gcloud specific args on the left and
SSH_ARGS on the right. Example:

```
gcloud alpha cloud-shell ssh -- -vvv
```

**FLAGS**

: **--authorize-session**:
If provided, sends OAuth credentials to the current Cloud Shell session on
behalf of the user. When this completes, the session will be authorized to run
various Google Cloud command-line tools without requiring the user to manually
authenticate.

**--command**:
A command to run in Cloud Shell.
Runs the command in Cloud Shell and then exits.

**--dry-run**:
If provided, prints the command that would be run to standard out instead of
executing it.

**--force-key-file-overwrite**:
If enabled gcloud will regenerate and overwrite the files associated with a
broken SSH key without asking for confirmation in both interactive and
non-interactive environment.
If disabled gcloud will not attempt to regenerate the files associated with a
broken SSH key and fail in both interactive and non-interactive environment.

**--ssh-flag**:
Additional flags to be passed to `ssh(1)`.

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
gcloud cloud-shell ssh
```

```
gcloud beta cloud-shell ssh
```