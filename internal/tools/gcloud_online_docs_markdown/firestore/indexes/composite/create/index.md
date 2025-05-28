# gcloud firestore indexes composite create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create)*

**NAME**

: **gcloud firestore indexes composite create - create a new composite index**

**SYNOPSIS**

: **`gcloud firestore indexes composite create` `[--field-config](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--field-config)`=[`array-config`=`ARRAY-CONFIG`],[`field-path`=`FIELD-PATH`],[`order`=`ORDER`],[`vector-config`=`VECTOR-CONFIG`] (`[--collection-group](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--collection-group)`=`COLLECTION_GROUP` : `[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--database)`=`DATABASE`) [`[--api-scope](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--api-scope)`=`API_SCOPE`; default="any-api"] [`[--async](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--async)`] [`[--density](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--density)`=`DENSITY`] [`[--multikey](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--multikey)`] [`[--query-scope](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--query-scope)`=`QUERY_SCOPE`; default="collection"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new composite index.

**EXAMPLES**

: The following command creates a composite index with fields `user_id`
(in descending order) followed by `timestamp` (in descending order)
in the `Events` collection group.

```
gcloud firestore indexes composite create --collection-group=Events --field-config=field-path=user-id,order=descending --field-config=field-path=timestamp,order=descending
```

```
gcloud firestore indexes composite create --database=(default) --collection-group=Events --field-config=field-path=user-id,order=descending --field-config=field-path=timestamp,order=descending
```

**REQUIRED FLAGS**

: **--field-config**:
Required, Configuration for an index field.

**`array-config`**:
Specifies the configuration for an array field. The only valid option is
'contains'. Exactly one of 'order', 'array-config', or 'vector-config' must be
specified.

**`field-path`**:
Specifies the field path (e.g. 'address.city'). This is required.

**`order`**:
Specifies the order. Valid options are 'ascending', 'descending'. Exactly one of
'order', 'array-config', or 'vector-config' must be specified.

**`vector-config`**:
Specifies the configuration for a vector field. Exactly one of 'order',
'array-config', or 'vector-config' must be specified.

**`dimension`**:
Sets `dimension` value.

**`flat`**:
Sets `flat` value.

`Shorthand Example:`

```
--field-config=array-config=string,field-path=string,order=string,vector-config={dimension=int,flat={}} --field-config=array-config=string,field-path=string,order=string,vector-config={dimension=int,flat={}}
```

`JSON Example:`

```
--field-config='[{"array-config": "string", "field-path": "string", "order": "string", "vector-config": {"dimension": int, "flat": {}}}]'
```

`File Example:`

```
--field-config=path_to_file.(yaml|json)
```

**Collection group resource - Collection group of the index. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--collection-group` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--collection-group**:
ID of the collection group or fully qualified identifier for the collection
group.
To set the `collection-group` attribute:

- provide the argument `--collection-group` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--database**:
Database of the collection group.
To set the `database` attribute:

- provide the argument `--collection-group` on the command line with a
fully specified name;
- provide the argument `--database` on the command line;
- the default value of argument [--database] is `(default)`.**

**OPTIONAL FLAGS**

: **--api-scope**:
Api scope the index applies to. `API_SCOPE` must be one
of: `any-api`, `datastore-mode-api`,
`mongodb-compatible-api`.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--density**:
Density of the index. `DENSITY` must be one of:
`dense`, `density-unspecified`, `sparse-all`,
`sparse-any`.

**--multikey**:
Optional. Whether the index is multikey. By default, the index is not multikey.
For non-multikey indexes, none of the paths in the index definition reach or
traverse an array, except via an explicit array index. For multikey indexes, at
most one of the paths in the index definition reach or traverse an array, except
via an explicit array index. Violations will result in errors. Note this field
only applies to index with MONGODB_COMPATIBLE_API ApiScope.

**--query-scope**:
Query scope the index applies to. `QUERY_SCOPE` must be
one of: `collection`, `collection-group`,
`collection-recursive`.

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
gcloud alpha firestore indexes composite create
```

```
gcloud beta firestore indexes composite create
```