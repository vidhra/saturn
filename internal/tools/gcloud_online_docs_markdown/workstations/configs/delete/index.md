# gcloud workstations configs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/configs/delete](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/delete)*

**NAME**

: **gcloud workstations configs delete - delete a workstation configuration**

**SYNOPSIS**

: **`gcloud workstations configs delete` (`[CONFIG](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/delete#CONFIG)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/delete#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/delete#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a workstation configuration.

**EXAMPLES**

: To delete a configuration, run:

```
gcloud workstations configs delete WORKSTATION
```

**POSITIONAL ARGUMENTS**

: **Config resource - The name of the configuration to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONFIG`**:
ID of the config or fully qualified identifier for the config.
To set the `config` attribute:

- provide the argument `config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
The name of the cluster containing the config.
To set the `cluster` attribute:

- provide the argument `config` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line;
- set the property `workstations/cluster`.

**--region**:
The name of the region of the config.
To set the `region` attribute:

- provide the argument `config` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `workstations/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha workstations configs delete
```

```
gcloud beta workstations configs delete
```