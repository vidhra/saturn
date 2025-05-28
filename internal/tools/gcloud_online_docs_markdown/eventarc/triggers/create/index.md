# gcloud eventarc triggers create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create)*

**NAME**

: **gcloud eventarc triggers create - create an Eventarc trigger**

**SYNOPSIS**

: **`gcloud eventarc triggers create` (`[TRIGGER](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#TRIGGER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--location)`=`LOCATION`) `[--event-filters](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--event-filters)`=[`ATTRIBUTE`=`VALUE`,…] ([`[--destination-gke-cluster](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-gke-cluster)`=`DESTINATION_GKE_CLUSTER` `[--destination-gke-service](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-gke-service)`=`DESTINATION_GKE_SERVICE` : `[--destination-gke-location](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-gke-location)`=`DESTINATION_GKE_LOCATION` `[--destination-gke-namespace](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-gke-namespace)`=`DESTINATION_GKE_NAMESPACE` `[--destination-gke-path](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-gke-path)`=`DESTINATION_GKE_PATH`]     | [`[--destination-http-endpoint-uri](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-http-endpoint-uri)`=`DESTINATION_HTTP_ENDPOINT_URI` : `[--network-attachment](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--network-attachment)`=`NETWORK_ATTACHMENT`]     | [`[--destination-run-service](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-run-service)`=`DESTINATION_RUN_SERVICE` : `[--destination-run-path](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-run-path)`=`DESTINATION_RUN_PATH` `[--destination-run-region](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-run-region)`=`DESTINATION_RUN_REGION`]     | [`[--destination-workflow](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-workflow)`=`DESTINATION_WORKFLOW` : `[--destination-workflow-location](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--destination-workflow-location)`=`DESTINATION_WORKFLOW_LOCATION`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--async)`] [`[--channel](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--channel)`=`CHANNEL`] [`[--event-data-content-type](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--event-data-content-type)`=`EVENT_DATA_CONTENT_TYPE`] [`[--event-filters-path-pattern](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--event-filters-path-pattern)`=[`ATTRIBUTE`=`PATH_PATTERN`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--transport-topic](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#--transport-topic)`=`TRANSPORT_TOPIC`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Eventarc trigger.

**EXAMPLES**

: To create a new trigger ``my-trigger`` for
events of type
``google.cloud.pubsub.topic.v1.messagePublished``
with destination Cloud Run service
``my-service``, run:

```
gcloud eventarc triggers create my-trigger --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" --destination-run-service=my-service
```

**POSITIONAL ARGUMENTS**

: **Trigger resource - The trigger to create. The arguments in this group can be
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

**REQUIRED FLAGS**

: **--event-filters**:
The trigger's list of filters that apply to CloudEvents attributes. This flag
can be repeated to add more filters to the list. Only events that match all
these filters will be sent to the destination. The filters must include the
``type`` attribute, as well as any other
attributes that are expected for the chosen type.

**--destination-gke-cluster**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**Channel resource - The channel to use in the trigger. The channel is needed only
if trigger is created for a third-party provider. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--channel` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--channel` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `eventarc/location`.

**--channel**:
ID of the channel or fully qualified identifier for the channel.
To set the `channel` attribute:

- provide the argument `--channel` on the command line.**

**--event-data-content-type**:
Depending on the event provider, you can specify the encoding of the event data
payload that will be delivered to your destination, to either be encoded in
``application/json`` or
``application/protobuf``. The default encoding
is ``application/json``. Note that for custom
sources or third-party providers, or for direct events from Cloud Pub/Sub, this
formatting option is not supported.

**--event-filters-path-pattern**:
The trigger's list of filters in path pattern format that apply to CloudEvent
attributes. This flag can be repeated to add more filters to the list. Only
events that match all these filters will be sent to the destination. Currently,
path pattern format is only available for the resourceName attribute for Cloud
Audit Log events.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--service-account**:
The IAM service account email associated with the trigger.

**Pub/Sub topic resource - The Cloud Pub/Sub topic to use for the trigger's
transport intermediary. This feature is currently only available for triggers of
event type
``google.cloud.pubsub.topic.v1.messagePublished``.
The topic must be in the same project as the trigger. If not specified, a
transport topic will be created. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--transport-topic` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--transport-topic**:
ID of the Pub/Sub topic or fully qualified identifier for the Pub/Sub topic.
To set the `transport-topic` attribute:

- provide the argument `--transport-topic` on the command line.**

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