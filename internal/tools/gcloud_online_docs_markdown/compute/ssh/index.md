# gcloud compute ssh  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/ssh](https://cloud.google.com/sdk/gcloud/reference/compute/ssh)*

**NAME**

: **gcloud compute ssh - SSH into a virtual machine instance**

**SYNOPSIS**

: **`gcloud compute ssh` [`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#INSTANCE)` [`[--command](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--command)`=`COMMAND`] [`[--container](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--container)`=`CONTAINER`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--dry-run)`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--force-key-file-overwrite)`] [`[--plain](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--plain)`] [`[--ssh-flag](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--ssh-flag)`=`SSH_FLAG`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--ssh-key-file)`=`SSH_KEY_FILE`] [`[--strict-host-key-checking](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--strict-host-key-checking)`=`STRICT_HOST_KEY_CHECKING`] [`[--troubleshoot](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--troubleshoot)`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--zone)`=`ZONE`] [`[--internal-ip](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--internal-ip)`     | `[--tunnel-through-iap](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--tunnel-through-iap)`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--network)`=`NETWORK` `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--region)`=`REGION` : `[--dest-group](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--dest-group)`=`DEST_GROUP`] [`[--ssh-key-expiration](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--ssh-key-expiration)`=`SSH_KEY_EXPIRATION`     | `[--ssh-key-expire-after](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--ssh-key-expire-after)`=`SSH_KEY_EXPIRE_AFTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#GCLOUD-WIDE-FLAGS) …`] [-- `[SSH_ARGS](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#SSH_ARGS)` …]**

**DESCRIPTION**

: `gcloud compute ssh` is a thin wrapper around the `ssh(1)`
command that takes care of authentication and the translation of the instance
name into an IP address.
To use SSH to connect to a Windows VM, refer to this guide: [https://cloud.google.com/compute/docs/connect/windows-ssh](https://cloud.google.com/compute/docs/connect/windows-ssh)
The default network comes preconfigured to allow ssh access to all VMs. If the
default network was edited, or if not using the default network, you may need to
explicitly enable ssh access by adding a firewall-rule:

```
gcloud compute firewall-rules create --network=NETWORK default-allow-ssh --allow=tcp:22
```

`gcloud compute ssh` ensures that the user's public SSH key is
present in the project's metadata. If the user does not have a public SSH key,
one is generated using `ssh-keygen(1)` (if the `--quiet`
flag is given, the generated key will have an empty passphrase).
If the `--region` and `--network` flags are provided, then
`--plain` and `--tunnel-through-iap` are implied and an IP
address must be supplied instead of an instance name. This is most useful for
connecting to on-prem resources.

**EXAMPLES**

: To SSH into 'example-instance' in zone
``us-central1-a``, run:

```
gcloud compute ssh example-instance --zone=us-central1-a
```

You can also run a command on the virtual machine. For example, to get a
snapshot of the guest's process tree, run:

```
gcloud compute ssh example-instance --zone=us-central1-a --command="ps -ejH"
```

When running a command on a virtual machine, a non-interactive shell will
typically be used. (See the INVOCATION section of [https://linux.die.net/man/1/bash](https://linux.die.net/man/1/bash) for
an overview.) That behavior can be overridden by specifying a shell to run the
command, and passing the `-t` flag to SSH to allocate a pseudo-TTY.
For example, to see the environment variables set during an interactive session,
run:

```
gcloud compute ssh example-instance --zone=us-central1-a --command="bash -i -c env" -- -t
```

If you are using the Google Container-Optimized virtual machine image, you can
SSH into one of your containers with:

```
gcloud compute ssh example-instance --zone=us-central1-a --container=CONTAINER
```

You can limit the allowed time to ssh. For example, to allow a key to be used
through 2019:

```
gcloud compute ssh example-instance --zone=us-central1-a --ssh-key-expiration="2020-01-01T00:00:00:00Z"
```

Or alternatively, allow access for the next two minutes:

```
gcloud compute ssh example-instance --zone=us-central1-a --ssh-key-expire-after=2m
```

To use the IP address of your remote VM (eg, for on-prem), you must also specify
the `--region` and `--network` flags:

```
gcloud compute ssh 10.1.2.3 --region=us-central1 --network=default
```

**POSITIONAL ARGUMENTS**

: **[`USER`@]`INSTANCE`**:
Specifies the instance to SSH into.
``USER`` specifies the username with which to
SSH. If omitted, the user login name is used. If using OS Login, USER will be
replaced by the OS Login user.
``INSTANCE`` specifies the name of the virtual
machine instance to SSH into.

**[-- `SSH_ARGS` …]**:
Flags and positionals passed to the underlying ssh implementation.
The '--' argument must be specified between gcloud specific args on the left and
SSH_ARGS on the right. Example:

```
gcloud compute ssh example-instance --zone=us-central1-a -- -vvv -L 80:%INSTANCE%:80
```

**FLAGS**

: **--command**:
A command to run on the virtual machine.
Runs the command on the target instance and then exits.

**--container**:
The name or ID of a container inside of the virtual machine instance to connect
to. This only applies to virtual machines that are using a Google
Container-Optimized virtual machine image. For more information, see [https://cloud.google.com/compute/docs/containers](https://cloud.google.com/compute/docs/containers).

**--dry-run**:
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

**--ssh-flag**:
Additional flags to be passed to `ssh(1)`. It is recommended that
flags be passed using an assignment operator and quotes. Example:

```
gcloud compute ssh example-instance --zone=us-central1-a --ssh-flag="-vvv" --ssh-flag="-L 80:localhost:80"
```

This flag will replace occurences of
``%USER%``,
``%INSTANCE%``, and
``%INTERNAL%`` with their dereferenced values.
For example, passing ``80:%INSTANCE%:80`` into
the flag is equivalent to passing
``80:162.222.181.197:80`` to
`ssh(1)` if the external IP address of 'example-instance' is
162.222.181.197.
If connecting to the instance's external IP, then
``%INSTANCE%`` is replaced with that, otherwise
it is replaced with the internal IP.
``%INTERNAL%`` is always replaced with the
internal interface of the instance.

**--ssh-key-file**:
The path to the SSH key file. By default, this is
``~/.ssh/google_compute_engine``.

**--strict-host-key-checking**:
Override the default behavior of StrictHostKeyChecking for the connection. By
default, StrictHostKeyChecking is set to 'no' the first time you connect to an
instance, and will be set to 'yes' for all subsequent connections.
`STRICT_HOST_KEY_CHECKING` must be one of:
`yes`, `no`, `ask`.

**--troubleshoot**:
If you can't connect to a virtual machine (VM) instance using SSH, you can
investigate the problem using the `--troubleshoot` flag:

```
gcloud compute ssh VM_NAME --zone=ZONE --troubleshoot [--tunnel-through-iap]
```

The troubleshoot flag runs tests and returns recommendations for the following
types of issues:

- VM status
- Network connectivity
- User permissions
- Virtual Private Cloud (VPC) settings
- VM boot

If you specify the `--tunnel-through-iap` flag, the tool also checks
IAP port forwarding.

**--zone**:
Zone of the instance to connect to. If not specified and the
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

**--internal-ip**

**--network**:
Configures the VPC network to use when connecting via IP address or FQDN.

**--region**:
Configures the region to use when connecting via IP address or FQDN.

**--dest-group**:
Configures the destination group to use when connecting via IP address or FQDN.

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
gcloud alpha compute ssh
```

```
gcloud beta compute ssh
```