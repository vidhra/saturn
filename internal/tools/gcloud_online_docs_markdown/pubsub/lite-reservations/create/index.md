# gcloud pubsub lite-reservations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/create](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/create)*

**NAME**

: **gcloud pubsub lite-reservations create - create a Pub/Sub Lite reservation**

**SYNOPSIS**

: **`gcloud pubsub lite-reservations create` `[RESERVATION](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/create#RESERVATION)` `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/create#--location)`=`LOCATION` `[--throughput-capacity](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/create#--throughput-capacity)`=`THROUGHPUT_CAPACITY` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Pub/Sub Lite reservation.

**EXAMPLES**

: To create a Pub/Sub lite-reservation, run:

```
gcloud pubsub lite-reservations create myreservation --location=us-central1 --throughput-capacity=2
```

**POSITIONAL ARGUMENTS**

: **`RESERVATION`**:
Reservation ID.

**REQUIRED FLAGS**

: **Location resource - Identifies the Cloud location this command will be executed
on. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

**--throughput-capacity**:
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
gcloud alpha pubsub lite-reservations create
```

```
gcloud beta pubsub lite-reservations create
```