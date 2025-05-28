# gcloud healthcare fhir-stores update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update)*

**NAME**

: **gcloud healthcare fhir-stores update - update a Cloud Healthcare API FHIR store**

**SYNOPSIS**

: **`gcloud healthcare fhir-stores update` (`[FHIR_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update#FHIR_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update#--location)`=`LOCATION`) [`[--enable-update-create](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update#--enable-update-create)`] [`[--pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update#--pubsub-topic)`=`PUBSUB_TOPIC`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Healthcare API FHIR store.

**EXAMPLES**

: To update the Cloud Pub/Sub topic on a FHIR store 'test-fhir-store', run:

```
gcloud healthcare fhir-stores update test-fhir-store --pubsub-topic=projects/my-project/topics/test-pubsub-topic
```

**POSITIONAL ARGUMENTS**

: **FhirStore resource - The Cloud Healthcare API FHIR store you want to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FHIR_STORE`**:
ID of the fhirStore or fully qualified identifier for the fhirStore.
To set the `fhir_store` attribute:

- provide the argument `fhir_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**FLAGS**

: **--enable-update-create**:
Whether this FHIR store has the [updateCreate]
(https://www.hl7.org/fhir/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.updateCreate)
capability. Determines if the client can use an Update operation to create a new
resource with a client-specified ID. If false, all IDs are server-assigned
through the Create operation and attempts to Update a non-existent resource will
return errors.

**--pubsub-topic**:
Google Cloud Pub/Sub topic to send updates to.
Note, a topic needs to be created before publishing or subscribing to it. For
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
gcloud alpha healthcare fhir-stores update
```

```
gcloud beta healthcare fhir-stores update
```