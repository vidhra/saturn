# gcloud policy-troubleshoot iam  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam)*

**NAME**

: **gcloud policy-troubleshoot iam - troubleshoot the IAM Policy**

**SYNOPSIS**

: **`gcloud policy-troubleshoot iam` `[RESOURCE](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#RESOURCE)` `[--permission](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#--permission)`=`PERMISSION` `[--principal-email](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#--principal-email)`=`PRINCIPAL_EMAIL` [`[--destination-ip](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#--destination-ip)`=`DESTINATION_IP`] [`[--destination-port](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#--destination-port)`=`DESTINATION_PORT`] [`[--request-time](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#--request-time)`=`REQUEST_TIME`] [`[--resource-name](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#--resource-name)`=`RESOURCE_NAME`] [`[--resource-service](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#--resource-service)`=`RESOURCE_SERVICE`] [`[--resource-type](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#--resource-type)`=`RESOURCE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Performs a check on whether a principal is granted a permission on a resource
and how that access is determined according to the resource's effective IAM
policy interpretation.

**EXAMPLES**

: To troubleshoot a permission of a principal on a resource, run:

```
gcloud policy-troubleshoot iam //cloudresourcemanager.googleapis.com/projects/project-id --principal-email=my-iam-account@somedomain.com --permission=resourcemanager.projects.get
```

See [https://cloud.google.com/iam/help/allow-policies/overview](https://cloud.google.com/iam/help/allow-policies/overview)
for more information about IAM policies.

**POSITIONAL ARGUMENTS**

: **`RESOURCE`**:
Full resource name that access is checked against. See: [https://cloud.google.com/iam/docs/resource-names](https://cloud.google.com/iam/docs/resource-names).

**REQUIRED FLAGS**

: **--permission**:
Cloud IAM permission to check, e.g. "resourcemanager.projects.get".

**--principal-email**:
Email address that identifies the principal to check. Only Google Accounts and
service accounts are supported.

**OPTIONAL FLAGS**

: **--destination-ip**:
The request destination IP address to use when checking conditional bindings.
For example, `198.1.1.1`.

**--destination-port**:
The request destination port to use when checking conditional bindings. For
example, 8080.

**--request-time**:
The request timestamp to use when checking conditional bindings. This string
must adhere to UTC format (RFC 3339). For example,2021-01-01T00:00:00Z. See: [https://tools.ietf.org/html/rfc3339](https://tools.ietf.org/html/rfc3339)

**--resource-name**:
The resource name value to use when checking conditional bindings. See: [https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).

**--resource-service**:
The resource service value to use when checking conditional bindings. See: [https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-service](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-service)

**--resource-type**:
The resource type value to use when checking conditional bindings. See: [https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-type](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-type)

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

: This command uses the `policytroubleshooter/v2alpha1` API. The full
documentation for this API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: These variants are also available:

```
gcloud alpha policy-troubleshoot iam
```

```
gcloud beta policy-troubleshoot iam
```