# gcloud compute commitments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create)*

**NAME**

: **gcloud compute commitments create - create Compute Engine commitments**

**SYNOPSIS**

: **`gcloud compute commitments create` `[COMMITMENT](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#COMMITMENT)` `[--plan](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--plan)`=`PLAN` (`[--resources](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--resources)`=[`local-ssd`=`LOCAL-SSD`],[`memory`=`MEMORY`],[`vcpu`=`VCPU`] `[--resources-accelerator](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--resources-accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]) [`[--auto-renew](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--auto-renew)`] [`[--custom-end-time](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--custom-end-time)`=`CUSTOM_END_TIME`] [`[--merge-source-commitments](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--merge-source-commitments)`=`MERGE_SOURCE_COMMITMENTS`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--region)`=`REGION`] [`[--split-source-commitment](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--split-source-commitment)`=`SPLIT_SOURCE_COMMITMENT`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--type)`=`TYPE`; default="general-purpose"] [`[--existing-reservation](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--existing-reservation)`=[`name`=`NAME`],[`zone`=`ZONE`]     | `[--reservations-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--reservations-from-file)`=`PATH_TO_FILE`     | [`[--reservation](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--reservation)`=`RESERVATION` : `[--reservation-zone](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--reservation-zone)`=`RESERVATION_ZONE` `[--accelerator](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`] `[--local-ssd](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--local-ssd)`=[`interface`=`INTERFACE`],[`size`=`SIZE`] `[--machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--machine-type)`=`MACHINE_TYPE` `[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--min-cpu-platform)`=`MIN_CPU_PLATFORM` `[--require-specific-reservation](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--require-specific-reservation)` `[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--resource-policies)`=[`KEY`=`VALUE`,…] `[--vm-count](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--vm-count)`=`VM_COUNT` `[--share-setting](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--share-setting)`=`SHARE_SETTING` `[--share-with](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#--share-with)`=`SHARE_WITH`,[`[SHARE_WITH](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#SHARE_WITH)`,…]]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create Compute Engine commitments.

**EXAMPLES**

: To create a commitment called ``commitment-1``
in the ``us-central1`` region, with a
``12-month`` plan,
``9GB`` of memory and 4 vcpu cores, run:

```
gcloud compute commitments create commitment-1 --plan=12-month --resources=memory=9GB,vcpu=4 --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`COMMITMENT`**:
Name of the commitment to create.

**REQUIRED FLAGS**

: **--plan**:
Duration of the commitment. `PLAN` must be one of:
`12-month`, `36-month`.

**--resources**

**OPTIONAL FLAGS**

: **--auto-renew**:
Enable auto renewal for the commitment.

**--custom-end-time**:
Specifies a custom future end date and extends the commitment's ongoing term.

**--merge-source-commitments**:
Creates the new commitment by merging the specified source commitments and
combining their resources.

**--region**:
Region of the commitment to create. If not specified, you might be prompted to
select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--split-source-commitment**:
Creates the new commitment by splitting the specified source commitment and
redistributing the specified resources.

**--type**:
Type of commitment. `memory-optimized` indicates that the commitment
is for memory-optimized VMs. `TYPE` must be one of:
`accelerator-optimized`, `accelerator-optimized-a3`,
`accelerator-optimized-a3-mega`,
`accelerator-optimized-a3-ultra`,
`accelerator-optimized-a4`, `compute-optimized`,
`compute-optimized-c2d`, `compute-optimized-c3`,
`compute-optimized-c3d`, `compute-optimized-h3`,
`compute-optimized-h4d`, `general-purpose`,
`general-purpose-c4`, `general-purpose-c4a`,
`general-purpose-c4d`, `general-purpose-e2`,
`general-purpose-n2`, `general-purpose-n2d`,
`general-purpose-n4`, `general-purpose-t2d`,
`graphics-optimized`, `memory-optimized`,
`memory-optimized-m3`, `memory-optimized-m4`,
`memory-optimized-m4-6tb`, `memory-optimized-x4-16tb`,
`memory-optimized-x4-24tb`, `memory-optimized-x4-32tb`,
`storage-optimized-z3`.

**--existing-reservation**

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
gcloud alpha compute commitments create
```

```
gcloud beta compute commitments create
```