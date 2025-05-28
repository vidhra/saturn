# gcloud logging buckets create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create)*

**NAME**

: **gcloud logging buckets create - create a bucket**

**SYNOPSIS**

: **`gcloud logging buckets create` `[BUCKET_ID](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#BUCKET_ID)` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#--location)`=`LOCATION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#--async)`] [`[--cmek-kms-key-name](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#--cmek-kms-key-name)`=`CMEK_KMS_KEY_NAME`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#--description)`=`DESCRIPTION`] [`[--enable-analytics](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#--enable-analytics)`] [`[--index](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#--index)`=[`KEY`=`VALUE`, …,…]] [`[--restricted-fields](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#--restricted-fields)`=[`RESTRICTED_FIELD`,…]] [`[--retention-days](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#--retention-days)`=`RETENTION_DAYS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: After creating a bucket, use a log sink to route logs into the bucket.

**EXAMPLES**

: To create a bucket 'my-bucket' in location 'global', run:

```
gcloud logging buckets create my-bucket --location=global --description="my custom bucket"
```

To create a bucket with extended retention, run:

```
gcloud logging buckets create my-bucket --location=global --retention-days=365
```

To create a bucket in cloud region 'us-central1', run:

```
gcloud logging buckets create my-bucket --location=us-central1
```

To create a bucket with custom index of 'jsonPayload.foo', run:

```
gcloud logging buckets create my-bucket --index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_STRING
```

To create a bucket with custom CMEK, run:

```
gcloud logging buckets create my-bucket --location=us-central1 --cmek-kms-key-name=CMEK_KMS_KEY_NAME
```

To asynchronously create a bucket enrolled into Log Analytics, run:

```
gcloud logging buckets create my-bucket --location=global --async --enable-analytics
```

**POSITIONAL ARGUMENTS**

: **`BUCKET_ID`**:
ID of the bucket to create.

**REQUIRED FLAGS**

: **--location**:
Location in which to create the bucket. Once the bucket is created, the location
cannot be changed.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cmek-kms-key-name**:
A valid `kms_key_name` will enable CMEK for the bucket.

**--description**:
A textual description for the bucket.

**--enable-analytics**:
Whether to opt the bucket into Log Analytics. Once opted in, the bucket cannot
be opted out of Log Analytics.

**--index**:
Specify an index to be added to the log bucket. This flag can be repeated. The
``fieldPath`` and
``type`` attributes are required. For example:
--index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_STRING. The following keys are
accepted:

**`fieldPath`**:
The LogEntry field path to index. For example: jsonPayload.request.status. Paths
are limited to 800 characters and can include only letters, digits, underscores,
hyphens, and periods.

**`type`**:
The type of data in this index. For example: INDEX_TYPE_STRING Supported types
are INDEX_TYPE_STRING and INDEX_TYPE_INTEGER.

**--restricted-fields**:
Comma-separated list of field paths that require permission checks in this
bucket. The following fields and their children are eligible: textPayload,
jsonPayload, protoPayload, httpRequest, labels, sourceLocation.

**--retention-days**:
The period logs will be retained, after which logs will automatically be
deleted. The default is 30 days.

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
gcloud alpha logging buckets create
```

```
gcloud beta logging buckets create
```