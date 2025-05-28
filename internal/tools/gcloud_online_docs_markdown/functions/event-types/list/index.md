# gcloud functions event-types list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/functions/event-types/list](https://cloud.google.com/sdk/gcloud/reference/functions/event-types/list)*

**NAME**

: **gcloud functions event-types list - list types of events that can be a trigger for a Google Cloud Function**

**SYNOPSIS**

: **`gcloud functions event-types list` [`[--gen2](https://cloud.google.com/sdk/gcloud/reference/functions/event-types/list#--gen2)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/functions/event-types/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud functions event-types list` displays types of events that can
be a trigger for a Google Cloud Function.

- For an event type, `EVENT_TYPE_DEFAULT` marks whether the given event
type is the default (in which case the `--trigger-event` flag may be
omitted).
- For a resource, `RESOURCE_OPTIONAL` marks whether the resource has a
corresponding default value (in which case the `--trigger-resource`
flag may be omitted).

**FLAGS**

: **--gen2**:
If enabled, this command will use Cloud Functions (Second generation). If
disabled with `--no-gen2`, Cloud Functions (First generation) will be
used. If not specified, the value of this flag will be taken from the
`functions/gen2` configuration property.

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
gcloud alpha functions event-types list
```

```
gcloud beta functions event-types list
```