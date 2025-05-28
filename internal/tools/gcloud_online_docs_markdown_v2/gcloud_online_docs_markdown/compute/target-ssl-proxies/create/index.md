# gcloud compute target-ssl-proxies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create)*

**NAME**

: **gcloud compute target-ssl-proxies create - create a target SSL proxy**

**SYNOPSIS**

: **`gcloud compute target-ssl-proxies create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#NAME)` `[--backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#--backend-service)`=`BACKEND_SERVICE` (`[--certificate-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#--certificate-map)`=`CERTIFICATE_MAP` `[--ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#--ssl-certificates)`=`SSL_CERTIFICATE`,[…]) [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#--description)`=`DESCRIPTION`] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#--proxy-header)`=`PROXY_HEADER`; default="NONE"] [`[--ssl-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#--ssl-policy)`=`SSL_POLICY`] [`[--global-ssl-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#--global-ssl-policy)`     | `[--ssl-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#--ssl-policy-region)`=`SSL_POLICY_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-ssl-proxies create` is used to create target
SSL proxies. A target SSL proxy is referenced by one or more forwarding rules
which define which packets the proxy is responsible for routing. The target SSL
proxy points to a backend service which handle the actual requests. The target
SSL proxy also points to at most 15 SSL certificates used for server-side
authentication or one certificate map. The target SSL proxy can be associated
with at most one SSL policy.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target SSL proxy to create.

**REQUIRED FLAGS**

: **--backend-service**:
A backend service that will be used for connections to the target SSL proxy.

**At least one of these must be specified:

**Certificate map resource - The certificate map to attach. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--certificate-map` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--certificate-map` on the command line with a
fully specified name;
- default value of location is [global].

**--certificate-map**:
ID of the certificate map or fully qualified identifier for the certificate map.
To set the `map` attribute:

- provide the argument `--certificate-map` on the command line.**

**--ssl-certificates**:
References to at most 15 SSL certificate resources that are used for server-side
authentication. The first SSL certificate in this list is considered the primary
SSL certificate associated with the load balancer. The SSL certificates must
exist and cannot be deleted while referenced by a target SSL proxy.**

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the target SSL proxy.

**--proxy-header**:
The type of proxy protocol header to be sent to the backend.
`PROXY_HEADER` must be one of:

**`NONE`**:
No proxy header is added.

**`PROXY_V1`**:
Enables PROXY protocol (version 1) for passing client connection information.

**--ssl-policy**:
A reference to an SSL policy resource that defines the server-side support for
SSL features and affects the connections between clients and load balancers that
are using the SSL proxy. The SSL policy must exist and cannot be deleted while
referenced by a target SSL proxy.

**--global-ssl-policy**

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
gcloud alpha compute target-ssl-proxies create
```

```
gcloud beta compute target-ssl-proxies create
```