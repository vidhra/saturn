# gcloud firestore indexes fields update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update)*

**NAME**

: **gcloud firestore indexes fields update - update the index configuration of the given field**

**SYNOPSIS**

: **`gcloud firestore indexes fields update` (`[FIELD](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update#FIELD)` : `[--collection-group](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update#--collection-group)`=`COLLECTION_GROUP` `[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update#--database)`=`DATABASE`) (`[--clear-exemption](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update#--clear-exemption)`     | `[--disable-indexes](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update#--disable-indexes)`     | `[--index](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update#--index)`=[`KEY`=`VALUE`,…]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the index configuration of the given field.
This creates an exemption for the field in question, allowing one to modify the
field's index settings and override the defaults.

**EXAMPLES**

: The following command creates an exemption for the `timestamp` field
in the `Events` collection group, in which all indexes are disabled:

```
gcloud firestore indexes fields update timestamp --collection-group=Events --disable-indexes
```

```
gcloud firestore indexes fields update timestamp --database=(default) --collection-group=Events --disable-indexes
```

The following command creates an exemption for the `timestamp` field
in the `Events` collection group, in which the list of indexes is
explicitly set to [ASCENDING, DESCENDING]:

```
gcloud firestore indexes fields update timestamp --collection-group=Events --index=order=ASCENDING --index=order=DESCENDING
```

The following command clears the exemption on the `timestamp` field
in the `Events` collection group, so that the field will return to
inheriting its index settings from its ancestors:

```
gcloud firestore indexes fields update timestamp --collection-group=Events --clear-exemption
```

**POSITIONAL ARGUMENTS**

: **Field resource - Field to update. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FIELD`**:
ID of the field or fully qualified identifier for the field.
To set the `field` attribute:

- provide the argument `field` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--collection-group**:
Collection group of the field.
To set the `collection-group` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- provide the argument `--collection-group` on the command line.

**--database**:
Database of the field.
To set the `database` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- provide the argument `--database` on the command line;
- the default value of argument [--database] is `(default)`.**

**REQUIRED FLAGS**

: **--clear-exemption**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

**API REFERENCE**

: This command uses the `firestore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/firestore](https://cloud.google.com/firestore)

**NOTES**

: These variants are also available:

```
gcloud alpha firestore indexes fields update
```

```
gcloud beta firestore indexes fields update
```