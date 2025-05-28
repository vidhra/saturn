# gcloud recommender recommender-config update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update)*

**NAME**

: **gcloud recommender recommender-config update - update a recommender configuration**

**SYNOPSIS**

: **`gcloud recommender recommender-config update` `[RECOMMENDER](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#RECOMMENDER)` `[--etag](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--etag)`=`ETAG` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--location)`=`LOCATION` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--billing-account)`=`BILLING_ACCOUNT`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--project)`=`PROJECT_ID`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--annotations)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#KEY)`=`VALUE`,…]] [`[--config-file](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--config-file)`=`CONFIG_FILE`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--display-name)`=`DISPLAY_NAME`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a recommender configuration based on a given entity (project,
organization, billing account), location, and recommender.

**EXAMPLES**

: To update a recommender configuration, run:

```
gcloud recommender recommender-config update ${RECOMMENDER} --project=${PROJECT} --location=${LOCATION} --etag=\"123\" --config-file=config.yaml
```

**POSITIONAL ARGUMENTS**

: **`RECOMMENDER`**:
Recommender to use for this invocation.

**REQUIRED FLAGS**

: **--etag**:
Etag of the recommender configuration.

**--location**:
Location to use for this invocation.

**--billing-account**

**OPTIONAL FLAGS**

: **--annotations**:
Store small amounts of arbitrary data on the recommender configuration.

**--config-file**:
Generation configuration file for the recommender configuration.

**--display-name**:
Display name of the recommender configuration.

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
gcloud beta recommender recommender-config update
```