# gcloud firestore fields ttls update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update)*

**NAME**

: **gcloud firestore fields ttls update - update the TTL configuration of the given field**

**SYNOPSIS**

: **`gcloud firestore fields ttls update` (`[FIELD](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update#FIELD)` : `[--collection-group](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update#--collection-group)`=`COLLECTION_GROUP` `[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update#--database)`=`DATABASE`) (`[--disable-ttl](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update#--disable-ttl)`     | `[--enable-ttl](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update#--enable-ttl)`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the TTL configuration of the given field.
This enables or disables using a field as the TTL field for its collection group
or kind. Note that only one field can be the TTL field for a collection group.

**EXAMPLES**

: The following command sets the `expiry` field of the
`Events` collection group (kind) to be the TTL field:

```
gcloud firestore fields ttls update expiry --collection-group=Events --enable-ttl
```

The following command disables the `expiry` field so it is no longer
the TTL for the `Events` collection group (kind):

```
gcloud firestore fields ttls update expiry --collection-group=Events --disable-ttl
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

: **--disable-ttl**

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
gcloud alpha firestore fields ttls update
```

```
gcloud beta firestore fields ttls update
```