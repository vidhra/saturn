# gcloud alpha compute future-reservations update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update)*

**NAME**

: **gcloud alpha compute future-reservations update - update Compute Engine future reservations**

**SYNOPSIS**

: **`gcloud alpha compute future-reservations update` `[FUTURE_RESERVATION](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#FUTURE_RESERVATION)` [`[--[no-]auto-delete-auto-created-reservations](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--[no-]auto-delete-auto-created-reservations)`] [`[--deployment-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--deployment-type)`=`DEPLOYMENT_TYPE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--description)`=`DESCRIPTION`] [`[--[no-]enable-emergent-maintenance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--[no-]enable-emergent-maintenance)`] [`[--planning-status](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--planning-status)`=`PLANNING_STATUS`] [`[--[no-]require-specific-reservation](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--[no-]require-specific-reservation)`] [`[--reservation-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--reservation-name)`=`RESERVATION_NAME`] [`[--scheduling-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--scheduling-type)`=`SCHEDULING_TYPE`] [`[--total-count](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--total-count)`=`TOTAL_COUNT`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--zone)`=`ZONE`] [`[--auto-created-reservations-delete-time](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--auto-created-reservations-delete-time)`=`AUTO_CREATED_RESERVATIONS_DELETE_TIME`     | `[--auto-created-reservations-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--auto-created-reservations-duration)`=`AUTO_CREATED_RESERVATIONS_DURATION`] [`[--clear-name-prefix](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--clear-name-prefix)`     | `[--name-prefix](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--name-prefix)`=`NAME_PREFIX`] [`[--clear-share-settings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--clear-share-settings)`     | `[--share-setting](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--share-setting)`=`SHARE_SETTING` `[--share-with](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--share-with)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#PROJECT)`,…]] [`[--commitment-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--commitment-name)`=`COMMITMENT_NAME` `[--commitment-plan](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--commitment-plan)`=`COMMITMENT_PLAN` `[--previous-commitment-terms](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--previous-commitment-terms)`=`PREVIOUS_COMMITMENT_TERMS`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--machine-type)`=`MACHINE_TYPE` `[--maintenance-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--maintenance-interval)`=`MAINTENANCE_INTERVAL` `[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--min-cpu-platform)`=`MIN_CPU_PLATFORM` `[--accelerator](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]     | `[--clear-accelerator](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--clear-accelerator)` `[--clear-local-ssd](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--clear-local-ssd)`     | `[--local-ssd](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--local-ssd)`=[`count`=`COUNT`],[`interface`=`INTERFACE`],[`size`=`SIZE`]] [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--start-time)`=`START_TIME` `[--duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--duration)`=`DURATION`     | `[--end-time](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#--end-time)`=`END_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update Compute Engine future reservations.

**EXAMPLES**

: To update total count, start and end time of a Compute Engine future reservation
in ``us-central1-a``, run:

```
gcloud alpha compute future-reservations update my-future-reservation --total-count=1000 --start-time=2021-11-10T07:00:00Z --end-time=2021-12-10T07:00:00Z --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`FUTURE_RESERVATION`**:
Name of the future reservation to update.

**FLAGS**

: **--[no-]auto-delete-auto-created-reservations**:
If specified, the auto-created reservations for a future reservation are deleted
at the end time (default) or at a specified delete time. Use
`--auto-delete-auto-created-reservations` to enable and
`--no-auto-delete-auto-created-reservations` to disable.

**--deployment-type**:
The deployment type for the reserved capacity.
`DEPLOYMENT_TYPE` must be one of:

**`DENSE`**:
DENSE mode is for densely deployed reservation blocks.

**`FLEXIBLE`**:
FLEXIBLE mode is for highly flexible, logical reservation blocks.

**--description**:
An optional description of the future reservation to create.

**--[no-]enable-emergent-maintenance**:
Emergent maintenance flag for the reservation, which enrolls all the underlying
vms, hosts and SB infrastructure to receive emergent maintenance notifications
in advance. Use `--enable-emergent-maintenance` to enable and
`--no-enable-emergent-maintenance` to disable.

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
Zone of the future reservation to update. If not specified and the
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

**--clear-name-prefix**

**--clear-share-settings**

**--commitment-name**

**--machine-type**

**--start-time**

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
gcloud beta compute future-reservations update
```