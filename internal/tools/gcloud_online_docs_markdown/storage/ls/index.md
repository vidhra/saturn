# gcloud storage ls  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/ls](https://cloud.google.com/sdk/gcloud/reference/storage/ls)*

**NAME**

: **gcloud storage ls - list Cloud Storage buckets and objects**

**SYNOPSIS**

: **`gcloud storage ls` [`[PATH](https://cloud.google.com/sdk/gcloud/reference/storage/ls#PATH)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--additional-headers)`=`HEADER`=`VALUE`] [`[--all-versions](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--all-versions)`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/ls#-a)`] [`[--buckets](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--buckets)`, `[-b](https://cloud.google.com/sdk/gcloud/reference/storage/ls#-b)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--etag)`, `[-e](https://cloud.google.com/sdk/gcloud/reference/storage/ls#-e)`] [`[--exhaustive](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--exhaustive)`] [`[--fetch-encrypted-object-hashes](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--fetch-encrypted-object-hashes)`] [`[--format](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--format)`=`FORMAT`] [`[--next-page-token](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--next-page-token)`=`NEXT_PAGE_TOKEN`] [`[--read-paths-from-stdin](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--read-paths-from-stdin)`, `-I`] [`[--readable-sizes](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--readable-sizes)`] [`[--recursive](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--recursive)`, `-R`, `[-r](https://cloud.google.com/sdk/gcloud/reference/storage/ls#-r)`] [`[--soft-deleted](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--soft-deleted)`] [`[--full](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--full)`, `-L`     | `[--json](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--json)`, `[-j](https://cloud.google.com/sdk/gcloud/reference/storage/ls#-j)`     | `[--long](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--long)`, `[-l](https://cloud.google.com/sdk/gcloud/reference/storage/ls#-l)`] [`[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/ls#--decryption-keys)`=[`DECRYPTION_KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/ls#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List your Cloud Storage buckets in a project and objects in a bucket. This
command treats forward slashes in object names as directories. See below for
examples of how to use wildcards to get the listing behavior you want.

**EXAMPLES**

: The following command lists the buckets in the default project:

```
gcloud storage ls
```

The following command lists the buckets in the specified project:

```
gcloud storage ls --project=my-project
```

The following command lists the contents of a bucket:

```
gcloud storage ls gs://my-bucket
```

You can use [wildcards](https://cloud.google.com/storage/docs/wildcards) to match
multiple paths (including multiple buckets). Bucket wildcards are expanded to
match only buckets contained in your current project. The following command
matches ``.txt`` objects that begin with
``log`` and that are stored in buckets in your
project that begin with ``my-b``:

```
gcloud storage ls gs://my-b*/log*.txt
```

You can use double-star wildcards to match zero or more directory levels in a
path. The following command matches all
``.txt`` objects in a bucket.

```
gcloud storage ls gs://my-bucket/**/*.txt
```

The wildcard `**` retrieves a flat list of objects in a single API
call and does not match prefixes. The following command would not match
`gs://my-bucket/dir/log.txt`:

```
gcloud storage ls gs://my-bucket/**/dir
```

Double-star expansion also can not be combined with other expressions in a given
path segment and operates as a single star in that context. For example, the
command `gs://my-bucket/dir**/log.txt` is treated as
`gs://my-bucket/dir*/log.txt`. To get the recursive behavior, the
command should instead be written the following way:

```
gs://my-bucket/dir*/**/log.txt
```

The following command lists all items recursively with formatting by using
`--recursive`:

```
gcloud storage ls --recursive gs://bucket
```

Recursive listings are similar to `**` except recursive listings
include line breaks and header formatting for each subdirectory.

**POSITIONAL ARGUMENTS**

: **[`PATH` …]**:
The path of objects and directories to list. The path must begin with gs:// and
is allowed to contain wildcard characters.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--all-versions**:
Include noncurrent object versions in the listing. This flag is typically only
useful for buckets with [object
versioning](https://cloud.google.com/storage/docs/object-versioning) enabled. If combined with the `--long` option, the
metageneration for each listed object is also included.

**--buckets**:
When given a bucket URL, only return buckets. Useful for avoiding the rule that
prints the top-level objects of buckets matching a query. Typically used in
combination with `--full` to get the full metadata of buckets.

**--etag**:
Include ETag metadata in listings that use the `--long` flag.

**--exhaustive**:
For features like soft delete, the API may return an empty list. If present,
continue querying. This may incur costs from repeated LIST calls and may not
return any additional objects.

**--fetch-encrypted-object-hashes**:
API requests to the LIST endpoint do not fetch the hashes for encrypted objects
by default. If this flag is set, a GET request is sent for each encrypted object
in order to fetch hashes. This can significantly increase the cost of the
command.

**--format**:
Use "gsutil" to get the style of the older gsutil CLI. (e.g. "--format=gsutil").
Other format values (e.g. "json") do not work. See different ls flags and
commands for alternative formatting.

**--next-page-token**:
Page token for resuming LIST calls.

**--read-paths-from-stdin**:
Read the list of URLs from stdin.

**--readable-sizes**:
When used with `--long`, print object sizes in human readable format,
such as 1 KiB, 234 MiB, or 2 GiB.

**--recursive**:
Recursively list the contents of any directories that match the path expression.

**--soft-deleted**:
Displays soft-deleted resources only. For objects, it will exclude live and
noncurrent ones.

**--full**

**ENCRYPTION FLAGS**

: **--decryption-keys**:
A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4
base64-encoded AES256 strings) that will be used to decrypt Cloud Storage
objects. Data encrypted with a customer-managed encryption key (CMEK) is
decrypted automatically, so CMEKs do not need to be listed here.

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
gcloud alpha storage ls
```