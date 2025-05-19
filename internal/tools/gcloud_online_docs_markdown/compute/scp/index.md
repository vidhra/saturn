# gcloud compute scp  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/scp](https://cloud.google.com/sdk/gcloud/reference/compute/scp)*

**NAME**

: **gcloud compute scp - copy files to and from Google Compute Engine virtual machines via scp**

**SYNOPSIS**

: **`gcloud compute scp` [[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/scp#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/scp#INSTANCE)`:]`[SRC](https://cloud.google.com/sdk/gcloud/reference/compute/scp#SRC)` [[[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/scp#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/scp#INSTANCE)`:]`[SRC](https://cloud.google.com/sdk/gcloud/reference/compute/scp#SRC)` …] [[`[USER](https://cloud.google.com/sdk/gcloud/reference/compute/scp#USER)`@]`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/scp#INSTANCE)`:]`[DEST](https://cloud.google.com/sdk/gcloud/reference/compute/scp#DEST)` [`[--compress](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--compress)`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--dry-run)`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--force-key-file-overwrite)`] [`[--plain](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--plain)`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--port)`=`PORT`] [`[--recurse](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--recurse)`] [`[--scp-flag](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--scp-flag)`=`SCP_FLAG`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--ssh-key-file)`=`SSH_KEY_FILE`] [`[--strict-host-key-checking](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--strict-host-key-checking)`=`STRICT_HOST_KEY_CHECKING`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--zone)`=`ZONE`] [`[--internal-ip](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--internal-ip)`     | `[--tunnel-through-iap](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--tunnel-through-iap)`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--network)`=`NETWORK` `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--region)`=`REGION` : `[--dest-group](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--dest-group)`=`DEST_GROUP`] [`[--ssh-key-expiration](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--ssh-key-expiration)`=`SSH_KEY_EXPIRATION`     | `[--ssh-key-expire-after](https://cloud.google.com/sdk/gcloud/reference/compute/scp#--ssh-key-expire-after)`=`SSH_KEY_EXPIRE_AFTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/scp#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute scp` securely copies files between a virtual machine
instance and your local machine using the scp command.
This command works for Linux VMs and Windows Server 2019 and later VMs that have
[SSH
enabled](https://cloud.google.com/compute/docs/connect/windows-ssh).
In order to set up a successful transfer, follow these guidelines:

- Prefix remote file names with the virtual machine instance name (e.g.,
`example-instance`:~/`FILE`).
- Local file names can be used as is (e.g., ~/`FILE`).
- File names containing a colon (``:´´) must be invoked by either
their absolute path or a path that begins with ``./´´.
- When the destination of your transfer is local, all source files must be from
the same virtual machine.
- When the destination of your transfer is remote instead, all sources must be
local.
- When the destination is Windows Server, the source must be using a similar SSH
version.

Under the covers, `scp(1)` is used to facilitate the transfer.
If the `--region` and `--network` flags are provided, then
`--plain` and `--tunnel-through-iap` are implied and any
remote file names must be prefixed with the remote IP address instead of the
instance name. This is most useful for connecting to on-prem resources.

**EXAMPLES**

: To copy a remote directory, `~/narnia`, from
``example-instance`` to the
`~/wardrobe` directory of your local host, run:

```
gcloud compute scp --recurse example-instance:~/narnia ~/wardrobe
```

Conversely, files from your local computer can be copied to a virtual machine:

```
gcloud compute scp ~/localtest.txt ~/localtest2.txt example-instance:~/narnia
```

Remote Windows-based virtual machines require you to provide a path using
backslash notation:

```
gcloud compute scp ~/localtest.txt ~/localtest2.txt example-windows-instance:"C:\Users\Public"
```

Paths for remote Windows-based virtual machines which contain spaces in
directory name should be appropriately protected with a pair of nested single
and double quotes:

```
gcloud compute scp ~/localtest.txt 'example-windows-instance:"C:\Users\Public\Test Folder"'
```

If the zone cannot be determined, you will be prompted for it. Use the
`--zone` flag to avoid being prompted:

```
gcloud compute scp --recurse example-instance:~/narnia ~/wardrobe --zone=us-central1-a
```

To specify the project, zone, and recurse all together, run:

```
gcloud compute scp --project="my-gcp-project" --zone="us-east1-b" --recurse ~/foo-folder/ gcp-instance-name:~/
```

You can limit the allowed time to ssh. For example, to allow a key to be used
through 2019:

```
gcloud compute scp --recurse example-instance:~/narnia ~/wardrobe --ssh-key-expiration="2020-01-01T00:00:00:00Z"
```

Or alternatively, allow access for the next two minutes:

```
gcloud compute scp --recurse example-instance:~/narnia ~/wardrobe --ssh-key-expire-after=2m
```

To use the IP address of your remote VM (eg, for on-prem), you must also specify
the `--region` and `--network` flags:

```
gcloud compute scp 10.1.2.3:~/narnia ~/wardrobe --region=us-central1 --network=default
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

**--plain**:
Suppress the automatic addition of `ssh(1)`/`scp(1)`
flags. This flag is useful if you want to take care of authentication yourself
or use specific ssh/scp features.

**--port**:
The port to connect to.

**--recurse**:
Upload directories recursively.

**--scp-flag**:
Extra flag to be sent to scp. This flag may be repeated.

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
gcloud alpha compute scp
```

```
gcloud beta compute scp
```