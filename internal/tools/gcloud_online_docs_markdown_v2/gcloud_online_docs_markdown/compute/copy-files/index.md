# gcloud compute copy-files  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/copy-files](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files)*

**NAME**

: **gcloud compute copy-files - copy files to and from Google Compute Engine virtual machines via scp**

**SYNOPSIS**

: **`gcloud compute copy-files` [[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#INSTANCE)`:]`[SRC](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#SRC)` [[[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#INSTANCE)`:]`[SRC](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#SRC)` …] [[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#INSTANCE)`:]`[DEST](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#DEST)` [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#--dry-run)`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#--force-key-file-overwrite)`] [`[--plain](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#--plain)`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#--ssh-key-file)`=`SSH_KEY_FILE`] [`[--strict-host-key-checking](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#--strict-host-key-checking)`=`STRICT_HOST_KEY_CHECKING`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#--zone)`=`ZONE`] [`[--ssh-key-expiration](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#--ssh-key-expiration)`=`SSH_KEY_EXPIRATION`     | `[--ssh-key-expire-after](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#--ssh-key-expire-after)`=`SSH_KEY_EXPIRE_AFTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute copy-files` copies files between a virtual machine
instance and your local machine using the scp command. This command does not
work for Windows VMs.
To denote a remote file, prefix the file name with the virtual machine instance
name (e.g.,
`example-instance`:~/`FILE`). To
denote a local file, do not add a prefix to the file name (e.g.,
~/`FILE`).
If a file contains a colon (``:´´), you must specify it by either
using an absolute path or a path that begins with ``./´´.
Under the covers, `scp(1)` or pscp (on Windows) is used to facilitate
the transfer.
When the destination is local, all sources must be the same virtual machine
instance. When the destination is remote, all sources must be local.

**EXAMPLES**

: To copy a remote directory '~/REMOTE-DIR' on the instance of 'example-instance'
to '~/LOCAL-DIR' on the local host, run:

```
gcloud compute copy-files example-instance:~/REMOTE-DIR ~/LOCAL-DIR --zone=us-central1-a
```

To copy files from your local host to a virtual machine, run:

```
gcloud compute copy-files ~/LOCAL-FILE-1 ~/LOCAL-FILE-2 example-instance:~/REMOTE-DIR --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **[[`USER`@]`INSTANCE`:]`SRC` [[[`USER`@]`INSTANCE`:]`SRC` …]**:
Specifies the files to copy.

**[[`USER`@]`INSTANCE`:]`DEST`**:
Specifies a destination for the source files.

**FLAGS**

: **--dry-run**:
Print the equivalent scp/ssh command that would be run to stdout, instead of
executing it.

**--force-key-file-overwrite**:
If enabled, the gcloud command-line tool will regenerate and overwrite the files
associated with a broken SSH key without asking for confirmation in both
interactive and non-interactive environments.
If disabled, the files associated with a broken SSH key will not be regenerated
and will fail in both interactive and non-interactive environments.

**--plain**:
Suppress the automatic addition of `ssh(1)`/`scp(1)`
flags. This flag is useful if you want to take care of authentication yourself
or use specific ssh/scp features.

**--ssh-key-file**:
The path to the SSH key file. By default, this is
``~/.ssh/google_compute_engine``.

**--strict-host-key-checking**:
Override the default behavior of StrictHostKeyChecking for the connection. By
default, StrictHostKeyChecking is set to 'no' the first time you connect to an
instance, and will be set to 'yes' for all subsequent connections.
`STRICT_HOST_KEY_CHECKING` must be one of:
`yes`, `no`, `ask`.

**--zone**:
The zone of the instance to copy files to/from.
If not specified and the ``compute/zone``
property isn't set, you might be prompted to select a zone (interactive mode
only).
To avoid prompting when this flag is omitted, you can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

**--ssh-key-expiration**

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

: These variants are also available:

```
gcloud alpha compute copy-files
```

```
gcloud beta compute copy-files
```