# gcloud compute tpus tpu-vm ssh  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh)*

**NAME**

: **gcloud compute tpus tpu-vm ssh - SSH into a Cloud TPU VM**

**SYNOPSIS**

: **`gcloud compute tpus tpu-vm ssh` [`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#USER)`@]`[TPU](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#TPU)` [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--dry-run)`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--force-key-file-overwrite)`] [`[--internal-ip](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--internal-ip)`] [`[--plain](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--plain)`] [`[--ssh-flag](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--ssh-flag)`=`SSH_FLAG`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--ssh-key-file)`=`SSH_KEY_FILE`] [`[--strict-host-key-checking](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--strict-host-key-checking)`=`STRICT_HOST_KEY_CHECKING`] [`[--worker](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--worker)`=`WORKER`; default="0"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--zone)`=`ZONE`] [`[--command](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--command)`=`COMMAND` `[--output-directory](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--output-directory)`=`OUTPUT_DIRECTORY`] [`[--ssh-key-expiration](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--ssh-key-expiration)`=`SSH_KEY_EXPIRATION`     | `[--ssh-key-expire-after](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#--ssh-key-expire-after)`=`SSH_KEY_EXPIRE_AFTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#GCLOUD-WIDE-FLAGS) …`] [-- `[SSH_ARGS](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh#SSH_ARGS)` …]**

**DESCRIPTION**

: SSH into a Cloud TPU VM.

**EXAMPLES**

: To SSH into a Cloud TPU VM, run:

```
gcloud compute tpus tpu-vm ssh my-tpu
```

To SSH into worker 1 on a Cloud TPU VM Pod, run:

```
gcloud compute tpus tpu-vm ssh my-tpu --worker=1
```

To run an SSH command in a Cloud TPU VM (for example, to print the time since
last boot), run:

```
gcloud compute tpus tpu-vm ssh my-tpu --command="last boot"
```

To run the same command in all workers in a Cloud TPU VM simultaneously, run:

```
gcloud compute tpus tpu-vm ssh my-tpu --command="last boot" --worker=all
```

**POSITIONAL ARGUMENTS**

: **[`USER`@]`TPU`**:
Specifies the Cloud TPU VM to SSH into.
``USER`` specifies the username with which to
SSH. If omitted, the user login name is used.
``TPU`` specifies the name of the Cloud TPU VM
to SSH into.

**[-- `SSH_ARGS` …]**:
Flags and positionals passed to the underlying ssh implementation.
The '--' argument must be specified between gcloud specific args on the left and
SSH_ARGS on the right. Example:

```
gcloud compute tpus tpu-vm ssh example-instance --zone=us-central1-a -- -vvv -L 80:%TPU%:80
```

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

**--internal-ip**:
Connect to TPU VMs using their internal IP addresses rather than their external
IP addresses. Use this to connect from a Google Compute Engine VM to a TPU VM on
the same VPC network, or between two peered VPC networks.

**--plain**:
Suppress the automatic addition of `ssh(1)`/`scp(1)`
flags. This flag is useful if you want to take care of authentication yourself
or use specific ssh/scp features.

**--ssh-flag**:
Additional flags to be passed to `ssh(1)`. It is recommended that
flags be passed using an assignment operator and quotes. Example:

```
gcloud compute tpus tpu-vm ssh example-instance --zone=us-central1-a --ssh-flag="-vvv" --ssh-flag="-L 80:localhost:80"
```

This flag will replace occurences of ``%USER%``
and ``%TPU%`` with their dereferenced values.
For example, passing ``80:%TPU%:80`` into the flag is equivalent to passing
``80:162.222.181.197:80`` to
`ssh(1)` if the external IP address of 'example-instance' is
162.222.181.197.
If connecting to the instance's external IP, then %TPU% is replaced with that,
otherwise it is replaced with the internal IP.

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
Zone of the tpu to ssh. If not specified and the
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

**--command**

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
gcloud alpha compute tpus tpu-vm ssh
```