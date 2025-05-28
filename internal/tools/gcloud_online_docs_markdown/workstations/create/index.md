# gcloud workstations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/create](https://cloud.google.com/sdk/gcloud/reference/workstations/create)*

**NAME**

: **gcloud workstations create - create a workstation**

**SYNOPSIS**

: **`gcloud workstations create` (`[WORKSTATION](https://cloud.google.com/sdk/gcloud/reference/workstations/create#WORKSTATION)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/workstations/create#--cluster)`=`CLUSTER` `[--config](https://cloud.google.com/sdk/gcloud/reference/workstations/create#--config)`=`CONFIG` `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/create#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/workstations/create#--async)`] [`[--env](https://cloud.google.com/sdk/gcloud/reference/workstations/create#--env)`=[`KEY`=`VALUE`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/workstations/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--source-workstation](https://cloud.google.com/sdk/gcloud/reference/workstations/create#--source-workstation)`=`SOURCE_WORKSTATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a workstation.

**EXAMPLES**

: To create a workstation, run:

```
gcloud workstations create WORKSTATION
```

**POSITIONAL ARGUMENTS**

: **Workstation resource - Arguments and flags that specify the workstation to
create. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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
The name of the cluster containing the workstation.
To set the `cluster` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line;
- set the property `workstations/cluster`.

**--config**:
The name of the config containing the workstation.
To set the `config` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--config` on the command line;
- set the property `workstations/config`.

**--region**:
The name of the region of the workstation.
To set the `region` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `workstations/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--env**:
Environment variables passed to the Workstation.

**--labels**:
Labels that are applied to the workstation and propagated to the underlying
Compute Engine resources.

**--source-workstation**:
Source workstation from which this workstations persistent directories are
cloned on creation. When specified, the workstations service agent must have
`compute.disks.createSnapshot` and
`compute.snapshots.useReadOnly` permissions on the source
workstation's host project.

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

**API REFERENCE**

: This command uses the `workstations/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/workstations](https://cloud.google.com/workstations)

**NOTES**

: These variants are also available:

```
gcloud alpha workstations create
```

```
gcloud beta workstations create
```