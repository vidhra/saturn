# gcloud compute reservations update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update)*

**NAME**

: **gcloud compute reservations update - update Compute Engine reservations**

**SYNOPSIS**

: **`gcloud compute reservations update` `[RESERVATION](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#RESERVATION)` [`[--add-share-with](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#--add-share-with)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#PROJECT)`,…]] [`[--remove-share-with](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#--remove-share-with)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#PROJECT)`,…]] [`[--reservation-sharing-policy](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#--reservation-sharing-policy)`=`RESERVATION_SHARING_POLICY`] [`[--vm-count](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#--vm-count)`=`VM_COUNT`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update Compute Engine reservations.

**EXAMPLES**

: To add `project-1,project-2,project-3` to the list of projects that
are shared with a Compute Engine reservation, `my-reservation` in
zone: `us-central1-a`, run:

```
gcloud compute reservations update my-reservation --add-share-with=project-1,project-2,project-3 --zone=us-central1-a
```

To remove `project-1,project-2,project-3` from the list of projects
that are shared with a Compute Engine reservation, `my-reservation`
in zone: `us-central1-a`, run:

```
gcloud compute reservations update my-reservation --remove-share-with=project-1,project-2,project-3 --zone=us-central1-a
```

To update the number of reserved VM instances to 500 for a Compute Engine
reservation, `my-reservation` in zone: `us-central1-a`,
run:

```
gcloud compute reservations update my-reservation --zone=us-central1-a --vm-count=500
```

**POSITIONAL ARGUMENTS**

: **`RESERVATION`**:
Name of the reservation to update.

**FLAGS**

: **--add-share-with**:
If this reservation is shared (--share-setting is projects), then specify a
comma-separated list of projects to share the reservation with. You must list
the projects using project IDs or project numbers.

**--remove-share-with**:
A list of specific projects to remove from the list of projects that this
reservation is shared with. List must contain project IDs or project numbers.

**--reservation-sharing-policy**:
The reservation sharing policy to use for this reservation.
`RESERVATION_SHARING_POLICY` must be one of:

**`ALLOW_ALL`**:
The reservation can be shared with Google Cloud services.

**`DISALLOW_ALL`**:
The reservation won't be shared with Google Cloud services. If you omit this
flag during creation, the default value is DISALLOW_ALL.

**--vm-count**:
The number of VM instances that are allocated to this reservation. The value of
this field must be an int in the range [1, 1000].

**--zone**:
Zone of the reservation to update. If not specified and the
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
gcloud alpha compute reservations update
```

```
gcloud beta compute reservations update
```