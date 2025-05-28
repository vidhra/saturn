# gcloud recommender insight-type-config update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update)*

**NAME**

: **gcloud recommender insight-type-config update - update an insight type configuration**

**SYNOPSIS**

: **`gcloud recommender insight-type-config update` `[INSIGHT_TYPE](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#INSIGHT_TYPE)` `[--etag](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--etag)`=`ETAG` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--location)`=`LOCATION` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--billing-account)`=`BILLING_ACCOUNT`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--project)`=`PROJECT_ID`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--annotations)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#KEY)`=`VALUE`,…]] [`[--config-file](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--config-file)`=`CONFIG_FILE`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--display-name)`=`DISPLAY_NAME`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an insight type configuration based on a given entity (project,
organization, billing account), location, and insight type.

**EXAMPLES**

: To update an insight type configuration, run:

```
gcloud recommender insight-type-config update ${INSIGHT_TYPE} --project=${PROJECT} --location=${LOCATION} --etag=\"123\" --config-file=config.yaml
```

**POSITIONAL ARGUMENTS**

: **`INSIGHT_TYPE`**:
Insight type to use for this invocation.

**REQUIRED FLAGS**

: **--etag**:
Etag of the insight type configuration.

**--location**:
Location to use for this invocation.

**--billing-account**

**OPTIONAL FLAGS**

: **--annotations**:
Store small amounts of arbitrary data on the insight type configuration.

**--config-file**:
Generation configuration file for the insight type configuration.

**--display-name**:
Display name of the insight type configuration.

**--validate-only**:
If true, validate the request and preview the change, but do not actually update
it.

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

: This variant is also available:

```
gcloud beta recommender insight-type-config update
```