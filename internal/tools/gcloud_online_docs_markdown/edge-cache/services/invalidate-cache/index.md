# gcloud edge-cache services invalidate-cache  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache)*

**NAME**

: **gcloud edge-cache services invalidate-cache - invalidate the cache for an EdgeCacheService resource**

**SYNOPSIS**

: **`gcloud edge-cache services invalidate-cache` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache#--location)`=`LOCATION`) (`[--host](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache#--host)`=`HOST` `[--path](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache#--path)`=`PATH` `[--tags](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache#--tags)`=[`TAGS`,…]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Invalidate the cache entries associated with an EdgeCacheService resource.

**EXAMPLES**

: To invalidate content via a tag, or tags for a given host for an
EdgeCacheService named 'my-service':

```
gcloud edge-cache services invalidate-cache my-service --tags="status=404" --host="media.example.com"
```

To invalidate all content under a specific path, specify an exact path, or a
prefix. Prefixes are denoted with a trailing `*` character.

```
gcloud edge-cache services invalidate-cache my-service --path="/static/*"
```

You can optionally combine this with a status code. For example, to invalidate
all cached HTTP 404s:

```
gcloud edge-cache services invalidate-cache my-service --tags="status=404" --path="/static/*"
```

**POSITIONAL ARGUMENTS**

: **Service resource - The EdgeCacheService resource you want to invalidate the
cache for. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `service` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- use global location.**

**REQUIRED FLAGS**

: **--host**

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

: This command uses the `networkservices/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cache services invalidate-cache
```