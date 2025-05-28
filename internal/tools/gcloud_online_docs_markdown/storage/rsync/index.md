# gcloud storage rsync  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/rsync](https://cloud.google.com/sdk/gcloud/reference/storage/rsync)*

**NAME**

: **gcloud storage rsync - synchronize content of two buckets/directories**

**SYNOPSIS**

: **`gcloud storage rsync` `[SOURCE](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#SOURCE)` `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#DESTINATION)` [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--additional-headers)`=`HEADER`=`VALUE`] [`[--canned-acl](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--canned-acl)`=`PREDEFINED_ACL`, `[--predefined-acl](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--predefined-acl)`=`PREDEFINED_ACL`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#-a)` `[PREDEFINED_ACL](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#PREDEFINED_ACL)`] [`[--checksums-only](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--checksums-only)`] [`[--no-clobber](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--clobber)`, `[-n](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#-n)`] [`[--content-md5](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--content-md5)`=`MD5_DIGEST`] [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#-c)`] [`[--delete-unmatched-destination-objects](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--delete-unmatched-destination-objects)`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--dry-run)`] [`[--exclude](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--exclude)`=[`REGEX`,…], `[-x](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#-x)` [`[REGEX](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#REGEX)`,…]] [`[--gzip-in-flight](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--gzip-in-flight)`=[`FILE_EXTENSIONS`,…], `[-j](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#-j)` [`[FILE_EXTENSIONS](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#FILE_EXTENSIONS)`,…]] [`[--gzip-in-flight-all](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--gzip-in-flight-all)`, `-J`] [`[--no-ignore-symlinks](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--ignore-symlinks)`] [`[--include-managed-folders](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--include-managed-folders)`] [`[--preserve-posix](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--preserve-posix)`, `-P`] [`[--recursive](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--recursive)`, `-R`, `[-r](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#-r)`] [`[--skip-if-dest-has-newer-mtime](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--skip-if-dest-has-newer-mtime)`, `[-u](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#-u)`] [`[--skip-unsupported](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--skip-unsupported)`, `-U`] [`[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--decryption-keys)`=[`DECRYPTION_KEY`,…] `[--encryption-key](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--encryption-key)`=`ENCRYPTION_KEY`] [`[--cache-control](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--cache-control)`=`CACHE_CONTROL` `[--content-disposition](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--content-disposition)`=`CONTENT_DISPOSITION` `[--content-encoding](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--content-encoding)`=`CONTENT_ENCODING` `[--content-language](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--content-language)`=`CONTENT_LANGUAGE` `[--content-type](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--content-type)`=`CONTENT_TYPE` `[--custom-time](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--custom-time)`=`CUSTOM_TIME` `[--clear-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--clear-custom-metadata)`     | `[--custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--custom-metadata)`=[`CUSTOM_METADATA_KEYS_AND_VALUES`,…]     | `[--remove-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--remove-custom-metadata)`=[`METADATA_KEYS`,…] `[--update-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--update-custom-metadata)`=[`CUSTOM_METADATA_KEYS_AND_VALUES`,…]] [`[--if-generation-match](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--if-generation-match)`=`GENERATION` `[--if-metageneration-match](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#--if-metageneration-match)`=`METAGENERATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/rsync#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage rsync` copies to and updates objects at
`DESTINATION` to match `SOURCE`. `SOURCE` must
specify a directory, bucket, or bucket subdirectory. `gcloud storage
rsync` does not copy empty directory trees, since storage providers use a
[flat namespace](https://cloud.google.com/storage/docs/folders).
Note, shells (like bash, zsh) sometimes attempt to expand wildcards in ways that
can be surprising. Also, attempting to copy files whose names contain wildcard
characters can result in problems.
If synchronizing a large amount of data between clouds you might consider
setting up a Google Compute Engine account and running `gcloud storage
rsync` there. Since `gcloud storage rsync` cross-provider data
transfers flow through the machine where `gcloud storage rsync` is
running, doing this can make your transfer run significantly faster than on your
local workstation.

**EXAMPLES**

: To sync the contents of the local directory `data` to the bucket
gs://my-bucket/data:

```
gcloud storage rsync data gs://my-bucket/data
```

To recurse into directories use `--recursive`:

```
gcloud storage rsync data gs://my-bucket/data --recursive
```

To make the local directory `my-data` the same as the contents of
gs://mybucket/data and delete objects in the local directory that are not in
gs://mybucket/data:

```
gcloud storage rsync gs://mybucket/data my-data --recursive --delete-unmatched-destination-objects
```

To make the contents of gs://mybucket2 the same as gs://mybucket1 and delete
objects in gs://mybucket2 that are not in gs://mybucket1:

```
gcloud storage rsync gs://mybucket1 gs://mybucket2 --recursive --delete-unmatched-destination-objects
```

To copy all objects from `dir1` into `dir2` and delete all
objects in `dir2` which are not in `dir1`:

```
gcloud storage rsync dir1 dir2 --recursive - --delete-unmatched-destination-objects
```

To mirror your objects across cloud providers:

```
gcloud storage rsync gs://my-gs-bucket s3://my-s3-bucket --recursive --delete-unmatched-destination-objects
```

To apply gzip compression to only uploaded image files in `dir`:

```
gcloud storage rsync dir gs://my-bucket/data --gzip-in-flight=jpeg,jpg,gif,png
```

To skip the file `dir/data1/a.txt`:

```
gcloud storage rsync dir gs://my-bucket --exclude="data./.*\.txt$"
```

To skip all .txt and .jpg files:

```
gcloud storage rsync dir gs://my-bucket --exclude=".*\.txt$|.*\.jpg$"
```

**POSITIONAL ARGUMENTS**

: **`SOURCE`**:
The source container path.

**`DESTINATION`**:
The destination container path.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--canned-acl**:
Applies predefined, or "canned," ACLs to a resource. See docs for a list of
predefined ACL constants: [https://cloud.google.com/storage/docs/access-control/lists#predefined-acl](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl)

**--checksums-only**:
When comparing objects with matching names at the source and destination, skip
modification time check and compare object hashes. Normally, hashes are only
compared if modification times are not available.

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

**--delete-unmatched-destination-objects**:
Delete extra files under DESTINATION not found under SOURCE. By default extra
files are not deleted. Managed folders are not affected by this flag.
Note: this option can delete data quickly if you specify the wrong source and
destination combination.

**--dry-run**:
Print what operations rsync would perform without actually executing them.

**--exclude**:
Exclude objects matching regex pattern from rsync.
Note that this is a Python regular expression, not a pure wildcard pattern. For
example, matching a string ending in "abc" is `.*abc$` rather than
`*abc`. Also note that the exclude path is relative, as opposed to
absolute (similar to Linux `rsync` and `tar` exclude
options).
For the Windows cmd.exe command line interpreter, use `^` as an
escape character instead of `\` and escape the `|`
character. When using Windows PowerShell, use `'` instead of
`"` and surround the `|` character with `"`.

**--gzip-in-flight**:
Applies gzip transport encoding to any file upload whose extension matches the
input extension list. This is useful when uploading files with compressible
content such as .js, .css, or .html files. This also saves network bandwidth
while leaving the data uncompressed in Cloud Storage.
When you specify the `--gzip-in-flight` option, files being uploaded
are compressed in-memory and on-the-wire only. Both the local files and Cloud
Storage objects remain uncompressed. The uploaded objects retain the
`Content-Type` and name of the original files.

**--gzip-in-flight-all**:
Applies gzip transport encoding to file uploads. This option works like the
`--gzip-in-flight` option described above, but it applies to all
uploaded files, regardless of extension.
CAUTION: If some of the source files don't compress well, such as binary data,
using this option may result in longer uploads.

**--ignore-symlinks**:
Ignore file symlinks instead of copying what they point to. Enabled by default,
use `--no-ignore-symlinks` to disable.

**--include-managed-folders**:
Includes managed folders in command operations. For transfers, gcloud storage
will set up managed folders in the destination with the same IAM policy bindings
as the source. Managed folders are only included with recursive cloud-to-cloud
transfers.

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

**--recursive**:
Recursively copy the contents of any directories that match the source path
expression.

**--skip-if-dest-has-newer-mtime**:
Skip operating on destination object if it has a newer modification time than
the source.

**--skip-unsupported**:
Skip objects with unsupported object types.

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
gcloud alpha storage rsync
```