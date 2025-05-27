# gcloud container hub policycontroller update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update)*

**NAME**

: **gcloud container hub policycontroller update - updates the configuration of Policy Controller Feature**

**SYNOPSIS**

: **`gcloud container hub policycontroller update` [`[--all-memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--all-memberships)`     | [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--location)`=`LOCATION`] `[--origin](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--origin)`=`ORIGIN`     | `[--audit-interval](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--audit-interval)`=`AUDIT_INTERVAL` `[--constraint-violation-limit](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--constraint-violation-limit)`=`CONSTRAINT_VIOLATION_LIMIT` `[--version](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--version)`=`VERSION` `[--clear-exemptable-namespaces](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--clear-exemptable-namespaces)`     | `[--exemptable-namespaces](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--exemptable-namespaces)`=`EXEMPTABLE_NAMESPACES` `[--log-denies](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--log-denies)`     | `[--no-log-denies](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--log-denies)` `[--monitoring](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--monitoring)`=`MONITORING`     | `[--no-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--monitoring)` `[--mutation](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--mutation)`     | `[--no-mutation](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--mutation)` `[--referential-rules](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--referential-rules)`     | `[--no-referential-rules](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#--referential-rules)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the configuration of the Policy Controller installation

**EXAMPLES**

: To change the installed version, run:

```
gcloud container hub policycontroller update --version=VERSION
```

To modify the audit interval to 120 seconds, run:

```
gcloud container hub policycontroller update --audit-interval=120
```

**FLAGS**

: **--all-memberships**

**--origin**

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
gcloud alpha container hub policycontroller update
```

```
gcloud beta container hub policycontroller update
```