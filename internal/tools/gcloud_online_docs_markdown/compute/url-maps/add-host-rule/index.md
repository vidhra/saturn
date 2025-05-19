# gcloud compute url-maps add-host-rule  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule)*

**NAME**

: **gcloud compute url-maps add-host-rule - add a rule to a URL map to map hosts to a path matcher**

**SYNOPSIS**

: **`gcloud compute url-maps add-host-rule` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule#URL_MAP)` `[--hosts](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule#--hosts)`=`HOST`,[`[HOST](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule#HOST)`,…] `[--path-matcher-name](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule#--path-matcher-name)`=`PATH_MATCHER_NAME` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule#--description)`=`DESCRIPTION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute url-maps add-host-rule` is used to add a mapping of
hosts to a path matcher in a URL map. The mapping will match the host component
of HTTP requests to path matchers which in turn map the request to a backend
service. Before adding a host rule, at least one path matcher must exist in the
URL map to take care of the path component of the requests. `[gcloud compute
url-maps add-path-matcher](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher)` or `[gcloud compute url-maps
edit](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit)` can be used to add path matchers.

**EXAMPLES**

: To create a host rule mapping the `*-foo.example.com` and
`example.com` hosts to the `www` path matcher, run:

```
gcloud compute url-maps add-host-rule MY-URL-MAP --hosts='*-foo.example.com,example.com' --path-matcher-name=www
```

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to operate on.

**REQUIRED FLAGS**

: **--hosts**:
The set of hosts to match requests against. Each host must be a fully qualified
domain name (FQDN) with the exception that the host can begin with a
``*´´ or ``*-´´. ``*´´ acts as a glob and
will match any string of atoms to the left where an atom is separated by dots
(``.´´) or dashes (``-´´).

**--path-matcher-name**:
The name of the path matcher to use if a request matches this host rule. The
path matcher must already exist in the URL map (see `[gcloud compute
url-maps add-path-matcher](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher)`).

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the host rule.

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
gcloud alpha compute url-maps add-host-rule
```

```
gcloud beta compute url-maps add-host-rule
```