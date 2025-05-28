# gcloud storage cp  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/cp](https://cloud.google.com/sdk/gcloud/reference/storage/cp)*

**NAME**

: **gcloud storage cp - upload, download, and copy Cloud Storage objects**

**SYNOPSIS**

: **`gcloud storage cp` [`[SOURCE](https://cloud.google.com/sdk/gcloud/reference/storage/cp#SOURCE)` …] `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/storage/cp#DESTINATION)` [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--additional-headers)`=`HEADER`=`VALUE`] [`[--all-versions](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--all-versions)`, `-A`] [`[--no-clobber](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--clobber)`, `[-n](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-n)`] [`[--content-md5](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--content-md5)`=`MD5_DIGEST`] [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-c)`] [`[--daisy-chain](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--daisy-chain)`, `-D`] [`[--do-not-decompress](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--do-not-decompress)`] [`[--include-managed-folders](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--include-managed-folders)`] [`[--manifest-path](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--manifest-path)`=`MANIFEST_PATH`, `-L` `[MANIFEST_PATH](https://cloud.google.com/sdk/gcloud/reference/storage/cp#MANIFEST_PATH)`] [`[--preserve-posix](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--preserve-posix)`, `-P`] [`[--print-created-message](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--print-created-message)`, `[-v](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-v)`] [`[--read-paths-from-stdin](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--read-paths-from-stdin)`, `-I`] [`[--recursive](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--recursive)`, `-R`, `[-r](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-r)`] [`[--skip-unsupported](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--skip-unsupported)`, `-U`] [`[--storage-class](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--storage-class)`=`STORAGE_CLASS`, `[-s](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-s)` `[STORAGE_CLASS](https://cloud.google.com/sdk/gcloud/reference/storage/cp#STORAGE_CLASS)`] [`[--canned-acl](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--canned-acl)`=`PREDEFINED_ACL`, `[--predefined-acl](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--predefined-acl)`=`PREDEFINED_ACL`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-a)` `[PREDEFINED_ACL](https://cloud.google.com/sdk/gcloud/reference/storage/cp#PREDEFINED_ACL)` `[--[no-]preserve-acl](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--[no-]preserve-acl)`, `[-p](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-p)`] [`[--gzip-in-flight](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--gzip-in-flight)`=[`FILE_EXTENSIONS`,…], `[-j](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-j)` [`[FILE_EXTENSIONS](https://cloud.google.com/sdk/gcloud/reference/storage/cp#FILE_EXTENSIONS)`,…]     | `[--gzip-in-flight-all](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--gzip-in-flight-all)`, `-J`     | `[--gzip-local](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--gzip-local)`=[`FILE_EXTENSIONS`,…], `[-z](https://cloud.google.com/sdk/gcloud/reference/storage/cp#-z)` [`[FILE_EXTENSIONS](https://cloud.google.com/sdk/gcloud/reference/storage/cp#FILE_EXTENSIONS)`,…]     | `[--gzip-local-all](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--gzip-local-all)`, `-Z`] [`[--ignore-symlinks](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--ignore-symlinks)`     | `[--preserve-symlinks](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--preserve-symlinks)`] [`[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--decryption-keys)`=[`DECRYPTION_KEY`,…] `[--encryption-key](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--encryption-key)`=`ENCRYPTION_KEY`] [`[--cache-control](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--cache-control)`=`CACHE_CONTROL` `[--content-disposition](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--content-disposition)`=`CONTENT_DISPOSITION` `[--content-encoding](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--content-encoding)`=`CONTENT_ENCODING` `[--content-language](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--content-language)`=`CONTENT_LANGUAGE` `[--content-type](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--content-type)`=`CONTENT_TYPE` `[--custom-time](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--custom-time)`=`CUSTOM_TIME` `[--clear-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--clear-custom-metadata)`     | `[--custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--custom-metadata)`=[`CUSTOM_METADATA_KEYS_AND_VALUES`,…]     | `[--remove-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--remove-custom-metadata)`=[`METADATA_KEYS`,…] `[--update-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--update-custom-metadata)`=[`CUSTOM_METADATA_KEYS_AND_VALUES`,…]] [`[--if-generation-match](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--if-generation-match)`=`GENERATION` `[--if-metageneration-match](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--if-metageneration-match)`=`METAGENERATION`] [`[--retain-until](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--retain-until)`=`DATETIME` `[--retention-mode](https://cloud.google.com/sdk/gcloud/reference/storage/cp#--retention-mode)`=`RETENTION_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/cp#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Copy data between your local file system and the cloud, within the cloud, and
between cloud storage providers.

**EXAMPLES**

: The following command uploads all text files from the local directory to a
bucket:

```
gcloud storage cp *.txt gs://my-bucket
```

The following command downloads all text files from a bucket to your current
directory:

```
gcloud storage cp gs://my-bucket/*.txt .
```

The following command transfers all text files from a bucket to a different
cloud storage provider:

```
gcloud storage cp gs://my-bucket/*.txt s3://my-bucket
```

Use the `--recursive` option to copy an entire directory tree. The
following command uploads the directory tree
``dir``:

```
gcloud storage cp --recursive dir gs://my-bucket
```

Recursive listings are similar to adding `**` to a query, except
`**` matches only cloud objects and will not match prefixes. For
example, the following would not match
``gs://my-bucket/dir/log.txt``

```
gcloud storage cp gs://my-bucket/**/dir dir
```

`**` retrieves a flat list of objects in a single API call. However,
`**` matches folders for non-cloud queries. For example, a folder
``dir`` would be copied in the following.

```
gcloud storage cp ~/Downloads/**/dir gs://my-bucket
```

**POSITIONAL ARGUMENTS**

: **[`SOURCE` …]**:
The source path(s) to copy.

**`DESTINATION`**:
The destination path.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--all-versions**:
Copy all source versions from a source bucket or folder. If not set, only the
live version of each source object is copied.
Note: This option is only useful when the destination bucket has Object
Versioning enabled. Additionally, the generation numbers of copied versions do
not necessarily match the order of the original generation numbers.

**--no-clobber**:
Do not overwrite existing files or objects at the destination. Skipped items
will be printed. This option may perform an additional GET request for cloud
objects before attempting an upload.

**--content-md5**:
Manually specified MD5 hash digest for the contents of an uploaded file. This
flag cannot be used when uploading multiple files. The custom digest is used by
the cloud provider for validation.

**--continue-on-error**:
If any operations are unsuccessful, the command will exit with a non-zero exit
status after completing the remaining operations. This flag takes effect only in
sequential execution mode (i.e. processor and thread count are set to 1).
Parallelism is default.

**--daisy-chain**:
Copy in "daisy chain" mode, which means copying an object by first downloading
it to the machine where the command is run, then uploading it to the destination
bucket. The default mode is a "copy in the cloud," where data is copied without
uploading or downloading. During a copy in the cloud, a source composite object
remains composite at its destination. However, you can use daisy chain mode to
change a composite object into a non-composite object. Note: Daisy chain mode is
automatically used when copying between providers.

**--do-not-decompress**:
Do not automatically decompress downloaded gzip files.

**--include-managed-folders**:
Includes managed folders in command operations. For transfers, gcloud storage
will set up managed folders in the destination with the same IAM policy bindings
as the source. Managed folders are only included with recursive cloud-to-cloud
transfers. Please note that for hierarchical namespace buckets, managed folders
are always included. Hence this flag would not be applicable to hierarchical
namespace buckets.

**--manifest-path**:
Outputs a manifest log file with detailed information about each item that was
copied. This manifest contains the following information for each item:

- Source path.
- Destination path.
- Source size.
- Bytes transferred.
- MD5 hash.
- Transfer start time and date in UTC and ISO 8601 format.
- Transfer completion time and date in UTC and ISO 8601 format.
- Final result of the attempted transfer: OK, error, or skipped.
- Details, if any.

If the manifest file already exists, gcloud storage appends log items to the
existing file.
Objects that are marked as "OK" or "skipped" in the existing manifest file are
not retried by future commands. Objects marked as "error" are retried.

**--preserve-posix**:
Causes POSIX attributes to be preserved when objects are copied. With this
feature enabled, gcloud storage will copy several fields provided by the stat
command: access time, modification time, owner UID, owner group GID, and the
mode (permissions) of the file.
For uploads, these attributes are read off of local files and stored in the
cloud as custom metadata. For downloads, custom cloud metadata is set as POSIX
attributes on files after they are downloaded.
On Windows, this flag will only set and restore access time and modification
time because Windows doesn't have a notion of POSIX UID, GID, and mode.

**--print-created-message**:
Prints the version-specific URL for each copied object.

**--read-paths-from-stdin**:
Read the list of resources to copy from stdin. No need to enter a source
argument if this flag is present. Example: "storage cp -I
gs://bucket/destination" Note: To copy the contents of one file directly from
stdin, use "-" as the source argument without the "-I" flag.

**--recursive**:
Recursively copy the contents of any directories that match the source path
expression.

**--skip-unsupported**:
Skip objects with unsupported object types.

**--storage-class**:
Specify the storage class of the destination object. If not specified, the
default storage class of the destination bucket is used. This option is not
valid for copying to non-cloud destinations.

**--canned-acl**:
Applies predefined, or "canned," ACLs to a resource. See docs for a list of
predefined ACL constants: [https://cloud.google.com/storage/docs/access-control/lists#predefined-acl](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl)

**--[no-]preserve-acl**:
Preserves ACLs when copying in the cloud. This option is Cloud Storage-only, and
you need OWNER access to all copied objects. If all objects in the destination
bucket should have the same ACL, you can also set a default object ACL on that
bucket instead of using this flag. Preserving ACLs is the default behavior for
updating existing objects. Use `--preserve-acl` to enable and
`--no-preserve-acl` to disable.

**--gzip-in-flight**

**--ignore-symlinks**

**ENCRYPTION FLAGS**

: **--decryption-keys**:
A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4
base64-encoded AES256 strings) that will be used to decrypt Cloud Storage
objects. Data encrypted with a customer-managed encryption key (CMEK) is
decrypted automatically, so CMEKs do not need to be listed here.

**--encryption-key**:
The encryption key to use for encrypting target objects. The specified
encryption key can be a customer-supplied encryption key (An RFC 4648 section 4
base64-encoded AES256 string), or a customer-managed encryption key of the form
`projects/{project}/locations/{location}/keyRings/{key-ring}/cryptoKeys/{crypto-key}`.
The specified key also acts as a decryption key, which is useful when copying or
moving encrypted data to a new location. Using this flag in an `objects
update` command triggers a rewrite of target objects.

**OBJECT METADATA FLAGS**

: **--cache-control**:
How caches should handle requests and responses.

**--content-disposition**:
How content should be displayed.

**--content-encoding**:
How content is encoded (e.g. ``gzip``).

**--content-language**:
Content's language (e.g. ``en`` signifies
"English").

**--content-type**:
Type of data contained in the object (e.g.
``text/html``).

**--custom-time**:
Custom time for Cloud Storage objects in RFC 3339 format.

**--clear-custom-metadata**

**PRECONDITION FLAGS**

: **--if-generation-match**:
Execute only if the generation matches the generation of the requested object.

**--if-metageneration-match**:
Execute only if the metageneration matches the metageneration of the requested
object.

**RETENTION FLAGS**

: **--retain-until**:
Ensures the destination object is retained until the specified time in RFC 3339
format.

**--retention-mode**:
Sets the destination object retention mode to either "Locked" or "Unlocked".
When retention mode is "Locked", the retain until time can only be increased.
`RETENTION_MODE` must be one of: `Locked`,
`Unlocked`.

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
gcloud alpha storage cp
```