# gcloud dns record-sets changes describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe)*

**NAME**

: **gcloud dns record-sets changes describe - view the details of a change**

**SYNOPSIS**

: **`gcloud dns record-sets changes describe` `[CHANGE_ID](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe#CHANGE_ID)` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe#ZONE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command displays the details of the specified change.

**EXAMPLES**

: To display the details of a change, run:

```
gcloud dns record-sets changes describe change_id
```

**POSITIONAL ARGUMENTS**

: **`CHANGE_ID`**:
The ID of the change you want details for.

**REQUIRED FLAGS**

: **--zone**:
Name of the managed zone whose record sets you want to manage.

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
gcloud alpha dns record-sets changes describe
```

```
gcloud beta dns record-sets changes describe
```