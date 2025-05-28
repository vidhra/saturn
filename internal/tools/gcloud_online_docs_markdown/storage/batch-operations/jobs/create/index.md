# gcloud storage batch-operations jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create)*

**NAME**

: **gcloud storage batch-operations jobs create - create a new batch operation job**

**SYNOPSIS**

: **`gcloud storage batch-operations jobs create` `[BATCH_JOB](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#BATCH_JOB)` `[--bucket](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--bucket)`=`BUCKET` (`[--included-object-prefixes](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--included-object-prefixes)`=[`PREFIXES`,…]     | `[--manifest-location](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--manifest-location)`=`MANIFEST_LOCATION`) (`[--put-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--put-metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#KEY)`=`VALUE`,…]     | `[--rewrite-object](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--rewrite-object)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#KEY)`=`VALUE`,…]     | [`[--delete-object](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--delete-object)` : `[--enable-permanent-object-deletion](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--enable-permanent-object-deletion)`]     | `[--[no-]put-object-event-based-hold](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--[no-]put-object-event-based-hold)` `[--[no-]put-object-temporary-hold](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--[no-]put-object-temporary-hold)`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--description)`=`DESCRIPTION`] [`[--log-actions](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--log-actions)`=[`LOG_ACTIONS`,…] `[--log-action-states](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#--log-action-states)`=[`LOG_ACTION_STATES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a batch operation job, allowing you to perform operations such as
deletion, updating metadata, and more on objects in a serverless manner.

**EXAMPLES**

: To create a batch job with the name `my-job` to perform object
deletion on bucket `my-bucket` and the manifest file
`gs://my-bucket/manifest.csv` specifies the objects to be
transformed:

```
gcloud storage batch-operations jobs create my-job --bucket=my-bucket --manifest-location=gs://my-bucket/manifest.csv --delete-object
```

To create a batch job with the name `my-job` to update object
metadata `Content-Disposition` to `inline` and
`Content-Language` to `en` on bucket
`my-bucket` where you want to match objects with the prefix
`prefix1` or `prefix2`:

```
gcloud storage batch-operations jobs create my-job --bucket=my-bucket --included-object-prefixes=prefix1,prefix2 --put-metadata=Content-Disposition=inline,Content-Language=en
```

To create a batch job with the name `my-job` to put object event
based hold on objects in bucket `my-bucket` with logging config
enabled for corresponding transform action and succeeded and failed action
states:

```
gcloud storage batch-operations jobs create my-job --bucket=my-bucket --put-object-event-based-hold --put-metadata=Content-Disposition=inline,Content-Language=en --log-actions=transform --log-action-states=succeeded,failed
```

**POSITIONAL ARGUMENTS**

: **Batch job resource - The batch job to create. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `batch_job` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `batch_job` on the command line with a fully
specified name;
- The default is `global`.

This must be specified.

**`BATCH_JOB`**:
ID of the batch-job or fully qualified identifier for the batch-job.
To set the `batch-job` attribute:

- provide the argument `batch_job` on the command line.**

**REQUIRED FLAGS**

: **--bucket**:
Bucket containing the objects that the batch job will operate on.

**--manifest-location=``MANIFEST_LOCATION**

**--put-metadata**

**FLAGS**

: **--description**:
Description for the batch job.

**LOGGING_CONFIG FLAGS**

: **--log-actions**

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

: This variant is also available:

```
gcloud alpha storage batch-operations jobs create
```