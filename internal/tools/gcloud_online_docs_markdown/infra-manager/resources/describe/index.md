# gcloud infra-manager resources describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/describe](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/describe)*

**NAME**

: **gcloud infra-manager resources describe - describe resources**

**SYNOPSIS**

: **`gcloud infra-manager resources describe` (`[RESOURCE](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/describe#RESOURCE)` : `[--deployment](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/describe#--deployment)`=`DEPLOYMENT` `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/describe#--location)`=`LOCATION` `[--revision](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/describe#--revision)`=`REVISION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a resource

**EXAMPLES**

: To describe a resource `compute-resource` under revision
`projects/p1/locations/us-central1/deployments/example-deployment/revisions/r-0`,
run:

```
gcloud infra-manager resources describe projects/p1/locations/us-central1/deployments/example-deployment/revisions/r-0/resources/compute-resource
```

**POSITIONAL ARGUMENTS**

: **Resource resource - The resource to describe The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `resource` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`RESOURCE`**:
ID of the resource or fully qualified identifier for the resource.
To set the `resource` attribute:

- provide the argument `resource` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--deployment**:
deployments TBD
To set the `deployment` attribute:

- provide the argument `resource` on the command line with a fully
specified name;
- provide the argument `--deployment` on the command line.

**--location**:
locations TBD
To set the `location` attribute:

- provide the argument `resource` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.

**--revision**:
revisions TBD
To set the `revision` attribute:

- provide the argument `resource` on the command line with a fully
specified name;
- provide the argument `--revision` on the command line.**

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

**API REFERENCE**

: This command uses the `config/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/infrastructure-manager/docs](https://cloud.google.com/infrastructure-manager/docs)