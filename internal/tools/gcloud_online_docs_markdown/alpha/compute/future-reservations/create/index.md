# gcloud alpha compute future-reservations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create)*

**NAME**

: **gcloud alpha compute future-reservations create - create a Compute Engine future reservation**

**SYNOPSIS**

: **`gcloud alpha compute future-reservations create` `[FUTURE_RESERVATION](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#FUTURE_RESERVATION)` `[--[no-]auto-delete-auto-created-reservations](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--<span>[no-]</span>auto-delete-auto-created-reservations)` (`[--source-instance-template](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--source-instance-template)`=`SOURCE_INSTANCE_TEMPLATE`     | [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--machine-type)`=`MACHINE_TYPE` : `[--accelerator](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`] `[--local-ssd](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--local-ssd)`=[`count`=`COUNT`],[`interface`=`INTERFACE`],[`size`=`SIZE`] `[--maintenance-freeze-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--maintenance-freeze-duration)`=`MAINTENANCE_FREEZE_DURATION` `[--maintenance-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--maintenance-interval)`=`MAINTENANCE_INTERVAL` `[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--min-cpu-platform)`=`MIN_CPU_PLATFORM`]     | [`[--tpu-version](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--tpu-version)`=`TPU_VERSION` : `[--chip-count](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--chip-count)`=`CHIP_COUNT` `[--workload-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--workload-type)`=`WORKLOAD_TYPE`]) (`[--start-time](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--start-time)`=`START_TIME` (`[--duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--duration)`=`DURATION` | `[--end-time](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--end-time)`=`END_TIME`)) [`[--deployment-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--deployment-type)`=`DEPLOYMENT_TYPE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--description)`=`DESCRIPTION`] [`[--name-prefix](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--name-prefix)`=`NAME_PREFIX`] [`[--planning-status](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--planning-status)`=`PLANNING_STATUS`] [`[--[no-]require-specific-reservation](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--[no-]require-specific-reservation)`] [`[--reservation-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--reservation-mode)`=`RESERVATION_MODE`] [`[--reservation-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--reservation-name)`=`RESERVATION_NAME`] [`[--scheduling-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--scheduling-type)`=`SCHEDULING_TYPE`] [`[--total-count](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--total-count)`=`TOTAL_COUNT`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--zone)`=`ZONE`] [`[--auto-created-reservations-delete-time](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--auto-created-reservations-delete-time)`=`AUTO_CREATED_RESERVATIONS_DELETE_TIME`     | `[--auto-created-reservations-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--auto-created-reservations-duration)`=`AUTO_CREATED_RESERVATIONS_DURATION`] [`[--commitment-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--commitment-name)`=`COMMITMENT_NAME` `[--commitment-plan](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--commitment-plan)`=`COMMITMENT_PLAN` `[--previous-commitment-terms](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--previous-commitment-terms)`=`PREVIOUS_COMMITMENT_TERMS`] [`[--share-setting](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--share-setting)`=`SHARE_SETTING` `[--share-with](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#--share-with)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#PROJECT)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a Compute Engine future reservation.

**EXAMPLES**

: To create a Compute Engine future reservation by specifying VM properties using
an instance template, run:

```
gcloud alpha compute future-reservations create my-future-reservation --total-count=1000 --start-time=2022-11-10 --end-time=2022-12-10 --name-prefix=prefix-reservation --source-instance-template=example-instance-template --zone=fake-zone
```

To create a Compute Engine future reservation by directly specifying VM
properties, run:

```
gcloud alpha compute future-reservations create my-future-reservation --total-count=1000 --start-time=2022-11-10 --end-time=2022-12-10 --name-prefix=prefix-reservation --machine-type=custom-8-10240 --min-cpu-platform="Intel Haswell" --accelerator=count=2,type=nvidia-tesla-v100 --local-ssd=size=375,interface=scsi
```

**POSITIONAL ARGUMENTS**

: **`FUTURE_RESERVATION`**:
Name of the future reservation to create.

**REQUIRED FLAGS**

: **--[no-]auto-delete-auto-created-reservations**:
If specified, the auto-created reservations for a future reservation are deleted
at the end time (default) or at a specified delete time. Use
`--auto-delete-auto-created-reservations` to enable and
`--no-auto-delete-auto-created-reservations` to disable.

**--source-instance-template**

**--start-time**

**OPTIONAL FLAGS**

: **--deployment-type**:
The deployment type for the reserved capacity.
`DEPLOYMENT_TYPE` must be one of:

**`DENSE`**:
DENSE mode is for densely deployed reservation blocks.

**`FLEXIBLE`**:
FLEXIBLE mode is for highly flexible, logical reservation blocks.

**--description**:
An optional description of the future reservation to create.

**--name-prefix**:
A name prefix for the auto-created reservations when capacity is delivered at
the start time. Each auto-created reservation name starts with the name prefix.

**--planning-status**:
The planning status of the future reservation. The default value is DRAFT. While
in DRAFT, any changes to the future reservation's properties will be allowed. If
set to SUBMITTED, the future reservation will submit and its procurementStatus
will change to PENDING_APPROVAL. Once the future reservation is pending
approval, changes to the future reservation's properties will not be allowed.
`PLANNING_STATUS` must be one of:

**`DRAFT`**:
Default planning status value.

**`SUBMITTED`**:
Planning status value to immediately submit the future reservation.

**--[no-]require-specific-reservation**:
Indicate whether the auto-created reservations can be consumed by VMs with "any
reservation" defined. If enabled, then only VMs that target the auto-created
reservation by name using `--reservation-affinity=specific` can
consume from this reservation. Auto-created reservations delivered with this
flag enabled will inherit the name of the future reservation. Use
`--require-specific-reservation` to enable and
`--no-require-specific-reservation` to disable.

**--reservation-mode**:
The mode of the reservation. `RESERVATION_MODE` must be
one of:

**`CALENDAR`**:
This indicates to create a future reservation in calendar mode, which is ideal
for reserving GPU VMs. The auto-created reservations for the future reservation
are automatically deleted at the end of the reservation period.

**`DEFAULT`**:
This indicates to create a standard future reservation. If you want to
automatically delete the auto-created reservations, then you must use the
--auto-delete-auto-created-reservations flag.

**--reservation-name**:
Name of reservations where the capacity is provisioned at the time of delivery
of future reservations. If the reservation with the given name does not exist
already, it is created automatically at the time of Approval with INACTIVE state
till specified start-time. Either provide the reservation_name or a name_prefix.

**--scheduling-type**:
Maintenance for the reserved capacity. `SCHEDULING_TYPE`
must be one of:

**`GROUPED`**:
In GROUPED mode, maintenance on all reserved instances is synchronized.

**`INDEPENDENT`**:
In INDEPENDENT mode, maintenance is not synchronized for this reservation, and
each instance has its own maintenance window.

**--total-count**:
The total number of instances for which capacity assurance is requested at a
future time period.

**--zone**:
Zone of the future reservation to create. If not specified and the
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

**--auto-created-reservations-delete-time**

**--commitment-name**

**--share-setting**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta compute future-reservations create
```