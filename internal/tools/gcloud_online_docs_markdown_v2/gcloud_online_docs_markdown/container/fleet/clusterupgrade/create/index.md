# gcloud container fleet clusterupgrade create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/create](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/create)*

**NAME**

: **gcloud container fleet clusterupgrade create - create the clusterupgrade feature for a fleet within a given project**

**SYNOPSIS**

: **`gcloud container fleet clusterupgrade create` [`[--default-upgrade-soaking](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/create#--default-upgrade-soaking)`=`DEFAULT_UPGRADE_SOAKING`] [`[--upstream-fleet](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/create#--upstream-fleet)`=`UPSTREAM_FLEET`] [`[--add-upgrade-soaking-override](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/create#--add-upgrade-soaking-override)`=`ADD_UPGRADE_SOAKING_OVERRIDE` `[--upgrade-selector](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/create#--upgrade-selector)`=[`name`=`NAME`],[`version`=`VERSION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create the clusterupgrade feature for a fleet within a given project.

**EXAMPLES**

: To create the clusterupgrade feature for the current fleet, run:

```
gcloud container fleet clusterupgrade create --default-upgrade-soaking=DEFAULT_UPGRADE_SOAKING
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
gcloud container fleet clusterupgrade create --default-upgrade-soaking=7d
```

**--upstream-fleet**:
The upstream fleet. GKE will finish upgrades on the upstream fleet before
applying the same upgrades to the current fleet.
To configure the upstream fleet, run:

```
gcloud container fleet clusterupgrade create             --upstream-fleet={upstream_fleet}
```

**Upgrade soaking override.

```
Defines a specific soaking time override for a particular upgrade
propagating through the current fleet that supercedes the default
soaking duration configured by `--default-upgrade-soaking`.
```

```
To set an upgrade soaking override of 12 hours for the upgrade with
name, `k8s_control_plane`, and version, `1.23.1-gke.1000`, run:
```

```
gcloud container fleet clusterupgrade create               --add-upgrade-soaking-override=12h               --upgrade-selector=name="k8s_control_plane",version="1.23.1-gke.1000"
```

**--add-upgrade-soaking-override**:
Overrides the soaking time for a particular upgrade name and version propagating
through the current fleet. Set soaking to 0 days to bypass soaking and
fast-forward the upgrade to the downstream fleet.
See `$ [gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--upgrade-selector**:
Name and version of the upgrade to be overridden where version is a full GKE
version. Currently, name can be either `k8s_control_plane` or
`k8s_node`.
This flag argument must be specified if any of the other arguments in this group
are specified.**

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
gcloud alpha container fleet clusterupgrade create
```

```
gcloud beta container fleet clusterupgrade create
```