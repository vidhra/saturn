# gcloud edge-cache services update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update)*

**NAME**

: **gcloud edge-cache services update - update an EdgeCacheService resource**

**SYNOPSIS**

: **`gcloud edge-cache services update` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--description)`=`DESCRIPTION`] [`[--edge-security-policy](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--edge-security-policy)`=`EDGE_SECURITY_POLICY`] [`[--edge-ssl-certificate](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--edge-ssl-certificate)`=[`EDGE_SSL_CERTIFICATE`,…]] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--enable-logging)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--logging-sample-rate](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--logging-sample-rate)`=`LOGGING_SAMPLE_RATE`] [`[--require-tls](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#--require-tls)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing EdgeCacheService resource.

**EXAMPLES**

: To update an EdgeCacheService resource called 'my-service' run:

```
gcloud edge-cache services update my-service --description="new description"
```

**POSITIONAL ARGUMENTS**

: **Service resource - The name of the EdgeCacheService resource to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Human-readable description of the resource.

**--edge-security-policy**:
Resource URL that points at the Cloud Armor edge security policy that is applied
on each request against the EdgeCacheService.
Security Policies should be specified as relative resource URLs - for example
`projects/my-project/locations/global/securityPolicies/my-policy`
Note that only security policies with a type of `EDGE` can be
attached to an EdgeCacheService.

**--edge-ssl-certificate**:
URLs to sslCertificate resources that are used to authenticate connections
between users and the EdgeCacheService.
Certificates should be specified as relative resource URLs - for example
`projects/my-project/locations/global/certificates/my-cert`
Note that only "global" certificates with a "scope" of `EDGE_CACHE`
can be attached to an EdgeCacheService.
You may specify up to 5 SSL certificates per Service.

**--enable-logging**:
Specifies whether to enable logging for traffic served by this service.
Defaults to false.

**--labels**:
List of KEY=VALUE labels to attach to this resource.

**--logging-sample-rate**:
Configures the sampling rate of requests, where 1.0 means all logged requests
are reported and 0.0 means no logged requests are reported. The default value is
1.0, and the value of the field must be in [0, 1].
This field can only be specified if logging is enabled for this service.

**--require-tls**:
Require TLS (HTTPS) for all clients connecting to this service.
Clients who connect over HTTP (port 80) will receive a HTTP 301 to the same URL
over HTTPS (port 443). You must have at least one (1) edgeSslCertificate
specified to enable this.

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
gcloud alpha edge-cache services update
```