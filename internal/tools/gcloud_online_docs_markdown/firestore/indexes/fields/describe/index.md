# gcloud firestore indexes fields describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/describe](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/describe)*

**NAME**

: **gcloud firestore indexes fields describe - describe the index configuration of the given field**

**SYNOPSIS**

: **`gcloud firestore indexes fields describe` [[`[FIELD](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/describe#FIELD)`] `[--collection-group](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/describe#--collection-group)`=`COLLECTION_GROUP` `[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/describe#--database)`=`DATABASE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/fields/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe the index configuration of the given field.

**EXAMPLES**

: The following command describes the database-wide default index settings:

```
gcloud firestore indexes fields describe
```

```
gcloud firestore indexes fields describe --database=(default)
```

The following command describes the index configuration of the
`timestamp` field in the `Events` collection group.

```
gcloud firestore indexes fields describe timestamp --collection-group=Events
```

**POSITIONAL ARGUMENTS**

: **Field resource - Field to describe.
This can be omitted to describe the database-wide default index settings. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`FIELD`]**:
ID of the field or fully qualified identifier for the field.
To set the `field` attribute:

- provide the argument `field` on the command line;
- .

**--collection-group**:
Collection group of the field.
To set the `collection-group` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- with a fully specified name;
- provide the argument `--collection-group` on the command line;
- .

**--database**:
Database of the field.
To set the `database` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- with a fully specified name;
- provide the argument `--database` on the command line;
- the default value of argument [--database] is `(default)`.**

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
gcloud alpha firestore indexes fields describe
```

```
gcloud beta firestore indexes fields describe
```