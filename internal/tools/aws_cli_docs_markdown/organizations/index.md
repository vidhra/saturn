# organizationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# organizations

## Description

Organizations is a web service that enables you to consolidate your multiple Amazon Web Services accounts into an *organization* and centrally manage your accounts and their resources.

This guide provides descriptions of the Organizations operations. For more information about using this service, see the [Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) .

**Support and feedback for Organizations**

We welcome your feedback. Send your comments to [feedback-awsorganizations@amazon.com](mailto:feedback-awsorganizations%40amazon.com) or post your feedback and questions in the [Organizations support forum](http://forums.aws.amazon.com/forum.jspa?forumID=219) . For more information about the Amazon Web Services support forums, see [Forums Help](http://forums.aws.amazon.com/help.jspa) .

**Endpoint to call When using the CLI or the Amazon Web Services SDK**

For the current release of Organizations, specify the `us-east-1` region for all Amazon Web Services API and CLI calls made from the commercial Amazon Web Services Regions outside of China. If calling from one of the Amazon Web Services Regions in China, then specify `cn-northwest-1` . You can do this in the CLI by using these parameters and commands:

- Use the following parameter with each command to specify both the endpoint and its region:  `--endpoint-url https://organizations.us-east-1.amazonaws.com` *(from commercial Amazon Web Services Regions outside of China)*   or  `--endpoint-url https://organizations.cn-northwest-1.amazonaws.com.cn` *(from Amazon Web Services Regions in China)*
- Use the default endpoint, but configure your default region with this command:  `aws configure set default.region us-east-1` *(from commercial Amazon Web Services Regions outside of China)*   or  `aws configure set default.region cn-northwest-1` *(from Amazon Web Services Regions in China)*
- Use the following parameter with each command to specify the endpoint:  `--region us-east-1` *(from commercial Amazon Web Services Regions outside of China)*   or  `--region cn-northwest-1` *(from Amazon Web Services Regions in China)*

**Recording API Requests**

Organizations supports CloudTrail, a service that records Amazon Web Services API calls for your Amazon Web Services account and delivers log files to an Amazon S3 bucket. By using information collected by CloudTrail, you can determine which requests the Organizations service received, who made the request and when, and so on. For more about Organizations and its support for CloudTrail, see [Logging Organizations API calls with CloudTrail](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_incident-response.html#orgs_cloudtrail-integration) in the *Organizations User Guide* . To learn more about CloudTrail, including how to turn it on and find your log files, see the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html) .

## Available Commands

- [accept-handshake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/accept-handshake.html)
- [attach-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html)
- [cancel-handshake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/cancel-handshake.html)
- [close-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/close-account.html)
- [create-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-account.html)
- [create-gov-cloud-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-gov-cloud-account.html)
- [create-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organization.html)
- [create-organizational-unit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organizational-unit.html)
- [create-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-policy.html)
- [decline-handshake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/decline-handshake.html)
- [delete-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organization.html)
- [delete-organizational-unit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organizational-unit.html)
- [delete-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-policy.html)
- [delete-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-resource-policy.html)
- [deregister-delegated-administrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/deregister-delegated-administrator.html)
- [describe-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-account.html)
- [describe-create-account-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-create-account-status.html)
- [describe-effective-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-effective-policy.html)
- [describe-handshake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-handshake.html)
- [describe-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-organization.html)
- [describe-organizational-unit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-organizational-unit.html)
- [describe-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-policy.html)
- [describe-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-resource-policy.html)
- [detach-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/detach-policy.html)
- [disable-aws-service-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/disable-aws-service-access.html)
- [disable-policy-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/disable-policy-type.html)
- [enable-all-features](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-all-features.html)
- [enable-aws-service-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-aws-service-access.html)
- [enable-policy-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-policy-type.html)
- [invite-account-to-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/invite-account-to-organization.html)
- [leave-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/leave-organization.html)
- [list-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-accounts.html)
- [list-accounts-for-parent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-accounts-for-parent.html)
- [list-aws-service-access-for-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-aws-service-access-for-organization.html)
- [list-children](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-children.html)
- [list-create-account-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-create-account-status.html)
- [list-delegated-administrators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-delegated-administrators.html)
- [list-delegated-services-for-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-delegated-services-for-account.html)
- [list-handshakes-for-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-handshakes-for-account.html)
- [list-handshakes-for-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-handshakes-for-organization.html)
- [list-organizational-units-for-parent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-organizational-units-for-parent.html)
- [list-parents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-parents.html)
- [list-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies.html)
- [list-policies-for-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies-for-target.html)
- [list-roots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-roots.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-tags-for-resource.html)
- [list-targets-for-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-targets-for-policy.html)
- [move-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/move-account.html)
- [put-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/put-resource-policy.html)
- [register-delegated-administrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/register-delegated-administrator.html)
- [remove-account-from-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/remove-account-from-organization.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/untag-resource.html)
- [update-organizational-unit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/update-organizational-unit.html)
- [update-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/update-policy.html)