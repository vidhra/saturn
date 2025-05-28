# gcloud container clusters  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters](https://cloud.google.com/sdk/gcloud/reference/container/clusters)*

**NAME**

: **gcloud container clusters - deploy and teardown Google Kubernetes Engine clusters**

**SYNOPSIS**

: **`gcloud container clusters` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container/clusters#COMMAND)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud container clusters command group lets you deploy and teardown Google
Kubernetes Engine clusters.
See $ [gcloud docker](https://cloud.google.com/sdk/gcloud/reference/docker) --help for
information about deploying docker images to clusters.

**FLAGS**

: **--location**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[check-autopilot-compatibility](https://cloud.google.com/sdk/gcloud/reference/container/clusters/check-autopilot-compatibility)`**:
Check autopilot compatibility of a running cluster.

**`[create](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create)`**:
Create a cluster for running containers.

**`[create-auto](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto)`**:
Create an Autopilot cluster for running containers.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete)`**:
Delete an existing cluster for running containers.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe)`**:
Describe an existing cluster for running containers.

**`[get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials)`**:
Fetch credentials for a running cluster.

**`[get-upgrade-info](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info)`**:
Get information about upgrades for existing clusters including auto upgrade
status, upgrade history, upgrade targets, and end of support timelines.

**`[list](https://cloud.google.com/sdk/gcloud/reference/container/clusters/list)`**:
List existing clusters for running containers.

**`[resize](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize)`**:
Resizes an existing cluster for running containers.

**`[update](https://cloud.google.com/sdk/gcloud/reference/container/clusters/update)`**:
Update cluster settings for an existing container cluster.

**`[upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade)`**:
Upgrade the Kubernetes version of an existing container cluster.

**NOTES**

: These variants are also available:

```
gcloud alpha container clusters
```

```
gcloud beta container clusters
```