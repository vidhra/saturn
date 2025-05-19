# gcloud compute diagnose routes  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes)*

**NAME**

: **gcloud compute diagnose routes - routes to/from Compute Engine virtual machine instances**

**SYNOPSIS**

: **`gcloud compute diagnose routes` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#NAME)` …] [`[--container](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--container)`=`CONTAINER`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--dry-run)`] [`[--external-route-ip](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--external-route-ip)`=`EXTERNAL_ROUTE_IP`] [`[--force-key-file-overwrite](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--force-key-file-overwrite)`] [`[--plain](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--plain)`] [`[--regexp](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--regexp)`=`REGEXP`, `[-r](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#-r)` `[REGEXP](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#REGEXP)`] [`[--reverse-traceroute](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--reverse-traceroute)`] [`[--ssh-flag](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--ssh-flag)`=`SSH_FLAG`] [`[--ssh-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--ssh-key-file)`=`SSH_KEY_FILE`] [`[--strict-host-key-checking](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--strict-host-key-checking)`=`STRICT_HOST_KEY_CHECKING`] [`[--user](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--user)`=`USER`] [`[--zones](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--zones)`=`ZONE`,[`[ZONE](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#ZONE)`,…]] [`[--ssh-key-expiration](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--ssh-key-expiration)`=`SSH_KEY_EXPIRATION`     | `[--ssh-key-expire-after](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#--ssh-key-expire-after)`=`SSH_KEY_EXPIRE_AFTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#GCLOUD-WIDE-FLAGS) …`] [-- `[TRACEROUTE_ARGS](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/routes#TRACEROUTE_ARGS)` …]**

**DESCRIPTION**

: Routes to/from Compute Engine virtual machine instances.
NOTE: The name filtering will cycle through all the VMs in the project.
Depending on the size of the project, this could be a considerable amount of
work.
If that is the case, use the --regexp flag to filter down the amount of VMs
considered in the filtering.

**EXAMPLES**

: To route to/from Compute Engine virtual machine instances, run:

```
gcloud compute diagnose routes
```

**POSITIONAL ARGUMENTS**

: **[`NAME` …]**:
If provided, show details for the specified names and/or URIs of resources.

**[-- `TRACEROUTE_ARGS` …]**:
Flags and positionals passed to the underlying traceroute call.
The '--' argument must be specified between gcloud specific args on the left and
TRACEROUTE_ARGS on the right. Example:

```
gcloud compute diagnose routes example-instance -- -w 0.5 -q 5 42
```

**FLAGS**

: **--container**:
The name or ID of a container inside of the virtual machine instance to connect
to. This only applies to virtual machines that are using a Container-Optimized
OS virtual machine image. For more information, see [https://cloud.google.com/compute/docs/containers](https://cloud.google.com/compute/docs/containers)

**--dry-run**:
Print the equivalent scp/ssh command that would be run to stdout, instead of
executing it.

**--external-route-ip**:
For reverse traceroute, this will be the ip given to the VM instance to
traceroute to. This will override all obtained ips.

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

**--regexp**:
Regular expression to filter the names of the results on. Any names that do not
match the entire regular expression will be filtered out.

**--reverse-traceroute**:
If enabled, will also run traceroute from the VM to the host

**--ssh-flag**:
Additional flags to be passed to `ssh(1)`. It is recommended that
flags be passed using an assignment operator and quotes. This flag will replace
occurences of ``%USER%`` and
``%INSTANCE%`` with their dereferenced values.
Example:

```
gcloud compute diagnose routes example-instance --zone us-central1-a           --ssh-flag="-vvv" --ssh-flag="-L 80:%INSTANCE%:80"
```

is equivalent to passing the flags ``--vvv``
and ``-L 80:162.222.181.197:80`` to
`ssh(1)` if the external IP address of 'example-instance' is
162.222.181.197.

**--ssh-key-file**:
The path to the SSH key file. By default, this is
``~/.ssh/google_compute_engine``.

**--strict-host-key-checking**:
Override the default behavior of StrictHostKeyChecking for the connection. By
default, StrictHostKeyChecking is set to 'no' the first time you connect to an
instance, and will be set to 'yes' for all subsequent connections.
`STRICT_HOST_KEY_CHECKING` must be one of:
`yes`, `no`, `ask`.

**--user**:
User for login to the selected VMs. If not specified, the default user will be
used.

**--zones**:
If provided, only resources from the given zones are queried.

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
gcloud alpha compute diagnose routes
```

```
gcloud beta compute diagnose routes
```