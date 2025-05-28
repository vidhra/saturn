# gcloud healthcare fhir-stores create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create)*

**NAME**

: **gcloud healthcare fhir-stores create - create a Cloud Healthcare API FHIR store**

**SYNOPSIS**

: **`gcloud healthcare fhir-stores create` (`[FHIR_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#FHIR_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#--location)`=`LOCATION`) `[--version](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#--version)`=`VERSION` [`[--disable-referential-integrity](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#--disable-referential-integrity)`] [`[--disable-resource-versioning](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#--disable-resource-versioning)`] [`[--enable-update-create](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#--enable-update-create)`] [`[--pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#--pubsub-topic)`=`PUBSUB_TOPIC`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a Cloud Healthcare API FHIR store.

**EXAMPLES**

: To create a FHIR store called 'test-fhir-store', run:

```
gcloud healthcare fhir-stores create test-fhir-store --dataset=test-dataset --version=r4
```

To create a fhir store with the Cloud Pub/Sub topic 'test-pubsub-topic', run:

```
gcloud healthcare fhir-stores create test-fhir-store --dataset=test-dataset --version=r4 --pubsub-topic=projects/my-project/topics/test-pubsub-topic
```

**POSITIONAL ARGUMENTS**

: **FhirStore resource - Cloud Healthcare API FHIR store to create. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--version**:
The FHIR specification version that this FHIR store supports natively. This
field is immutable after store creation. Requests are rejected if they contain
FHIR resources of a different version. An empty value is treated as STU3.
`VERSION` must be one of:

**`dstu2`**:
Draft Standard for Trial Use, [Release
2](https://www.hl7.org/fhir/DSTU2)

**`r4`**:
[Release 4](https://www.hl7.org/fhir/R4)

**`stu3`**:
Standard for Trial Use, [Release 3](https://www.hl7.org/fhir/STU3)

**OPTIONAL FLAGS**

: **--disable-referential-integrity**:
Whether to disable referential integrity in this FHIR store. Default value is
false, meaning that the API will enforce referential integrity and fail the
requests that will result in inconsistent state in the FHIR store. When this
field is set to true, the API will skip referential integrity check. This field
is immutable after store creation.

**--disable-resource-versioning**:
Whether to disable resource versioning for this FHIR store. If set to false,
which is the default behavior, all write operations will cause historical
versions to be recorded automatically. Historical versions can be fetched
through the history APIs, but cannot be updated. This field is immutable after
store creation.

**--enable-update-create**:
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
gcloud alpha healthcare fhir-stores create
```

```
gcloud beta healthcare fhir-stores create
```