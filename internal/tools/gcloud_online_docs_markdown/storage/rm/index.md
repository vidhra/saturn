# gcloud storage rm  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/rm](https://cloud.google.com/sdk/gcloud/reference/storage/rm)*

**NAME**

: **gcloud storage rm - delete objects and buckets**

**SYNOPSIS**

: **`gcloud storage rm` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/rm#URLS)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/rm#--additional-headers)`=`HEADER`=`VALUE`] [`[--all-versions](https://cloud.google.com/sdk/gcloud/reference/storage/rm#--all-versions)`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/rm#-a)`] [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/rm#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/rm#-c)`] [`[--exclude-managed-folders](https://cloud.google.com/sdk/gcloud/reference/storage/rm#--exclude-managed-folders)`] [`[--read-paths-from-stdin](https://cloud.google.com/sdk/gcloud/reference/storage/rm#--read-paths-from-stdin)`, `-I`] [`[--recursive](https://cloud.google.com/sdk/gcloud/reference/storage/rm#--recursive)`, `-R`, `[-r](https://cloud.google.com/sdk/gcloud/reference/storage/rm#-r)`] [`[--if-generation-match](https://cloud.google.com/sdk/gcloud/reference/storage/rm#--if-generation-match)`=`GENERATION` `[--if-metageneration-match](https://cloud.google.com/sdk/gcloud/reference/storage/rm#--if-metageneration-match)`=`METAGENERATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/rm#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete objects and buckets.

**EXAMPLES**

: The following command deletes a Cloud Storage object named
``my-object`` from the bucket
``my-bucket``:

```
gcloud storage rm gs://my-bucket/my-object
```

The following command deletes all objects directly within the directory
``my-dir`` but no objects within
subdirectories:

```
gcloud storage rm gs://my-bucket/my-dir/*
```

The following command deletes all objects and subdirectories within the
directory ``my-dir``:

```
gcloud storage rm gs://my-bucket/my-dir/**
```

Note that for buckets that contain [versioned
objects](https://cloud.google.com/storage/docs/object-versioning), the above command only affects live versions. Use the
`--recursive` flag instead to delete all versions.
The following command deletes all versions of all resources in
``my-bucket`` and then deletes the bucket.

```
gcloud storage rm --recursive gs://my-bucket/
```

The following command deletes all text files in the top-level of
``my-bucket``, but not text files in
subdirectories:

```
gcloud storage rm -recursive gs://my-bucket/*.txt
```

The following command deletes one wildcard expression per line passed in by
stdin:

```
some_program | gcloud storage rm -I
```

**POSITIONAL ARGUMENTS**

: **[`URLS` …]**:
The URLs of the resources to delete.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--all-versions**:
Delete all [versions](https://cloud.google.com/storage/docs/object-versioning) of
an object.

**--continue-on-error**:
If any operations are unsuccessful, the command will exit with a non-zero exit
status after completing the remaining operations. This flag takes effect only in
sequential execution mode (i.e. processor and thread count are set to 1).
Parallelism is default.

**--exclude-managed-folders**:
Excludes managed folders from command operations. By default gcloud storage
includes managed folders in recursive removals. Please note that this flag would
not be applicable for hierarchical namespace buckets as we always list managed
folders for these buckets.

**--read-paths-from-stdin**:
Read the list of URLs from stdin.

**--recursive**:
Recursively delete the contents of buckets or directories that match the path
expression. By default, this will delete managed folders as well. If the path is
set to a bucket, like ``gs://bucket``, the
bucket is also deleted. This option implies the `--all-versions`
option. If you want to delete only live object versions, use the
``**´´ wildcard instead.

**PRECONDITION FLAGS**

: **--if-generation-match**:
Execute only if the generation matches the generation of the requested object.

**--if-metageneration-match**:
Execute only if the metageneration matches the metageneration of the requested
object.

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
gcloud alpha storage rm
```