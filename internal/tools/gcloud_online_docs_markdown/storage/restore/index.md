# gcloud storage restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/restore](https://cloud.google.com/sdk/gcloud/reference/storage/restore)*

**NAME**

: **gcloud storage restore - restore one or more soft-deleted objects**

**SYNOPSIS**

: **`gcloud storage restore` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/restore#URLS)` …] [`[--all-versions](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--all-versions)`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/restore#-a)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--async)`] [`[--[no-]preserve-acl](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--[no-]preserve-acl)`, `[-p](https://cloud.google.com/sdk/gcloud/reference/storage/restore#-p)`] [`[--read-paths-from-stdin](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--read-paths-from-stdin)`, `-I`] [`[--allow-overwrite](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--allow-overwrite)` `[--deleted-after-time](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--deleted-after-time)`=`DELETED_AFTER_TIME` `[--deleted-before-time](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--deleted-before-time)`=`DELETED_BEFORE_TIME`] [`[--if-generation-match](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--if-generation-match)`=`GENERATION` `[--if-metageneration-match](https://cloud.google.com/sdk/gcloud/reference/storage/restore#--if-metageneration-match)`=`METAGENERATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The restore command restores soft-deleted resources:

```
gcloud storage restore url…
```

**EXAMPLES**

: Restore soft-deleted version of bucket with generations:

```
gcloud storage restore gs://bucket#123
```

Restore several soft-deleted buckets with generations:

```
gcloud storage restore gs://bucket1#123 gs://bucket2#456
```

Restore latest soft-deleted version of object in a bucket.

```
gcloud storage restore gs://bucket/file1.txt
```

Restore a specific soft-deleted version of object in a bucket by specifying the
generation.

```
gcloud storage restore gs://bucket/file1.txt#123
```

Restore all soft-deleted versions of object in a bucket.

```
gcloud storage restore gs://bucket/file1.txt --all-versions
```

Restore several objects in a bucket (with or without generation):

```
gcloud storage restore gs://bucket/file1.txt gs://bucket/file2.txt#456
```

Restore the latest soft-deleted version of all text objects in a bucket:

```
gcloud storage restore gs://bucket/**.txt
```

Restore a list of objects read from stdin (with or without generation):

```
cat list-of-files.txt | gcloud storage restore --read-paths-from-stdin
```

Restore object with its original ACL policy:

```
gcloud storage restore gs://bucket/file1.txt --preserve-acl
```

Restore all objects in a bucket asynchronously:

```
gcloud storage restore gs://bucket/** --async
```

Restore all text files in a bucket asynchronously:

```
gcloud storage restore gs://bucket/**.txt --async
```

**POSITIONAL ARGUMENTS**

: **[`URLS` …]**:
The url of objects to list.

**FLAGS**

: **--all-versions**

**--async**:
Initiates an asynchronous bulk restore operation on the specified bucket.

**--[no-]preserve-acl**:
Preserves ACLs when copying in the cloud. This option is Cloud Storage-only, and
you need OWNER access to all copied objects. If all objects in the destination
bucket should have the same ACL, you can also set a default object ACL on that
bucket instead of using this flag. Preserving ACLs is the default behavior for
updating existing objects. Use `--preserve-acl` to enable and
`--no-preserve-acl` to disable.

**--read-paths-from-stdin**:
Read the list of URLs from stdin.

**--allow-overwrite**

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
gcloud alpha storage restore
```