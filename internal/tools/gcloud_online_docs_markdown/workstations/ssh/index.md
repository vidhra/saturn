# gcloud workstations ssh  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/ssh](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh)*

**NAME**

: **gcloud workstations ssh - SSH into a running workstation**

**SYNOPSIS**

: **`gcloud workstations ssh` (`[WORKSTATION](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#WORKSTATION)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#--cluster)`=`CLUSTER` `[--config](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#--config)`=`CONFIG` `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#--region)`=`REGION`) [`[--command](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#--command)`=`COMMAND`] [`[--local-host-port](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#--local-host-port)`=`LOCAL_HOST_PORT`; default="localhost:0"] [`[--port](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#--port)`=`PORT`; default=22] [`[--ssh-flag](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#--ssh-flag)`=`SSH_FLAG`] [`[--user](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#--user)`=`USER`; default="user"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#GCLOUD-WIDE-FLAGS) …`] [-- `[SSH_ARGS](https://cloud.google.com/sdk/gcloud/reference/workstations/ssh#SSH_ARGS)` …]**

**DESCRIPTION**

: SSH into a running workstation.

**EXAMPLES**

: To ssh into a running workstation, run:

```
gcloud workstations ssh WORKSTATION
```

To specify the workstation port, run:

```
gcloud workstations ssh WORKSTATION --port=22
```

To ssh into a running workstation with a username, run:

```
gcloud workstations ssh WORKSTATION --user=my-user
```

To run a command on the workstation, such as getting a snapshot of the guest's
process tree, run:
```
gcloud workstations ssh WORKSTATION --command="ps -ejH"
```

**POSITIONAL ARGUMENTS**

: **Workstation resource - The group of arguments defining a workstation The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`WORKSTATION`**:
ID of the workstation or fully qualified identifier for the workstation.
To set the `workstation` attribute:

- provide the argument `workstation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
The cluster for the workstation.
To set the `cluster` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line;
- set the property `workstations/cluster`.

**--config**:
The config for the workstation.
To set the `config` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--config` on the command line;
- set the property `workstations/config`.

**--region**:
The region for the workstation.
To set the `region` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `workstations/region`.**

**[-- `SSH_ARGS` …]**:
Flags and positionals passed to the underlying ssh implementation.
The '--' argument must be specified between gcloud specific args on the left and
SSH_ARGS on the right.

**FLAGS**

: **--command**:
A command to run on the workstation.
Runs the command on the target workstation and then exits.

**--local-host-port**:
`LOCAL_HOST:LOCAL_PORT` on which gcloud should bind and listen for
connections that should be tunneled.
`LOCAL_PORT` may be omitted, in which case it is treated as 0 and an
arbitrary unused local port is chosen. The colon also may be omitted in that
case.
If `LOCAL_PORT` is 0, an arbitrary unused local port is chosen.

**--port**:
The port on the workstation to which traffic should be sent.

**--ssh-flag**:
Additional flags to be passed to `ssh(1)`. It is recommended that
flags be passed using an assignment operator and quotes. Example:

```
gcloud workstations ssh --ssh-flag="-vvv" --ssh-flag="-L 80:localhost:80"
```

**--user**:
The username with which to SSH.

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
gcloud alpha workstations ssh
```

```
gcloud beta workstations ssh
```