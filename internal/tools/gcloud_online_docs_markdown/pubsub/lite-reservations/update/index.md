# gcloud pubsub lite-reservations update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/update](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/update)*

**NAME**

: **gcloud pubsub lite-reservations update - update a Pub/Sub Lite reservation**

**SYNOPSIS**

: **`gcloud pubsub lite-reservations update` (`[RESERVATION](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/update#RESERVATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/update#--location)`=`LOCATION`) `[--throughput-capacity](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/update#--throughput-capacity)`=`THROUGHPUT_CAPACITY` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Pub/Sub Lite reservation.

**EXAMPLES**

: To update a Pub/Sub Lite reservation, run:

```
gcloud pubsub lite-reservations update myreservation --location=us-central1 --throughput-capacity=2
```

**POSITIONAL ARGUMENTS**

: **Reservation resource - Reservation to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `reservation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`RESERVATION`**:
ID of the reservation or fully qualified identifier for the reservation.
To set the `reservation` attribute:

- provide the argument `reservation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location of the Pub/Sub Lite resource.
To set the `location` attribute:

- provide the argument `reservation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--throughput-capacity**:
Reservation throughput capacity. Every unit of throughput capacity is equivalent
to 1 MiB/s of published messages or 2 MiB/s of subscribed messages.

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

: This command uses the `pubsublite/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/pubsub/lite/docs](https://cloud.google.com/pubsub/lite/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha pubsub lite-reservations update
```

```
gcloud beta pubsub lite-reservations update
```