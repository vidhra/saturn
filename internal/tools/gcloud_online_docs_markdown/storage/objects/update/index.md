# gcloud storage objects update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/objects/update](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update)*

**NAME**

: **gcloud storage objects update - update Cloud Storage objects**

**SYNOPSIS**

: **`gcloud storage objects update` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#URL)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--additional-headers)`=`HEADER`=`VALUE`] [`[--all-versions](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--all-versions)`] [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#-c)`] [`[--[no-]event-based-hold](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--[no-]event-based-hold)`] [`[--read-paths-from-stdin](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--read-paths-from-stdin)`, `-I`] [`[--recursive](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--recursive)`, `-R`, `[-r](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#-r)`] [`[--storage-class](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--storage-class)`=`STORAGE_CLASS`, `[-s](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#-s)` `[STORAGE_CLASS](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#STORAGE_CLASS)`] [`[--[no-]temporary-hold](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--[no-]temporary-hold)`] [`[--acl-file](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--acl-file)`=`ACL_FILE` `[--add-acl-grant](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--add-acl-grant)`=[`ACL_GRANT`,…] `[--canned-acl](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--canned-acl)`=`PREDEFINED_ACL`, `[--predefined-acl](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--predefined-acl)`=`PREDEFINED_ACL`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#-a)` `[PREDEFINED_ACL](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#PREDEFINED_ACL)` `[--[no-]preserve-acl](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--[no-]preserve-acl)`, `[-p](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#-p)` `[--remove-acl-grant](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--remove-acl-grant)`=`REMOVE_ACL_GRANT`] [`[--clear-encryption-key](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-encryption-key)` `[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--decryption-keys)`=[`DECRYPTION_KEY`,…] `[--encryption-key](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--encryption-key)`=`ENCRYPTION_KEY`] [`[--cache-control](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--cache-control)`=`CACHE_CONTROL` `[--clear-cache-control](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-cache-control)` `[--clear-content-disposition](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-content-disposition)` `[--clear-content-encoding](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-content-encoding)` `[--clear-content-language](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-content-language)` `[--clear-content-type](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-content-type)` `[--clear-custom-time](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-custom-time)` `[--content-disposition](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--content-disposition)`=`CONTENT_DISPOSITION` `[--content-encoding](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--content-encoding)`=`CONTENT_ENCODING` `[--content-language](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--content-language)`=`CONTENT_LANGUAGE` `[--content-type](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--content-type)`=`CONTENT_TYPE` `[--custom-time](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--custom-time)`=`CUSTOM_TIME` `[--clear-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-custom-metadata)`     | `[--custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--custom-metadata)`=[`CUSTOM_METADATA_KEYS_AND_VALUES`,…]     | `[--remove-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--remove-custom-metadata)`=[`METADATA_KEYS`,…] `[--update-custom-metadata](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--update-custom-metadata)`=[`CUSTOM_METADATA_KEYS_AND_VALUES`,…]] [`[--if-generation-match](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--if-generation-match)`=`GENERATION` `[--if-metageneration-match](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--if-metageneration-match)`=`METAGENERATION`] [`[--clear-retention](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--clear-retention)` `[--override-unlocked-retention](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--override-unlocked-retention)` `[--retain-until](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--retain-until)`=`DATETIME` `[--retention-mode](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#--retention-mode)`=`RETENTION_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/objects/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update Cloud Storage objects.

**EXAMPLES**

: Update a Google Cloud Storage object's custom-metadata:

```
gcloud storage objects update gs://bucket/my-object --custom-metadata=key1=value1,key2=value2
```

One can use [wildcards](https://cloud.google.com/storage/docs/wildcards) to update
multiple objects in a single command. for instance to update all objects to have
a custom-metadata key:

```
gcloud storage objects update gs://bucket/** --custom-metadata=key1=value1,key2=value2
```

Rewrite all JPEG images to the NEARLINE storage class:

```
gcloud storage objects update gs://bucket/*.jpg --storage-class=NEARLINE
```

You can also provide a precondition on an object's metageneration in order to
avoid potential race conditions:

```
gcloud storage objects update gs://bucket/*.jpg --storage-class=NEARLINE --if-metageneration-match=123456789
```

**POSITIONAL ARGUMENTS**

: **[`URL` …]**:
Specifies URLs of objects to update.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--all-versions**:
Perform the operation on all object versions.

**--continue-on-error**:
If any operations are unsuccessful, the command will exit with a non-zero exit
status after completing the remaining operations. This flag takes effect only in
sequential execution mode (i.e. processor and thread count are set to 1).
Parallelism is default.

**--[no-]event-based-hold**:
Enables or disables an event-based hold on objects. Use
`--event-based-hold` to enable and `--no-event-based-hold`
to disable.

**--read-paths-from-stdin**:
Read the list of objects to update from stdin. No need to enter a source
argument if this flag is present. Example: "storage objects update -I
--content-type=new-type"

**--recursive**:
Recursively update objects under any buckets or directories that match the URL
expression.

**--storage-class**:
Specify the storage class of the object. Using this flag triggers a rewrite of
underlying object data.

**--[no-]temporary-hold**:
Enables or disables a temporary hold on objects. Use
`--temporary-hold` to enable and `--no-temporary-hold` to
disable.

**--acl-file**:
Path to a local JSON or YAML formatted file containing a valid policy. See the
[ObjectAccessControls
resource](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for a representation of JSON formatted files. The output of
`gcloud storage [buckets|objects] describe`
`--format="multi(acl:format=json)"` is a valid file and can be edited
for more fine-grained control.

**--add-acl-grant**:
Key-value pairs mirroring the JSON accepted by your cloud provider. For example,
for Cloud
Storage,`--add-acl-grant=entity=user-tim@gmail.com,role=OWNER`

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

**--remove-acl-grant**:
Key-value pairs mirroring the JSON accepted by your cloud provider. For example,
for Cloud Storage, `--remove-acl-grant=ENTITY`, where
`ENTITY` has a valid ACL entity format, such as
`user-tim@gmail.com`, `group-admins`,
`allUsers`, etc.

**ENCRYPTION FLAGS**

: **--clear-encryption-key**:
Clears the encryption key associated with an object. Using this flag triggers a
rewrite of affected objects, which are then encrypted using the default
encryption key set on the bucket, if one exists, or else with a Google-managed
encryption key.

**--decryption-keys**:
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

**--clear-cache-control**:
Clears object cache control.

**--clear-content-disposition**:
Clears object content disposition.

**--clear-content-encoding**:
Clears content encoding.

**--clear-content-language**:
Clears object content language.

**--clear-content-type**:
Clears object content type.

**--clear-custom-time**:
Clears object custom time.

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

: **--clear-retention**:
Clears object retention settings and unlocks the configuration. Requires
--override-unlocked-retention flag as confirmation.

**--override-unlocked-retention**:
Needed for certain retention configuration modifications, such as clearing
retention settings and reducing retention time. Note that locked configurations
cannot be edited even with this flag.

**--retain-until**:
Ensures the object is retained until the specified time in RFC 3339 format.
Requires --override-unlocked-retention flag to shorten the retain-until time in
unlocked configurations.

**--retention-mode**:
Sets the object retention mode to either "Locked" or "Unlocked". When retention
mode is "Locked", the retain until time can only be increased.
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
gcloud alpha storage objects update
```