# gcloud compute tpus tpu-vm scp  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp)*

**NAME**

: **gcloud compute tpus tpu-vm scp - copy files to and from a Cloud TPU VM via SCP**

**SYNOPSIS**

: **`gcloud compute tpus tpu-vm scp` [[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#INSTANCE)`:]`[SRC](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#SRC)` [[[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#INSTANCE)`:]`[SRC](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#SRC)` …] [[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#INSTANCE)`:]`[DEST](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#DEST)` [`[--compress](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--compress)`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--dry-run)`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--force-key-file-overwrite)`] [`[--internal-ip](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--internal-ip)`] [`[--plain](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--plain)`] [`[--recurse](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--recurse)`] [`[--scp-flag](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--scp-flag)`=`SCP_FLAG`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--ssh-key-file)`=`SSH_KEY_FILE`] [`[--strict-host-key-checking](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--strict-host-key-checking)`=`STRICT_HOST_KEY_CHECKING`] [`[--worker](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--worker)`=`WORKER`; default="0"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--zone)`=`ZONE`] [`[--ssh-key-expiration](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--ssh-key-expiration)`=`SSH_KEY_EXPIRATION`     | `[--ssh-key-expire-after](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#--ssh-key-expire-after)`=`SSH_KEY_EXPIRE_AFTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Copy files to and from a Cloud TPU VM via SCP.

**EXAMPLES**

: To copy a file (for example, a text file in the local home directory) to a Cloud
TPU VM, run:

```
gcloud compute tpus tpu-vm scp ~/my-file my-tpu:
```

To copy a file into all workers in a Cloud TPU VM, run:

```
gcloud compute tpus tpu-vm scp ~/my-file my-tpu: --worker=all
```

To copy a file from a Cloud TPU VM to the home directory of the local computer,
run:

```
gcloud compute tpus tpu-vm scp my-tpu:~/my-file ~/
```

To copy all files in a folder to a Cloud TPU VM, run:

```
gcloud compute tpus tpu-vm scp ~/my-folder/ my-tpu: --recurse
```

**POSITIONAL ARGUMENTS**

: **[[`USER`@]`INSTANCE`:]`SRC` [[[`USER`@]`INSTANCE`:]`SRC` …]**:
Specifies the files to copy.

**[[`USER`@]`INSTANCE`:]`DEST`**:
Specifies a destination for the source files.

**FLAGS**

: **--compress**:
Enable compression.

**--dry-run**:
Print the equivalent scp/ssh command that would be run to stdout, instead of
executing it.

**--force-key-file-overwrite**:
If enabled, the gcloud command-line tool will regenerate and overwrite the files
associated with a broken SSH key without asking for confirmation in both
interactive and non-interactive environments.
If disabled, the files associated with a broken SSH key will not be regenerated
and will fail in both interactive and non-interactive environments.

**--internal-ip**:
Connect to TPU VMs using their internal IP addresses rather than their external
IP addresses. Use this to connect from a Google Compute Engine VM to a TPU VM on
the same VPC network, or between two peered VPC networks.

**--plain**:
Suppress the automatic addition of `ssh(1)`/`scp(1)`
flags. This flag is useful if you want to take care of authentication yourself
or use specific ssh/scp features.

**--recurse**:
Upload directories recursively.

**--scp-flag**:
Additional flags to be passed to `scp(1)`. This flag may be repeated.

**--ssh-key-file**:
The path to the SSH key file. By default, this is
``~/.ssh/google_compute_engine``.

**--strict-host-key-checking**:
Override the default behavior of StrictHostKeyChecking for the connection. By
default, StrictHostKeyChecking is set to 'no' the first time you connect to an
instance, and will be set to 'yes' for all subsequent connections.
`STRICT_HOST_KEY_CHECKING` must be one of:
`yes`, `no`, `ask`.

**--worker**:
TPU worker to connect to. The supported value is a single 0-based index of the
worker in the case of a TPU Pod. When also using the `--command`
flag, it additionally supports a comma-separated list (e.g. '1,4,6'), range
(e.g. '1-3'), or special keyword ``all" to run the command concurrently on each
of the specified workers.
Note that when targeting multiple workers, you should run 'ssh-add' with your
private key prior to executing the gcloud command. Default: 'ssh-add
~/.ssh/google_compute_engine'.

**--zone**:
Zone of the tpu to scp. If not specified and the
``compute/zone`` property isn't set, you might
be prompted to select a zone (interactive mode only).
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

: This variant is also available:

```
gcloud alpha compute tpus tpu-vm scp
```