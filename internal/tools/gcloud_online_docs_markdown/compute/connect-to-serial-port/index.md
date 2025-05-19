# gcloud compute connect-to-serial-port  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port)*

**NAME**

: **gcloud compute connect-to-serial-port - connect to the serial port of an instance**

**SYNOPSIS**

: **`gcloud compute connect-to-serial-port` [`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#INSTANCE)` [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--dry-run)`] [`[--extra-args](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--extra-args)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#KEY)`=`VALUE`,…]] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--force-key-file-overwrite)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--location)`=`LOCATION`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--port)`=`PORT`; default=1] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--ssh-key-file)`=`SSH_KEY_FILE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--zone)`=`ZONE`] [`[--ssh-key-expiration](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--ssh-key-expiration)`=`SSH_KEY_EXPIRATION`     | `[--ssh-key-expire-after](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#--ssh-key-expire-after)`=`SSH_KEY_EXPIRE_AFTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute connect-to-serial-port` allows users to connect to,
and interact with, a VM's virtual serial port using ssh as the secure,
authenticated transport protocol.
The user must first enable serial port access to a given VM by setting the
'serial-port-enable=true' metadata key-value pair. Setting 'serial-port-enable'
on the project-level metadata enables serial port access to all VMs in the
project.
This command uses the same SSH key pair as the `[gcloud compute ssh](https://cloud.google.com/sdk/gcloud/reference/compute/ssh)` command
and also ensures that the user's public SSH key is present in the project's
metadata. If the user does not have a public SSH key, one is generated using
ssh-keygen.

**EXAMPLES**

: To connect to the serial port of the instance 'my-instance' in zone
'us-central1-f', run:

```
gcloud compute connect-to-serial-port my-instance --zone=us-central1-f
```

**POSITIONAL ARGUMENTS**

: **[`USER`@]`INSTANCE`**:
Specifies the user/instance for the serial port connection.
``USER`` specifies the username to authenticate
as. If omitted, the current OS user is selected.

**FLAGS**

: **--dry-run**:
If provided, the ssh command is printed to standard out rather than being
executed.

**--extra-args**:
Optional arguments can be passed to the serial port connection by passing
key-value pairs to this flag, such as max-connections=N or replay-lines=N. See
[https://cloud.google.com/compute/docs/instances/interacting-with-serial-console](https://cloud.google.com/compute/docs/instances/interacting-with-serial-console)
for additional options.

**--force-key-file-overwrite**:
If enabled, the gcloud command-line tool will regenerate and overwrite the files
associated with a broken SSH key without asking for confirmation in both
interactive and non-interactive environments.
If disabled, the files associated with a broken SSH key will not be regenerated
and will fail in both interactive and non-interactive environments.

**--location**:
If provided, the region in which the serial console connection will occur. Must
be the region of the VM to connect to.

**--port**:
The number of the requested serial port. Can be 1-4, default is 1.
Instances can support up to four serial ports. By default, this command will
connect to the first serial port. Setting this flag will connect to the
requested serial port.

**--ssh-key-file**:
The path to the SSH key file. By default, this is
``~/.ssh/google_compute_engine``.

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
gcloud alpha compute connect-to-serial-port
```

```
gcloud beta compute connect-to-serial-port
```