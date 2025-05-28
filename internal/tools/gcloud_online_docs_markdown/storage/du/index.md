# gcloud storage du  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/du](https://cloud.google.com/sdk/gcloud/reference/storage/du)*

**NAME**

: **gcloud storage du - displays the amount of space in bytes used by storage resources**

**SYNOPSIS**

: **`gcloud storage du` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/du#URL)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/du#--additional-headers)`=`HEADER`=`VALUE`] [`[--all-versions](https://cloud.google.com/sdk/gcloud/reference/storage/du#--all-versions)`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/du#-a)`] [`[--exclude-name-pattern](https://cloud.google.com/sdk/gcloud/reference/storage/du#--exclude-name-pattern)`=`EXCLUDE_NAME_PATTERN`, `[-e](https://cloud.google.com/sdk/gcloud/reference/storage/du#-e)` `[EXCLUDE_NAME_PATTERN](https://cloud.google.com/sdk/gcloud/reference/storage/du#EXCLUDE_NAME_PATTERN)`] [`[--exclude-name-pattern-file](https://cloud.google.com/sdk/gcloud/reference/storage/du#--exclude-name-pattern-file)`=`EXCLUDE_NAME_PATTERN_FILE`, `-X` `[EXCLUDE_NAME_PATTERN_FILE](https://cloud.google.com/sdk/gcloud/reference/storage/du#EXCLUDE_NAME_PATTERN_FILE)`] [`[--readable-sizes](https://cloud.google.com/sdk/gcloud/reference/storage/du#--readable-sizes)`, `[-r](https://cloud.google.com/sdk/gcloud/reference/storage/du#-r)`] [`[--summarize](https://cloud.google.com/sdk/gcloud/reference/storage/du#--summarize)`, `[-s](https://cloud.google.com/sdk/gcloud/reference/storage/du#-s)`] [`[--total](https://cloud.google.com/sdk/gcloud/reference/storage/du#--total)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/du#-c)`] [`[--zero-terminator](https://cloud.google.com/sdk/gcloud/reference/storage/du#--zero-terminator)`, `[-0](https://cloud.google.com/sdk/gcloud/reference/storage/du#-0)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/du#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Displays the amount of space in bytes used by the objects in a bucket,
subdirectory, or project. This command calculates the current space usage by
making a series of object listing requests, which can take a long time for large
buckets. If your bucket contains hundreds of thousands of objects, or if you
want to monitor your bucket size over time, use Monitoring instead, as described
in [Get
bucket size](https://cloud.google.com/storage/docs/getting-bucket-size)

**EXAMPLES**

: To list the size of each object in a bucket:

```
gcloud storage du gs://bucketname
```

To list the size of each object in the prefix subdirectory:

```
gcloud storage du gs://bucketname/prefix/*
```

To print the total number of bytes in a bucket in human-readable form:

```
gcloud storage du -c gs://bucketname
```

To see a summary of the total number of bytes in two given buckets:

```
gcloud storage du -s gs://bucket1 gs://bucket2
```

To list the size of each object in a bucket with Object Versioning enabled,
including noncurrent objects:

```
gcloud storage du -a gs://bucketname
```

To list the size of each object in a bucket, except objects that end in ".bak",
with each object printed ending in a null byte:

```
gcloud storage du -e "*.bak" -0 gs://bucketname
```

To list the size of each bucket in a project and the total size of the project:

```
gcloud storage du --summarize --readable-sizes --total
```

**POSITIONAL ARGUMENTS**

: **[`URL` …]**:
The url of objects to list.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--all-versions**:
Includes noncurrent object versions for a bucket with Object Versioning enabled.
Also prints the generation and metageneration number for each listed object.

**--exclude-name-pattern**:
Exclude a pattern from the report. Example: `-e "*.o"` excludes any
object that ends in ".o". Can be specified multiple times.

**--exclude-name-pattern-file**:
Similar to -e, but excludes patterns from the given file. The patterns to
exclude should be listed one per line.

**--readable-sizes**:
Prints object sizes in human-readable format. For example, 1 KiB, 234 MiB, or
2GiB.

**--summarize**:
Displays only the summary for each argument.

**--total**:
Includes a total size of all input sources.

**--zero-terminator**:
Ends each output line with a 0 byte rather than a newline. You can use this to
make the output machine-readable.

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
gcloud alpha storage du
```