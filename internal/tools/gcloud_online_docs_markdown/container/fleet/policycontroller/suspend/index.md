# gcloud container fleet policycontroller suspend  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/suspend](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/suspend)*

**NAME**

: **gcloud container fleet policycontroller suspend - suspend Policy Controller Feature**

**SYNOPSIS**

: **`gcloud container fleet policycontroller suspend` [`[--all-memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/suspend#--all-memberships)`     | [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/suspend#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/suspend#--location)`=`LOCATION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/suspend#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Suspends the Policy Controller. This will disable all kubernetes webhooks on the
configured cluster, thereby removing admission and mutation functionality. Audit
functionality will remain in place.

**EXAMPLES**

: To suspend Policy Controller, run:

```
gcloud container fleet policycontroller suspend
```

To re-enable Policy Controller webhooks, use the `enable` command:

```
gcloud container fleet policycontroller enable
```

**FLAGS**

: **--all-memberships**

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
gcloud alpha container fleet policycontroller suspend
```

```
gcloud beta container fleet policycontroller suspend
```