# gcloud spanner databases change-quorum  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum)*

**NAME**

: **gcloud spanner databases change-quorum - change quorum of a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner databases change-quorum` (`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum#DATABASE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum#--instance)`=`INSTANCE`) (`[--dual-region](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum#--dual-region)`     | `[--serving-location](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum#--serving-location)`=`SERVING_LOCATION` `[--single-region](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum#--single-region)`) [`[--etag](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Change quorum of a Cloud Spanner database.

**EXAMPLES**

: To trigger change quorum from single-region mode to dual-region mode, run:

```
gcloud spanner databases change-quorum my-database-id --instance=my-instance-id --dual-region
```

To trigger change quorum from dual-region mode to single-region mode with
serving location as `asia-south1`, run:

```
gcloud spanner databases change-quorum my-database-id --instance=my-instance-id --single-region --serving-location=asia-south1
```

To trigger change quorum using etag specified, run:

```
gcloud spanner databases change-quorum my-database-id --instance=my-instance-id --dual-region --etag=ETAG
```

**POSITIONAL ARGUMENTS**

: **Database resource - The Cloud Spanner database to change quorum. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `database` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATABASE`**:
ID of the database or fully qualified identifier for the database.
To set the `database` attribute:

- provide the argument `database` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
The Cloud Spanner instance for the database.
To set the `instance` attribute:

- provide the argument `database` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

**REQUIRED FLAGS**

: **--dual-region**

**OPTIONAL FLAGS**

: **--etag**:
Used for optimistic concurrency control.

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

: These variants are also available:

```
gcloud alpha spanner databases change-quorum
```

```
gcloud beta spanner databases change-quorum
```