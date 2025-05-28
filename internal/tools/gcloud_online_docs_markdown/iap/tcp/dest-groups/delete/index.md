# gcloud iap tcp dest-groups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/delete](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/delete)*

**NAME**

: **gcloud iap tcp dest-groups delete - delete the IAP TCP Destination Group resource**

**SYNOPSIS**

: **`gcloud iap tcp dest-groups delete` `[GROUP_NAME](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/delete#GROUP_NAME)` `[--region](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/delete#--region)`=`REGION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the IAP TCP Destination Group resource.

**EXAMPLES**

: To delete a DestGroup with name ``GROUP_NAME``,
in region ``REGION`` in the current project
run:

```
gcloud iap tcp dest-groups delete DEST_GROUP_NAME --region=REGION
```

To delete a DestGroup with name ``GROUP_NAME``,
in region ``REGION`` in the project
``PROJECT_ID`` run:

```
gcloud iap tcp dest-groups delete DEST_GROUP_NAME --region=REGION --project=PROJECT_ID
```

**POSITIONAL ARGUMENTS**

: **`GROUP_NAME`**:
Name of the Destination Group.

**REQUIRED FLAGS**

: **--region**:
Region of the Destination Group.

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
gcloud alpha iap tcp dest-groups delete
```

```
gcloud beta iap tcp dest-groups delete
```