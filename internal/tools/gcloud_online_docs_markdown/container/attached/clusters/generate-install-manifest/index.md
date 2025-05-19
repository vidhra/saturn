# gcloud container attached clusters generate-install-manifest  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest)*

**NAME**

: **gcloud container attached clusters generate-install-manifest - generate Install Manifest for an Attached cluster**

**SYNOPSIS**

: **`gcloud container attached clusters generate-install-manifest` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest#--location)`=`LOCATION`) `[--platform-version](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest#--platform-version)`=`PLATFORM_VERSION` [`[--output-file](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest#--output-file)`=`OUTPUT_FILE`] [`[--proxy-secret-name](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest#--proxy-secret-name)`=`PROXY_SECRET_NAME` `[--proxy-secret-namespace](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest#--proxy-secret-namespace)`=`PROXY_SECRET_NAMESPACE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/generate-install-manifest#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Generate Install Manifest for an Attached cluster.

**EXAMPLES**

: To generate install manifest for cluster named
``my-cluster`` managed in location
``us-west1``, run:

```
gcloud container attached clusters generate-install-manifest my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION
```

To store the manifest in a file named
``manifest.yaml``, run:

```
gcloud container attached clusters generate-install-manifest my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --output-file=manifest.yaml
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to generate install manifest. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the cluster.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_attached/location`.**

**REQUIRED FLAGS**

: **--platform-version**:
Platform version to use for the cluster.
To retrieve a list of valid versions, run:

```
gcloud alpha container attached get-server-config --location=LOCATION
```

Replace ``LOCATION`` with the target Google
Cloud location for the cluster.

**OPTIONAL FLAGS**

: **--output-file**:
Path to the output file to store manifest.

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
gcloud alpha container attached clusters generate-install-manifest
```