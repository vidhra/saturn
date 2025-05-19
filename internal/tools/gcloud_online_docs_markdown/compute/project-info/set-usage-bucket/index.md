# gcloud compute project-info set-usage-bucket  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/project-info/set-usage-bucket](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/set-usage-bucket)*

**NAME**

: **gcloud compute project-info set-usage-bucket - set usage reporting bucket for a project**

**SYNOPSIS**

: **`gcloud compute project-info set-usage-bucket` (`[--bucket](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/set-usage-bucket#--bucket)`=`BUCKET`     | `[--no-bucket](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/set-usage-bucket#--bucket)`) [`[--prefix](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/set-usage-bucket#--prefix)`=`PREFIX`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/set-usage-bucket#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute project-info set-usage-bucket` configures usage
reporting for projects.
Setting usage reporting will cause a log of usage per resource to be written to
a specified Google Cloud Storage bucket daily.
For example, to write daily logs of the form usage_gce_YYYYMMDD.csv to the
bucket `my-bucket`, run:

```
gcloud compute project-info set-usage-bucket --bucket=gs://my-bucket
```

To disable this feature, issue the command:

```
gcloud compute project-info set-usage-bucket --no-bucket
```

**REQUIRED FLAGS**

: **--bucket**

**OPTIONAL FLAGS**

: **--prefix**:
Optional prefix for the name of the usage report object stored in the bucket. If
not supplied, then this defaults to ``usage``.
The report is stored as a CSV file named PREFIX_gce_YYYYMMDD.csv where YYYYMMDD
is the day of the usage according to Pacific Time. The prefix should conform to
Google Cloud Storage object naming conventions. This flag must not be provided
when clearing the usage bucket.

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
gcloud alpha compute project-info set-usage-bucket
```

```
gcloud beta compute project-info set-usage-bucket
```