# gcloud storage buckets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update)*

**NAME**

: **gcloud storage buckets update - update bucket settings**

**SYNOPSIS**

: **`gcloud storage buckets update` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#URL)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--additional-headers)`=`HEADER`=`VALUE`] [`[--clear-soft-delete](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-soft-delete)`] [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#-c)`] [`[--[no-]default-event-based-hold](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--[no-]default-event-based-hold)`] [`[--default-storage-class](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--default-storage-class)`=`DEFAULT_STORAGE_CLASS`] [`[--lock-retention-period](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--lock-retention-period)`] [`[--read-paths-from-stdin](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--read-paths-from-stdin)`, `-I`] [`[--recovery-point-objective](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--recovery-point-objective)`=`SETTING`, `[--rpo](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--rpo)`=`SETTING`] [`[--[no-]requester-pays](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--[no-]requester-pays)`] [`[--soft-delete-duration](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--soft-delete-duration)`=`SOFT_DELETE_DURATION`] [`[--[no-]uniform-bucket-level-access](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--[no-]uniform-bucket-level-access)`] [`[--[no-]versioning](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--[no-]versioning)`] [`[--acl-file](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--acl-file)`=`ACL_FILE` `[--add-acl-grant](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--add-acl-grant)`=[`ACL_GRANT`,…] `[--canned-acl](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--canned-acl)`=`PREDEFINED_ACL`, `[--predefined-acl](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--predefined-acl)`=`PREDEFINED_ACL`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#-a)` `[PREDEFINED_ACL](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#PREDEFINED_ACL)` `[--remove-acl-grant](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--remove-acl-grant)`=`REMOVE_ACL_GRANT`] [`[--add-default-object-acl-grant](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--add-default-object-acl-grant)`=[`DEFAULT_OBJECT_ACL_GRANT`,…] `[--default-object-acl-file](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--default-object-acl-file)`=`DEFAULT_OBJECT_ACL_FILE` `[--predefined-default-object-acl](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--predefined-default-object-acl)`=`PREDEFINED_DEFAULT_OBJECT_ACL` `[--remove-default-object-acl-grant](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--remove-default-object-acl-grant)`=`REMOVE_DEFAULT_OBJECT_ACL_GRANT`] [`[--clear-cors](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-cors)`     | `[--cors-file](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--cors-file)`=`CORS_FILE`] [`[--clear-default-encryption-key](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-default-encryption-key)`     | `[--default-encryption-key](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--default-encryption-key)`=`DEFAULT_ENCRYPTION_KEY`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-labels)`     | `[--labels-file](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--labels-file)`=`LABELS_FILE`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--remove-labels)`=[`LABEL_KEYS`,…] `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--update-labels)`=[`LABEL_KEYS_AND_VALUES`,…]] [`[--clear-lifecycle](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-lifecycle)`     | `[--lifecycle-file](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--lifecycle-file)`=`LIFECYCLE_FILE`] [`[--clear-log-bucket](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-log-bucket)`     | `[--log-bucket](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--log-bucket)`=`LOG_BUCKET`] [`[--clear-log-object-prefix](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-log-object-prefix)`     | `[--log-object-prefix](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--log-object-prefix)`=`LOG_OBJECT_PREFIX`] [`[--clear-pap](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-pap)`, `[--clear-public-access-prevention](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-public-access-prevention)`     | `[--[no-]pap](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--[no-]pap)`, `[--[no-]public-access-prevention](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--[no-]public-access-prevention)`] [`[--clear-retention-period](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-retention-period)`     | `[--retention-period](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--retention-period)`=`RETENTION_PERIOD`] [`[--clear-web-error-page](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-web-error-page)`     | `[--web-error-page](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--web-error-page)`=`WEB_ERROR_PAGE`] [`[--clear-web-main-page-suffix](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--clear-web-main-page-suffix)`     | `[--web-main-page-suffix](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--web-main-page-suffix)`=`WEB_MAIN_PAGE_SUFFIX`] [`[--autoclass-terminal-storage-class](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--autoclass-terminal-storage-class)`=`AUTOCLASS_TERMINAL_STORAGE_CLASS` `[--[no-]enable-autoclass](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--[no-]enable-autoclass)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the settings for a bucket.

**EXAMPLES**

: The following command updates the default storage class of a Cloud Storage
bucket named "my-bucket" to NEARLINE and sets requester pays to true:

```
gcloud storage buckets update gs://my-bucket --default-storage-class=NEARLINE --requester-pays
```

The following command updates the retention period of a Cloud Storage bucket
named "my-bucket" to one year and thirty-six minutes:

```
gcloud storage buckets update gs://my-bucket --retention-period=1y36m
```

The following command clears the retention period of a bucket:

```
gcloud storage buckets update gs://my-bucket --clear-retention-period
```

**POSITIONAL ARGUMENTS**

: **[`URL` …]**:
Specifies the URLs of the buckets to update.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--clear-soft-delete**:
Clears bucket soft delete settings. Does not affect objects already in
soft-deleted state.

**--continue-on-error**:
If any operations are unsuccessful, the command will exit with a non-zero exit
status after completing the remaining operations. This flag takes effect only in
sequential execution mode (i.e. processor and thread count are set to 1).
Parallelism is default.

**--[no-]default-event-based-hold**:
Sets the default value for an event-based hold on the bucket. By setting the
default event-based hold on a bucket, newly-created objects inherit that value
as their event-based hold (it is not applied retroactively). Use
`--default-event-based-hold` to enable and
`--no-default-event-based-hold` to disable.

**--default-storage-class**:
Sets the default storage class for the bucket.

**--lock-retention-period**:
Locks an unlocked retention policy on the buckets. Caution: A locked retention
policy cannot be removed from a bucket or reduced in duration. Once locked,
deleting the bucket is the only way to "remove" a retention policy.

**--read-paths-from-stdin**:
Read the list of URLs from stdin.

**--recovery-point-objective**:
Sets the [recovery
point objective](https://cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) of a bucket. This flag can only be used with multi-region
and dual-region buckets. `DEFAULT` option is valid for multi-region
and dual-regions buckets. `ASYNC_TURBO` option is only valid for
dual-region buckets. If unspecified when the bucket is created, it defaults to
`DEFAULT` for dual-region and multi-region buckets. For more
information, see [replication
in Cloud Storage](https://cloud.google.com/storage/docs/availability-durability#cross-region-redundancy). `SETTING` must be one of:
`ASYNC_TURBO`, `DEFAULT`.

**--[no-]requester-pays**:
Allows you to configure a Cloud Storage bucket so that the requester pays all
costs related to accessing the bucket and its objects. Use
`--requester-pays` to enable and `--no-requester-pays` to
disable.

**--soft-delete-duration**:
Duration to retain soft-deleted objects. For example, "2w1d" is two weeks and
one day.

**--[no-]uniform-bucket-level-access**:
Enables or disables [uniform
bucket-level access](https://cloud.google.com/storage/docs/bucket-policy-only) for the buckets. Use
`--uniform-bucket-level-access` to enable and
`--no-uniform-bucket-level-access` to disable.

**--[no-]versioning**:
Allows you to configure a Cloud Storage bucket to keep old versions of objects.
Use `--versioning` to enable and `--no-versioning` to
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

**--remove-acl-grant**:
Key-value pairs mirroring the JSON accepted by your cloud provider. For example,
for Cloud Storage, `--remove-acl-grant=ENTITY`, where
`ENTITY` has a valid ACL entity format, such as
`user-tim@gmail.com`, `group-admins`,
`allUsers`, etc.

**--add-default-object-acl-grant**:
Adds default object ACL grant. See --add-acl-grant help text for more details.

**--default-object-acl-file**:
Sets the default object ACL from file for the bucket.

**--predefined-default-object-acl**:
Apply a predefined set of default object access controls tobuckets

**--remove-default-object-acl-grant**:
Removes default object ACL grant. See --remove-acl-grant help text for more
details.

**--clear-cors**

**--clear-default-encryption-key**

**--clear-labels**

**--clear-lifecycle**

**--clear-log-bucket**

**--clear-log-object-prefix**

**--clear-pap**

**--clear-retention-period**

**--clear-web-error-page**

**--clear-web-main-page-suffix**

**AUTOCLASS FLAGS**

: **--autoclass-terminal-storage-class**:
The storage class that objects in the bucket eventually transition to if they
are not read for a certain length of time. Only valid if Autoclass is enabled.

**--[no-]enable-autoclass**:
The Autoclass feature automatically selects the best storage class for objects
based on access patterns. Use `--enable-autoclass` to enable and
`--no-enable-autoclass` to disable.

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
gcloud alpha storage buckets update
```