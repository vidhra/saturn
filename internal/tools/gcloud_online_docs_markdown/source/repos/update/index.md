# gcloud source repos update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/source/repos/update](https://cloud.google.com/sdk/gcloud/reference/source/repos/update)*

**NAME**

: **gcloud source repos update - update the configuration of a Cloud Source Repository**

**SYNOPSIS**

: **`gcloud source repos update` `[REPO](https://cloud.google.com/sdk/gcloud/reference/source/repos/update#REPO)` ((`[--add-topic](https://cloud.google.com/sdk/gcloud/reference/source/repos/update#--add-topic)`=`ADD_TOPIC` | `[--remove-topic](https://cloud.google.com/sdk/gcloud/reference/source/repos/update#--remove-topic)`=`REMOVE_TOPIC` | `[--update-topic](https://cloud.google.com/sdk/gcloud/reference/source/repos/update#--update-topic)`=`UPDATE_TOPIC`) : `[--message-format](https://cloud.google.com/sdk/gcloud/reference/source/repos/update#--message-format)`=`MESSAGE_FORMAT` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/source/repos/update#--service-account)`=`SERVICE_ACCOUNT` `[--topic-project](https://cloud.google.com/sdk/gcloud/reference/source/repos/update#--topic-project)`=`TOPIC_PROJECT`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/source/repos/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To associate a Cloud Pub/Sub topic to receive repository update notifications,
run:

```
gcloud source repos update REPO_NAME --add-topic=TOPIC_NAME --service-account=SERVICE_ACCOUNT_EMAIL --message-format=json
```

**POSITIONAL ARGUMENTS**

: **Repo resource - Name of the Cloud Source repository to update. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `repo` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**`REPO`**:
ID of the repo or fully qualified identifier for the repo.
To set the `repo` attribute:

- provide the argument `repo` on the command line.**

**REQUIRED FLAGS**

: **--message-format**

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
gcloud alpha source repos update
```

```
gcloud beta source repos update
```