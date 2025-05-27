# gcloud datastream locations fetch-static-ips  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/locations/fetch-static-ips](https://cloud.google.com/sdk/gcloud/reference/datastream/locations/fetch-static-ips)*

**NAME**

: **gcloud datastream locations fetch-static-ips - list Datastream static ips per location**

**SYNOPSIS**

: **`gcloud datastream locations fetch-static-ips` `[LOCATION](https://cloud.google.com/sdk/gcloud/reference/datastream/locations/fetch-static-ips#LOCATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/locations/fetch-static-ips#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Datastream static IPs.

**EXAMPLES**

: To list the static IPs, run:

```
gcloud datastream locations fetch-static-ips my-location
```

**POSITIONAL ARGUMENTS**

: **Location resource - The location you want to list static ips of. This represents
a Cloud resource. (NOTE) Some attributes are not given arguments in this group
but can be set in other ways.
To set the `project` attribute:

- provide the argument `location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`LOCATION`**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `location` on the command line.**

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

: This command uses the `datastream/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/datastream/](https://cloud.google.com/datastream/)

**NOTES**

: This variant is also available:

```
gcloud beta datastream locations fetch-static-ips
```