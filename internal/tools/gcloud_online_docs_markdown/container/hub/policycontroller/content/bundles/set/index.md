# gcloud container hub policycontroller content bundles set  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set)*

**NAME**

: **gcloud container hub policycontroller content bundles set - sets bundle installation for Policy Controller content**

**SYNOPSIS**

: **`gcloud container hub policycontroller content bundles set` `[BUNDLE_NAME](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set#BUNDLE_NAME)` [`[--all-memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set#--all-memberships)`     | [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set#--location)`=`LOCATION`]] [`[--exempted-namespaces](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set#--exempted-namespaces)`=`EXEMPTED_NAMESPACES`     | `[--no-exempted-namespaces](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set#--exempted-namespaces)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/set#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Google-defined policy bundles of constraints can be installed onto Policy
Controller installations.
The namespace exclusion flag (`--exempted-namespaces`) will specify a
set of namespaces that the installed bundle will ignore. Subsequent calls with
the same bundle name and this flag will overwrite what namespaces are being
ignored. Using `--no-exempted-namespaces` or specifying no namespaces
with `--exempted-namespaces` will remove all namespaces from the
ignore list.
To uninstall a bundle, use the `remove` command.

**EXAMPLES**

: To install a policy bundle:

```
gcloud container hub policycontroller content bundles set cis-k8s-v1.5.1
```

To install a policy bundle, while ignoring (exempting) certain namespaces from
being affected by the bundle:

```
gcloud container hub policycontroller content bundles set cis-k8s-v1.5.1 --exempted-namespaces=kube-system,gatekeeper-system
```

To remove all exempted namespaces from a particular bundles ignore list:

```
gcloud container hub policycontroller content bundles set cis-k8s-v1.5.1 --no-exempted-namespaces
```

**POSITIONAL ARGUMENTS**

: **`BUNDLE_NAME`**:
The constraint bundle to install in Policy Controller.

**FLAGS**

: **--all-memberships**

**--exempted-namespaces**

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
gcloud alpha container hub policycontroller content bundles set
```

```
gcloud beta container hub policycontroller content bundles set
```