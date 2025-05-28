# gcloud eventarc triggers update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update)*

**NAME**

: **gcloud eventarc triggers update - update an Eventarc trigger**

**SYNOPSIS**

: **`gcloud eventarc triggers update` (`[TRIGGER](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#TRIGGER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--async)`] [`[--event-data-content-type](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--event-data-content-type)`=`EVENT_DATA_CONTENT_TYPE`] [`[--event-filters](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--event-filters)`=[`ATTRIBUTE`=`VALUE`,…]] [`[--event-filters-path-pattern](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--event-filters-path-pattern)`=[`ATTRIBUTE`=`PATH_PATTERN`,…]] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--remove-labels)`=[`KEY`,…]] [`[--clear-service-account](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--clear-service-account)`     | `[--service-account](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--service-account)`=`SERVICE_ACCOUNT`] [`[--destination-gke-namespace](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--destination-gke-namespace)`=`DESTINATION_GKE_NAMESPACE` `[--destination-gke-service](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--destination-gke-service)`=`DESTINATION_GKE_SERVICE` `[--clear-destination-gke-path](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--clear-destination-gke-path)`     | `[--destination-gke-path](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--destination-gke-path)`=`DESTINATION_GKE_PATH`     | `[--destination-run-region](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--destination-run-region)`=`DESTINATION_RUN_REGION` `[--destination-run-service](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--destination-run-service)`=`DESTINATION_RUN_SERVICE` `[--clear-destination-run-path](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--clear-destination-run-path)`     | `[--destination-run-path](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--destination-run-path)`=`DESTINATION_RUN_PATH`     | `[--destination-workflow](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--destination-workflow)`=`DESTINATION_WORKFLOW` `[--destination-workflow-location](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#--destination-workflow-location)`=`DESTINATION_WORKFLOW_LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Eventarc trigger.

**EXAMPLES**

: To update the trigger ``my-trigger`` by setting
its destination Cloud Run service to
``my-service``, run:

```
gcloud eventarc triggers update my-trigger --destination-run-service=my-service
```

**POSITIONAL ARGUMENTS**

: **Trigger resource - The trigger to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `trigger` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TRIGGER`**:
ID of the trigger or fully qualified identifier for the trigger.
To set the `trigger` attribute:

- provide the argument `trigger` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the Eventarc trigger, which should be either
``global`` or one of the supported regions.
Alternatively, set the [eventarc/location] property.
To set the `location` attribute:

- provide the argument `trigger` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `eventarc/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--event-data-content-type**:
Depending on the event provider, you can specify the encoding of the event data
payload that will be delivered to your destination, to either be encoded in
``application/json`` or
``application/protobuf``. The default encoding
is ``application/json``. Note that for custom
sources or third-party providers, or for direct events from Cloud Pub/Sub, this
formatting option is not supported.

**--event-filters**:
The trigger's list of filters that apply to CloudEvents attributes. This flag
can be repeated to add more filters to the list. Only events that match all
these filters will be sent to the destination. The filters must include the
``type`` attribute, as well as any other
attributes that are expected for the chosen type.

**--event-filters-path-pattern**:
The trigger's list of filters in path pattern format that apply to CloudEvent
attributes. This flag can be repeated to add more filters to the list. Only
events that match all these filters will be sent to the destination. Currently,
path pattern format is only available for the resourceName attribute for Cloud
Audit Log events.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--clear-service-account**

**--destination-gke-namespace**

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