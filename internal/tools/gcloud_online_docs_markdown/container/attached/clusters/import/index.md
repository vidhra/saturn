# gcloud container attached clusters import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import)*

**NAME**

: **gcloud container attached clusters import - import fleet membership for an Attached cluster**

**SYNOPSIS**

: **`gcloud container attached clusters import` `[--distribution](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--distribution)`=`DISTRIBUTION` `[--platform-version](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--platform-version)`=`PLATFORM_VERSION` (`[--context](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--context)`=`CONTEXT` : `[--kubeconfig](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--kubeconfig)`=`KUBECONFIG`) (`[--fleet-membership](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--fleet-membership)`=`FLEET_MEMBERSHIP` : `[--fleet-membership-location](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--fleet-membership-location)`=`FLEET_MEMBERSHIP_LOCATION`; default="global") [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--async)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--location)`=`LOCATION`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--validate-only)`] [`[--proxy-secret-name](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--proxy-secret-name)`=`PROXY_SECRET_NAME` `[--proxy-secret-namespace](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#--proxy-secret-namespace)`=`PROXY_SECRET_NAMESPACE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import fleet membership for an Attached cluster.

**EXAMPLES**

: To import the fleet membership of an attached cluster in fleet
``FLEET_MEMBERSHIP`` managed in location
``us-west1``, run:

```
gcloud container attached clusters import --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-membership=FLEET_MEMBERSHIP --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --kubeconfig=KUBECONFIG_PATH
```

**REQUIRED FLAGS**

: **--distribution**:
Set the base platform type of the cluster to attach.
Examples:

```
gcloud container attached clusters import --distribution=aks
gcloud container attached clusters import --distribution=eks
gcloud container attached clusters import --distribution=generic
```

**--platform-version**:
Platform version to use for the cluster.
To retrieve a list of valid versions, run:

```
gcloud alpha container attached get-server-config --location=LOCATION
```

Replace ``LOCATION`` with the target Google
Cloud location for the cluster.

**--context**

**Fleet membership resource - Membership of the registered cluster. Membership can
be the membership ID or the full resource name. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--fleet-membership` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--fleet-membership**:
ID of the fleet_membership or fully qualified identifier for the
fleet_membership.
To set the `fleet_membership` attribute:

- provide the argument `--fleet-membership` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--fleet-membership-location**:
Google Cloud location for the fleet_membership.
To set the `location` attribute:

- provide the argument `--fleet-membership` on the command line with a
fully specified name;
- provide the argument `--fleet-membership-location` on the command
line;
- set the property `container_attached/location`.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**Location resource - Google Cloud location to import attached cluster.. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `container_attached/location` with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- set the property `container_attached/location`.**

**--validate-only**:
Validate the cluster to import, but don't actually perform it.

**--proxy-secret-name**

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
gcloud alpha container attached clusters import
```