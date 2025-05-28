# gcloud recommender recommendations mark-claimed  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed)*

**NAME**

: **gcloud recommender recommendations mark-claimed - mark a recommendation's state as CLAIMED**

**SYNOPSIS**

: **`gcloud recommender recommendations mark-claimed` `[RECOMMENDATION](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#RECOMMENDATION)` `[--etag](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#--etag)`=`ETAG` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#--location)`=`LOCATION` `[--recommender](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#--recommender)`=`RECOMMENDER` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#--billing-account)`=`BILLING_ACCOUNT`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#--project)`=`PROJECT_ID`) [`[--state-metadata](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#--state-metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#KEY)`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Mark a recommendation's state as CLAIMED. Can be applied to recommendations in
CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Users can use this method to
indicate to the Recommender API that they are starting to apply the
recommendation themselves. This stops the recommendation content from being
updated.

**EXAMPLES**

: To mark a recommendation as CLAIMED:

```
gcloud recommender recommendations mark-claimed abcd-1234 --project=project-id --location=global --recommender=google.compute.instance.MachineTypeRecommender --etag=abc123 --state-metadata=key1=value1,key2=value2
```

**POSITIONAL ARGUMENTS**

: **`RECOMMENDATION`**:
Recommendation id which will be marked as claimed

**REQUIRED FLAGS**

: **--etag**:
Etag of a recommendation

**--location**:
Location

**--recommender**:
Recommender of recommendation

**--billing-account**

**OPTIONAL FLAGS**

: **--state-metadata**:
State metadata for recommendation, in format of
--state-metadata=key1=value1,key2=value2

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
gcloud alpha recommender recommendations mark-claimed
```

```
gcloud beta recommender recommendations mark-claimed
```