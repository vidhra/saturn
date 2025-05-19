# gcloud container fleet clusterupgrade update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update)*

**NAME**

: **gcloud container fleet clusterupgrade update - update the clusterupgrade feature for a fleet within a given project**

**SYNOPSIS**

: **`gcloud container fleet clusterupgrade update` [`[--default-upgrade-soaking](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update#--default-upgrade-soaking)`=`DEFAULT_UPGRADE_SOAKING`] [`[--remove-upgrade-soaking-overrides](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update#--remove-upgrade-soaking-overrides)`     | `[--add-upgrade-soaking-override](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update#--add-upgrade-soaking-override)`=`ADD_UPGRADE_SOAKING_OVERRIDE` `[--upgrade-selector](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update#--upgrade-selector)`=[`name`=`NAME`],[`version`=`VERSION`]] [`[--reset-upstream-fleet](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update#--reset-upstream-fleet)`     | `[--upstream-fleet](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update#--upstream-fleet)`=`UPSTREAM_FLEET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the clusterupgrade feature for a fleet within a given project.

**EXAMPLES**

: To update the clusterupgrade feature for the current fleet, run:

```
gcloud container fleet clusterupgrade update --default-upgrade-soaking=DEFAULT_UPGRADE_SOAKING
```

**FLAGS**

: **--default-upgrade-soaking**:
Configures the default soaking duration for each upgrade propagating through the
current fleet to become "COMPLETE". Soaking begins after all clusters in the
fleet are on the target version, or after 30 days if all cluster upgrades are
not complete. Once an upgrade state becomes "COMPLETE", it will automatically be
propagated to the downstream fleet. Max is 30 days.
To configure Rollout Sequencing for a fleet, this attribute must be set. To do
this while specifying a default soaking duration of 7 days, run:

```
gcloud container fleet clusterupgrade update --default-upgrade-soaking=7d
```

**--remove-upgrade-soaking-overrides**

**--reset-upstream-fleet**

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
gcloud alpha container fleet clusterupgrade update
```

```
gcloud beta container fleet clusterupgrade update
```