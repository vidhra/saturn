# gcloud run services update-traffic  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic)*

**NAME**

: **gcloud run services update-traffic - adjust the traffic assignments for a Cloud Run service**

**SYNOPSIS**

: **`gcloud run services update-traffic` [[`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#SERVICE)`] `[--namespace](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--namespace)`=`NAMESPACE`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--async)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--region)`=`REGION`] [`[--clear-tags](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--clear-tags)`     | `[--set-tags](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--set-tags)`=[`TAG`=`REVISION`,…]     | `[--remove-tags](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--remove-tags)`=[`TAG`,…] `[--update-tags](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--update-tags)`=[`TAG`=`REVISION`,…]] [`[--to-latest](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--to-latest)`     | `[--to-revisions](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--to-revisions)`=[`REVISION-NAME`=`PERCENTAGE`,…]     | `[--to-tags](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#--to-tags)`=[`TAG`=`PERCENTAGE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Adjust the traffic assignments for a Cloud Run service.

**EXAMPLES**

: To assign 10% of traffic to revision myservice-s5sxn and 90% of traffic to
revision myservice-cp9kw run:

```
gcloud run services update-traffic myservice --to-revisions=myservice-s5sxn=10,myservice-cp9kw=90
```

To increase the traffic to revision myservice-s5sxn to 20% and by reducing the
traffic to revision myservice-cp9kw to 80% run:

```
gcloud run services update-traffic myservice --to-revisions=myservice-s5sxn=20
```

To rollback to revision myservice-cp9kw run:

```
gcloud run services update-traffic myservice --to-revisions=myservice-cp9kw=100
```

To assign 100% of traffic to the current or future LATEST revision run:

```
gcloud run services update-traffic myservice --to-latest
```

You can also refer to the current or future LATEST revision in --to-revisions by
the string "LATEST". For example, to set 10% of traffic to always float to the
latest revision:

```
gcloud run services update-traffic myservice --to-revisions=LATEST=10
```

**POSITIONAL ARGUMENTS**

: **Service resource - Service to update the configuration of. The arguments in this
group can be used to specify the attributes of this resource.

**[`SERVICE`]**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `SERVICE` on the command line;
- specify the service name from an interactive prompt.

**--namespace**:
Specific to Cloud Run for Anthos: Kubernetes namespace for the service.
To set the `namespace` attribute:

- provide the argument `SERVICE` on the command line with a fully
specified name;
- specify the service name from an interactive prompt with a fully specified name;
- provide the argument `--namespace` on the command line;
- set the property `run/namespace`;
- For Cloud Run on Kubernetes Engine, defaults to "default". Otherwise, defaults
to project ID.;
- provide the argument `project` on the command line;
- set the property `core/project`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**--clear-tags**

**--to-latest**

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
gcloud alpha run services update-traffic
```

```
gcloud beta run services update-traffic
```