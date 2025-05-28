# gcloud compute ssl-policies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/describe](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/describe)*

**NAME**

: **gcloud compute ssl-policies describe - describe a Compute Engine ssl policy**

**SYNOPSIS**

: **`gcloud compute ssl-policies describe` `[SSL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/describe#SSL_POLICY)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute ssl-policies describe` is used to display all data
associated with a Compute Engine SSL policy in a project.
An SSL policy specifies the server-side support for SSL features. An SSL policy
can be attached to a TargetHttpsProxy or a TargetSslProxy. This affects
connections between clients and the load balancer. SSL policies do not affect
the connection between the load balancers and the backends. SSL policies are
used by Application Load Balancers and proxy Network Load Balancers.

**POSITIONAL ARGUMENTS**

: **`SSL_POLICY`**:
Name of the SSL policy to describe.

**FLAGS**

: **--global**

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
gcloud alpha compute ssl-policies describe
```

```
gcloud beta compute ssl-policies describe
```