# gcloud service-directory locations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/service-directory/locations/describe](https://cloud.google.com/sdk/gcloud/reference/service-directory/locations/describe)*

**NAME**

: **gcloud service-directory locations describe - describes a location**

**SYNOPSIS**

: **`gcloud service-directory locations describe` `[LOCATION](https://cloud.google.com/sdk/gcloud/reference/service-directory/locations/describe#LOCATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/service-directory/locations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describes a location.

**EXAMPLES**

: To describe a Service Directory location, run:

```
gcloud service-directory locations describe location us-east1
```

**POSITIONAL ARGUMENTS**

: **Location resource - The Service Directory location to describe. This represents
a Cloud resource. (NOTE) Some attributes are not given arguments in this group
but can be set in other ways.
To set the `project` attribute:

- provide the argument `location` on the command line with a fully
specified name;
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

: These variants are also available:

```
gcloud alpha service-directory locations describe
```

```
gcloud beta service-directory locations describe
```