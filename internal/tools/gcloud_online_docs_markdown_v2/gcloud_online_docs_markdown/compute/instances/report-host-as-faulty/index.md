# gcloud compute instances report-host-as-faulty  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty](https://cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty)*

**NAME**

: **gcloud compute instances report-host-as-faulty - report a host as faulty to start the repair process**

**SYNOPSIS**

: **`gcloud compute instances report-host-as-faulty` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty#INSTANCE_NAME)` `[--disruption-schedule](https://cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty#--disruption-schedule)`=`DISRUPTION_SCHEDULE` `[--fault-reasons](https://cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty#--fault-reasons)`=[`behavior`=`BEHAVIOR`],[`description`=`DESCRIPTION`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty#--async)`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances report-host-as-faulty` is used to report a
host as faulty to start the repair process.

**EXAMPLES**

: To report a host as faulty for an instance named
``test-instance``, run:

```
gcloud compute instances report-host-as-faulty test-instance --fault-reasons=behavior=SILENT_DATA_CORRUPTION,description="affecting our ML job" --disruption-schedule=IMMEDIATE
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**REQUIRED FLAGS**

: **--disruption-schedule**:
Specifies the timing for initiating the fault reporting process. The default
value is ['IMMEDIATE'] which initiates the process right away.
`DISRUPTION_SCHEDULE` must be (only one value is
supported): `IMMEDIATE`.

**--fault-reasons**:
Specified and can include one or more of the following types:
['BEHAVIOR_UNSPECIFIED', 'PERFORMANCE', 'SILENT_DATA_CORRUPTION',
'UNRECOVERABLE_GPU_ERROR']. This helps categorize the nature of the fault being
reported.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
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
gcloud alpha compute instances report-host-as-faulty
```

```
gcloud beta compute instances report-host-as-faulty
```