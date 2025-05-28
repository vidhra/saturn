# gcloud pubsub schemas create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/create](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/create)*

**NAME**

: **gcloud pubsub schemas create - create a Pub/Sub schema**

**SYNOPSIS**

: **`gcloud pubsub schemas create` `[SCHEMA](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/create#SCHEMA)` `[--type](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/create#--type)`=`TYPE` (`[--definition](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/create#--definition)`=`DEFINITION`     | `[--definition-file](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/create#--definition-file)`=`PATH_TO_FILE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Pub/Sub schema.

**EXAMPLES**

: To create a PROTOCOL_BUFFER schema called "key-schema" that requires exactly one
string field named "key", run:
```
gcloud pubsub schemas create key-schema --definition="syntax = 'proto3'; message Message { optional string key = 1; }" --type=PROTOCOL_BUFFER
```

To create an equivalent AVRO schema, run:
```
gcloud pubsub schemas create key-schema --definition='{ "type": "record", "namespace": "my.ns", "name":
 "KeyMsg", "fields": [ { "name": "key", "type": "string" } ] }' \
    --type=AVRO
```

**POSITIONAL ARGUMENTS**

: **Schema resource - Pub/Sub schema to create. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `schema` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SCHEMA`**:
ID of the schema or fully qualified identifier for the schema.
To set the `schema` attribute:

- provide the argument `schema` on the command line.**

**REQUIRED FLAGS**

: **--type**:
Type of the schema. `TYPE` must be one of:
`avro`, `protocol-buffer`.

**--definition**

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

: This command uses the `pubsub/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/pubsub/docs](https://cloud.google.com/pubsub/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha pubsub schemas create
```

```
gcloud beta pubsub schemas create
```