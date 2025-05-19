# gcloud alpha compute future-reservations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/cancel](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/cancel)*

**NAME**

: **gcloud alpha compute future-reservations cancel - cancel a Compute Engine future reservation**

**SYNOPSIS**

: **`gcloud alpha compute future-reservations cancel` (`[FUTURE_RESERVATION](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/cancel#FUTURE_RESERVATION)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/cancel#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/cancel#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Cancel a Compute Engine future reservation.

**EXAMPLES**

: To cancel a given Compute Engine future reservation, run:

```
gcloud alpha compute future-reservations cancel my-reservation --zone=ZONE
```

**POSITIONAL ARGUMENTS**

: **Future reservation resource - The name of the future reservation to cancel. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `future_reservation` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FUTURE_RESERVATION`**:
ID of the future reservation or fully qualified identifier for the future
reservation.
To set the `future_reservation` attribute:

- provide the argument `future_reservation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The name of the Google Compute Engine zone.
To set the `zone` attribute:

- provide the argument `future_reservation` on the command line with a
fully specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `compute/alpha` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta compute future-reservations cancel
```