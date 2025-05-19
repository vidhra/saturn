# gcloud apphub locations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apphub/locations/describe](https://cloud.google.com/sdk/gcloud/reference/apphub/locations/describe)*

**NAME**

: **gcloud apphub locations describe - describe an Apphub location**

**SYNOPSIS**

: **`gcloud apphub locations describe` `[LOCATION](https://cloud.google.com/sdk/gcloud/reference/apphub/locations/describe#LOCATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apphub/locations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an Apphub location.

**EXAMPLES**

: To describe a specific apphub location with the name `my-location`,
run:

```
gcloud apphub locations describe my-location
```

**POSITIONAL ARGUMENTS**

: **Location resource - Location. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**NOTES**

: This variant is also available:

```
gcloud alpha apphub locations describe
```