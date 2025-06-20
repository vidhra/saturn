# gcloud eventarc providers describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/eventarc/providers/describe](https://cloud.google.com/sdk/gcloud/reference/eventarc/providers/describe)*

**NAME**

: **gcloud eventarc providers describe - describe an Eventarc event provider**

**SYNOPSIS**

: **`gcloud eventarc providers describe` (`[PROVIDER](https://cloud.google.com/sdk/gcloud/reference/eventarc/providers/describe#PROVIDER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/eventarc/providers/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/eventarc/providers/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an Eventarc event provider.

**EXAMPLES**

: To describe the provider ``my-provider``, run:

```
gcloud eventarc providers describe my-provider
```

**POSITIONAL ARGUMENTS**

: **Provider resource - The event provider to describe. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PROVIDER`**:
ID of the provider or fully qualified identifier for the provider.
To set the `provider` attribute:

- provide the argument `provider` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the Eventarc provider, which should be either
``global`` or one of the supported regions.
Alternatively, set the [eventarc/location] property.
To set the `location` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `eventarc/location`.**

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