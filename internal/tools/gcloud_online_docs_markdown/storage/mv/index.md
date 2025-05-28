# gcloud storage mv  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/mv](https://cloud.google.com/sdk/gcloud/reference/storage/mv)*

**NAME**

: **gcloud storage mv - moves or renames objects**

**SYNOPSIS**

: **`gcloud storage mv` [`[SOURCE](https://cloud.google.com/sdk/gcloud/reference/storage/mv#SOURCE)` …] `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/storage/mv#DESTINATION)` [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--additional-headers)`=`HEADER`=`VALUE`] [`[--all-versions](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--all-versions)`, `-A`] [`[--no-clobber](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--clobber)`, `[-n](https://cloud.google.com/sdk/gcloud/reference/storage/mv#-n)`] [`[--content-md5](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--content-md5)`=`MD5_DIGEST`] [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/mv#-c)`] [`[--daisy-chain](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--daisy-chain)`, `-D`] [`[--do-not-decompress](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--do-not-decompress)`] [`[--include-managed-folders](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--include-managed-folders)`] [`[--manifest-path](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--manifest-path)`=`MANIFEST_PATH`, `-L` `[MANIFEST_PATH](https://cloud.google.com/sdk/gcloud/reference/storage/mv#MANIFEST_PATH)`] [`[--preserve-posix](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--preserve-posix)`, `-P`] [`[--print-created-message](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--print-created-message)`, `[-v](https://cloud.google.com/sdk/gcloud/reference/storage/mv#-v)`] [`[--read-paths-from-stdin](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--read-paths-from-stdin)`, `-I`] [`[--skip-unsupported](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--skip-unsupported)`, `-U`] [`[--storage-class](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--storage-class)`=`STORAGE_CLASS`, `[-s](https://cloud.google.com/sdk/gcloud/reference/storage/mv#-s)` `[STORAGE_CLASS](https://cloud.google.com/sdk/gcloud/reference/storage/mv#STORAGE_CLASS)`] [`[--canned-acl](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--canned-acl)`=`PREDEFINED_ACL`, `[--predefined-acl](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--predefined-acl)`=`PREDEFINED_ACL`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/mv#-a)` `[PREDEFINED_ACL](https://cloud.google.com/sdk/gcloud/reference/storage/mv#PREDEFINED_ACL)` `[--[no-]preserve-acl](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--[no-]preserve-acl)`, `[-p](https://cloud.google.com/sdk/gcloud/reference/storage/mv#-p)`] [`[--gzip-in-flight](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--gzip-in-flight)`=[`FILE_EXTENSIONS`,…], `[-j](https://cloud.google.com/sdk/gcloud/reference/storage/mv#-j)` [`[FILE_EXTENSIONS](https://cloud.google.com/sdk/gcloud/reference/storage/mv#FILE_EXTENSIONS)`,…]     | `[--gzip-in-flight-all](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--gzip-in-flight-all)`, `-J`     | `[--gzip-local](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--gzip-local)`=[`FILE_EXTENSIONS`,…], `[-z](https://cloud.google.com/sdk/gcloud/reference/storage/mv#-z)` [`[FILE_EXTENSIONS](https://cloud.google.com/sdk/gcloud/reference/storage/mv#FILE_EXTENSIONS)`,…]     | `[--gzip-local-all](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--gzip-local-all)`, `-Z`] [`[--ignore-symlinks](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--ignore-symlinks)`     | `[--preserve-symlinks](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--preserve-symlinks)`] [`[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--decryption-keys)`=[`DECRYPTION_KEY`,…] `[--encryption-key](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--encryption-key)`=`ENCRYPTION_KEY`] [`[--cache-control](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--cache-control)`=`CACHE_CONTROL` `[--content-disposition](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--content-disposition)`=`CONTENT_DISPOSITION` `[--content-encoding](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--content-encoding)`=`CONTENT_ENCODING` `[--content-language](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--content-language)`=`CONTENT_LANGUAGE` `[--content-type](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--content-type)`=`CONTENT_TYPE` `[--custom-time](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--custom-time)`=`CUSTOM_TIME` `[--clear-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--clear-custom-metadata)`     | `[--custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--custom-metadata)`=[`CUSTOM_METADATA_KEYS_AND_VALUES`,…]     | `[--remove-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--remove-custom-metadata)`=[`METADATA_KEYS`,…] `[--update-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--update-custom-metadata)`=[`CUSTOM_METADATA_KEYS_AND_VALUES`,…]] [`[--if-generation-match](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--if-generation-match)`=`GENERATION` `[--if-metageneration-match](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--if-metageneration-match)`=`METAGENERATION`] [`[--retain-until](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--retain-until)`=`DATETIME` `[--retention-mode](https://cloud.google.com/sdk/gcloud/reference/storage/mv#--retention-mode)`=`RETENTION_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/mv#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The mv command allows you to move data between your local file system and the
cloud, move data within the cloud, and move data between cloud storage
providers.
`Renaming Groups Of Objects`
You can use the mv command to rename all objects with a given prefix to have a
new prefix. For example, the following command renames all objects under
gs://my_bucket/oldprefix to be under gs://my_bucket/newprefix, otherwise
preserving the naming structure:

```
gcloud storage mv gs://my_bucket/oldprefix gs://my_bucket/newprefix
```

Note that when using mv to rename groups of objects with a common prefix, you
cannot specify the source URL using wildcards; you must spell out the complete
name.
If you do a rename as specified above and you want to preserve ACLs.
`Non-Atomic Operation`
Unlike the case with many file systems, the mv command does not perform a single
atomic operation. Rather, it performs a copy from source to destination followed
by removing the source for each object.
A consequence of this is that, in addition to normal network and operation
charges, if you move a Nearline Storage, Coldline Storage, or Archive Storage
object, deletion and data retrieval charges apply. See the documentation for
pricing details.

**EXAMPLES**

: To move all objects from a bucket to a local directory you could use:

```
gcloud storage mv gs://my_bucket/* dir
```

Similarly, to move all objects from a local directory to a bucket you could use:

```
gcloud storage mv ./dir gs://my_bucket
```

The following command renames all objects under gs://my_bucket/oldprefix to be
under gs://my_bucket/newprefix, otherwise preserving the naming structure:

```
gcloud storage mv gs://my_bucket/oldprefix gs://my_bucket/newprefix
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
gcloud alpha storage mv
```