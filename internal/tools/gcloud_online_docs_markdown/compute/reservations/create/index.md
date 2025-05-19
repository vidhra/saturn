# gcloud compute reservations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create)*

**NAME**

: **gcloud compute reservations create - create a Compute Engine reservation**

**SYNOPSIS**

: **`gcloud compute reservations create` `[RESERVATION](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#RESERVATION)` (`[--vm-count](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--vm-count)`=`VM_COUNT` (`[--source-instance-template](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--source-instance-template)`=`SOURCE_INSTANCE_TEMPLATE` | [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--machine-type)`=`MACHINE_TYPE` : `[--accelerator](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`] `[--local-ssd](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--local-ssd)`=[`count`=`COUNT`],[`interface`=`INTERFACE`],[`size`=`SIZE`] `[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--min-cpu-platform)`=`MIN_CPU_PLATFORM`]) : `[--require-specific-reservation](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--require-specific-reservation)` `[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--resource-policies)`=[`KEY`=`VALUE`,…]) [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--description)`=`DESCRIPTION`] [`[--reservation-sharing-policy](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--reservation-sharing-policy)`=`RESERVATION_SHARING_POLICY`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--zone)`=`ZONE`] [`[--share-setting](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--share-setting)`=`SHARE_SETTING` `[--share-with](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#--share-with)`=`SHARE_WITH`,[`[SHARE_WITH](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#SHARE_WITH)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Compute Engine reservation.

**EXAMPLES**

: To create a Compute Engine reservation by specifying VM properties using an
instance template, run:

```
gcloud compute reservations create my-reservation --vm-count=1 --source-instance-template=example-instance-template --zone=fake-zone
```

To create a Compute Engine reservation by directly specifying VM properties,
run:

```
gcloud compute reservations create my-reservation --vm-count=1 --machine-type=custom-8-10240 --min-cpu-platform="Intel Haswell" --accelerator=count=2,type=nvidia-tesla-v100 --local-ssd=size=375,interface=scsi --zone=fake-zone
```

**POSITIONAL ARGUMENTS**

: **`RESERVATION`**:
Name of the reservation to create.

**REQUIRED FLAGS**

: **--vm-count**

**OPTIONAL FLAGS**

: **--description**:
An optional description of the reservation to create.

**--reservation-sharing-policy**:
The reservation sharing policy to use for this reservation.
`RESERVATION_SHARING_POLICY` must be one of:

**`ALLOW_ALL`**:
The reservation can be shared with Google Cloud services.

**`DISALLOW_ALL`**:
The reservation won't be shared with Google Cloud services. If you omit this
flag during creation, the default value is DISALLOW_ALL.

**--zone**:
Zone of the reservation to create. If not specified and the
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

: These variants are also available:

```
gcloud alpha compute reservations create
```

```
gcloud beta compute reservations create
```