# gcloud alpha asset feeds create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create)*

**NAME**

: **gcloud alpha asset feeds create - create a Cloud Asset Inventory Feed**

**SYNOPSIS**

: **`gcloud alpha asset feeds create` `[FEED_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#FEED_ID)` `[--pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--pubsub-topic)`=`PUBSUB_TOPIC` (`[--asset-names](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--asset-names)`=[`ASSET_NAMES`,…] `[--asset-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--asset-types)`=[`ASSET_TYPES`,…] `[--relationship-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--relationship-types)`=[`RELATIONSHIP_TYPES`,…]) (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--project)`=`PROJECT_ID`) [`[--condition-description](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--condition-description)`=`CONDITION_DESCRIPTION`] [`[--condition-expression](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--condition-expression)`=`CONDITION_EXPRESSION`] [`[--condition-title](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--condition-title)`=`CONDITION_TITLE`] [`[--content-type](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#--content-type)`=`CONTENT_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Cloud Asset Inventory Feed for updates on
assets.

**EXAMPLES**

: To create a new feed 'feed1' in project 'p1' which alerts on compute disks and
network resources types, run:

```
gcloud alpha asset feeds create feed1 --project=p1 --asset-types=compute.googleapis.com/Network,compute.googleapis.com/Disk --content-type=resource --pubsub-topic=projects/project1/topics/feed-topic
```

**POSITIONAL ARGUMENTS**

: **`FEED_ID`**:
Asset feed identifier being created, it must be unique under the specified
parent resource project/folder/organization.

**REQUIRED FLAGS**

: **--pubsub-topic**:
Name of the Cloud Pub/Sub topic to publish to, of the form
`projects/PROJECT_ID/topics/TOPIC_ID`. You can list existing topics
with `gcloud pubsub topics list --format="text(name)"`

**--asset-names**

**--folder**

**OPTIONAL FLAGS**

: **--condition-description**:
Description of the feed condition. For reference only.

**--condition-expression**:
Feed condition expression. If not specified, no condition will be applied to
feed. For more information, see: [https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes#feed_with_condition](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes#feed_with_condition)

**--condition-title**:
Title of the feed condition. For reference only.

**--content-type**:
Asset content type. If not specified, no content but the asset name and type
will be returned in the feed. For more information, see [https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview#asset_content_type](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview#asset_content_type).
`CONTENT_TYPE` must be one of: `resource`,
`iam-policy`, `org-policy`, `access-policy`,
`os-inventory`, `relationship`.

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
gcloud asset feeds create
```

```
gcloud beta asset feeds create
```