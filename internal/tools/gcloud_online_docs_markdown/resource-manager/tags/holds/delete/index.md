# gcloud resource-manager tags holds delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/delete](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/delete)*

**NAME**

: **gcloud resource-manager tags holds delete - delete a TagHold**

**SYNOPSIS**

: **`gcloud resource-manager tags holds delete` `[TAG_HOLD_NAME](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/delete#TAG_HOLD_NAME)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/delete#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a TagHold given its full name, specified as
tagValues/{tag_value_id}/tagHolds/{tag_hold_id}.

**EXAMPLES**

: To delete a TagHold under tagValue/111 with id abc-123-def in region
us-central1-a, run:

```
gcloud resource-manager tags holds delete tagValue/111/tagHolds/abc-123-def --location=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`TAG_HOLD_NAME`**:
TagHold given its full name, specified as
tagValues/{tag_value_id}/tagHolds/{tag_hold_id}

**FLAGS**

: **--location**:
Region where the TagHold is stored. If not provided, the API will attempt to
find and delete the specified TagHold from the "global" region.

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
gcloud alpha resource-manager tags holds delete
```

```
gcloud beta resource-manager tags holds delete
```