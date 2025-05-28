# gcloud domains registrations search-domains  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/search-domains](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/search-domains)*

**NAME**

: **gcloud domains registrations search-domains - search for available domains**

**SYNOPSIS**

: **`gcloud domains registrations search-domains` `[DOMAIN_QUERY](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/search-domains#DOMAIN_QUERY)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/search-domains#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Search for available domains relevant to a specified query.
This command uses cached domain name availability information. Use the
get-register-params command to get up-to-date availability information.

**EXAMPLES**

: To search for domains for ``my-new-project``,
run:

```
gcloud domains registrations search-domains my-new-project
```

To search for a specific domain, like
``example.com``, and get suggestions for other
domain endings, run:

```
gcloud domains registrations search-domains example.com
```

**POSITIONAL ARGUMENTS**

: **`DOMAIN_QUERY`**:
Domain search query. May be a domain name or arbitrary search terms.

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
gcloud alpha domains registrations search-domains
```

```
gcloud beta domains registrations search-domains
```