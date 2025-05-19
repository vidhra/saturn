# gcloud compute url-maps add-path-matcher  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher)*

**NAME**

: **gcloud compute url-maps add-path-matcher - add a path matcher to a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps add-path-matcher` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#URL_MAP)` `[--path-matcher-name](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--path-matcher-name)`=`PATH_MATCHER_NAME` (`[--default-backend-bucket](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--default-backend-bucket)`=`DEFAULT_BACKEND_BUCKET`     | `[--default-service](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--default-service)`=`DEFAULT_SERVICE`) [`[--backend-bucket-path-rules](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--backend-bucket-path-rules)`=`PATH`=`BUCKET`,[`[PATH](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#PATH)`=`BUCKET`,…]] [`[--backend-service-path-rules](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--backend-service-path-rules)`=`PATH`=`SERVICE`,[…]] [`[--delete-orphaned-path-matcher](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--delete-orphaned-path-matcher)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--description)`=`DESCRIPTION`] [`[--path-rules](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--path-rules)`=`PATH`=`SERVICE`,[…]] [`[--existing-host](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--existing-host)`=`EXISTING_HOST`     | `[--new-hosts](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--new-hosts)`=`NEW_HOST`,[`[NEW_HOST](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#NEW_HOST)`,…]] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute url-maps add-path-matcher` is used to add a path
matcher to a URL map. A path matcher maps HTTP request paths to backend services
or backend buckets. Each path matcher must be referenced by at least one host
rule. This command can create a new host rule through the
`--new-hosts` flag or it can reconfigure an existing host rule to
point to the newly added path matcher using `--existing-host`. In the
latter case, if a path matcher is orphaned as a result of the operation, this
command will fail unless `--delete-orphaned-path-matcher` is
provided. Path matcher constraints can be found [here](https://cloud.google.com/load-balancing/docs/url-map-concepts#pm-constraints).

**EXAMPLES**

: To create a rule for mapping the path `/search/*` to the hypothetical
`search-service`, `/static/*` to the
`static-bucket` backend bucket and `/images/*` to the
`images-service` under the hosts `example.com` and
`*.example.com`, run:

```
gcloud compute url-maps add-path-matcher MY-URL-MAP --path-matcher-name=MY-MATCHER --default-service=MY-DEFAULT-SERVICE --backend-service-path-rules='/search/*=search_service,/images/*=images-service' --backend-bucket-path-rules='/static/*=static-bucket' --new-hosts=example.com '*.example.com'
```

Note that a default service or default backend bucket must be provided to handle
paths for which there is no mapping.

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to operate on.

**REQUIRED FLAGS**

: **--path-matcher-name**:
The name to assign to the path matcher.

**--default-backend-bucket**

**OPTIONAL FLAGS**

: **--backend-bucket-path-rules**:
Rules for mapping request paths to backend buckets.

**--backend-service-path-rules**:
Rules for mapping request paths to services.

**--delete-orphaned-path-matcher**:
If provided and a path matcher is orphaned as a result of this command, the
command removes the orphaned path matcher instead of failing.

**--description**:
An optional, textual description for the path matcher.

**--path-rules**:
Rules for mapping request paths to services.

**--existing-host**

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
gcloud alpha compute url-maps add-path-matcher
```

```
gcloud beta compute url-maps add-path-matcher
```