# gcloud source project-configs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update)*

**NAME**

: **gcloud source project-configs update - update the Cloud Source Repositories configuration of the current project**

**SYNOPSIS**

: **`gcloud source project-configs update` (`[--disable-pushblock](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#--disable-pushblock)`     | `[--enable-pushblock](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#--enable-pushblock)`     | `[--message-format](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#--message-format)`=`MESSAGE_FORMAT` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#--service-account)`=`SERVICE_ACCOUNT` `[--topic-project](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#--topic-project)`=`TOPIC_PROJECT` `[--add-topic](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#--add-topic)`=`ADD_TOPIC`     | `[--remove-topic](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#--remove-topic)`=`REMOVE_TOPIC`     | `[--update-topic](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#--update-topic)`=`UPDATE_TOPIC`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/source/project-configs/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To enable PushBlock for all repositories under current project, run:

```
gcloud source project-configs update --enable-pushblock
```

To associate a Cloud Pub/Sub topic to receive repository update notifications,
run:

```
gcloud source project-configs update --add-topic=TOPIC_NAME --service-account=SERVICE_ACCOUNT_EMAIL --message-format=json
```

**REQUIRED FLAGS**

: **--disable-pushblock**

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
gcloud alpha source project-configs update
```

```
gcloud beta source project-configs update
```