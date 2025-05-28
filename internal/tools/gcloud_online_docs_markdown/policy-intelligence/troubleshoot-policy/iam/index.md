# gcloud policy-intelligence troubleshoot-policy iam  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam)*

**NAME**

: **gcloud policy-intelligence troubleshoot-policy iam - troubleshoot IAM allow and deny policies**

**SYNOPSIS**

: **`gcloud policy-intelligence troubleshoot-policy iam` `[RESOURCE](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#RESOURCE)` `[--permission](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#--permission)`=`PERMISSION` `[--principal-email](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#--principal-email)`=`EMAIL` [`[--destination-ip](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#--destination-ip)`=`DESTINATION_IP`] [`[--destination-port](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#--destination-port)`=`DESTINATION_PORT`] [`[--request-time](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#--request-time)`=`REQUEST_TIME`] [`[--resource-name](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#--resource-name)`=`RESOURCE_NAME`] [`[--resource-service](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#--resource-service)`=`RESOURCE_SERVICE`] [`[--resource-type](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#--resource-type)`=`RESOURCE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/troubleshoot-policy/iam#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Uses a resource's effective IAM allow policy and IAM deny policy to check
whether a principal has a specific permission on the resource.

**EXAMPLES**

: The following command checks whether the principal
``my-user@example.com`` has the permission
``resourcemanager.projects.get`` on the project
``my-project``:

```
gcloud policy-intelligence troubleshoot-policy iam //cloudresourcemanager.googleapis.com/projects/my-project --principal-email=my-user@example.com --permission=resourcemanager.projects.get
```

The following command checks whether the principal
``my-user@example.com`` has the
``compute.images.get`` permission on the
project ``my-project``. The command also
provides additional context that lets Troubleshooter evaluate conditional role
bindings:

```
gcloud policy-intelligence troubleshoot-policy iam //cloudresourcemanager.googleapis.com/projects/my-project --principal-email=my-user@example.com --permission=compute.images.get --resource-name=//compute.googleapis.com/projects/my-project/zones/images/my-image'
 --resource-service='compute.googleapis.com'         \
    --resource-type='compute.googleapis.com/Image'         \
    --destination-ip='192.2.2.2'--destination-port=8080 \
    --request-time='2023-01-01T00:00:00Z'
```

**POSITIONAL ARGUMENTS**

: **`RESOURCE`**:
Full resource name that access is checked against. For a list of full resource
name formats, see: [https://cloud.google.com/iam/docs/resource-names](https://cloud.google.com/iam/docs/resource-names).

**REQUIRED FLAGS**

: **--permission**:
IAM permission to check. The permssion can be in the `v1` or
`v2` format. For example, `resourcemanager.projects.get`
or `cloudresourcemanager.googleapis.com/projects.get`. For a list of
permissions, see [https://cloud.google.com/iam/docs/permissions-reference](https://cloud.google.com/iam/docs/permissions-reference)
and [https://cloud.google.com/iam/docs/deny-permissions-support](https://cloud.google.com/iam/docs/deny-permissions-support)

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
must adhere to UTC format (RFC 3339). For example,2021-01-01T00:00:00Z. For more
information, see: [https://tools.ietf.org/html/rfc3339](https://tools.ietf.org/html/rfc3339)

**--resource-name**:
The resource name value to use when checking conditional bindings. For accepted
values, see: [https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).

**--resource-service**:
The resource service value to use when checking conditional bindings. For
accepted values, see: [https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-service](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-service)

**--resource-type**:
The resource type value to use when checking conditional bindings. For accepted
values, see: [https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-type](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-type)

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