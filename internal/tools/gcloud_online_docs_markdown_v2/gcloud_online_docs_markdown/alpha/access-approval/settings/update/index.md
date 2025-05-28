# gcloud alpha access-approval settings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/update](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/update)*

**NAME**

: **gcloud alpha access-approval settings update - update Access Approval settings**

**SYNOPSIS**

: **`gcloud alpha access-approval settings update` [`--active_key_version`=`ACTIVE_KEY_VERSION`] [`--approval_policy`=`APPROVAL_POLICY`] [`--enrolled_services`=`ENROLLED_SERVICES`] [`--notification_emails`=`NOTIFICATION_EMAILS`] [`--notification_pubsub_topic`=`NOTIFICATION_PUBSUB_TOPIC`] [`--prefer_no_broad_approval_requests`=`PREFER_NO_BROAD_APPROVAL_REQUESTS`] [`--preferred_request_expiration_days`=`PREFERRED_REQUEST_EXPIRATION_DAYS`] [`--request_scope_max_width_preference`=`REQUEST_SCOPE_MAX_WIDTH_PREFERENCE`] [`--require_customer_visible_justification`=`REQUIRE_CUSTOMER_VISIBLE_JUSTIFICATION`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/update#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/update#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/update#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/settings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update the Access Approval settings associated with a
project, a folder, or organization. Partial updates are supported (for example,
you can update the notification emails without modifying the enrolled services).

**EXAMPLES**

: Update notification emails associated with project `p1`, run:

```
gcloud alpha access-approval settings update --project=p1 --notification_emails='foo@example.com, bar@example.com'
```

Enable Access Approval enforcement for folder `f1`:

```
gcloud alpha access-approval settings update --folder=f1 --enrolled_services=all
```

Enable Access Approval enforcement for organization `org1` for only
Cloud Storage and Compute products and set the notification emails at the same
time:

```
gcloud alpha access-approval settings update --organization=org1 --enrolled_services='storage.googleapis.com,compute.googleapis.com' --notification_emails='security_team@example.com'
```

Update active key version for project `p1`:

```
gcloud alpha access-approval settings update --project=p1 --active_key_version='projects/p1/locations/global/keyRings/signing-keys/cryptoKeys/signing-key/cryptoKeyVersions/1'
```

Update preferred request expiration days for project `p1`:

```
gcloud alpha access-approval settings update --project=p1 --preferred_request_expiration_days=5
```

Enable prefer no broad approval requests for project `p1`:

```
gcloud alpha access-approval settings update --project=p1 --prefer_no_broad_approval_requests=true
```

Update notification pubsub topic for project `p1`:

```
gcloud alpha access-approval settings update --project=p1 --notification_pubsub_topic='exampleTopic'
```

Update request scope max width preference for project `p1`:

```
gcloud alpha access-approval settings update --project=p1 --request_scope_max_width_preference=PROJECT
```

Update approval policy for project `p1`:

```
gcloud alpha access-approval settings update --project=p1 --approval_policy=transparency
```

**FLAGS**

: **--active_key_version**:
The asymmetric crypto key version to use for signing approval requests. Use ''
to remove the custom signing key.

**--approval_policy**:
The preference to configure the approval policy for access requests.
`APPROVAL_POLICY` must be one of:
`transparency`, `streamlined-support`,
`access-approval`, `inherit-policy-from-parent`.

**--enrolled_services**:
Comma-separated list of services to enroll for Access Approval or 'all' for all
supported services. Note for project and folder enrollments, only 'all' is
supported. Use '' to clear all enrolled services.

**--notification_emails**:
Comma-separated list of email addresses to which notifications relating to
approval requests should be sent or '' to clear all saved notification emails.

**--notification_pubsub_topic**:
The pubsub topic to publish notifications to when approval requests are made.

**--prefer_no_broad_approval_requests**:
If set to true it will communicate the preference to Google personnel to request
access with as targeted a resource scope as possible.

**--preferred_request_expiration_days**:
The default expiration time for approval requests. This value must be between 1
and 30. Note that this can be overridden at time of Approval Request creation
and modified by the customer at approval time.

**--request_scope_max_width_preference**:
The preference for the broadest scope of access for access requests without a
specific method. `REQUEST_SCOPE_MAX_WIDTH_PREFERENCE` must
be one of: `ORGANIZATION`, `FOLDER`, `PROJECT`.

**--require_customer_visible_justification**:
The preference to configure if a customer visible justification (i.e. Vector
Case) is required for a Googler to create an Access Ticket to send to the
customer when attempting to access customer resources.

**--folder**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-approval settings update
```

```
gcloud beta access-approval settings update
```