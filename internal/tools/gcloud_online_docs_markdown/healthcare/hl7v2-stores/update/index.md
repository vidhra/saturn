# gcloud healthcare hl7v2-stores update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/update](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/update)*

**NAME**

: **gcloud healthcare hl7v2-stores update - update a Cloud Healthcare API HL7v2 store**

**SYNOPSIS**

: **`gcloud healthcare hl7v2-stores update` (`[HL7V2_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/update#HL7V2_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/update#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/update#--location)`=`LOCATION`) [`[--notification-config](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/update#--notification-config)`=[`filter`=`FILTER`],[`pubsub-topic`=`PUBSUB-TOPIC`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Healthcare API HL7v2 store.

**EXAMPLES**

: To update the Cloud Pub/Sub topics on a HL7v2 store
``test-hl7v2-store``, run:

```
gcloud healthcare hl7v2-stores update test-hl7v2-store --notification-config=pubsub-topic=projects/my-project/topics/test-pubsub-topic1,filter="labels.priority=high" --notification-config=pubsub-topic=projects/my-project/topics/test-pubsub-topic2
```

**POSITIONAL ARGUMENTS**

: **Hl7v2Store resource - Cloud Healthcare API HL7v2 store to update. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `hl7v2_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`HL7V2_STORE`**:
ID of the hl7v2Store or fully qualified identifier for the hl7v2Store.
To set the `hl7v2_store` attribute:

- provide the argument `hl7v2_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `hl7v2_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `hl7v2_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**FLAGS**

: **--notification-config**:
A list of notification configs. Each configuration uses a filter to determine
whether to publish a message (both Ingest & Create) on the corresponding
notification destination. Only the message name is sent as part of the
notification. Supplied by the client.
See [https://cloud.google.com/appengine/docs/standard/python/search/query_strings](https://cloud.google.com/appengine/docs/standard/python/search/query_strings)
for the syntax of the filter.
Note: A topic must be created before publishing or subscribing to it. For
instructions on creating topics, refer to: [https://cloud.google.com/pubsub/docs/admin#create_a_topic](https://cloud.google.com/pubsub/docs/admin#create_a_topic)

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

: This command uses the `healthcare/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/healthcare](https://cloud.google.com/healthcare)

**NOTES**

: These variants are also available:

```
gcloud alpha healthcare hl7v2-stores update
```

```
gcloud beta healthcare hl7v2-stores update
```