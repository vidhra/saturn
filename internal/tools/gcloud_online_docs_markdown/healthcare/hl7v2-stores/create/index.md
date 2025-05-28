# gcloud healthcare hl7v2-stores create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create)*

**NAME**

: **gcloud healthcare hl7v2-stores create - create a Cloud Healthcare API HL7v2 store**

**SYNOPSIS**

: **`gcloud healthcare hl7v2-stores create` (`[HL7V2_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create#HL7V2_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create#--location)`=`LOCATION`) [`[--notification-config](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create#--notification-config)`=[`filter`=`FILTER`],[`pubsub-topic`=`PUBSUB-TOPIC`]] [`[--parser-version](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create#--parser-version)`=`PARSER_VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Healthcare API HL7v2 store.

**EXAMPLES**

: To create a HL7v2 store called
``test-hl7v2-store``, run:

```
gcloud healthcare hl7v2-stores create test-hl7v2-store --dataset=test-dataset
```

To create a HL7v2 store with two Cloud Pub/Sub topics
``test-pubsub-topic1`` and
``test-pubsub-topic2`` with corresponding
filters, run:

```
gcloud healthcare hl7v2-stores create test-hl7v2-store --dataset=test-dataset --notification-config=pubsub-topic=projects/my-project/topics/test-pubsub-topic1,filter="labels.priority=high" --notification-config=pubsub-topic=projects/my-project/topics/test-pubsub-topic2,filter=PatientId("123456", "MRN")
```

**POSITIONAL ARGUMENTS**

: **Hl7v2Store resource - Cloud Healthcare API HL7v2 store to create. The arguments
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

**--parser-version**:
Immutable. Determines the version of both the default parser to be used when [schema](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig.FIELDS.schema)
is not given, as well as the schematized parser used when [schema](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig.FIELDS.schema)
is specified. This field is immutable after HL7v2 store creation.
`PARSER_VERSION` must be one of:

**`v1`**:
The parsedData includes every given non-empty message field except the Field
Separator (MSH-1) field. As a result, the parsed MSH segment starts with the
MSH-2 field and the field numbers are off-by-one with respect to the HL7
standard.

**`v2`**:
The parsedData includes every given non-empty message field.

**`v3`**:
This version is the same as V2, with the following change. The parsedData
contains unescaped escaped field separators, component separators, sub-component
separators, repetition separators, escape characters, and truncation characters.
If [schema](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig.FIELDS.schema)
is specified, the schematized parser uses improved parsing heuristics compared
to previous versions.

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
gcloud alpha healthcare hl7v2-stores create
```

```
gcloud beta healthcare hl7v2-stores create
```