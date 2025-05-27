# gcloud container hub policycontroller enable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable)*

**NAME**

: **gcloud container hub policycontroller enable - enable Policy Controller Feature**

**SYNOPSIS**

: **`gcloud container hub policycontroller enable` [`[--all-memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--all-memberships)`     | [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--location)`=`LOCATION`] `[--audit-interval](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--audit-interval)`=`AUDIT_INTERVAL` `[--constraint-violation-limit](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--constraint-violation-limit)`=`CONSTRAINT_VIOLATION_LIMIT` `[--no-content](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--content)` `[--no-default-bundles](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--default-bundles)` `[--version](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--version)`=`VERSION` `[--clear-exemptable-namespaces](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--clear-exemptable-namespaces)`     | `[--exemptable-namespaces](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--exemptable-namespaces)`=`EXEMPTABLE_NAMESPACES` `[--log-denies](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--log-denies)`     | `[--no-log-denies](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--log-denies)` `[--monitoring](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--monitoring)`=`MONITORING`     | `[--no-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--monitoring)` `[--mutation](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--mutation)`     | `[--no-mutation](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--mutation)` `[--referential-rules](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--referential-rules)`     | `[--no-referential-rules](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--referential-rules)`     | `[--fleet-default-member-config](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--fleet-default-member-config)`=`FLEET_DEFAULT_MEMBER_CONFIG`     | `[--no-fleet-default-member-config](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#--fleet-default-member-config)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Enables the Policy Controller Feature in a fleet.

**EXAMPLES**

: To enable the Policy Controller Feature, run:

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
gcloud alpha container hub policycontroller enable
```

```
gcloud beta container hub policycontroller enable
```