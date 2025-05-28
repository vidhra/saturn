# gcloud compute reservations blocks perform-maintenance  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance)*

**NAME**

: **gcloud compute reservations blocks perform-maintenance - perform maintenance on a reservation block within a reservation**

**SYNOPSIS**

: **`gcloud compute reservations blocks perform-maintenance` `[RESERVATION](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance#RESERVATION)` `[--block-name](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance#--block-name)`=`BLOCK_NAME` [`[--scope](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance#--scope)`=`SCOPE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Perform maintenance on a reservation block within a reservation.

**EXAMPLES**

: To perform maintenance on a reservation block in reservation my-reservation in
my-zone with block name my-reservation-block-0001 with scope all, run:

```
gcloud compute reservations blocks perform-maintenance my-reservation --zone=my-zone --block-name=my-reservation-block-0001 --scope=all
```

**POSITIONAL ARGUMENTS**

: **`RESERVATION`**:
Name of the reservation to perform-maintenance.

**REQUIRED FLAGS**

: **--block-name**:
The name of the reservation block.

**OPTIONAL FLAGS**

: **--scope**:
The maintenance scope to set for the reservation block.
`SCOPE` must be one of:

**`all`**:
Perform maintenance on all hosts in the reservation block.

**`running`**:
Perform maintenance only on the hosts in the reservation block that have running
VMs.

**`unused`**:
Perform maintenance only on the hosts in the reservation block that don't have
running VMs.

**--zone**:
Zone of the reservation to perform-maintenance. If not specified and the
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
gcloud alpha compute reservations blocks perform-maintenance
```

```
gcloud beta compute reservations blocks perform-maintenance
```