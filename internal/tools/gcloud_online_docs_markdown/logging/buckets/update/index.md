# gcloud logging buckets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update)*

**NAME**

: **gcloud logging buckets update - update a bucket**

**SYNOPSIS**

: **`gcloud logging buckets update` `[BUCKET_ID](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#BUCKET_ID)` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--location)`=`LOCATION` [`[--add-index](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--add-index)`=[`KEY`=`VALUE`, …,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--async)`] [`[--clear-indexes](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--clear-indexes)`] [`[--cmek-kms-key-name](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--cmek-kms-key-name)`=`CMEK_KMS_KEY_NAME`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--description)`=`DESCRIPTION`] [`[--enable-analytics](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--enable-analytics)`] [`[--locked](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--locked)`] [`[--remove-indexes](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--remove-indexes)`=[`FIELD` `[PATH](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#PATH)`,…]] [`[--restricted-fields](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--restricted-fields)`=[`RESTRICTED_FIELD`,…]] [`[--retention-days](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--retention-days)`=`RETENTION_DAYS`] [`[--update-index](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--update-index)`=[`KEY`=`VALUE`, …,…]] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the properties of a bucket.

**EXAMPLES**

: To update a bucket in your project, run:

```
gcloud logging buckets update my-bucket --location=global --description=my-new-description
```

To update a bucket in your project and remove all indexes, run:

```
gcloud logging buckets update my-bucket --location=global --clear-indexes
```

To update a bucket in your project and remove an index, run:

```
gcloud logging buckets update my-bucket --location=global --remove-indexes=jsonPayload.foo2
```

To update a bucket in your project and add an index, run:

```
gcloud logging buckets update my-bucket --location=global --add-index=fieldPath=jsonPayload.foo2,type=INDEX_TYPE_STRING
```

To update a bucket in your project and update an existing index, run:

```
gcloud logging buckets update my-bucket --location=global --update-index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_INTEGER
```

To update a bucket in your project and update existing cmek, run:

```
gcloud logging buckets update my-bucket --location=global --cmek-kms-key-name=CMEK_KEY_NAME
```

To asynchronously enroll a bucket in your project into Log Analytics, run:

```
gcloud logging buckets update my-bucket --location=global --async --enable-analytics
```

**POSITIONAL ARGUMENTS**

: **`BUCKET_ID`**:
The id of the bucket to update.

**REQUIRED FLAGS**

: **--location**:
Location of the bucket.

**OPTIONAL FLAGS**

: **--add-index**:
Add an index to be added to the log bucket. This flag can be repeated. The
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
are strings and integers.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--clear-indexes**:
Remove all logging indexes from the bucket.

**--cmek-kms-key-name**:
A valid `kms_key_name` will enable CMEK for the bucket.

**--description**:
A new description for the bucket.

**--enable-analytics**:
Whether to opt the bucket into Log Analytics. Once opted in, the bucket cannot
be opted out of Log Analytics.

**--locked**:
Lock the bucket and prevent it from being modified or deleted (unless it is
empty).

**--remove-indexes**:
Specify the field path of the logging index(es) to delete.

**--restricted-fields**:
A new set of restricted fields for the bucket.

**--retention-days**:
A new retention period for the bucket.

**--update-index**:
Update an index to be added to the log bucket. This will update the type of the
index, and also update its createTime to the new update time. This flag can be
repeated. The ``fieldPath`` and
``type`` attributes are required. For example:
--index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_STRING. The following keys are
accepted:

**`fieldPath`**:
The LogEntry field path to index. For example: jsonPayload.request.status. Paths
are limited to 800 characters and can include only letters, digits, underscores,
hyphens, and periods.

**`type`**:
The type of data in this index. For example: INDEX_TYPE_STRING Supported types
are strings and integers.

**--billing-account**

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
gcloud alpha logging buckets update
```

```
gcloud beta logging buckets update
```