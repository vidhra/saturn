# gcloud storage buckets create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create)*

**NAME**

: **gcloud storage buckets create - create buckets for storing objects**

**SYNOPSIS**

: **`gcloud storage buckets create` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#URL)` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#URL)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--additional-headers)`=`HEADER`=`VALUE`] [`[--default-encryption-key](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--default-encryption-key)`=`DEFAULT_ENCRYPTION_KEY`, `[-k](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#-k)` `[DEFAULT_ENCRYPTION_KEY](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#DEFAULT_ENCRYPTION_KEY)`] [`[--default-storage-class](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--default-storage-class)`=`DEFAULT_STORAGE_CLASS`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#-c)` `[DEFAULT_STORAGE_CLASS](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#DEFAULT_STORAGE_CLASS)`, `[-s](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#-s)` `[DEFAULT_STORAGE_CLASS](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#DEFAULT_STORAGE_CLASS)`] [`[--enable-hierarchical-namespace](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--enable-hierarchical-namespace)`] [`[--enable-per-object-retention](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--enable-per-object-retention)`] [`[--lifecycle-file](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--lifecycle-file)`=`LIFECYCLE_FILE`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--location)`=`LOCATION`, `[-l](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#-l)` `[LOCATION](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#LOCATION)`] [`[--[no-]pap](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--[no-]pap)`, `[--[no-]public-access-prevention](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--[no-]public-access-prevention)`] [`[--placement](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--placement)`=[`REGION`,…]] [`[--recovery-point-objective](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--recovery-point-objective)`=`SETTING`, `[--rpo](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--rpo)`=`SETTING`] [`[--retention-period](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--retention-period)`=`RETENTION_PERIOD`] [`[--soft-delete-duration](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--soft-delete-duration)`=`SOFT_DELETE_DURATION`] [`[--[no-]uniform-bucket-level-access](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--[no-]uniform-bucket-level-access)`, `[-b](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#-b)`] [`[--autoclass-terminal-storage-class](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--autoclass-terminal-storage-class)`=`AUTOCLASS_TERMINAL_STORAGE_CLASS` `[--[no-]enable-autoclass](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--[no-]enable-autoclass)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create new buckets.

**EXAMPLES**

: The following command creates 2 Cloud Storage buckets, one named
``my-bucket`` and a second bucket named
``my-other-bucket``:

```
gcloud storage buckets create gs://my-bucket gs://my-other-bucket
```

The following command creates a bucket with the
``nearline`` default [storage class](https://cloud.google.com/storage/docs/storage-classes)
in the ``asia`` [location](https://cloud.google.com/storage/docs/locations):

```
gcloud storage buckets create gs://my-bucket --default-storage-class=nearline --location=asia
```

**POSITIONAL ARGUMENTS**

: **`URL` [`URL` …]**:
The URLs of the buckets to create.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--default-encryption-key**:
Set the default KMS key using the full path to the key, which has the following
form:
``projects/[project-id]/locations/[location]/keyRings/[key-ring]/cryptoKeys/[my-key]``.

**--default-storage-class**:
Default [storage
class](https://cloud.google.com/storage/docs/storage-classes) for the bucket. If not specified, the default storage class used by
Cloud Storage is "Standard".

**--enable-hierarchical-namespace**:
Enable hierarchical namespace for the bucket. To use this flag, you must also
use --uniform-bucket-level-access

**--enable-per-object-retention**:
Enables each object in the bucket to have its own retention settings, which
prevents deletion until stored for a specific length of time.

**--lifecycle-file**:
Sets the lifecycle management configuration on a bucket. For example, The
following lifecycle management configuration JSON document specifies that all
objects in this bucket that are more than 365 days old are deleted
automatically:

```
{
  "rule":
  [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 365}
    }
  ]
}
```

**--location**:
[Location](https://cloud.google.com/storage/docs/locations) for the
bucket. If not specified, the location used by Cloud Storage is
``us``. A bucket's location cannot be changed
after creation.

**--[no-]pap**:
Sets public access prevention to "enforced". For details on how exactly public
access is blocked, see: [http://cloud.google.com/storage/docs/public-access-prevention](http://cloud.google.com/storage/docs/public-access-prevention).
Use `--public-access-prevention` to enable and
`--no-public-access-prevention` to disable.

**--placement**:
A comma-separated list of regions that form the custom [dual-region](https://cloud.google.com/storage/docs/locations#location-dr).
Only regions within the same continent are or will ever be valid. Invalid
location pairs (such as mixed-continent, or with unsupported regions) will
return an error.

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

**--retention-period**:
Minimum [retention
period](https://cloud.google.com/storage/docs/bucket-lock#retention-periods) for objects stored in the bucket, for example
``--retention-period=P1Y1M1DT5S``. Objects
added to the bucket cannot be deleted until they've been stored for the
specified length of time. Default is no retention period. Only available for
Cloud Storage using the JSON API.

**--soft-delete-duration**:
Duration to retain soft-deleted objects. For example, "2w1d" is two weeks and
one day. See `[gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for more information on the duration format. Setting
`0` will disable soft delete policy on the bucket. Default is 7 days.

**--[no-]uniform-bucket-level-access**:
Turns on uniform bucket-level access setting. Default is False. Use
`--uniform-bucket-level-access` to enable and
`--no-uniform-bucket-level-access` to disable.

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
gcloud alpha storage buckets create
```