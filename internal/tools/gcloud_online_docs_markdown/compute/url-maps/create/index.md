# gcloud compute url-maps create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create)*

**NAME**

: **gcloud compute url-maps create - create a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps create` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create#URL_MAP)` (`[--default-backend-bucket](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create#--default-backend-bucket)`=`DEFAULT_BACKEND_BUCKET`     | `[--default-service](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create#--default-service)`=`DEFAULT_SERVICE`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create#--description)`=`DESCRIPTION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute url-maps create` is used to create URL maps which map
HTTP and HTTPS request URLs to backend services and backend buckets. Mappings
are done using a longest-match strategy.
There are two components to a mapping: a host rule and a path matcher. A host
rule maps one or more hosts to a path matcher. A path matcher maps request paths
to backend services or backend buckets. For example, a host rule can map the
hosts ``*.google.com`` and
``google.com`` to a path matcher called
``www``. The
``www`` path matcher in turn can map the path
``/search/*`` to the search backend service,
the path ``/static/*`` to the static backend
bucket and everything else to a default backend service or default backend
bucket.
Host rules and patch matchers can be added to the URL map after the map is
created by using `[gcloud compute url-maps
edit](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit)` or by using `[gcloud compute
url-maps add-path-matcher](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher)` and `[gcloud compute
url-maps add-host-rule](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule)`.

**EXAMPLES**

: To create a global URL map with a default service, run:

```
gcloud compute url-maps create URL_MAP_NAME --default-service=BACKEND_SERVICE_NAME
```

To create a regional URL map with a default service, run:

```
gcloud compute url-maps create URL_MAP_NAME --default-service=BACKEND_SERVICE_NAME --region=REGION_NAME
```

To create a global URL map with a default backend bucket, run:

```
gcloud compute url-maps create URL_MAP_NAME --default-backend-bucket=BACKEND_BUCKET_NAME
```

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to create.

**REQUIRED FLAGS**

: **--default-backend-bucket**

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the URL map.

**--global**

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
gcloud alpha compute url-maps create
```

```
gcloud beta compute url-maps create
```