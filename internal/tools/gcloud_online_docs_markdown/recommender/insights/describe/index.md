# gcloud recommender insights describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe)*

**NAME**

: **gcloud recommender insights describe - describe an insight**

**SYNOPSIS**

: **`gcloud recommender insights describe` `[INSIGHT](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe#INSIGHT)` `[--insight-type](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe#--insight-type)`=`INSIGHT_TYPE` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe#--location)`=`LOCATION` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe#--billing-account)`=`BILLING_ACCOUNT`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an insight. This currently supports the following parent entities:
project, billing account, folder, and organization.

**EXAMPLES**

: To describe an insight:

```
gcloud recommender insights describe INSIGHT_ID --project=${PROJECT} --location=${LOCATION}
```

**POSITIONAL ARGUMENTS**

: **`INSIGHT`**:
insight to describe

**REQUIRED FLAGS**

: **--insight-type**:
Insight type to describe insights

**--location**:
Location

**--billing-account**

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
gcloud alpha recommender insights describe
```

```
gcloud beta recommender insights describe
```