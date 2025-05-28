# gcloud storage objects compose  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose)*

**NAME**

: **gcloud storage objects compose - concatenate a sequence of objects into a new composite object**

**SYNOPSIS**

: **`gcloud storage objects compose` `[SOURCE](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#SOURCE)` [`[SOURCE](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#SOURCE)` …] `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#DESTINATION)` [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#--additional-headers)`=`HEADER`=`VALUE`] [`[--if-generation-match](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#--if-generation-match)`=`GENERATION` `[--if-metageneration-match](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#--if-metageneration-match)`=`METAGENERATION`] [`[--retain-until](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#--retain-until)`=`DATETIME` `[--retention-mode](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#--retention-mode)`=`RETENTION_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/objects/compose#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud storage objects compose creates a new object whose content is the
concatenation of a given sequence of source objects in the same bucket. For more
information, please see: [composite objects
documentation](https://cloud.google.com/storage/docs/composite-objects).
There is a limit (currently 32) to the number of components that can be composed
in a single operation.

**EXAMPLES**

: The following command creates a new object `target.txt` by
concatenating `a.txt` and `b.txt`:

```
gcloud storage objects compose gs://bucket/a.txt gs://bucket/b.txt gs://bucket/target.txt
```

**POSITIONAL ARGUMENTS**

: **`SOURCE` [`SOURCE` …]**:
The list of source objects that will be concatenated into a single object.

**`DESTINATION`**:
The destination object.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

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
gcloud alpha storage objects compose
```