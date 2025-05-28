# gcloud app services set-traffic  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic)*

**NAME**

: **gcloud app services set-traffic - set traffic splitting settings**

**SYNOPSIS**

: **`gcloud app services set-traffic` [`[SERVICES](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic#SERVICES)` …] `[--splits](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic#--splits)`=`SPLITS`,[`[SPLITS](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic#SPLITS)`,…] [`[--migrate](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic#--migrate)`] [`[--split-by](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic#--split-by)`=`SPLIT_BY`; default="ip"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command sets the traffic split of versions across a service or a project.

**EXAMPLES**

: To send all traffic to 'v2' of service 's1', run:

```
gcloud app services set-traffic s1 --splits=v2=1
```

To split traffic evenly between 'v1' and 'v2' of service 's1', run:

```
gcloud app services set-traffic s1 --splits=v2=.5,v1=.5
```

To split traffic across all services:

```
gcloud app services set-traffic --splits=v2=.5,v1=.5
```

**POSITIONAL ARGUMENTS**

: **[`SERVICES` …]**:
The services to modify.

**REQUIRED FLAGS**

: **--splits**:
Key-value pairs describing what proportion of traffic should go to each version.
The split values are added together and used as weights. The exact values do not
matter, only their relation to each other. For example, v1=2,v2=2 is equivalent
to v1=.5,v2=.5

**OPTIONAL FLAGS**

: **--migrate**:
The migrate flag determines whether or not to use traffic migration during the
operation. Traffic migration will attempt to automatically migrate traffic from
the previous version to the new version, giving the autoscaler time to respond.
See the documentation here: [https://cloud.google.com/appengine/docs/python/console/trafficmigration](https://cloud.google.com/appengine/docs/python/console/trafficmigration)
for more information.

**--split-by**:
Whether to split traffic based on cookie, IP address or random.
`SPLIT_BY` must be one of: `cookie`,
`ip`, `random`.

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
gcloud beta app services set-traffic
```