# gcloud alpha cloud-shell scp  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp)*

**NAME**

: **gcloud alpha cloud-shell scp - copies files between Cloud Shell and the local machine**

**SYNOPSIS**

: **`gcloud alpha cloud-shell scp` (`cloudshell`|`localhost`):`[SRC](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#SRC)` [(`cloudshell`|`localhost`):`[SRC](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#SRC)` …] (`cloudshell`|`localhost`):`[DEST](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#DEST)` [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#--dry-run)`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#--force-key-file-overwrite)`] [`[--recurse](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#--recurse)`] [`[--scp-flag](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#--scp-flag)`=`SCP_FLAG`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#--ssh-key-file)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha cloud-shell scp` copies files
between your Cloud Shell instance and your local machine using the scp command.

**EXAMPLES**

: To denote a file in Cloud Shell, prefix the file name with the string
"cloudshell:" (e.g.
`cloudshell:`~/`FILE`). To denote a
local file, prefix the file name with the string "localhost:" (e.g.
`localhost:`~/`FILE`). For example,
to copy a remote directory to your local machine, run:

```
gcloud alpha cloud-shell scp cloudshell:~/REMOTE-DIR localhost:~/LOCAL-DIR
```

In the above example, ``~/REMOTE-DIR`` from
your Cloud Shell instance is copied into the ~/`LOCAL-DIR`
directory.
Conversely, files from your local computer can be copied into Cloud Shell:

```
gcloud alpha cloud-shell scp localhost:~/LOCAL-FILE-1 localhost:~/LOCAL-FILE-2 cloudshell:~/REMOTE-DIR
```

Under the covers, `scp(1)` or pscp (on Windows) is used to facilitate
the transfer.

**POSITIONAL ARGUMENTS**

: **cloudshell|`localhost`):`SRC`-[(`cloudshell`|`localhost`):`SRC`-…]">(`cloudshell`|`localhost`):`SRC` [(`cloudshell`|`localhost`):`SRC` …]**:
Specifies the files to copy.

**cloudshell|`localhost`):`DEST`">(`cloudshell`|`localhost`):`DEST`**:
Specifies a destination for the source files.

**FLAGS**

: **--dry-run**:
If provided, prints the command that would be run to standard out instead of
executing it.

**--force-key-file-overwrite**:
If enabled gcloud will regenerate and overwrite the files associated with a
broken SSH key without asking for confirmation in both interactive and
non-interactive environment.
If disabled gcloud will not attempt to regenerate the files associated with a
broken SSH key and fail in both interactive and non-interactive environment.

**--recurse**:
Upload directories recursively.

**--scp-flag**:
Extra flag to be sent to scp. This flag may be repeated.

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
gcloud cloud-shell scp
```

```
gcloud beta cloud-shell scp
```