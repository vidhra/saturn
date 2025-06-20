# gcloud run services proxy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/services/proxy](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy)*

**NAME**

: **gcloud run services proxy - proxy a service to localhost authenticating as the active account or with the specified token**

**SYNOPSIS**

: **`gcloud run services proxy` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy#SERVICE)` : `[--namespace](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy#--namespace)`=`NAMESPACE`) [`[--port](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy#--port)`=`PORT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy#--region)`=`REGION`] [`[--tag](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy#--tag)`=`TAG`] [`[--token](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy#--token)`=`TOKEN`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Runs a server on localhost that proxies requests to the specified Cloud Run
Service with credentials attached.
You can use this to test services protected with IAM authentication.
The Cloud Run service must be reachable from the machine running this command.
For example, if the Cloud Run Service is configured to only allow
`internal` ingress, this command will not work from outside the
service's VPC network.

**EXAMPLES**

: To proxy the service 'my-service' at localhost port 8080:

```
gcloud run services proxy my-service --port=8080
```

To proxy the existing traffic tag 'my-tag' on the service 'my-service:

```
gcloud run services proxy my-service --tag=my-tag
```

**POSITIONAL ARGUMENTS**

: **Service resource - Service to proxy locally. The arguments in this group can be
used to specify the attributes of this resource.
This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `SERVICE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--namespace**:
Specific to Cloud Run for Anthos: Kubernetes namespace for the service.
To set the `namespace` attribute:

- provide the argument `SERVICE` on the command line with a fully
specified name;
- provide the argument `--namespace` on the command line;
- set the property `run/namespace`;
- For Cloud Run on Kubernetes Engine, defaults to "default". Otherwise, defaults
to project ID.;
- provide the argument `project` on the command line;
- set the property `core/project`.**

**FLAGS**

: **--port**:
Local port number to expose the proxied service. If not specified, it will be
set to 8080.

**--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**--tag**:
Traffic tag of the service to expose via the proxy. If not specified, the
default service URL will be proxied which may serve different revisions based on
traffic-splits. Custom tags can be used to proxy specific revisions. Please see
[https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags).

**--token**:
The specific identity token to add to all requests of the proxied service. If
not specified, the identity token of the currently active authenticated account
will be used (e.g. gcloud auth print-identity-token).

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
gcloud alpha run services proxy
```

```
gcloud beta run services proxy
```