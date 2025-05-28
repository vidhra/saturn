# gcloud workstations start-tcp-tunnel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel)*

**NAME**

: **gcloud workstations start-tcp-tunnel - start a tunnel through which a local process can forward TCP traffic to the workstation**

**SYNOPSIS**

: **`gcloud workstations start-tcp-tunnel` (`[WORKSTATION](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel#WORKSTATION)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel#--cluster)`=`CLUSTER` `[--config](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel#--config)`=`CONFIG` `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel#--region)`=`REGION`) `[WORKSTATION_PORT](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel#WORKSTATION_PORT)` [`[--local-host-port](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel#--local-host-port)`=`LOCAL_HOST_PORT`; default="localhost:0"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Start a tunnel through which a local process can forward TCP traffic to the
workstation.

**EXAMPLES**

: To start a tunnel to port 22 on a workstation, run:

```
gcloud workstations start-tcp-tunnel --project=my-project --region=us-central1 --cluster=my-cluster --config=my-config my-workstation 22
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

**`WORKSTATION_PORT`**:
The port on the workstation to which traffic should be sent.

**FLAGS**

: **--local-host-port**:
`LOCAL_HOST:LOCAL_PORT` on which gcloud should bind and listen for
connections that should be tunneled.
`LOCAL_PORT` may be omitted, in which case it is treated as 0 and an
arbitrary unused local port is chosen. The colon also may be omitted in that
case.
If `LOCAL_PORT` is 0, an arbitrary unused local port is chosen.

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
gcloud alpha workstations start-tcp-tunnel
```

```
gcloud beta workstations start-tcp-tunnel
```