# gcloud firestore indexes composite delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/delete](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/delete)*

**NAME**

: **gcloud firestore indexes composite delete - delete the given composite index**

**SYNOPSIS**

: **`gcloud firestore indexes composite delete` (`[INDEX](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/delete#INDEX)` : `[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/delete#--database)`=`DATABASE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the given composite index.

**EXAMPLES**

: The following command deletes the composite index with ID `3421ef`:

```
gcloud firestore indexes composite delete 3421ef
```

```
gcloud firestore indexes composite delete 3421ef --database=(default)
```

**POSITIONAL ARGUMENTS**

: **Composite index resource - Index to delete. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `index` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `collection-group` attribute:

- provide the argument `index` on the command line with a fully
specified name;
- provide the argument [--collection-group] on the command line.

This must be specified.

**`INDEX`**:
ID of the composite index or fully qualified identifier for the composite index.
To set the `index` attribute:

- provide the argument `index` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--database**:
Database of the composite index.
To set the `database` attribute:

- provide the argument `index` on the command line with a fully
specified name;
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
gcloud alpha firestore indexes composite delete
```

```
gcloud beta firestore indexes composite delete
```