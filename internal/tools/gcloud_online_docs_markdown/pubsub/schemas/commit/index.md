# gcloud pubsub schemas commit  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit)*

**NAME**

: **gcloud pubsub schemas commit - commit a Pub/Sub schema revision**

**SYNOPSIS**

: **`gcloud pubsub schemas commit` `[SCHEMA](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit#SCHEMA)` `[--type](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit#--type)`=`TYPE` (`[--definition](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit#--definition)`=`DEFINITION`     | `[--definition-file](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit#--definition-file)`=`PATH_TO_FILE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Commit a Pub/Sub schema revision.

**EXAMPLES**

: To commit a PROTOCOL_BUFFER schema revision called "key-schema" that requires
exactly one-string field named "key", run:

```
gcloud pubsub schemas commit key-schema --definition="syntax = 'proto3'; message Message { optional string key = 1; }" --type=protocol-buffer To commit an equivalent AVRO schema revision, run:
```

```
gcloud pubsub schemas commit key-schema --definition="{ 'type': 'record', 'namespace': 'my.ns', 'name': 'KeyMsg', 'fields': [ { 'name': 'key', 'type': 'string' } ] }" --type=avro
```

**POSITIONAL ARGUMENTS**

: **Schema resource - Name of the schema to revise. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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
The type of the schema.

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

**NOTES**

: These variants are also available:

```
gcloud alpha pubsub schemas commit
```

```
gcloud beta pubsub schemas commit
```