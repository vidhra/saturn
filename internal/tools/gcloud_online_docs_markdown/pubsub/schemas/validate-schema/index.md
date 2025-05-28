# gcloud pubsub schemas validate-schema  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema)*

**NAME**

: **gcloud pubsub schemas validate-schema - validate a Pub/Sub schema**

**SYNOPSIS**

: **`gcloud pubsub schemas validate-schema` `[--type](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema#--type)`=`TYPE` (`[--definition](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema#--definition)`=`DEFINITION`     | `[--definition-file](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema#--definition-file)`=`PATH_TO_FILE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Validate a new Pub/Sub schema.

**EXAMPLES**

: To validate a PROTOCOL_BUFFER schema, run:

```
gcloud pubsub schemas validate-schema --definition="syntax = 'proto3'; message Message { optional string key = 1; }" --type=PROTOCOL_BUFFER
```

To validate an equivalent AVRO schema, run:

```
gcloud pubsub schemas validate-schema --definition='{ "type": "record", "namespace": "my.ns", "name":
 "KeyMsg", "fields": [ { "name": "key", "type": "string" } ] }' \
    --type=AVRO
```

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
gcloud alpha pubsub schemas validate-schema
```

```
gcloud beta pubsub schemas validate-schema
```