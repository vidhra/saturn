# gcloud container hub policycontroller detach  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/detach](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/detach)*

**NAME**

: **gcloud container hub policycontroller detach - detach Policy Controller Feature**

**SYNOPSIS**

: **`gcloud container hub policycontroller detach` [`[--all-memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/detach#--all-memberships)`     | [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/detach#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/detach#--location)`=`LOCATION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/detach#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Detaches Policy Controller. This will halt all administration of the Policy
Controller installation by the GKE Fleet. It will not uninstall it from the
cluster. To re-attach Policy Controller, use the `enable` command.

**EXAMPLES**

: To detach Policy Controller, run:

```
gcloud container hub policycontroller detach
```

To re-attach Policy Controller, use the `enable` command:

```
gcloud container hub policycontroller enable
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
gcloud alpha container hub policycontroller detach
```

```
gcloud beta container hub policycontroller detach
```