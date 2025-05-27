# gcloud container hub policycontroller content bundles remove  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/remove](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/remove)*

**NAME**

: **gcloud container hub policycontroller content bundles remove - removes a bundle installation for Policy Controller content**

**SYNOPSIS**

: **`gcloud container hub policycontroller content bundles remove` `[BUNDLE_NAME](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/remove#BUNDLE_NAME)` [`[--all-memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/remove#--all-memberships)`     | [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/remove#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/remove#--location)`=`LOCATION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/remove#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Google-defined policy bundles of constraints can be installed onto Policy
Controller installations. This command removes those bundles.

**EXAMPLES**

: To remove a policy bundle:

```
gcloud container hub policycontroller content bundles remove cis-k8s-v1.5.1
```

**POSITIONAL ARGUMENTS**

: **`BUNDLE_NAME`**:
The constraint bundle to remove from Policy Controller.

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
gcloud alpha container hub policycontroller content bundles remove
```

```
gcloud beta container hub policycontroller content bundles remove
```