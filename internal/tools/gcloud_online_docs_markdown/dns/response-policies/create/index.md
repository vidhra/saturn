# gcloud dns response-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create)*

**NAME**

: **gcloud dns response-policies create - creates a new Cloud DNS response policy**

**SYNOPSIS**

: **`gcloud dns response-policies create` `[RESPONSE_POLICIES](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create#RESPONSE_POLICIES)` `[--description](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create#--description)`=`DESCRIPTION` [`[--gkeclusters](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create#--gkeclusters)`=[`GKECLUSTERS`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create#--location)`=`LOCATION`] [`[--networks](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create#--networks)`=[`NETWORKS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a new Cloud DNS response policy.

**EXAMPLES**

: To create a new response policy with minimal arguments, run:

```
gcloud dns response-policies create myresponsepolicy --description='My new response policy.' --networks=''
```

To create a new response policy with all optional arguments, run:

```
gcloud dns response-policies create myresponsepolicy --description='My new response policy.' --networks=network1,network2
```

To create a new zonal response policy scoped to a GKE cluster in
```
us-central1-a, run (alpha/beta):
```

```
gcloud dns response-policies create beta myresponsepolicy --description='My new response
policy.' --gkeclusters=cluster1 --location=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **Response policy resource - The response policy to create. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `response_policies` on the command line with a
fully specified name;
- set the property `core/project`.

This must be specified.

**`RESPONSE_POLICIES`**:
ID of the response_policy or fully qualified identifier for the response_policy.
To set the `response-policy` attribute:

- provide the argument `response_policies` on the command line.**

**REQUIRED FLAGS**

: **--description**:
A description of the response policy.

**OPTIONAL FLAGS**

: **--gkeclusters**:
The comma-separated list of GKE cluster names to associate with the response
policy.

**--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

**--networks**:
The comma-separated list of network names to associate with the response policy.

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
gcloud alpha dns response-policies create
```

```
gcloud beta dns response-policies create
```