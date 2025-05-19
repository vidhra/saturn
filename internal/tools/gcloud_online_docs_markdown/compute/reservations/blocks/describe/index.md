# gcloud compute reservations blocks describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/describe](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/describe)*

**NAME**

: **gcloud compute reservations blocks describe - describe a Compute Engine reservation block**

**SYNOPSIS**

: **`gcloud compute reservations blocks describe` `[RESERVATION](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/describe#RESERVATION)` `[--block-name](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/describe#--block-name)`=`BLOCK_NAME` [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/describe#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Compute Engine reservation block.

**EXAMPLES**

: To describe a reservation block in reservation my-reservation in my-zone with
block name my-reservation-block-0001, run:

```
gcloud compute reservations blocks describe my-reservation --zone=my-zone --block-name=my-reservation-block-0001
```

**POSITIONAL ARGUMENTS**

: **`RESERVATION`**:
Name of the reservation to describe.

**REQUIRED FLAGS**

: **--block-name**:
The name of the reservation block.

**OPTIONAL FLAGS**

: **--zone**:
Zone of the reservation to describe. If not specified and the
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
gcloud alpha compute reservations blocks describe
```

```
gcloud beta compute reservations blocks describe
```