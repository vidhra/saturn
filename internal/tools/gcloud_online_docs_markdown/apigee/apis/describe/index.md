# gcloud apigee apis describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee/apis/describe](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/describe)*

**NAME**

: **gcloud apigee apis describe - describe an Apigee API proxy**

**SYNOPSIS**

: **`gcloud apigee apis describe` (`[API](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/describe#API)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/describe#--organization)`=`ORGANIZATION`) [`[--verbose](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/describe#--verbose)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an Apigee API proxy.
`gcloud apigee apis describe` shows metadata about an API proxy and
its revisions.

**EXAMPLES**

: To describe an API proxy called ``proxy-name``
given that its matching Cloud Platform project has been set in gcloud settings,
run:

```
gcloud apigee apis describe proxy-name
```

To describe an API proxy called
``other-proxy-name`` in another project whose
Apigee organization is named ``org-name``, run:

```
gcloud apigee apis describe other-proxy-name --organization=org-name
```

To describe an API proxy called ``proxy-name``
and include details on its revisions, run:

```
gcloud apigee apis describe proxy-name --verbose
```

To describe an API proxy called ``proxy-name``
as a JSON object, run:

```
gcloud apigee apis describe proxy-name --format=json
```

**POSITIONAL ARGUMENTS**

: **API proxy resource - API proxy to be described. To get a list of available API
proxies, run `[gcloud
apigee apis list](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/list)`. The arguments in this group can be used to specify
the attributes of this resource.
This must be specified.

**`API`**:
ID of the API proxy or fully qualified identifier for the API proxy.
To set the `api` attribute:

- provide the argument `API` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
Apigee organization containing the API proxy. If unspecified, the Cloud Platform
project's associated organization will be used.
To set the `organization` attribute:

- provide the argument `API` on the command line with a fully specified
name;
- provide the argument `--organization` on the command line;
- set the property [project] or provide the argument [--project] on the command
line, using a Cloud Platform project with an associated Apigee organization.**

**FLAGS**

: **--verbose**:
Include proxy revision info in the description.

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
gcloud alpha apigee apis describe
```

```
gcloud beta apigee apis describe
```