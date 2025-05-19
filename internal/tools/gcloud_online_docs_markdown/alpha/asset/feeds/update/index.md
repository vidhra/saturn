# gcloud alpha asset feeds update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update)*

**NAME**

: **gcloud alpha asset feeds update - update an existing Cloud Asset Inventory Feed**

**SYNOPSIS**

: **`gcloud alpha asset feeds update` `[FEED_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#FEED_ID)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--project)`=`PROJECT_ID`) [`[--pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--pubsub-topic)`=`PUBSUB_TOPIC`] [`[--add-asset-names](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--add-asset-names)`=[`ASSET-NAMES`,…]     | `[--clear-asset-names](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--clear-asset-names)`     | `[--remove-asset-names](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--remove-asset-names)`=[`ASSET-NAMES`,…]] [`[--add-asset-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--add-asset-types)`=[`ASSET-TYPES`,…]     | `[--clear-asset-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--clear-asset-types)`     | `[--remove-asset-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--remove-asset-types)`=[`ASSET-TYPES`,…]] [`[--add-relationship-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--add-relationship-types)`=[`RELATIONSHIP-TYPES`,…]     | `[--clear-relationship-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--clear-relationship-types)`     | `[--remove-relationship-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--remove-relationship-types)`=[`RELATIONSHIP-TYPES`,…]] [`[--clear-condition-description](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--clear-condition-description)`     | `[--condition-description](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--condition-description)`=`CONDITION_DESCRIPTION`] [`[--clear-condition-expression](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--clear-condition-expression)`     | `[--condition-expression](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--condition-expression)`=`CONDITION_EXPRESSION`] [`[--clear-condition-title](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--clear-condition-title)`     | `[--condition-title](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--condition-title)`=`CONDITION_TITLE`] [`[--clear-content-type](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--clear-content-type)`     | `[--content-type](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#--content-type)`=`CONTENT_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an existing Cloud Asset Inventory Feed.

**EXAMPLES**

: To add an asset-type to an existing feed, run:

```
gcloud alpha asset feeds update feed1 --project=p1 --add-asset-types=pubsub.googleapis.com/Topic
```

**POSITIONAL ARGUMENTS**

: **`FEED_ID`**:
Identifier of the asset feed to update, which must be unique in its parent
resource. Parent resource can be a project, folder, or an organization.

**REQUIRED FLAGS**

: **--folder**

**OPTIONAL FLAGS**

: **--pubsub-topic**:
Name of the Cloud Pub/Sub topic to publish to, of the form
`projects/PROJECT_ID/topics/TOPIC_ID`. You can list existing topics
with `gcloud pubsub topics list --format="text(name)"`

**--add-asset-names**

**--add-asset-types**

**--add-relationship-types**

**--clear-condition-description**

**--clear-condition-expression**

**--clear-condition-title**

**--clear-content-type**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud asset feeds update
```

```
gcloud beta asset feeds update
```